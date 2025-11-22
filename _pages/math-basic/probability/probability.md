---
title: "Probability"
permalink: /probability/

nav: probability
---

Probability theory forms the foundation of quantitative finance. It provides the mathematical framework to model uncertainty, evaluate risk, and make informed decisions in environments dominated by randomness. From pricing derivatives and evaluating portfolios to designing trading algorithms and conducting statistical inference, probability plays a central role in the toolkit of a quant.

Below is a concise walkthrough of key concepts and formulas in probability theory, structured to aid quick reference and understanding.

Link to handwritten notes: [probability-handwritten.pdf](Probability.pdf)

Additional topics in probability:

- Moment Generating Functions
- Characteristic Functions
- [General Probability Theory](general-probability-theory.md) (A more advanced treatment of probability theory)

## 1. Combinatorial Analysis

### 1.1 Permutations

For n distinct objects, the number of permutations is
$$
n! = n(n-1)(n-2)\cdots 1.
$$

If some objects are alike with counts $n_1,n_2,\ldots,n_r$,
$$
\frac{n!}{n_1! \, n_2! \cdots n_r!}.
$$

**Example (PEPPER):**
$$
\frac{6!}{3! \, 2! \, 1!} = 60.
$$

### 1.2 Combinations

Number of ways to choose $r$ from $n$:
$$
\binom{n}{r} = \frac{n!}{(n-r)!\,r!}.
$$

Basic facts:
$$
\binom{n}{0}=\binom{n}{n}=1, \qquad
\binom{n}{i}=0 \ \text{if}\ i<0 \ \text{or}\ i>n.
$$

Pascal identity:
$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}.
$$

Binomial theorem:
$$
(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{\,n-k}.
$$

Multinomial theorem:
$$
(x_1+\cdots+x_r)^n
= \sum_{n_1+\cdots+n_r=n} \frac{n!}{n_1! \cdots n_r!}\,
x_1^{n_1}\cdots x_r^{n_r}.
$$

## 2. Axioms of Probability

### 2.1 Basics

$$
0 \le P(A) \le 1, \qquad P(\Omega)=1.
$$

For pairwise disjoint $A_i$,
$$
P\!\left(\bigcup_{i} A_i\right) = \sum_{i} P(A_i).
$$

### 2.2 Conditional Probability and Independence

Conditional probability:
$$
P(A \mid B) = \frac{P(AB)}{P(B)}.
$$

Law of total probability:
$$
P(A) = P(A \mid B)P(B) + P(A \mid B^{c})P(B^{c}).
$$

Independence of events $A,B$:
$$
P(AB)=P(A)P(B).
$$

## 2.3 Random Variables and Distributions

CDF:

$$
F(x) = P(X \le x).
$$

Discrete (PMF) and continuous (PDF):

$$
p(x)=P(X=x), \qquad \sum_{x} p(x)=1;
$$

$$
P(X \in C)=\int_{C} f(x)\,dx, \qquad
F(x)=\int_{-\infty}^{x} f(s)\,ds.
$$

Joint distributions:

$$
F_{X,Y}(x,y)=P(X\le x,\ Y\le y)
= \int_{-\infty}^{x}\!\!\int_{-\infty}^{y} f(u,v)\,du\,dv.
$$

Independence of random variables:

$$
f_{X,Y}(x,y) = f_X(x)\,f_Y(y).
$$

## 2.4 Expectation, Variance, Covariance

Expectation

Discrete:

$$
E[X] = \sum_{i} x_i\,p(x_i) \quad \text{(discrete)}.
$$

Continuous:

$$
E[X] = \int_{-\infty}^{\infty} x f(x)\,dx \quad \text{(continuous)}.
$$

For a function $g$:

Discrete:

$$
E[g(X)] = \sum_{i} g(x_i)\,p(x_i).
$$

Continuous:

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx.
$$

Variance and covariance:
$$
\operatorname{Var}(X)=E[X^2]-\big(E[X]\big)^2,
\qquad
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
$$

Sum of two variables:
$$
\operatorname{Var}(X+Y) =
\operatorname{Var}(X)+\operatorname{Var}(Y)+2\,\operatorname{Cov}(X,Y).
$$

Correlation:
$$
\operatorname{Corr}(X,Y)=\frac{\operatorname{Cov}(X,Y)}{
\sqrt{\operatorname{Var}(X)\,\operatorname{Var}(Y)}}.
$$

## 2.5 Inequalities and Laws of Large Numbers

Markov (for nonnegative $X$ and $a>0$):
$$
P(X \ge a) \le \frac{E[X]}{a}.
$$

Chebyshev (mean $\mu$, variance $\sigma^2$):
$$
P\big(|X-\mu|\ge k\sigma\big) \le \frac{1}{k^2}.
$$

Weak Law of Large Numbers (i.i.d. mean $\mu$):
$$
\frac{1}{n}\sum_{k=1}^{n} X_k \ \xrightarrow{P}\ \mu.
$$

Strong Law of Large Numbers (i.i.d. mean $\mu$):
$$
\frac{1}{n}\sum_{k=1}^{n} X_k \ \xrightarrow{\text{a.s.}}\ \mu.
$$

## 3. Discrete Distributions

### 3.1 Binomial

$$
P(X=i)=\binom{n}{i} p^{\,i} (1-p)^{\,n-i}, \quad i=0,1,\ldots,n.
$$
$$
E[X]=np, \qquad \operatorname{Var}(X)=np(1-p).
$$

### 3.2 Poisson

$$
P(X=i)=e^{-\lambda}\frac{\lambda^{i}}{i!}, \quad i=0,1,2,\ldots
$$
$$
E[X]=\lambda, \qquad \operatorname{Var}(X)=\lambda.
$$
Limit of Binomial: $n\to\infty$, $p\to 0$, $np=\lambda$.

### 3.3 Geometric (first success on trial $n$)

$$
P(X=n)=(1-p)^{\,n-1}p, \quad n=1,2,\ldots
$$
$$
E[X]=\frac{1}{p}, \qquad \operatorname{Var}(X)=\frac{1-p}{p^{2}}.
$$

### 3.4 Negative Binomial (trials until $r$-th success)

$$
P(X=n)=\binom{n-1}{r-1} p^{\,r} (1-p)^{\,n-r}, \quad n=r,r+1,\ldots
$$
$$
E[X]=\frac{r}{p}, \qquad \operatorname{Var}(X)=\frac{r(1-p)}{p^{2}}.
$$

### 3.5 Hypergeometric (without replacement)

Population has $N+M$ items, $N$ of type A and $M$ of type B. Draw $n$.
$$
P(X=i)=\frac{\binom{N}{i}\,\binom{M}{\,n-i\,}}{\binom{N+M}{n}}.
$$
$$
E[X]=\frac{nN}{N+M}, \qquad
\operatorname{Var}(X)=\frac{nNM}{(N+M)^2}\left(1-\frac{n-1}{N+M-1}\right).
$$

## 4. Continuous Distributions

### 4.1 Uniform on $(a,b)$

$$
f(x)=\frac{1}{b-a}, \quad a<x<b; \qquad
F(x)=\frac{x-a}{b-a} \ \ (a\le x\le b).
$$
$$
E[X]=\frac{a+b}{2}, \qquad \operatorname{Var}(X)=\frac{(b-a)^2}{12}.
$$

### 4.2 Normal

$$
f(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
$$
Standard normal: $Z\sim N(0,1)$, CDF $\Phi\!\left(\frac{x-\mu}{\sigma}\right)$.

### 4.3 Exponential

$$
f(x)=\lambda e^{-\lambda x}, \quad x>0; \qquad
E[X]=\frac{1}{\lambda}, \quad \operatorname{Var}(X)=\frac{1}{\lambda^2}.
$$
Memoryless: $P(X>s+t\mid X>s)=P(X>t)$.

### 4.4 Poisson Process and Gamma

Homogeneous Poisson process with rate $\lambda$:
$$
N(t) \sim \text{Poisson}(\lambda t).
$$
Interarrival times are i.i.d. exponential$(\lambda)$; the sum of $n$ such interarrivals is gamma$(n,\lambda)$.

### 4.5 Nonhomogeneous Poisson Process

Time-varying rate $\lambda(t)$, mean value function
$$
m(t)=\int_{0}^{t} \lambda(s)\,ds.
$$
Then
$$
N(t+s)-N(t) \sim \text{Poisson}\!\left(m(t+s)-m(t)\right).
$$

## 5. Conditional Expectation and Variance

Discrete:
$$
E[X \mid Y=y] = \sum_{x} x \, P(X=x \mid Y=y).
$$

Continuous:
$$
E[X \mid Y=y] = \int_{-\infty}^{\infty} x \, \frac{f(x,y)}{f_Y(y)} \, dx.
$$

Tower property:
$$
E\!\left[ E[X \mid Y] \right] = E[X].
$$

Law of total variance:
$$
\operatorname{Var}(X)=E\!\left[\operatorname{Var}(X\mid Y)\right] + \operatorname{Var}\!\left(E[X\mid Y]\right).
$$
