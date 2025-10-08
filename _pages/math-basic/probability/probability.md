---
title: "Probability"
permalink: /probability/
---

# Probability Theory Cheatsheet

## Introduction
Probability theory forms the foundation of quantitative finance. It provides the mathematical framework to model uncertainty, evaluate risk, and make informed decisions in environments dominated by randomness. From pricing derivatives and evaluating portfolios to designing trading algorithms and conducting statistical inference, probability plays a central role in the toolkit of a quant. This cheatsheet consolidates the essential definitions, theorems, and formulas from probability theory and combinatorics so you can review quickly and apply confidently.

---

## 1. Combinatorial Analysis

### 1.1 Permutations
- For **n distinct objects**, the number of permutations is:
  $$n! = n(n-1)(n-2)\cdots 1$$

- If objects are not distinct, with $n_1, n_2, \ldots, n_r$ alike:
  $$\dfrac{n!}{n_1! \, n_2! \cdots n_r!}$$

**Example:** PEPPER has 6 letters, with 3 P’s and 2 E’s:  
$$\dfrac{6!}{3! \, 2! \, 1!} = 60$$

---

### 1.2 Combinations
- The number of ways to choose $r$ objects from $n$ is:
  $$inom{n}{r} = \dfrac{n!}{(n-r)!r!}$$

Properties:  
- $$inom{n}{0} = inom{n}{n} = 1$$  
- $$inom{n}{i} = 0 \quad 	ext{if } i<0 	ext{ or } i>n$$

**Identity (Pascal):**  
$$inom{n}{r} = inom{n-1}{r-1} + inom{n-1}{r}$$

**Binomial Theorem:**  
$$(x+y)^n = \sum_{k=0}^n inom{n}{k} x^k y^{n-k}$$

**Multinomial Theorem:**  
$$(x_1 + x_2 + \cdots + x_r)^n =
\sum_{n_1+\cdots+n_r=n} \dfrac{n!}{n_1! n_2! \cdots n_r!} \,
x_1^{n_1} \cdots x_r^{n_r}$$

---

## 2. Axioms of Probability

### 2.1 Basic Axioms
1. $$0 \leq P(A) \leq 1$$
2. $$P(\Omega) = 1$$
3. For mutually exclusive $A_i$:  
   $$P\left(igcup_i A_iight) = \sum_i P(A_i)$$

---

### 2.2 Conditional Probability and Independence
- Conditional probability:  
  $$P(A\mid B) = \dfrac{P(AB)}{P(B)}$$

- Law of total probability:  
  $$P(A) = P(A\mid B)P(B) + P(A\mid B^c)P(B^c)$$

- Independence: $$P(AB)=P(A)P(B)$$

---

## 2.3 Random Variables

- **CDF:** $$F(x) = P(X \leq x)$$  
- **PMF (discrete):** $$p(x)=P(X=x), \ \sum p(x)=1$$  
- **PDF (continuous):** $$P(X\in C)=\int_C f(x)\,dx$$, with  
  $$F(x)=\int_{-\infty}^x f(s)\,ds$$  

- **Joint Distribution:**  
  $$F_{X,Y}(x,y) = \int_{-\infty}^x \int_{-\infty}^y f(u,v)\,du\,dv$$

- **Independence:** $$f_{X,Y}(x,y)=f_X(x)f_Y(y)$$

---

## 2.4 Expectation

- **Discrete:** $$E[X] = \sum_i x_i \, p(x_i)$$  
- **Continuous:** $$E[X] = \int_{-\infty}^{\infty} x f(x) \, dx$$  
- **Function of RV:**  
  $$E[g(X)] = \sum_i g(x_i)p(x_i) \quad 	ext{or} \quad \int g(x)f(x) \, dx$$

---

## 2.5 Variance and Covariance

- Variance: $$Var(X)=E[X^2]-(E[X])^2$$  
- Covariance: $$Cov(X,Y)=E[XY]-E[X]E[Y]$$  
- Variance of sum: $$Var(X+Y)=Var(X)+Var(Y)+2\,Cov(X,Y)$$  
- Correlation:  
  $$Corr(X,Y)=\dfrac{Cov(X,Y)}{\sqrt{Var(X)\,Var(Y)}}$$

---

## 2.6 Markov & Chebyshev Inequalities

- **Markov:** $$P(X\geq a)\leq \dfrac{E[X]}{a}, \quad a>0$$  
- **Chebyshev:** $$P(|X-\mu|\geq k\sigma)\leq \dfrac{1}{k^2}$$  

---

## 2.7 Law of Large Numbers

- **Weak Law:** Sample mean converges in probability to $\mu$.  
- **Strong Law:** Sample mean converges almost surely to $\mu$.  

---

## 3. Some Discrete Distributions

### 3.1 Binomial
- PMF: $$P(X=i)=inom{n}{i}p^i(1-p)^{n-i}$$  
- Mean: $$E[X]=np$$  
- Var: $$Var(X)=np(1-p)$$  

### 3.2 Poisson
- PMF: $$P(X=i)=e^{-\lambda}\dfrac{\lambda^i}{i!}$$  
- Mean: $$\lambda$$, Var: $$\lambda$$  
- Limit of Binomial: $$n	o\infty,\ p	o 0,\ np=\lambda$$  

### 3.3 Geometric
- PMF: $$P(X=n)=(1-p)^{\,n-1}p$$ (first success on trial $n$).  
- Mean: $$1/p$$, Var: $$(1-p)/p^2$$  

### 3.4 Negative Binomial
- PMF: $$P(X=n)=inom{n-1}{r-1} p^r (1-p)^{\,n-r}$$ (trials until $r$-th success).  
- Mean: $$r/p$$, Var: $$r(1-p)/p^2$$  

### 3.5 Hypergeometric
- Sampling without replacement from $N+M$ balls ($N$ light, $M$ dark).  
- PMF:  
  $$P(X=i)=\dfrac{inom{N}{i}inom{M}{\,n-i\,}}{inom{N+M}{n}}$$  
- Mean: $$\dfrac{nN}{N+M}$$  
- Var:  
  $$\dfrac{nNM}{(N+M)^2}\left(1-\dfrac{n-1}{N+M-1}ight)$$  

---

## 4. Continuous Random Variables

### 4.1 Uniform $(a,b)$
- PDF: $$f(x)=\dfrac{1}{b-a}, \quad a<x<b$$  
- Mean: $$(a+b)/2$$  
- Var: $$(b-a)^2/12$$  
- CDF: $$(x-a)/(b-a)$$  

### 4.2 Normal
- PDF:  
  $$f(x)=\dfrac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\dfrac{(x-\mu)^2}{2\sigma^2}ight)$$  
- Standard normal: $$Z\sim N(0,1)$$  
- CDF: $$\Phi\!\left(\dfrac{x-\mu}{\sigma}ight)$$  

### 4.3 Exponential
- PDF: $$f(x)=\lambda e^{-\lambda x}, \quad x>0$$  
- Mean: $$1/\lambda$$, Var: $$1/\lambda^2$$  
- Memoryless property:  
  $$P(X>s+t\mid X>s)=P(X>t)$$  

### 4.4 Comparing Geometric, Poisson, Exponential
- **Geometric (discrete):** trials until first success.  
- **Poisson (discrete):** number of events in an interval.  
- **Exponential (continuous):** waiting time until the next event.

### 4.5 Poisson Process & Gamma Distribution
- Poisson process with rate $\lambda$: $$N(t)\sim 	ext{Poisson}(\lambda t)$$.  
- Interarrival times are i.i.d. exponential$(\lambda)$.  
- **Gamma$(n,\lambda)$** is the sum of $n$ i.i.d. exponential$(\lambda)$ variables.

### 4.6 Nonhomogeneous Poisson Process
- Time–varying rate $\lambda(t)$.  
- Mean value function: $$m(t)=\int_0^t \lambda(s)\,ds$$.  
- Increments: $$N(t+s)-N(t)\sim 	ext{Poisson}\!ig(m(t+s)-m(t)ig)$$.  

---

## 5. Conditional Expectation & Variance

- **Discrete:**  
  $$E[X\mid Y=y]=\sum_x x \, P(X=x\mid Y=y)$$  
- **Continuous:**  
  $$E[X\mid Y=y]=\int x \, \dfrac{f(x,y)}{f_Y(y)} \, dx$$  

**Tower property:**  
$$E\!\left[E[X\mid Y]ight]=E[X]$$  

**Law of total variance:**  
$$Var(X)=E\!\left[Var(X\mid Y)ight] + Var\!\left(E[X\mid Y]ight)$$

---
