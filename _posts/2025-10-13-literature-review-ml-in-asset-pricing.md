---
title: "Machine Learning in Empirical Asset Pricing"
excerpt: "A Comprehensive Literature Review (Up to 2025)"
tags:
  - factor models
  - machine learning
  - literature review
permalink: /literature-review-ml-in-asset-pricing/
header:
  overlay_image: /assets/images/headers/ml_header_dark.png
  overlay_filter: 0.2
---

## Introduction

Empirical asset pricing is undergoing a transformation with the advent
of big data and machine learning (ML). Traditional linear factor models
like the Capital Asset Pricing Model (CAPM) and Fama--French frameworks
offer economic intuition but struggle to accommodate the *"factor zoo"*
of hundreds of discovered return predictors and complex nonlinear
relationships[\[1\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=Empirical%20asset%20pricing%20is%20undergoing,the%20stochastic%20discount%20factor%20is)[\[2\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=The%20latest%20development%20in%20empirical,approach%20they%20employ%3A%20regularization%2C%20dimension).
ML methods, by contrast, offer greater flexibility and predictive power
in high-dimensional
settings[\[1\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=Empirical%20asset%20pricing%20is%20undergoing,the%20stochastic%20discount%20factor%20is).
Recent research leverages ML to address central asset pricing tasks --
from predicting stock returns to constructing better factor models --
often yielding improved out-of-sample performance but raising new
challenges regarding interpretability and economic
insight[\[2\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=The%20latest%20development%20in%20empirical,approach%20they%20employ%3A%20regularization%2C%20dimension).
This review synthesizes the academic literature, both foundational and
cutting-edge, on applying ML in empirical asset pricing. We organize the
discussion around key application areas, methodological innovations,
comparisons with traditional approaches, emerging trends, data and
evaluation practices, and known limitations. Throughout, we cite
representative studies to illustrate how machine learning is reshaping
asset pricing research.

## Applications of Machine Learning in Asset Pricing

### Return Prediction in the Cross-Section and Time Series

A primary focus of ML in finance has been predicting asset returns --
both the cross-section of individual stock returns and the time-series
of aggregate market returns. **In the cross-section**, researchers use
ML to forecast which stocks will earn higher future returns (i.e. to
measure firms' risk premia). Pioneering work by Gu, Kelly, and Xiu
(2020) compares a variety of ML algorithms on U.S. equities and finds
they substantially outperform traditional regressions in predicting
returns[\[3\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20perform%20a%20comparative%20analysis,on%20momentum%2C%20liquidity%2C%20and%20volatility).
In economic terms, portfolios formed using ML forecasts can *double* the
Sharpe ratio of strategies based on classic linear
models[\[3\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20perform%20a%20comparative%20analysis,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the).
For example, a long--short portfolio trading on stock-level return
predictions from a neural network achieved an out-of-sample Sharpe ratio
of 1.35, more than double that of a leading linear factor-based strategy
(0.67) in the same
sample[\[5\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=relative%20to%20preceding%20literature%20that,based%20strategy%20from%20the%20literature).
The best-performing algorithms in this study were nonlinear models --
tree ensembles and deep neural networks -- which can capture predictor
interactions that linear methods
miss[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility).
Notably, despite the flexibility of ML, there is broad agreement on
*which* variables matter most for prediction: both linear and nonlinear
methods consistently emphasize a handful of firm characteristics (e.g.
past return **momentum**, liquidity measures, and volatility-related
metrics) as the dominant return
predictors[\[7\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=from%20the%20literature,on%20momentum%2C%20liquidity%2C%20and%20volatility).
This not only validates decades of anomaly research identifying these
effects, but also suggests ML models are detecting many of the same risk
factors or mispricing indicators identified by traditional approaches.

Beyond individual stocks, ML has also been applied to **forecast
aggregate market returns** (the equity risk premium over time). Classic
studies like Welch and Goyal (2008) showed the difficulty of predicting
the market using a few economic indicators. ML offers a way to exploit
many predictors and potential nonlinear dynamics. For instance, Feng,
He, and Polson (2018) use deep learning on the historical U.S.
macroeconomic and market data, showing that nonlinear combinations of
predictors can improve out-of-sample forecasts of market
returns[\[8\]](https://arxiv.org/abs/1804.09314#:~:text=,the%20extremes%20of%20the%20characteristic).
Their deep neural network uncovers *"nonlinear factors"* that enhance
predictability, especially at the extremes of the predictor space (e.g.
during extreme market conditions), which a simple linear model would
miss[\[8\]](https://arxiv.org/abs/1804.09314#:~:text=,the%20extremes%20of%20the%20characteristic).
Gu, Kelly, and Xiu (2020) likewise apply ML to time-series market return
prediction and find meaningful economic gains: timing the market with an
ML-forecasted signal (e.g. a neural network using dozens of macro
predictors) yields a substantially higher Sharpe ratio than a static
buy-and-hold
strategy[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the).
These results illustrate that ML can extract signal from the noisy
financial data that confound traditional time-series regressions,
although the improvements are modest in absolute terms and often
sensitive to how well models guard against overfitting.

**Why ML helps in return prediction.** Two characteristics of return
prediction problems make them well-suited to ML techniques. First, the
set of candidate predictor variables is enormous. Decades of research
have produced **hundreds** of potential stock-return predictors (firm
characteristics or "anomalies") and dozens of macroeconomic variables
for market
timing[\[9\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Second%2C%20the%20collection%20of%20candidate,and%20dimension%20reduction%20techniques%2C%20machine).
Many of these predictors are correlated and relatively weak, making it
challenging for traditional OLS or small-scale models to select the true
signals. ML methods excel at high-dimensional variable selection and can
handle cases where the number of predictors $P$ approaches or exceeds
the number of observations $N$ by using regularization and dimension
reduction[\[9\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Second%2C%20the%20collection%20of%20candidate,and%20dimension%20reduction%20techniques%2C%20machine).
Second, the relationship between predictors and returns may be complex.
There is no guarantee that effects are strictly linear or additive;
interactions and nonlinear functional forms can arise (e.g. an earnings
yield may matter only for small firms, an interaction a linear model
would miss). Machine learning algorithms (like trees and neural nets)
can flexibly model such nonlinearities and interactions, searching a
vast space of functional forms for patterns that improve
predictions[\[10\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Third%2C%20further%20complicating%20the%20problem,linear%20models%20to%20regression%20trees)[\[11\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=variables%20and%20functional%20forms,overfit%20biases%20and%20false%20discovery).
By addressing both the *"wide data"* problem (too many predictors) and
the *"unknown functional form"* problem, ML has pushed the frontier of
risk premium measurement in the cross-section and time
series[\[12\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=various%20researchers%20have%20argued%20possess,condensing%20redundant%20variation%20among%20predictors)[\[10\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Third%2C%20further%20complicating%20the%20problem,linear%20models%20to%20regression%20trees).

Empirically, the application of ML to return forecasting has revealed
that much of the incremental predictive power comes from better handling
of well-known effects and combinations thereof, rather than discovering
entirely new anomalies. For example, both Gu et al. (2020) and
Freyberger et al. (2020) find that **past return measures** (momentum or
short-term reversal signals) are among the most powerful features in
explaining the cross-section of stock
returns[\[13\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=networks,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and).
Freyberger, Neuhierl, and Weber (2020) applied an adaptive group LASSO
(with nonparametric spline terms) to 62 firm characteristics and
confirmed that *"past-return-based predictors stand out"* as providing
independent information, whereas many other touted anomalies added
little incremental
power[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
In their nonparametric framework, only a small subset of characteristics
-- primarily those related to momentum and reversals -- had robust
predictive content once redundant or spurious signals were
penalized[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and)[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
These results reinforce the idea that markets contain a few strong
cross-sectional return drivers and a long tail of weaker effects, and ML
methods are useful for distinguishing the former from the latter. At the
same time, studies note that the gains from complex ML models are not
uniform across all stocks: the most substantial predictive improvements
tend to concentrate in small and illiquid
stocks[\[16\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=type%20II%20errors%20are%20a,predictable%20throughout%20the%20entire%20sample).
For large blue-chip firms, which are closely followed by investors, even
powerful ML algorithms often find little predictability beyond what
simple models
capture[\[16\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=type%20II%20errors%20are%20a,predictable%20throughout%20the%20entire%20sample).
This suggests that ML is largely picking up mispricing or risk effects
that are strongest where arbitrage is limited (small stocks), consistent
with market efficiency imposing a lower bound on predictability for
heavily traded assets.

### Factor Models, the Stochastic Discount Factor, and the "Factor Zoo"

Another major application of ML in asset pricing is in **factor model
construction and anomaly selection** -- essentially, making sense of the
factor zoo. Traditional empirical asset pricing revolves around
explaining returns through a linear combination of factors (portfolios
or characteristics) that carry risk premia. However, with hundreds of
published anomalies, a key challenge is to **identify which factors
truly matter** and to parsimoniously model the stochastic discount
factor (SDF) or pricing kernel. Machine learning is being used to (a)
**select or reduce** large sets of candidate factors, and (b) **discover
latent factors** or functional forms that better explain asset returns.

One thread of research uses **regularization and model selection
techniques** to tame the factor zoo. For example, Feng, Giglio, and Xiu
(2020) propose a LASSO-based procedure to systematically test the
marginal contribution of new factors in the presence of many existing
ones[\[17\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=%E2%80%93%20Feng%2C%20Giglio%2C%20and%20Xiu,parametric%20LASSO).
Applying this to a universe of 99 reported anomalies, they find that
only on the order of **14 factors** are truly important -- the rest
provide redundant or negligible explanatory power once the important
ones are in the
model[\[17\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=%E2%80%93%20Feng%2C%20Giglio%2C%20and%20Xiu,parametric%20LASSO).
This result dramatically highlights how ML can cut through the noise of
numerous candidate factors and isolate a sparse set of dominant returns
drivers. In a related vein, *shrinking* or penalizing factor models has
proven effective. Kozak, Nagel, and Santosh (2020) show that imposing
heavy shrinkage toward a zero risk premium on a large set of factors
results in a model that effectively uses just a few composite factors,
yet prices the cross-section almost as well as using the full set of
characteristics[\[18\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=,2020%29%20find%20significant).
Such approaches borrow the bias--variance tradeoff perspective from ML
to improve out-of-sample performance of factor models: by allowing a
small bias (excluding many weak factors) they achieve lower variance and
better predictive stability.

A complementary line of work uses **dimension reduction and latent
factor discovery** via ML. These methods recognize that the plethora of
firm characteristics may reflect a smaller number of underlying risk
factors. Traditional tools like principal components analysis (PCA) have
been used to extract latent factors, but ML offers more sophisticated
variants. Kelly, Pruitt, and Su (2019) introduce *Instrumented Principal
Component Analysis (IPCA)*, an algorithm that treats firm
characteristics as instruments to identify latent factors and their
time-varying loadings. This technique effectively bridges
characteristics and factor modeling, and was shown to outperform
conventional factor models in explaining asset
returns[\[19\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=characteristics%20%28Freyberger%20et%20al,them%20to%20circumvent%20daunting%20issues).
Another example is Lettau and Pelger's (2020) *"max Sharpe ratio" PCA*,
which is a modified PCA that weights covariance information by assets'
mean returns, thereby extracting factors that are not just statistically
important but also carry high risk premia. This method, which can be
seen as an ML-enhanced unsupervised learning of factors, yields improved
pricing of cross-sectional returns compared to unweighted PCA
factors[\[20\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=low,2011%29%E2%80%99s%20advice).
There have also been experimental uses of **autoencoders and matrix
completion** techniques (common in ML for uncovering low-dimensional
structure) to identify factors from large panels of asset
returns[\[21\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=We%20survey%20recent%20methodological%20contributions,harnessing%20modern%20tools%20with%20rigor).
These approaches often find that a few nonlinear combinations of
characteristics can reproduce the cross-section about as well as dozens
of raw anomalies, reinforcing the idea of a low-dimensional factor
structure underlying the apparent
complexity[\[20\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=low,2011%29%E2%80%99s%20advice).

Rather than building factor models in a two-step fashion (first
identifying factors, then running cross-sectional regressions), some
researchers directly target the **stochastic discount factor** using ML.
The SDF $m_{t+1}$ prices assets by $E[m_{t+1}R_{i,t+1}]=1$ for
all assets $i$, and it can in principle be expressed as a function of
many state variables or characteristics. Machine learning can be used to
estimate this function flexibly. **Deep neural networks** have been
deployed to approximate the SDF, treating asset returns and
characteristics as training data for a complex function
$m_{\theta}(Z_i)$ that minimizes pricing errors. Chen, Pelger, and
Zhu (2023) provide a notable example: they use a deep learning model to
estimate an SDF for individual stocks, incorporating a "no-arbitrage"
loss function to ensure the network's predictions satisfy the absence of
arbitrage
opportunities[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).
Their innovations include using an *adversarial approach* to generate
test assets that stress-test the model (improving robustness) and
incorporating a large number of macroeconomic time series to capture the
state of the
economy[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).
The resulting deep SDF model significantly outperforms traditional
factor models out-of-sample, achieving higher Sharpe ratios and lower
pricing errors (mean absolute unexplained returns) than benchmarks like
Fama--French, and it *"identifies the key factors that drive asset
prices."*[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).
In essence, the network discovers a few composite factors (combinations
of characteristics and macro variables) that mimic the complex nonlinear
SDF. This and similar efforts (e.g. autoencoder-based
SDFs[\[21\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=We%20survey%20recent%20methodological%20contributions,harnessing%20modern%20tools%20with%20rigor))
highlight ML's ability to integrate information from myriad sources into
a coherent pricing model. Importantly, researchers often impose economic
structure in these models -- for example, Chen *et al.* enforce the
fundamental *no-arbitrage* condition in the training objective -- to
ensure the ML-driven SDF remains grounded in financial
theory[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).

**Handling the factor zoo.** A central theme across these studies is
addressing the proliferating number of factors or anomalies in a
statistically rigorous way. Whereas traditional approaches might add new
factors one-by-one (running the risk of *p-hacking* and overfitting),
machine learning enables a more **systematic evaluation of predictors**.
By penalizing complexity (LASSO, ridge, etc.), ML methods control
overfit and avoid selecting spurious factors that don't truly improve
pricing. For instance, Freyberger *et al.* (2020) not only selected
which characteristics matter, but by allowing flexible functional forms
for each, they could detect non-monotonic or conditional effects (like
nonlinearity in size or value effects) that fixed linear factors would
miss[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
They found that most firm characteristics contributed little once a core
subset (including momentum) was in the model, and that allowing
nonlinear transforms did not radically change which characteristics were
chosen -- it mainly refined how they were
modeled[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
Another insight from this literature is that many anomalies might be
manifestations of a **few broad themes** (e.g. momentum, liquidity,
investment, intangibles, etc.), and ML can help cluster or reduce the
factors accordingly. For example, when Feng, Giglio, and Xiu (2020)
winnowed 99 factors down to 14, those that survived tended to correspond
to well-known categories like momentum, volatility,
quality/profitability, and
investment[\[17\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=%E2%80%93%20Feng%2C%20Giglio%2C%20and%20Xiu,parametric%20LASSO).
In practical terms, such results are encouraging: they suggest that
despite the deluge of proposed factors, asset returns can be
parsimoniously explained by a limited set of robust factors -- which ML
techniques can help identify. This dovetails with theoretical work
arguing for a low-dimensional risk structure and provides a degree of
comfort that ML isn't just fitting noise but is often rediscovering
sensible economic factors.

## Theoretical and Methodological Advances: Key ML Models Employed

Methodologically, the incursion of machine learning into asset pricing
has introduced a toolkit of models and algorithms beyond the traditional
econometric repertoire. Here we outline the main classes of ML models
used in empirical asset pricing, highlighting what they contribute:

- **Penalized Regression (LASSO, Ridge, Elastic Net):** Regularization
methods constrain or shrink regression coefficients to prevent
overfitting and perform variable selection. In asset pricing,
*LASSO* (Least Absolute Shrinkage and Selection Operator) has been a
workhorse for selecting the most important factors or
characteristics from a large
pool[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
For example, studies have applied LASSO in cross-sectional return
prediction to decide which firm characteristics to include, finding
it improves prediction accuracy over OLS by reducing
noise[\[23\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=We%20investigate%20whether%20Lasso,predictable%20throughout%20the%20entire%20sample).
LASSO tends to outperform OLS especially when avoiding **Type II
errors** (missing true predictors) is
important[\[23\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=We%20investigate%20whether%20Lasso,predictable%20throughout%20the%20entire%20sample).
Variants like *adaptive group LASSO* (used by Freyberger *et
al.* 2020) go further by selecting whole groups of feature
expansions, enabling discovery of nonlinear effects while keeping
the model
sparse[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
*Ridge regression* (which shrinks coefficients continuously rather
than zeroing them out) has been used in factor shrinkage contexts
(e.g. Kozak *et al.* 2020) to infer a low-dimensional factor
structure. **Elastic net** combines LASSO and ridge penalties, and
is useful when there are many correlated predictors -- a frequent
situation with stock characteristics. Overall, penalized regressions
have become a fundamental tool to address the high-dimensionality in
asset pricing
problems[\[9\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Second%2C%20the%20collection%20of%20candidate,and%20dimension%20reduction%20techniques%2C%20machine),
effectively guarding against overfitting while selecting relevant
predictors.

- **Tree-Based Methods (Regression Trees, Random Forests, Gradient
Boosting):** Tree models recursively partition the predictor space
to fit piecewise constant predictions, which can capture complex
interaction effects. *Regression trees* by themselves are simple and
interpretable (much like decision rules), though often not very
predictive. However, *ensemble* tree methods such as **Random
Forests** (which average many randomized trees) and **Boosted
Trees** (which iteratively grow trees to correct errors) have shown
strong performance in asset pricing
tasks[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility).
These methods can model **nonlinear interactions** between
characteristics -- for example, a random forest can implicitly learn
that a value factor matters only among small-cap stocks, by
splitting first on size then on valuation. Gu *et al.* (2020) report
that tree-based models were among the best predictors for stock
returns, rivaled only by neural
networks[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility).
An advantage of tree ensembles is that they provide measures of
*variable importance* (how much each predictor improves the splits),
which can be used to rank which features are most influential. This
often aids interpretability: even if the model is complex, one can
see that, say, **momentum, size,** and **volatility** were the top
drivers -- consistent with domain knowledge. Tree methods tend to be
robust against outliers and can naturally accommodate different
predictor types. In finance applications, gradient boosting
(including XGBoost) and random forests have been used not only for
return prediction but also for classification tasks like default
prediction and for constructing *characteristic-sorted portfolios*
in novel
ways[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and).
A limitation, however, is that ensemble trees are less interpretable
than a simple linear model or a single decision tree, so their
economic meaning needs careful extraction.

- **Neural Networks (Deep Learning):** Neural networks are flexible
function approximators composed of layers of interconnected
"neurons" (nonlinear transformations). They can capture extremely
rich patterns, including highly nonlinear interactions, at the cost
of being the least transparent model and requiring large data and
tuning. In asset pricing, **deep neural networks** have been applied
to both cross-sectional and time-series problems. For predicting
stock returns, multilayer feed-forward networks (often with 2--3
hidden layers) have been used to map dozens of firm characteristics
to future
returns[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility).
These nets often outperform other methods by fitting complex
relations, but they require regularization techniques like dropout
or weight decay to avoid overfitting the noise in financial
data[\[24\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=important%20limitations%20%28Dixon%20et%20al,which%20shrink%20the%20network%20weights).
As noted, Gu *et al.* found dense neural networks performed on par
with tree ensembles as the best return
predictors[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility).
For conditional factor models and SDF estimation, more specialized
architectures have been explored. Chen *et al.* (2023) use a deep
network with an input layer for stock characteristics and macro
variables, multiple hidden layers, and an output that represents the
SDF, trained under a no-arbitrage
condition[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).
Others have tried **recurrent neural networks** (e.g. LSTM models)
to capture time-series dynamics in return
predictors[\[25\]](https://arxiv.org/abs/1804.09314#:~:text=returns,the%20extremes%20of%20the%20characteristic),
though this is still nascent. The great flexibility of neural
networks means they can in principle approximate the true but
unknown asset pricing function very well; however, their *"black
box"* nature makes it hard to interpret what they have learned, and
they are *"coupled with high risks of overfitting"* if not carefully
constrained[\[24\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=important%20limitations%20%28Dixon%20et%20al,which%20shrink%20the%20network%20weights).
Ensemble approaches (e.g. averaging multiple network
initializations) can improve stability but at the cost of even more
complexity[\[24\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=important%20limitations%20%28Dixon%20et%20al,which%20shrink%20the%20network%20weights).
As a result, while deep learning has achieved top predictive
performance in several
studies[\[3\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20perform%20a%20comparative%20analysis,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[26\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=adversarial%20approach%20and%20to%20extract,factors%20that%20drive%20asset%20prices),
researchers are actively working on ways to make neural network
models more transparent and aligned with financial theory (discussed
more under *Emerging Trends*).

- **Hybrid and Other Models:** Some works combine elements of the
above methods or embed ML into traditional frameworks. For example,
*Partial Least Squares (PLS)* and *Principal Components Regression*
are classical dimension reduction tools that have seen renewed use
as benchmarks in the age of
ML[\[27\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20study%20a%20set%20of,boosted%20trees%20and%20random%20forests).
Bayesian machine learning approaches (e.g. Bayesian additive
regression trees, variational autoencoders for factors) provide
probabilistic predictions and have been proposed to quantify the
uncertainty in return
forecasts[\[28\]](https://arxiv.org/html/2503.00549v1#:~:text=1%20arxiv,develop%20new%20methods%20to).
There are also *two-stage learners* (sometimes called *"double ML"*)
where one stage might predict an intermediate parameter (like factor
loadings or state variables) and another stage uses those for
returns -- these allow integrating economic structure into ML
predictions[\[21\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=We%20survey%20recent%20methodological%20contributions,harnessing%20modern%20tools%20with%20rigor).
Ensemble methods in general (bagging, boosting, model stacking) are
popular to improve predictive robustness: for instance, averaging
across many different ML models can reduce variance and deliver more
stable out-of-sample performance, albeit at a loss of
interpretability. In sum, the methodological advances in this
literature are not about inventing brand-new algorithms, but rather
**adapting and selecting the right tools from machine learning to
solve asset pricing problems**. The choice of method often depends
on the task: if the goal is *interpretation* and insight, a simpler
model with regularization (like LASSO or a shallow tree) might be
preferred; if pure *prediction accuracy* is the aim, ensemble trees
or deep networks might be deployed and later analyzed for economic
meaning.

## Comparing ML Models to Traditional Approaches

A recurring question is how these ML-based models compare to the
classical econometric approaches long used in asset pricing -- both in
terms of predictive performance and in terms of economic
interpretability.

**Predictive performance.** Across numerous studies, ML models have
demonstrated superior predictive accuracy relative to traditional linear
models when evaluated out-of-sample. This is evident in metrics like
*out-of-sample $R^2$* (the fraction of variance of returns explained
in fresh data) and investor utility gains. Gu *et al.* report that their
machine learning methods achieved **higher out-of-sample $R^2$** than
any prior literature on U.S. stock returns, even after accounting for
the inherent difficulty of
prediction[\[29\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Our%20primary%20contributions%20are%20twofold,51%20Sharpe%20ratio%20of%20a).
The improvements, while statistically significant, are on the order of a
few percentage points in $R^2$ -- reflecting the noisy nature of
returns -- but in economic terms these translate into substantial gains
for a mean-variance
investor[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the).
As noted earlier, timing the market with ML forecasts or forming
long--short stock portfolios based on ML yields Sharpe ratios far above
those obtained by models like CAPM or
Fama--French[\[5\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=relative%20to%20preceding%20literature%20that,based%20strategy%20from%20the%20literature).
Moreover, ML can **adapt to structural changes** or detect
regime-specific predictors more quickly than static models, potentially
maintaining performance in evolving markets (though this claim is still
being tested with longer samples). It's important to emphasize that
traditional factor models are typically designed for *explanatory power*
and economic interpretation rather than pure prediction, so a degree of
performance gap is expected when forecasting criteria are optimized.
Even so, the magnitude of ML's predictive edge in many studies
underscores that classical models left valuable predictive information
on the table -- information that ML algorithms have been able to exploit
by considering more variables and complex relationships.

**Economic interpretability.** On the flip side of the performance coin
is the question of interpretability. Traditional asset pricing models
have a clear economic narrative: each factor has a story (market risk,
size, value, etc.), and linear exposures (betas) measure an asset's
sensitivity to those factors. This transparency allows researchers and
practitioners to debate the *economic mechanisms* (risk-based or
behavioral) behind asset returns. Machine learning models, especially
high-dimensional or nonlinear ones, often sacrifice this clarity. A
random forest or a neural network with dozens of inputs is essentially a
black box -- it may yield accurate predictions, but understanding *why*
a particular stock is predicted to have high returns can be difficult.
As Bagnara (2024) notes in a critical review, *"probably the biggest
downside of ML methods is their lack of
interpretability."*[\[30\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Giglio%20and%20Xiu%2C%202021%29,This%20partially)
The complexity that gives ML its edge also means the models do not
readily produce human-interpretable parameters analogous to factor
premia or betas. This lack of interpretability is not just an academic
concern; it matters for practical implementation (e.g. portfolio
managers need to trust and explain their models) and for connecting
empirical results back to theory.

That said, researchers are finding ways to **extract economic insight
from ML models**. One straightforward approach is to examine which
predictors the model relies on most. As discussed, even complex ML
models tend to highlight familiar predictors like momentum, liquidity,
and volatility as
important[\[13\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=networks,on%20momentum%2C%20liquidity%2C%20and%20volatility),
providing reassurance that ML isn't finding arbitrary patterns that
contradict known finance principles. Some studies report that
ML-predicted returns still conform to known risk factor structures. For
example, portfolios sorted on ML forecasts have been shown to have large
exposures to factors like momentum and quality, implying the ML is in
part repackaging these known
strategies[\[13\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=networks,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and).
Another strategy to improve interpretability is to impose economic
structure on the model *ex ante*. Chuan Shi (2025) advocates a unified
framework based on the **stochastic discount factor** that integrates
machine learning **while preserving economic
interpretability**[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance).
By forcing the ML model to take the form of an SDF (essentially a
weighted combination of asset payoffs or characteristics that prices all
assets), one can ensure the outputs have the interpretation of state
prices or factor risk prices. This approach can bridge the gap between
traditional theory and ML: the ML model can be very flexible in how it
forms the SDF from inputs, but the end object is still an SDF that one
can analyze in terms of priced risk dimensions.

There is also a growing use of **explainable AI (XAI) techniques** to
interpret ML models in finance. Methods like *partial dependence plots*,
*Shapley value decomposition*, and *LIME* (Local Interpretable
Model-agnostic Explanations) can be applied to complex models to gauge
the effect of each input on the prediction. For instance, one can
compute the Shapley values for each characteristic on a particular
stock's predicted return to see which traits contributed most to a high
or low forecast. These tools can sometimes reveal economically sensible
patterns (e.g. the model gives a boost to stocks with high momentum or
low valuations, consistent with anomaly literature) or detect nonlinear
thresholds (e.g. maybe the model only values an earnings yield once it's
above a certain level, indicating a nonlinear value effect). Although
these techniques provide insight, they are essentially *post hoc* and do
not replace having a simple model. Thus, a tension remains: **ML models
excel in predictive power, but traditional models excel in
transparency**. The consensus in recent literature is that ML and
classical approaches should be seen as complements: ML can uncover
patterns and push the frontier of predictability, while economic theory
and simple models are vital for interpreting those patterns and ensuring
they make sense. As one survey put it, the goal is to harness ML's power
*"with rigor, robustness, and power to make new asset pricing
discoveries"* in a way that advances our understanding of
markets[\[32\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=returns%2C%20factors%2C%20risk%20exposures%2C%20risk,future%20research%20and%20methodological%20advances).

## Emerging Trends and Future Directions

The intersection of machine learning and asset pricing is evolving
rapidly. We highlight several emerging trends and research frontiers
that are shaping this field:

- **Interpretability and Explainability:** Addressing the black-box
nature of ML models has become a priority. Recent studies explicitly
call for enhancing the interpretability of deep learning models in
finance to increase their utility for both practitioners and
academics[\[33\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=area%3A%20time,potentially%20usher%20in%20groundbreaking%20developments).
This has led to a surge in work on explainable AI tailored to asset
pricing. Researchers are exploring restriction of model complexity
(e.g. using **monotonic neural networks** that enforce economically
plausible monotonic relations between characteristics and returns)
and developing visualization tools to interpret ML predictions. For
example, partial dependence analysis can illustrate how predicted
returns change as one characteristic varies (holding others fixed),
shedding light on whether the ML model's inferred relationship is
linear, threshold-based, or something more complex. Another trend is
**proximate modeling**, where a simpler model is trained to
approximate the predictions of a complex model -- essentially
distilling the ML model's knowledge into an interpretable form. The
literature is also embracing the idea of *"opening the black box"*
by examining learned representations: for instance, in a deep
network that produces an SDF, one might try to interpret the
intermediate layers as latent factors or economic signals. While
full interpretability remains challenging, the intent is clear: ML
models in asset pricing will not gain full acceptance until we can
understand and trust the basis of their forecasts. We expect future
work to incorporate more *economic constraints or priors* (e.g.
no-arbitrage, positivity of certain effects, diminishing returns,
etc.) directly into model architectures to ensure outputs are not
only accurate but also make economic
sense[\[33\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=area%3A%20time,potentially%20usher%20in%20groundbreaking%20developments).

- **Integration with Economic Theory:** A related trend is combining
machine learning models with traditional economic theory to create
hybrid approaches. Rather than viewing ML and theory-driven models
as separate, researchers are finding ways to enforce theory within
ML or use ML to test theory. One example is the **no-arbitrage
regularization** used by Chen *et al.* (2023), where the network is
penalized based on pricing errors to adhere to arbitrage-free
pricing[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices).
Another example is constraining ML models to respect known
equilibrium relations -- for instance, ensuring that if a
characteristic is theoretically linked to higher expected returns
(say via a risk story), the ML model is structured to capture a
monotonically increasing relationship. There is growing interest in
*"structural ML"* where machine learning methods are used to
estimate models that come from solving economic agents' problems
(such as consumption-based asset pricing models with investor
heterogeneity), blending deep learning with deep theory. While still
in early stages, such approaches could allow estimation of complex
general equilibrium models that were previously intractable, using
techniques like reinforcement learning to solve for equilibrium
policies or pricing kernels. More immediately, researchers like
Chuan Shi (2025) propose integrating ML into the **stochastic
discount factor framework**, which is fundamentally grounded in
asset pricing theory, thereby *"preserving economic
interpretability"* and rigor even as we unleash flexible
algorithms[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance).
This kind of integration will likely intensify, as it offers a path
to ensure ML advances are not just statistical tricks but contribute
to the core understanding of what drives asset prices.

- **Combining ML with Traditional Models (Ensemble or Two-Stage
Approaches):** A practical emerging trend is to use ML in
conjunction with simpler models rather than outright replacing them.
For example, one might use machine learning to **screen or transform
inputs** to a traditional regression -- essentially using ML for
feature engineering -- and then use a linear model for the final
pricing equation. Alternatively, ML could generate candidate factors
which are then tested in a classic Fama--MacBeth two-pass setting
for statistical significance. This hybrid approach is appealing
because it leverages ML's ability to sift through data while
retaining the familiarity of linear factors for the end result. An
illustration is the work of Bryzgalova, Pelger, and Zhu (2021), who
combine ML-based portfolio optimization with the Fama--MacBeth
procedure to construct factors that maximize Sharpe ratio under
certain
constraints[\[19\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=characteristics%20%28Freyberger%20et%20al,them%20to%20circumvent%20daunting%20issues)[\[20\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=low,2011%29%E2%80%99s%20advice).
By design, those factors are interpretable (they are portfolios of
stocks) even if the way they were found involved an ML optimization.
Another area of interest is **Bayesian machine learning** in asset
pricing, which offers a probabilistic ensemble of models. Bayesian
approaches can incorporate prior beliefs about, say, the sign of
coefficients or the number of significant factors, blending expert
knowledge with data-driven learning. They also provide credible
intervals for predictions and estimated risk premia, addressing the
need to quantify *uncertainty* in ML forecasts (a topic of recent
research)[\[28\]](https://arxiv.org/html/2503.00549v1#:~:text=1%20arxiv,develop%20new%20methods%20to).
The ability to produce not just point predictions but also
confidence intervals or distributions (e.g. via Bayesian neural nets
or quantile regression forests) is likely to become more important,
since understanding the uncertainty is crucial for risk management
applications of ML forecasts.

- **New Data Sources and Alternative Data:** While most academic
studies to date focus on structured data (prices, accounting ratios,
etc.), a burgeoning trend is to incorporate **alternative data**
into asset pricing models using ML. Textual data from news, earnings
calls, or social media, for instance, can be converted into
sentiment or topic scores via natural language processing (NLP)
models and used as predictors for returns or risk factors. Machine
learning is particularly well-suited to handling unstructured data
like text and images, and we are seeing early research that brings
such data into pricing models (e.g. using news sentiment to predict
factor returns, or satellite images to gauge economic activity
impacting asset prices). While this area is more prevalent in
industry, academic work is catching up, often using ML to bridge the
gap between large alternative datasets and asset pricing theory. For
example, researchers might use NLP-derived signals as additional
characteristics in a return prediction ML model to see if they
capture information beyond traditional fundamentals. The **keyword
"alternative data"** has started to appear in asset pricing and ML
contexts[\[34\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=addressing%20empirical%20challenges%2C%20and%20comparing,sample%20performance),
indicating that the scope of empirical asset pricing is expanding
beyond standard databases. One must be cautious, however, as
alternative data can introduce new pitfalls (survivorship bias,
lookahead bias, etc.), and its economic interpretation is not always
clear. But as these data become more available, ML will be the
primary tool to extract their value for asset pricing insights.

- **Open Platforms and Reproducibility:** Given the complexity of ML
models, ensuring results are robust and reproducible is an emerging
concern. There is a movement toward **open-source asset pricing
research** and public testing platforms. For instance, Chen *et
al.* (2025) introduce the **FactorWiki** project as a public
platform providing an expansive dataset of asset returns and
anomalies for researchers to test new
models[\[35\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=articles%20illustrates%20the%20merging%20paths,asset%20pricing%20are%20highly%20noisy).
The goal is to enable apples-to-apples comparisons of different ML
models on a common dataset and to reduce the "secret sauce" aspect
of data processing that might give false impressions of one method's
superiority. By analyzing 782 articles, Chen *et al.* also emphasize
the need for standardized evaluation practices and data engineering,
noting that *time-series factors are highly noisy* and careful
feature engineering (such as standardizing and de-noising inputs) is
crucial[\[36\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=researchers%20in%20analyzing%2C%20evaluating%2C%20and,to%20potentially%20usher%20in%20groundbreaking).
The FactorWiki and similar efforts reflect a trend towards
**collaborative validation** of ML asset pricing models. Researchers
are increasingly sharing code and data, which helps in identifying
what truly works versus what might have been an artefact of a
particular sample or set of choices. As this culture grows, we can
expect a tighter feedback loop where promising ML methods are
verified by multiple teams, solidifying the findings.

In summary, the future of ML in empirical asset pricing is likely to be
characterized by more **interpretability, more theory-driven
innovations, the inclusion of novel data, and greater collaboration**.
The initial excitement of "let's throw a complex model at financial data
and see if R\^2 improves" is giving way to a more mature approach:
integrating domain knowledge, assessing economic significance, and
ensuring that the ML models not only predict well but also enhance our
understanding of asset pricing mechanisms.

## Data Sets and Evaluation Metrics in ML-Based Asset Pricing

Empirical studies in this domain draw on a range of data sets and have
developed specific metrics to evaluate model performance. Here we
outline the most notable data sources and the common evaluation
criteria:

**Data Sets and Universes:**

- **Equity Cross-Section Data:** The prototypical data for many
studies is the CRSP--Compustat merged database of U.S. stocks, often
supplemented by additional data on firm characteristics (accounting
ratios, price-based signals, etc.). Many papers examine decades of
monthly U.S. stock returns (e.g. 1963--present) along with a large
set of firm characteristics compiled from prior anomaly studies. For
example, Gu *et al.* (2020) use an extensive list of 94
characteristics spanning fundamental, technical, and market
variables[\[9\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Second%2C%20the%20collection%20of%20candidate,and%20dimension%20reduction%20techniques%2C%20machine).
Similarly, Freyberger *et al.* (2020) focus on 62 characteristics
drawn from prominent anomaly
papers[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
Some researchers rely on already synthesized anomaly portfolios --
e.g. the **100+ "characteristic-sorted" test portfolios** often used
in factor model tests (such as size-value sorted portfolios,
momentum-sorted deciles, etc.). These provide a lower-dimensional
target (portfolio returns instead of individual stocks) which can
reduce estimation noise. However, with ML's ability to handle high
dimensions, many studies work directly at the stock level despite
the noise, aiming to fully exploit the cross-sectional richness. In
recent years, **international data** have also been used to assess
generalizability -- for instance, there are "global" versions of the
empirical asset pricing via ML exercise that include stocks from
many countries, as well as studies on specific markets like China to
verify that patterns are not U.S.-centric. By and large, the data
requirement for ML models is large: one needs a long history or a
broad cross-section (ideally both) to train complex models without
overfitting. This is a challenge in asset pricing, where time-series
are limited (we rarely have more than \~100 years of stock data at a
monthly frequency) and cross-sectional expansion (to thousands of
stocks) comes with the cost of heterogeneity and missing data.
Nonetheless, the assembly of *anomaly databases* by academia (e.g.
the datasets from Hou, Xue, and Zhang or from Green *et al.*, which
curate hundreds of anomaly variables in a consistent way) has been a
catalyst for ML research -- providing a fertile ground for
algorithms to test themselves against a broad menu of potential
predictors.

- **Macro and Market Time-Series:** For predicting aggregate market
returns or factors, researchers often use databases of economic
indicators. A well-known example is the **Welch--Goyal (2008)
dataset**, which contains dozens of macroeconomic and market
variables (dividend yield, yield curve measures, credit spreads,
etc.) often used to forecast the U.S. equity premium. ML studies
(like Feng *et al.* 2018; Gu *et al.* 2020) use expanded versions of
such datasets, sometimes adding more recent predictors (e.g.
volatility indices, sentiment indices, international macro
variables) to cast a wide net. **Macroeconomic panel data** (e.g.
many quarterly series on consumption, output, unemployment, etc.)
have been fed into ML models that attempt to learn the "state of the
economy" affecting expected
returns[\[37\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=variation,factors%20that%20drive%20asset%20prices).
One novel approach (Chen *et al.* 2023) is extracting *"hidden
states of the economy"* via unsupervised learning on a large panel
of macro series, and then using those as inputs to asset pricing
models[\[37\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=variation,factors%20that%20drive%20asset%20prices).
The idea is that ML can distill a few latent factors from dozens of
macro variables more effectively than economists manually can. For
bonds and other asset classes, analogous datasets (like yield curve
data, inflation expectations, etc.) have been used in ML forecasting
contexts, though equity has been the primary focus.

- **Alternative and Unstructured Data:** As noted, some emerging
studies incorporate alternative data. Examples include textual data
(news articles, earnings call transcripts), which require NLP
processing to turn into numerical features, or even **market
microstructure data** (order books, high-frequency trading data) for
short-term prediction. While not mainstream in published asset
pricing papers yet, these data are being explored using ML in
working papers and could become more common. **Options data** is
another domain: some work looks at option-implied information (like
implied volatility skew, etc.) as additional features for predicting
stock or factor
returns[\[38\]](https://oxfordre.com/economics/display/10.1093/acrefore/9780190625979.001.0001/acrefore-9780190625979-e-870?d=%2F10.1093%2Facrefore%2F9780190625979.001.0001%2Facrefore-9780190625979-e-870&p=emailA%2FL66KGI9MmXI#:~:text=Asset%20Pricing%3A%20Cross,%28).
The broad availability of data and the ease of merging different
sources via machine learning pipelines mean that the definition of
"asset pricing data" is expanding. To keep research grounded,
though, many scholars stick to well-vetted datasets (like
CRSP/Compustat, macro data from the Federal Reserve, etc.) for the
core analysis, to avoid the pitfalls of obscure or
lightly-scrutinized data sources that might introduce biases.

- **Public Benchmarks:** An important development is the creation of
public benchmark datasets specifically for testing asset pricing
models. The **FactorWiki** project mentioned earlier is one such
effort, aiming to provide a large, cleaned, and regularly updated
dataset of asset returns and candidate factors for
researchers[\[35\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=articles%20illustrates%20the%20merging%20paths,asset%20pricing%20are%20highly%20noisy).
It includes not only U.S. equities but potentially other asset
classes and is meant to serve as a *common ground* for evaluating
new ML models. Similarly, some papers release their processed
datasets (for instance, Gu *et al.* provided an *Internet Appendix*
with details of their data and code). This improves comparability:
if two ML papers use the same underlying data and period,
differences in performance can more credibly be attributed to the
method rather than data quirks. We anticipate that as the field
matures, the community will converge on certain **benchmark tasks**
(e.g. predicting monthly U.S. stock returns using a given list of
characteristics from 1965--2015) that every new ML method is tested
on, much like standardized datasets in machine learning literature
(e.g. ImageNet in computer vision). This will facilitate an
apples-to-apples comparison of models.

**Evaluation Metrics:**

To gauge the success of ML models in asset pricing, researchers employ a
variety of evaluation metrics, often distinguishing between
**statistical performance** and **economic significance**:

- **Out-of-Sample $R^2$:** This measures the fraction of variance
of the outcome (returns) explained by the model's predictions in a
holdout sample, defined as $R^2_{\text{OOS}} = 1 -
\frac{\text{MSE}_{\text{model}}}{\text{MSE}_{\text{benchmark}}}$. A common
benchmark is either a simple historical mean (for time-series) or a
cross-sectional mean or CAPM baseline (for stocks). While $R^2$
values in predicting stock returns are typically low (because most
return variation is noise), ML papers have reported OOS $R^2$ on
the order of 1%--5% in challenging settings, which often *dwarfs*
the essentially zero or negative OOS $R^2$* of naive models or
non-ML
approaches[\[39\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Our%20primary%20contributions%20are%20twofold,short%20decile%20spread%20strategy).
For example, Gu *et al.* found an OOS $R^2$ around 5% for their
best stock-level model, compared to essentially 0% for a simple
linear model -- a notable improvement in this
context[\[29\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Our%20primary%20contributions%20are%20twofold,51%20Sharpe%20ratio%20of%20a).
In factor models, a related metric is the *explained variation* in
average returns; some studies report how much cross-sectional
variance in asset mean returns is captured by the ML factors versus
Fama--French (e.g. "pricing $R^2$" from cross-sectional
regressions of mean returns on beta estimates). Chen *et al.* (2023)
note that their deep learning SDF explains a greater portion of
cross-sectional return variance and yields smaller pricing errors
than traditional
models[\[26\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=adversarial%20approach%20and%20to%20extract,factors%20that%20drive%20asset%20prices).

- **Sharpe Ratios and Investor Utility:** Because a model's value
ultimately lies in improving investment decisions, many papers
translate predictions into portfolio returns and compute *Sharpe
ratios, information ratios,* or utility gains. A typical exercise is
to form a long-short portfolio that goes long the top decile of
stocks (with highest predicted returns) and short the bottom decile,
then evaluate its out-of-sample performance. The Sharpe ratio of
this strategy is a convenient single statistic summarizing
performance. As mentioned, ML-based strategies have achieved Sharpe
ratios that are 1.3--1.5 in some studies, compared to about 0.5--0.7
for strategies based on simpler
models[\[5\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=relative%20to%20preceding%20literature%20that,based%20strategy%20from%20the%20literature).
Another approach is to compute the **certainty-equivalent return**
for an investor using the model's forecasts to optimize a portfolio
(subject to risk aversion). This directly measures how much a
risk-averse investor would pay for the model's information. Such
utility-based metrics often reveal that even modest improvements in
prediction $R^2$ can translate to sizeable utility gains, because
the model consistently tilts the portfolio in the right direction
(avoiding big losses, capturing more
gains)[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the).
Some research also looks at *turnover and trading costs* in these
strategies, ensuring that the theoretical performance net of
reasonable costs still shows an improvement -- an important reality
check for economic significance.

- **Classification Metrics:** In some contexts (like predicting the
direction of return, or default/no-default), classification metrics
such as *accuracy, precision/recall, AUC (Area Under ROC Curve)* are
relevant. For equity returns, which are continuous, these are less
commonly reported, but one might consider the frequency with which
the model correctly signs the return or identifies the top-quartile
performers, etc. By and large, regression metrics (MSE, $R^2$)
and portfolio performance metrics are favored, since they align with
how an investor would use the model.

- **Pricing Error Metrics:** For factor models and SDF estimates,
evaluation focuses on **pricing errors**. A popular metric is the
*mean absolute error (MAE)* or *root mean squared error (RMSE)* of
pricing, i.e. the difference between actual average returns and
those implied by the model (given the estimated factor risk premia).
The **Hansen--Jagannathan distance** is another measure used -- it
essentially quantifies the distance between the model's SDF and any
true SDF that could price all assets, with smaller distances
indicating a better fit. Studies that propose new factor
constructions often report these metrics relative to benchmarks. For
instance, an ML factor model might achieve an pricing RMSE of only
1% per month on test assets compared to 2% for Fama--French,
indicating a tighter fit to the cross-section of returns.
Additionally, **GRS tests** (Gibbons, Ross, Shanken test) can be
used to statistically test if residual alphas (unexplained returns)
are jointly zero; an ML model that significantly reduces these
alphas would likely pass a GRS test where a simpler model fails.
Recent work also considers **multiple testing adjustments** when
evaluating many alphas (since using hundreds of test assets can lead
to false rejections by chance) -- linking back to Harvey, Liu, and
Zhu (2016) concerns about the factor zoo and statistical
significance[\[40\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=After%20years%20of%20strong%20growth,This%20work%20aims%20to).

- **Stability and Robustness Checks:** While not formal metrics, a
critical part of evaluation is testing robustness -- e.g. how
sensitive the results are to the training sample period, to
different hyperparameter choices, or to subsetting the universe of
stocks. Many papers do **subsample analyses** (e.g. train the model
in earlier decades and test in later decades) to ensure the
performance isn't driven by one period. They may also evaluate
*stability of variable importance*: do the same predictors keep
emerging as important in different folds of the data? Consistency in
what the model finds predictive lends credence to its economic
meaningfulness. Another diagnostic is to compare *model-implied
factor premia or betas* to known values -- for example, if an ML-SDF
assigns a high price of risk to a factor that we know is likely
unpriced, that could indicate overfitting or a problem. Hence, a mix
of quantitative metrics and qualitative economic checks is used to
evaluate ML models in asset pricing. The literature has been
increasingly diligent about such checks, especially after early
enthusiasm was tempered by the realization that complex models can
overfit if not rigorously validated.

In summary, the evaluation toolkit for ML asset pricing models spans
both the *statistical domain* (forecast errors, $R^2$) and the
*economic domain* (portfolio returns, Sharpe ratios, pricing errors). A
model is considered truly successful if it improves predictive accuracy
**and** those improvements lead to economically meaningful gains
*without* generating unreasonable or nonrobust implications. Because
finance ultimately cares about risk and return trade-offs, metrics like
Sharpe ratio and pricing error are often given more weight than pure
statistical metrics. This ensures that ML models are judged not just by
how well they fit the data, but by whether they would actually benefit
investors or help explain asset prices in a way consistent with
financial theory.

## Limitations and Critiques of Machine Learning in Asset Pricing

While the marriage of machine learning and asset pricing has been
fruitful, it is not without its critics and clear limitations. We
discuss several key concerns that emerge from the literature:

- **Lack of Interpretability:** As mentioned, opacity is a fundamental
drawback of complex ML models. Unlike a linear factor model where
one can interpret coefficients as risk premia, ML models often defy
simple explanation. This opacity leads to skepticism: If we cannot
understand the *why* behind a prediction, can we trust it in
high-stakes settings? Moreover, lack of interpretability makes it
harder to **cumulatively build knowledge**. In traditional asset
pricing, if many studies find a particular factor is important, it
spurs theoretical explanations and further tests. If an ML model
finds a pattern but cannot articulate it, it's difficult to
translate that into an advance in theory. This has led to calls for
caution -- some argue that ML might produce *"accurate predictions
of returns as point estimates, but without advancing our
understanding of the underlying risks or mispricings"*. The
literature is addressing this by, as noted, bringing
interpretability methods and theory constraints into models, but the
issue remains that a lot of ML results are initially a black box.
Bagnara (2024) summarizes that ML techniques *"offer great
flexibility and prediction accuracy but require special care as they
strongly depart from traditional
econometrics"*[\[41\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=problem%20of%20the%20factor%20zoo,We%20sum%02marize%20the%20empirical%20findings).
The implicit warning is that one should not blindly trust an ML
model's output without interrogating it and ensuring it aligns with
reasonable economic rationale.

- **Overfitting and False Discoveries:** Finance data is notoriously
noisy -- much of the variation in returns is random noise or one-off
events that do not repeat. ML models, especially highly flexible
ones like deep networks, run the risk of **overfitting this noise**
and mistaking it for signal. Even with regularization, the sheer
complexity of some models means they could latch onto patterns that
are artifacts of the particular sample. This is exacerbated by the
factor zoo problem: if one is not careful, using ML to search
through hundreds of predictors could easily result in some
combination that fits past data well but has no true predictive
power (a manifestation of data mining). Harvey, Liu, and Zhu (2016)
famously cautioned that many published anomalies may be false
positives, and with ML one could data-mine even more intensely if
proper validation is not
used[\[40\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=After%20years%20of%20strong%20growth,This%20work%20aims%20to).
Researchers have learned to mitigate this via strict **out-of-sample
testing, cross-validation, and even multiple-hypothesis testing
corrections**. For example, strict separation of training and test
sets and reporting of out-of-sample performance (not just in-sample
fit) is now standard -- a cultural shift partly imported from
machine learning's best practices. Some studies use *white-noise
simulations or bootstrap* to sanity-check that their methods aren't
finding spurious structure (e.g. applying the ML model on randomized
returns to see if it still "finds" something -- it shouldn't).
Nonetheless, the risk remains that a complex model might be
*over-tuned* to past market regimes and may fail if conditions
change. Indeed, *stability over time* is a concern: some papers have
found that certain ML models' performance decays in more recent
years or needs frequent re-estimation, suggesting they might be
capturing ephemeral patterns.

- **Non-Stationarity and Regime Changes:** Financial markets evolve.   Relationships that held in one period (say, the value premium in the
1980s-1990s) might attenuate or even reverse in another
(2000s-2010s) due to changing investor behavior, regulations, or
technology. ML models, unless specifically designed for
adaptability, can struggle with such non-stationarity. A static
model trained on 1960--2000 data might not perform well post-2000 if
new regimes emerge. While rolling re-estimation can help, it also
introduces the possibility of overfitting on shorter windows. A
critique here is that ML, with its emphasis on historical data,
might be *inherently backward-looking* and not robust to structural
breaks. This is not a new issue (econometric models face it too),
but the complexity of ML can make diagnosing failure modes harder
when a regime shift happens. For instance, if an ML model's
performance deteriorates, is it because of a regime change or
because it overfit the past? Researchers are beginning to address
this by using techniques from online learning or by incorporating
regime indicators, but it remains a challenge. In practice, it
underscores the need for **continuous monitoring** of ML model
performance and a willingness to retrain or rethink models as
markets change.

- **Economic Meaning and Theoretical Consistency:** A more
philosophical critique is that ML models might lack a grounding in
economic theory, raising the danger that they pick up patterns that
lack *any economic meaning*. A classic asset pricing tension is
between **risk-based explanations** (where return predictors proxy
for exposures to some systematic risk) and **mispricing
explanations** (where predictors exploit behavioral or structural
market inefficiencies). An ML model could exploit mispricings that
are profitable in-sample but get arbitraged away once discovered
(leading to lack of stability), or it could mix together so many
effects that it's unclear what the investor is being compensated
for. Without theory, we might end up with models that work until
they don't, and we won't know why. Some critics from the traditional
camp argue that *"predictive power alone is not enough; we need to
know the why."* This has spurred efforts to ensure ML models are at
least *consistent with no-arbitrage and other fundamental
constraints*. For example, a model that implied a free lunch
(arbitrage opportunity) would be deemed suspect even if it fit the
data well. By incorporating theory (as discussed in *Emerging
Trends*), researchers aim to rule out grossly illogical results. But
a lingering critique is that ML models might be capturing mostly
*mispricing rather than risk*. If that's the case, one might worry
about whether those mispricings will persist. On the other hand, if
ML is capturing risk in a complicated way, we'd like to identify
what risk it is (e.g. is it learning some nonlinear exposure to
recession risk? or an interaction of leverage and volatility that
indicates financial distress risk?). The literature is only starting
to unravel these questions.

- **Practical Constraints and Implementability:** From a
practitioner's viewpoint, a strategy that looks great on paper may
falter in reality due to costs, turnover, and other frictions. ML
strategies often involve frequent trading (since they continuously
update forecasts and may chase short-term signals) and can be heavy
in small stocks (where many anomalies reside). This can lead to high
**transaction costs** that erode theoretical returns. Indeed, some
studies note that the impressive Sharpe ratios of ML long--short
portfolios are partly driven by microcap stocks with limited
capacity[\[16\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=type%20II%20errors%20are%20a,predictable%20throughout%20the%20entire%20sample).
Once one accounts for realistic trading costs, the net advantage of
ML can shrink. Moreover, ML models can be **computationally
intensive and complex to maintain**. In an industry setting, the
most complex models might be deemed too unstable or hard to justify
to risk managers. Simpler but slightly less predictive models might
be preferred for operational robustness. These considerations mean
that not every academic ML innovation will translate to an immediate
industry application, at least without modification. However, we do
see quantitative finance firms adopting ML techniques, often in a
piecemeal way (e.g. using ML signals as inputs to a human-driven
strategy, or using ML to optimize execution of trades). The critique
here is simply that academic studies sometimes focus on the maximum
theoretical improvement and less on the nitty-gritty of
implementation -- a gap that future work is starting to fill by
considering costs, market impact, etc., more explicitly.

- **Biases in Data and ML Models:** Finally, one should be aware of
biases that can creep in. Look-ahead bias or survival bias in the
data can fool an ML model into overstating its performance. If a
researcher is not careful in aligning accounting data with returns
(ensuring the data was available at the time of the return
prediction), an ML model might be "cheating" by using information
that investors wouldn't have had. Traditional asset pricing has long
warned about these biases, and they equally apply in ML research. ML
models also have their own quirks: they can be sensitive to how data
is normalized or encoded. A characteristic like market
capitalization, which ranges over several orders of magnitude, needs
scaling or else a neural network might struggle to learn from it.
Fortunately, most studies handle this by normalizing characteristics
(often rank-transforming to uniform \[0,1\]
distributions)[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The).
Another issue is **model uncertainty** -- there are so many
algorithms and hyperparameter choices that results could
inadvertently be cherry-picked (consciously or not). The community
is addressing this by emphasizing that one should either fix a
procedure before seeing results or use techniques like
cross-validation to choose parameters objectively. In any case,
transparency in reporting (e.g. reporting if many models were tried
and only the best presented) is crucial to maintain credibility.

In light of these critiques, the overall sentiment in recent literature
is one of guarded optimism. Machine learning is recognized as a powerful
tool that can yield genuine improvements in asset pricing empirics, but
**its use must be accompanied by rigor and skepticism**. As one review
put it, ML is *"not a substitute for theory"* but a tool to explore the
data; blindly applied, it could lead us astray, but tailored and
interpreted wisely, it can help *"fortify the relevance and robustness
of financial
models."*[\[33\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=area%3A%20time,potentially%20usher%20in%20groundbreaking%20developments).
The responsibility lies with researchers to ensure that ML models are
robust, interpretable, and economically sensible -- a standard that, if
met, could truly augment the field of asset pricing.

## Conclusion

Machine learning has undeniably opened a new frontier in empirical asset
pricing. It has enabled researchers to grapple with the challenges of
high-dimensional data (the myriad firm characteristics and macro
signals) and complex relationships, yielding improved predictive
performance in measuring risk premia and pricing assets. Key areas of
impact include more accurate return prediction models, refined
identification of which factors or anomalies are truly important, and
novel approaches to estimating factor structures and the stochastic
discount factor. Equally important, ML methods have prompted a
re-examination of long-held models -- for instance, by highlighting that
a few well-chosen factors (often found via ML) can explain returns
nearly as well as an encyclopedia of anomalies, they encourage a more
disciplined understanding of asset pricing signals.

The literature to date demonstrates that machine learning can
**complement** and **enhance** traditional asset pricing methods, rather
than wholesale replace them. ML models often rediscover established
factors like momentum, size, and value, but also show how interactions
or nonlinear effects add nuance to these well-known
patterns[\[7\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=from%20the%20literature,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and).
In comparing approaches, we see a trade-off: ML delivers greater
predictive accuracy and the ability to model complex phenomena, while
classical models provide clear economic interpretations. The current
trajectory of research is to get the best of both worlds -- integrating
economic theory into ML and using ML insights to inform theory. Emerging
trends such as improving model interpretability, enforcing theoretical
structure (no-arbitrage, equilibrium constraints), and utilizing new
data sources all point toward a synthesis of machine learning techniques
with financial economic
reasoning[\[36\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=researchers%20in%20analyzing%2C%20evaluating%2C%20and,to%20potentially%20usher%20in%20groundbreaking)[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance).

Nonetheless, caution is warranted. The enthusiasm for machine learning
is tempered by reminders of past episodes in finance where overly
complex models or overfit strategies failed in real time. The community
is actively addressing these issues by emphasizing out-of-sample
testing, reproducibility (through public datasets like
FactorWiki[\[35\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=articles%20illustrates%20the%20merging%20paths,asset%20pricing%20are%20highly%20noisy)),
and the development of statistical inference for ML estimates (to know
when an improvement is significant or just noise). The intersection of
ML and asset pricing is still relatively young, and many open questions
remain -- for example, how to best quantify the uncertainty in ML
predictions[\[28\]](https://arxiv.org/html/2503.00549v1#:~:text=1%20arxiv,develop%20new%20methods%20to),
how to handle regime shifts gracefully, or how to design algorithms that
yield economically interpretable factors by construction. As researchers
continue to explore these questions, the dialogue between data science
and financial economics will deepen.

In conclusion, machine learning has proven to be a **powerful catalyst**
for empirical asset pricing research. It has led to better-performing
models and sharpened our tools for dealing with the factor zoo and
prediction problems. Perhaps most encouraging, it has sparked fresh
perspectives on age-old questions: *What drives asset returns?* ML
encourages us to let the data speak with minimal assumptions, but the
ultimate goal is to translate what it says into the language of economic
insight. By focusing on interpretability, theoretical consistency, and
robustness -- not just raw predictive power -- researchers aim to ensure
that the ML revolution in asset pricing yields lasting knowledge and
practical advances. The journey is ongoing, but the potential for
machine learning to help unravel asset pricing puzzles, in partnership
with theory, marks an exciting era for the
field[\[33\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=area%3A%20time,potentially%20usher%20in%20groundbreaking%20developments)[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance).

**Sources:** The review draws upon a range of recent studies and surveys
in this area, including Gu *et al.*
(2020)[\[3\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20perform%20a%20comparative%20analysis,on%20momentum%2C%20liquidity%2C%20and%20volatility)[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the),
Bagnara
(2024)[\[2\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=The%20latest%20development%20in%20empirical,approach%20they%20employ%3A%20regularization%2C%20dimension)[\[30\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Giglio%20and%20Xiu%2C%202021%29,This%20partially),
Chuan Shi
(2025)[\[42\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=Empirical%20asset%20pricing%20is%20undergoing,machine%20learning%20while%20preserving%20economic)[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance),
Chen *et al.*
(2025)[\[43\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=multiple%20Nobel%20Prizes%20in%20Economics%2C,More)[\[36\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=researchers%20in%20analyzing%2C%20evaluating%2C%20and,to%20potentially%20usher%20in%20groundbreaking),
Freyberger *et al.*
(2020)[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The),
Feng *et al.*
(2020)[\[17\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=%E2%80%93%20Feng%2C%20Giglio%2C%20and%20Xiu,parametric%20LASSO),
Chen, Pelger & Zhu
(2023)[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices),
among others. These and numerous other works collectively illustrate the
promises and challenges of applying machine learning to empirical asset
pricing, as synthesized above.

[\[1\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=Empirical%20asset%20pricing%20is%20undergoing,the%20stochastic%20discount%20factor%20is)
[\[31\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=provides%20a%20promising%20alternative,sample%20performance)
[\[34\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=addressing%20empirical%20challenges%2C%20and%20comparing,sample%20performance)
[\[42\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205#:~:text=Empirical%20asset%20pricing%20is%20undergoing,machine%20learning%20while%20preserving%20economic)
From Econometrics to Machine Learning: Transforming Empirical Asset
Pricing by Chuan Shi :: SSRN

<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5150205>

[\[2\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=The%20latest%20development%20in%20empirical,approach%20they%20employ%3A%20regularization%2C%20dimension)
[\[14\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=predictors%20associated%20with%20news%20about,predictors%20stand%20out%3B%20Conditional%20and)
[\[15\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Freyberger%20et%20al,section%20of%20expected%20returns.%20The)
[\[19\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=characteristics%20%28Freyberger%20et%20al,them%20to%20circumvent%20daunting%20issues)
[\[20\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=low,2011%29%E2%80%99s%20advice)
[\[24\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=important%20limitations%20%28Dixon%20et%20al,which%20shrink%20the%20network%20weights)
[\[30\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=Giglio%20and%20Xiu%2C%202021%29,This%20partially)
[\[41\]](https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf#:~:text=problem%20of%20the%20factor%20zoo,We%20sum%02marize%20the%20empirical%20findings)
Asset Pricing and Machine Learning: A critical review

<https://www.econstor.eu/bitstream/10419/288177/1/JOES_JOES12532.pdf>

[\[3\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20perform%20a%20comparative%20analysis,on%20momentum%2C%20liquidity%2C%20and%20volatility)
[\[4\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=premiums%20of%20the%20aggregate%20market,35%2C%20more%20than%20doubling%20the)
[\[5\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=relative%20to%20preceding%20literature%20that,based%20strategy%20from%20the%20literature)
[\[6\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=demonstrate%20large%20economic%20gains%20to,on%20momentum%2C%20liquidity%2C%20and%20volatility)
[\[7\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=from%20the%20literature,on%20momentum%2C%20liquidity%2C%20and%20volatility)
[\[9\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Second%2C%20the%20collection%20of%20candidate,and%20dimension%20reduction%20techniques%2C%20machine)
[\[10\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Third%2C%20further%20complicating%20the%20problem,linear%20models%20to%20regression%20trees)
[\[11\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=variables%20and%20functional%20forms,overfit%20biases%20and%20false%20discovery)
[\[12\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=various%20researchers%20have%20argued%20possess,condensing%20redundant%20variation%20among%20predictors)
[\[13\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=networks,on%20momentum%2C%20liquidity%2C%20and%20volatility)
[\[27\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=We%20study%20a%20set%20of,boosted%20trees%20and%20random%20forests)
[\[29\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Our%20primary%20contributions%20are%20twofold,51%20Sharpe%20ratio%20of%20a)
[\[39\]](https://academic.oup.com/rfs/article/33/5/2223/5758276#:~:text=Our%20primary%20contributions%20are%20twofold,short%20decile%20spread%20strategy)
Empirical Asset Pricing via Machine Learning \| The Review of Financial
Studies \| Oxford Academic

<https://academic.oup.com/rfs/article/33/5/2223/5758276>

[\[8\]](https://arxiv.org/abs/1804.09314#:~:text=,the%20extremes%20of%20the%20characteristic)
[\[25\]](https://arxiv.org/abs/1804.09314#:~:text=returns,the%20extremes%20of%20the%20characteristic)
\[1804.09314\] Deep Learning for Predicting Asset Returns

<https://arxiv.org/abs/1804.09314>

[\[16\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=type%20II%20errors%20are%20a,predictable%20throughout%20the%20entire%20sample)
[\[23\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=We%20investigate%20whether%20Lasso,predictable%20throughout%20the%20entire%20sample)
[\[40\]](https://www.mdpi.com/2571-9394/4/4/53#:~:text=After%20years%20of%20strong%20growth,This%20work%20aims%20to)
The Lasso and the Factor Zoo-Predicting Expected Returns in the
Cross-Section

<https://www.mdpi.com/2571-9394/4/4/53>

[\[17\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=%E2%80%93%20Feng%2C%20Giglio%2C%20and%20Xiu,parametric%20LASSO)
[\[18\]](https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf#:~:text=,2020%29%20find%20significant)
koijen.net

<https://www.koijen.net/uploads/3/4/4/7/34470013/2_factorzoo_2021.pdf>

[\[21\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=We%20survey%20recent%20methodological%20contributions,harnessing%20modern%20tools%20with%20rigor)
[\[32\]](https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf#:~:text=returns%2C%20factors%2C%20risk%20exposures%2C%20risk,future%20research%20and%20methodological%20advances)
economics.smu.edu.sg

<https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/economics/pdf/Seminar/2021/2021120301.pdf>

[\[22\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=We%20use%20deep%20neural%20networks,factors%20that%20drive%20asset%20prices)
[\[26\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=adversarial%20approach%20and%20to%20extract,factors%20that%20drive%20asset%20prices)
[\[37\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138#:~:text=variation,factors%20that%20drive%20asset%20prices)
Deep Learning in Asset Pricing by Luyang Chen, Markus Pelger, Jason Zhu
:: SSRN

<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3350138>

[\[28\]](https://arxiv.org/html/2503.00549v1#:~:text=1%20arxiv,develop%20new%20methods%20to)
The Uncertainty of Machine Learning Predictions in Asset Pricing 1

<https://arxiv.org/html/2503.00549v1>

[\[33\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=area%3A%20time,potentially%20usher%20in%20groundbreaking%20developments)
[\[35\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=articles%20illustrates%20the%20merging%20paths,asset%20pricing%20are%20highly%20noisy)
[\[36\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=researchers%20in%20analyzing%2C%20evaluating%2C%20and,to%20potentially%20usher%20in%20groundbreaking)
[\[43\]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505#:~:text=multiple%20Nobel%20Prizes%20in%20Economics%2C,More)
Unraveling Asset Pricing with AI: A Systematic Literature Review by Yan
Chen, lin zhang, Zhilong Xie, Wenjie Zhang, Qing Li :: SSRN

<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5380505>

[\[38\]](https://oxfordre.com/economics/display/10.1093/acrefore/9780190625979.001.0001/acrefore-9780190625979-e-870?d=%2F10.1093%2Facrefore%2F9780190625979.001.0001%2Facrefore-9780190625979-e-870&p=emailA%2FL66KGI9MmXI#:~:text=Asset%20Pricing%3A%20Cross,%28)
Asset Pricing: Cross-Section Predictability

<https://oxfordre.com/economics/display/10.1093/acrefore/9780190625979.001.0001/acrefore-9780190625979-e-870?d=%2F10.1093%2Facrefore%2F9780190625979.001.0001%2Facrefore-9780190625979-e-870&p=emailA%2FL66KGI9MmXI>
