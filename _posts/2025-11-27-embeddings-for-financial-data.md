---
title: "The Ghost in the Machine: Mastering Entity Embeddings for Financial Data"
layout: post
header:
  overlay_image: /assets/images/headers/entity_embedding_v2.png
excerpt: "From Word2Vec to Wall Street: How to give your neural networks a memory of corporate identity."
---

In the world of quantitative finance, we are often guilty of reducing a company to a spreadsheet row. We strip away the name "Apple Inc." and replace it with a vector of numbers: Price-to-Earnings, Volatility, Momentum. We assume that if two companies have the same numbers, they are the same thing.

But they aren't.

A biotech startup with high volatility is a lottery ticket; a utility company with high volatility is a crisis. The context—the *identity* of the firm—changes how the numbers should be interpreted.

For years, quant models struggled to "remember" who they were looking at. We used One-Hot Encoding, which created massive, sparse matrices that treated every stock as a stranger to every other stock.

Then came the **Embedding Layer**, a technique borrowed from linguistics that changed everything. This is the story of how we taught machines to understand identity, and how you can use it to predict returns.

## The Origin Story

To understand why we use embeddings in finance today, we have to look back at Google in 2013.

### The King - Man + Woman Moment
Researchers led by Tomas Mikolov were trying to solve a problem in Natural Language Processing (NLP). Computers treated words like "Apple" and "Orange" as completely unrelated integers. The machine had no concept that these were both fruits.

They introduced **Word2Vec**, a technique that mapped words to dense vectors in a geometric space. The results were shocking. The model learned that if you took the vector for "King", subtracted the vector for "Man", and added the vector for "Woman", the result was mathematically closest to the vector for "Queen".

$$
\vec{v}_{King} - \vec{v}_{Man} + \vec{v}_{Woman} \approx \vec{v}_{Queen}
$$

The model had captured the *semantic concept* of gender and royalty purely from data.

### The Kaggle Revolution
Fast forward to 2016. The Rossmann Store Sales competition on Kaggle challenged data scientists to predict sales for a chain of drugstores. Most participants used Gradient Boosted Trees (XGBoost).

But the winners, Cheng Guo and Felix Berkhahn, did something different. They realized that "Store ID #5" wasn't just a number. It had a personality—maybe it was in a city center, maybe near a school. They applied the logic of Word2Vec to the store IDs, creating **Entity Embeddings**.

Their neural network crushed the competition. It learned that Store A and Store B were "similar" (close in vector space) because they had similar customer patterns, even though they were hundreds of miles apart.

Today, we apply this exact logic to stock tickers (`permno`).

## Inside the Black Box

So, what is an embedding layer, technically speaking?

At its core, an embedding layer is a **Differentiable Lookup Table**. It serves as a translator between the discrete world of IDs and the continuous world of neural networks.

### The Mechanics
Imagine you have $N$ unique stocks (e.g., 5,000) and you want to represent them in a $D$-dimensional space (e.g., 32 dimensions).

The Embedding Layer is a matrix $W_E$ of size $N \times D$.

$$
W_E = \begin{bmatrix}
0.12 & -0.59 & \dots & 0.04 \\
-0.91 & 0.22 & \dots & -0.11 \\
\vdots & \vdots & \ddots & \vdots \\
0.55 & 0.10 & \dots & 0.88
\end{bmatrix}
$$

When you feed the model `permno` index $i$, it effectively multiplies a "One-Hot" vector $x$ (which is all zeros except for a single $1$ at position $i$) by this matrix.

$$
\text{Embedding}(i) = x^T \cdot W_E = \text{Row}_i \text{ of } W_E
$$

This operation is computationally cheap—it's just an array indexing operation $O(1)$, not a matrix multiplication $O(N^2)$.

### The Learning Process
Here is the magic: **The numbers in the matrix are initialized randomly.**

At epoch 0, the vector for "Microsoft" is random noise. But as your model tries to predict next month's return, it calculates an error (Loss). During **Backpropagation**, the gradients flow all the way back to this lookup table.

The model nudges the numbers in Microsoft's vector. It says, *"Every time I see this vector, the return is higher than I expected. Let me adjust the vector elements to reflect that."*

Over thousands of iterations, the random noise organizes itself into a meaningful map. Tech stocks drift toward one corner of the 32-dimensional hyperspace; Energy stocks drift to another.

## Implementation Strategy

To build this "Two-Headed" model for stock prediction, you need to structure your data and architecture carefully.

### Data Preprocessing Ordinal Encoding
Neural networks cannot ingest raw database identifiers like `14593` directly because they require contiguous integers to index the lookup table efficiently.

To prepare your data, you must create a mapping dictionary. Iterate through every unique `permno` in your historical dataset and assign it an integer from $0$ to $N-1$. You then create a new column in your dataframe (e.g., `permno_idx`) where the raw IDs are replaced by these integers. This new column acts as the categorical input for the network.

### The Architecture
Your model will accept two distinct inputs:

* **Categorical Input (`permno_idx`)**: Shape $(Batch, 1)$. This goes into the Embedding Layer.
* **Continuous Input (Features)**: Shape $(Batch, K)$. This goes into a standard Dense layer (often called a highway or encoder).

The embedding output (vector size $D$) and the feature output (size $K$) are **concatenated** into a single vector of size $D+K$, which then flows into the final prediction layers.

$$
\vec{h}_{combined} = \text{Concat}(\vec{v}_{embedding}, \vec{v}_{features})
$$

### Handling the Cold Start New IPOs
This is the most common failure mode in production. If your model is trained on 2010-2020 data, and you try to predict returns for a company that IPO'd in 2021, the `permno` will not exist in your lookup table.

**The Strategy:**
Reserve Index `0` for "Unknown".
* **Training:** Randomly mask a small percentage (e.g., 1%) of your `permno_idx` values to `0`. This forces the network to learn a "Generic Stock" vector at Index `0` that represents the average behavior of the market when identity is unknown.
* **Inference:** When you encounter a new `permno` in the test set, map it to `0`. The model will use the generic vector, preventing a crash and providing a sensible baseline prediction.

## Why This Matters for Alpha

Using embeddings allows your model to capture **interaction effects** between identity and data.

A standard linear regression assumes:
$$\text{Return} = \beta_1 \cdot \text{Volatility} + \beta_2 \cdot \text{Momentum}$$

An embedding model effectively learns:
$$\text{Return} = f(\text{Who You Are}, \text{Volatility}, \text{Momentum})$$

It allows the model to learn that **Volatility is good for Stock A but bad for Stock B**, without you ever having to manually code "Sector" or "Industry" variables. It learns the "DNA" of the stock directly from the returns.

Furthermore, embeddings can capture **latent relationships**. Two companies in different sectors may behave similarly due to underlying factors (e.g., macroeconomic exposure). The embedding space can reveal these hidden connections. Also it could be a powerful tool for identifying peer effects, we could easily construct a continuous measure of similarity between firms based on their embeddings, which could be used to enhance portfolio construction and risk management strategies, the post [Construct Peer Based Features](https://bagelquant.com/construct-peer-based-features/) addresses this topic in more detail.

