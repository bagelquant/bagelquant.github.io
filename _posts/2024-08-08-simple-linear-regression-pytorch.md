---
title: "Build a Simple Linear Regression Machine Learning Model with PyTorch"
date: 2024-08-08
categories:
  - PyTorch
tags:
  - machine-learning
---

In this post, I will show you how to build a simple linear regression model using PyTorch. This will illustrate the basic concepts of PyTorch, such as tensors, operations, and autograd. 

## Create a Dataset

First, let's create a simple linear dataset with some noise. We will use this dataset to train our model. 

```python
import numpy as np
def sample_linear_data(n: int = 100, 
                slope: float = 1, intercept: float = 0, 
                noise: float = 0.1) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate linear data with noise.
    
    :param n: Number of data points.
    :param slope: Slope of the line.
    :param intercept: Intercept of the line.
    :param noise: Standard deviation of the noise.
    :return: x, y
    """
    x = np.linspace(0, 1, n)
    y = slope * x + intercept + np.random.normal(0, noise, n)
    return x, y
```

This function generates a linear dataset with some noise. We can use it to create our training data. plot the data to visualize it.

```python
import matplotlib.pyplot as plt
X, y = sample_linear_data()
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
```

![sample linear data](/assets/post_img/sample%20linear%20data.png)

## How Machine Learning Works

In linear regression, machine learning process works as follows:

1. draw a random line on the plot.
2. calculate the error between the line and the data points.
3. adjust the line try to minimize the error.
4. repeat the process until the error is minimized.

The first step is to define the **model(draw a random line)**. Therefore, define a model as: `y = weight * x + bias`.

The second step is to find a way to describe how fit the **model(line)** is to the data. In this example, we will use the mean squared error. This also called the **loss function** or **cost function**.

[Learn more about loss functions](https://towardsdatascience.com/understanding-different-loss-functions-for-neural-networks-dd1ed0274718)

The third step is to adjust the **model** to minimize the **loss**. This is done by using an optimization algorithm. A common optimization algorithm is **gradient descent**. 

[How Gradient Descent Works](https://towardsdatascience.com/understanding-the-mathematics-behind-gradient-descent-dde5dc9be06e)

### Key Concepts so far

- **Model**: `y = weight * x + bias`
- **Loss Function**: How well the model fits the data. When the loss is low, the model fits the data well.
- **Optimization Algorithm**: Adjust the model to minimize the loss. In this case, we will use **gradient descent**.

> In PyTorch, we will replicate these steps.


## Replicate the Process in PyTorch

### Step 1: Define the Model

```python
import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
                self.weight = nn.Parameter(torch.randn(1, 
                                               requires_grad=True,
                                               dtype=torch.float32))
        self.bias = nn.Parameter(torch.randn(1,
                                             requires_grad=True,
                                             dtype=torch.float32))


    def forward(self, x):
        return self.weight * x + self.bias
```

In PyTorch, we define the model as a class that inherits from `nn.Module`. The `__init__` method initializes the model parameters. In this case, we have two parameters: `weight` and `bias`. These are the parameters we want to learn from the data.

The `forward` method is required in all PyTorch models. It defines how the model processes the input data. In this case, the model is a simple linear function: `y = weight * x + bias`.

### Step 2: Define the Loss Function

```python
loss_fn = nn.MSELoss()
```

`nn.MSELoss` is the mean squared error loss function. It calculates the mean squared error between the model's predictions and the actual data. The goal is to minimize this loss.

### Step 3: Define the Optimization Algorithm

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
```

`torch.optim.SGD` is the stochastic gradient descent optimizer. It adjusts the model parameters to minimize the loss. The `lr` parameter is the learning rate, which controls how much the model parameters are adjusted.

### Step 4: Training the Model

Training in PyTorch is a basic python loop. In each iteration, we perform the following steps:

1. **Forward Pass**: use `model.forward()` method to make predictions.
2. **Calculate Loss**: use the loss function to calculate the loss.
3. **Zero Gradients**: set the gradients to zero before backpropagation.
4. **Backward Pass**: calculate the gradients of the loss with respect to the model parameters.
5. **Update Parameters**: use the optimizer to update the model parameters.

In this post, we will not cover the details of the 5 steps. Just remember that this 5 steps process is a required process in training a machine learning model.

The short version explanation is: in each iteration, we feed the data to the model(called epoch), calculate the loss, adjust the model parameters to minimize the loss. We repeat this process until the loss is minimized.

We will cover these topics in future posts.

> Pytorch requires the data to be in tensor format. Therefore, we need to convert the data to tensor format. Tensor we could consider as a multi-dimensional array for PyTorch.

```python
# get the data
X, y = sample_linear_data()
# PyTorch requires the data to be in tensor format
X = torch.tensor(X, dtype=torch.float32)  # convert to tensor
y = torch.tensor(y, dtype=torch.float32)  # convert to tensor
# Create the model
model = LinearRegression()

# Loop through the training data
epochs = 1000
for epoch in range(epochs):
    # Set the model to training mode
    model.train()

    # 1. Forward pass
    pred = model(X)
    # 2. Compute loss
    loss = loss_fn(pred, y)
    # 3. Zero gradients
    optimizer.zero_grad()
    # 4. Backward pass
    loss.backward()
    # 5. Update weights
    optimizer.step()

    # print the loss, see if the loss is decreasing
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss {loss:.6f}')
```

## Compare Model predictions with the Original Data

After training the model, we can compare the model's predictions with the original data. We can plot the original data and the model's predictions to see how well the model fits the data.

```python
# calculate the model's predictions
with torch.inference_mode():  # This will set the model to evaluation mode
    predict_y = model(X)
# plot the original data
plt.scatter(X, y)
# plot the model's predictions
plt.plot(X, predict_y.detach().numpy(), color='red')
```

![Result](/assets/post_img/linear%20pytorch%20model.png)

## Conclusion

This is a simple example of building a linear regression model using PyTorch. PyTorch provides a flexible and powerful framework for building machine learning models. 

However this post neglects some important concepts in machine learning, such as validation, testing, and hyperparameter tuning, etc.

In future posts, we will cover more advanced topics in PyTorch. Stay tuned!

