---
title: "Constructing Peer-Based Features Using Gaussian Similarity in Embedding Space"
layout: post
header:
  overlay_image: /assets/images/headers/network-dark.png
---

Peer effects are a long-standing theme in empirical asset pricing and corporate finance, appearing in areas such as investment spillovers, product market competition, and information diffusion across related firms. Traditional models typically rely on predefined peer groups constructed using industry classifications, size buckets, or ad-hoc distance metrics. These approaches can be effective, but they also embed strong assumptions about firm similarity that may not capture the evolving and high-dimensional structure of modern equity data.

The goal of this work is to build a data-driven peer effect feature that adapts to the cross-sectional structure of firms at each date. Rather than relying on static industry classifications, I use a neural network to learn an embedding for each firm-date observation and then define peers based on similarity in this latent space. Embeddings act as compact summaries of the complex information contained in the underlying features. Once these embeddings are available, similarity between firms can be computed using a Gaussian kernel. The resulting peer-weighted feature represents a locally smoothed cross-sectional signal and can be incorporated into predictive models or factor construction exercises.

## Motivation

High-dimensional financial data present several challenges. Firms operate in rapidly changing environments, and simple classifications may be too coarse to capture nuanced relationships. A neural embedding offers an alternative representation: it is learned directly from the predictive task, and therefore emphasizes characteristics relevant for explaining variation in future returns.

This idea aligns with a growing literature in machine learning for asset pricing that uses latent representations to capture hidden structure. For example, Gu, Kelly, and Xiu (2020) demonstrated that deep neural networks can learn cross-sectional nonlinearity, and several recent studies use embeddings to identify economic clusters or latent factors. A peer effect built from learned embeddings extends this logic: firms with similar underlying characteristics (as encoded by the embedding) influence each other more strongly.

## Overview of the Approach

The peer feature construction proceeds date-by-date in a way that respects the time structure of panel data. The process unfolds in three stages:

### Generating Embeddings

A neural network is trained to predict next-period returns from the available firm characteristics. One of the hidden layers is designated as the embedding layer. For each date and each firm, the forward pass of the network produces an embedding vector. These vectors capture how the network represents firm-level information in a lower-dimensional space that is optimized for the predictive task.

### Defining Gaussian Similarity

Once embeddings are available for a given date, the similarity between firms is defined through a Gaussian kernel:

$$
w_{ij,t} = \exp\left( -\frac{\|z_{i,t} - z_{j,t}\|^2}{2\,\text{bw}_t^2} \right)
$$

Here $z_{i,t}$ and $z_{j,t}$ denote the embeddings of firms $i$ and $j$ at date $t$. The parameter $\text{bw}_t$ is a bandwidth that governs how rapidly similarity decays as distance grows. When the distance between two firms is small, their similarity weight is close to one. As the distance increases, the weight smoothly approaches zero.

The bandwidth can be chosen adaptively each period. A natural choice is the median of the nonzero pairwise distances at that date, which allows the similarity scale to adjust to changes in the cross-section.

### Constructing Peer-Weighted Features

To obtain a peer-based feature for a target firm, the Gaussian weights must be normalized to ensure they sum to one. Then a relevant firm-level quantity is aggregated across peers using these normalized weights. This quantity could be either the model’s predicted future return or another observed characteristic. The resulting peer feature represents a locally smoothed cross-sectional estimate that captures how similar firms behave.

## Comparison with Inverse-Distance Weighting

Inverse-distance weighting is a traditional technique for constructing peer measures:

$$
w_{ij} = \frac{1}{d_{ij} + \varepsilon}.
$$

While simple, it exhibits two limitations. First, the weight becomes extremely sensitive when distances are very small, creating instability in crowded regions of the embedding space. Second, its decay is slow; distant firms retain residual influence even when they are poor matches.

Gaussian similarity offers a more controlled alternative. It is smooth, bounded, and rapidly suppresses the influence of distant firms. This aligns with the intuition that only close peers should meaningfully contribute to the peer effect. Gaussian kernels also have a long history in kernel regression, nonparametric smoothing, and machine learning, where they serve as the foundation for many similarity-based methods.

## Comparison with Clustering and Other Peer-Definition Methods

Clustering-based approaches (e.g., k-means, hierarchical clustering, spectral clustering, or community detection on graphs) are a common alternative for defining peer groups. These methods partition the cross-section into discrete groups and then aggregate information within each cluster. Compared with Gaussian similarity in embedding space:

- Flexibility: clustering produces hard group memberships, while Gaussian similarity yields soft, continuous weights that reflect graded similarity. Soft weights can better capture partial membership when firms lie near cluster boundaries.
- Locality vs group structure: clusters emphasize global partitioning of the space, which can be useful for interpretability but may pool together firms that are heterogeneous along return-relevant dimensions. Gaussian kernels focus on local neighborhoods and adapt smoothly to density variations.
- Peer set size: clustering enforces a fixed or variable-sized group depending on the algorithm, whereas Gaussian weighting naturally adjusts the effective peer set via the bandwidth parameter.
- Hyperparameter choice: clustering requires selecting the number of clusters (`k`) or a cutting threshold (e.g., dendrogram height), and different choices can materially change peer definitions. By contrast, the embedding plus Gaussian-weighting workflow constructs a continuous similarity measure and therefore yields continuous peer-weighted features without hard discretization.
- Stability and time-variation: clusters can be unstable over time (especially with many clusters or small samples) unless regularized; embeddings with Gaussian weights can adapt continuously each date, reducing abrupt group shifts.
- Computational trade-offs: clustering can be computationally cheaper for large cross-sections (assign each firm to one cluster) and useful as a preprocessing step to restrict similarity calculations. A practical hybrid is to cluster first, then compute Gaussian-weighted peers within each cluster to get the best of both worlds.

In practice, the choice depends on the research goal. If interpretability and simple group-based comparisons are primary, clustering is attractive. If the goal is a smooth, local peer effect that reflects nuanced similarity, the Gaussian-embedding approach is preferable. I recommend evaluating both approaches empirically (e.g., information coefficients, out-of-sample predictive performance, and stability of signals) and considering hybrid workflows when scaling to large universes.

## Interpretation and Use Cases

The peer-weighted feature can be interpreted as a form of cross-sectional smoothing in a data-driven metric space. If the embedding layer successfully captures economically meaningful structure, then the peer feature represents an aggregation over firms that share similar return-relevant attributes. In practice, this can improve signal stability, reduce noise, and capture diffusion-like effects across related firms.

Because the construction is performed separately for each date and uses only information available at that time, it avoids look-ahead bias and is compatible with predictive modeling frameworks. Peer features can be included as regressors in linear models, tree-based models, or neural networks, or evaluated directly as factors using information coefficients.

This method provides an alternative to fixed peer definitions and may uncover relationships not visible through standard classifications. By allowing the neural embedding to define similarity endogenously, the resulting peer effect adapts to time-varying cross-sectional patterns and better reflects the underlying economic environment.
