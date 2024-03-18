from typing import Any

from sympy import Equality, Integral, Piecewise
from sympy.concrete.summations import Sum
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.core.relational import Ne, Relational
from sympy.series.order import Order
from sympy.sets.sets import FiniteSet, Set
from sympy.stats.symbolic_multivariate_probability import CrossCovarianceMatrix, ExpectationMatrix, VarianceMatrix
from sympy.stats.symbolic_probability import CentralMoment, Covariance, Expectation, Moment, Variance

__all__ = ['P', 'E', 'H', 'density', 'where', 'given', 'sample', 'cdf', 'characteristic_function', 'pspace', 'sample_iter', 'variance', 'std', 'skewness', 'kurtosis', 'covariance', 'dependent', 'entropy', 'median', 'independent', 'random_symbols', 'correlation', 'factorial_moment', 'moment', 'cmoment', 'sampling_density', 'moment_generating_function', 'smoment', 'quantile', 'sample_stochastic_process']

def moment(X, n, c=..., condition=..., *, evaluate=..., **kwargs) -> Any | Moment:
    """
    Return the nth moment of a random expression about c.

    .. math::
        moment(X, c, n) = E((X-c)^{n})

    Default value of c is 0.

    Examples
    ========

    >>> from sympy.stats import Die, moment, E
    >>> X = Die('X', 6)
    >>> moment(X, 1, 6)
    -5/2
    >>> moment(X, 2)
    91/6
    >>> moment(X, 1) == E(X)
    True
    """
    ...

def variance(X, condition=..., **kwargs) -> VarianceMatrix | Variance | Any | CentralMoment:
    """
    Variance of a random expression.

    .. math::
        variance(X) = E((X-E(X))^{2})

    Examples
    ========

    >>> from sympy.stats import Die, Bernoulli, variance
    >>> from sympy import simplify, Symbol

    >>> X = Die('X', 6)
    >>> p = Symbol('p')
    >>> B = Bernoulli('B', p, 1, 0)

    >>> variance(2*X)
    35/3

    >>> simplify(variance(B))
    p*(1 - p)
    """
    ...

def standard_deviation(X, condition=..., **kwargs) -> Pow:
    r"""
    Standard Deviation of a random expression

    .. math::
        std(X) = \sqrt(E((X-E(X))^{2}))

    Examples
    ========

    >>> from sympy.stats import Bernoulli, std
    >>> from sympy import Symbol, simplify

    >>> p = Symbol('p')
    >>> B = Bernoulli('B', p, 1, 0)

    >>> simplify(std(B))
    sqrt(p*(1 - p))
    """
    ...

std = ...
def entropy(expr, condition=..., **kwargs) -> int | Mul | Basic | Expectation | tuple[Any, ...] | Sum | Order | Any | Piecewise | Equality | Relational | Ne | Integral | ExpectationMatrix | None:
    """
    Calculuates entropy of a probability distribution.

    Parameters
    ==========

    expression : the random expression whose entropy is to be calculated
    condition : optional, to specify conditions on random expression
    b: base of the logarithm, optional
       By default, it is taken as Euler's number

    Returns
    =======

    result : Entropy of the expression, a constant

    Examples
    ========

    >>> from sympy.stats import Normal, Die, entropy
    >>> X = Normal('X', 0, 1)
    >>> entropy(X)
    log(2)/2 + 1/2 + log(pi)/2

    >>> D = Die('D', 4)
    >>> entropy(D)
    log(4)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Entropy_%28information_theory%29
    .. [2] https://www.crmarsh.com/static/pdf/Charles_Marsh_Continuous_Entropy.pdf
    .. [3] https://kconrad.math.uconn.edu/blurbs/analysis/entropypost.pdf
    """
    ...

def covariance(X, Y, condition=..., **kwargs) -> CrossCovarianceMatrix | Covariance | Basic | Expectation | tuple[Any, ...] | Sum | Order | Any | Piecewise | Equality | Relational | Ne | Integral | ExpectationMatrix | None:
    """
    Covariance of two random expressions.

    Explanation
    ===========

    The expectation that the two variables will rise and fall together

    .. math::
        covariance(X,Y) = E((X-E(X)) (Y-E(Y)))

    Examples
    ========

    >>> from sympy.stats import Exponential, covariance
    >>> from sympy import Symbol

    >>> rate = Symbol('lambda', positive=True, real=True)
    >>> X = Exponential('X', rate)
    >>> Y = Exponential('Y', rate)

    >>> covariance(X, X)
    lambda**(-2)
    >>> covariance(X, Y)
    0
    >>> covariance(X, Y + rate*X)
    1/lambda
    """
    ...

def correlation(X, Y, condition=..., **kwargs):
    r"""
    Correlation of two random expressions, also known as correlation
    coefficient or Pearson's correlation.

    Explanation
    ===========

    The normalized expectation that the two variables will rise
    and fall together

    .. math::
        correlation(X,Y) = E((X-E(X))(Y-E(Y)) / (\sigma_x  \sigma_y))

    Examples
    ========

    >>> from sympy.stats import Exponential, correlation
    >>> from sympy import Symbol

    >>> rate = Symbol('lambda', positive=True, real=True)
    >>> X = Exponential('X', rate)
    >>> Y = Exponential('Y', rate)

    >>> correlation(X, X)
    1
    >>> correlation(X, Y)
    0
    >>> correlation(X, Y + rate*X)
    1/sqrt(1 + lambda**(-2))
    """
    ...

def cmoment(X, n, condition=..., *, evaluate=..., **kwargs) -> Any | CentralMoment:
    """
    Return the nth central moment of a random expression about its mean.

    .. math::
        cmoment(X, n) = E((X - E(X))^{n})

    Examples
    ========

    >>> from sympy.stats import Die, cmoment, variance
    >>> X = Die('X', 6)
    >>> cmoment(X, 3)
    0
    >>> cmoment(X, 2)
    35/12
    >>> cmoment(X, 2) == variance(X)
    True
    """
    ...

def smoment(X, n, condition=..., **kwargs):
    r"""
    Return the nth Standardized moment of a random expression.

    .. math::
        smoment(X, n) = E(((X - \mu)/\sigma_X)^{n})

    Examples
    ========

    >>> from sympy.stats import skewness, Exponential, smoment
    >>> from sympy import Symbol
    >>> rate = Symbol('lambda', positive=True, real=True)
    >>> Y = Exponential('Y', rate)
    >>> smoment(Y, 4)
    9
    >>> smoment(Y, 4) == smoment(3*Y, 4)
    True
    >>> smoment(Y, 3) == skewness(Y)
    True
    """
    ...

def skewness(X, condition=..., **kwargs):
    r"""
    Measure of the asymmetry of the probability distribution.

    Explanation
    ===========

    Positive skew indicates that most of the values lie to the right of
    the mean.

    .. math::
        skewness(X) = E(((X - E(X))/\sigma_X)^{3})

    Parameters
    ==========

    condition : Expr containing RandomSymbols
            A conditional expression. skewness(X, X>0) is skewness of X given X > 0

    Examples
    ========

    >>> from sympy.stats import skewness, Exponential, Normal
    >>> from sympy import Symbol
    >>> X = Normal('X', 0, 1)
    >>> skewness(X)
    0
    >>> skewness(X, X > 0) # find skewness given X > 0
    (-sqrt(2)/sqrt(pi) + 4*sqrt(2)/pi**(3/2))/(1 - 2/pi)**(3/2)

    >>> rate = Symbol('lambda', positive=True, real=True)
    >>> Y = Exponential('Y', rate)
    >>> skewness(Y)
    2
    """
    ...

def kurtosis(X, condition=..., **kwargs):
    r"""
    Characterizes the tails/outliers of a probability distribution.

    Explanation
    ===========

    Kurtosis of any univariate normal distribution is 3. Kurtosis less than
    3 means that the distribution produces fewer and less extreme outliers
    than the normal distribution.

    .. math::
        kurtosis(X) = E(((X - E(X))/\sigma_X)^{4})

    Parameters
    ==========

    condition : Expr containing RandomSymbols
            A conditional expression. kurtosis(X, X>0) is kurtosis of X given X > 0

    Examples
    ========

    >>> from sympy.stats import kurtosis, Exponential, Normal
    >>> from sympy import Symbol
    >>> X = Normal('X', 0, 1)
    >>> kurtosis(X)
    3
    >>> kurtosis(X, X > 0) # find kurtosis given X > 0
    (-4/pi - 12/pi**2 + 3)/(1 - 2/pi)**2

    >>> rate = Symbol('lamda', positive=True, real=True)
    >>> Y = Exponential('Y', rate)
    >>> kurtosis(Y)
    9

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Kurtosis
    .. [2] https://mathworld.wolfram.com/Kurtosis.html
    """
    ...

def factorial_moment(X, n, condition=..., **kwargs) -> type[UndefinedFunction] | Basic | Expectation | tuple[Any, ...] | Sum | Order | Any | Piecewise | Equality | Relational | Ne | Integral | ExpectationMatrix | None:
    """
    The factorial moment is a mathematical quantity defined as the expectation
    or average of the falling factorial of a random variable.

    .. math::
        factorial-moment(X, n) = E(X(X - 1)(X - 2)...(X - n + 1))

    Parameters
    ==========

    n: A natural number, n-th factorial moment.

    condition : Expr containing RandomSymbols
            A conditional expression.

    Examples
    ========

    >>> from sympy.stats import factorial_moment, Poisson, Binomial
    >>> from sympy import Symbol, S
    >>> lamda = Symbol('lamda')
    >>> X = Poisson('X', lamda)
    >>> factorial_moment(X, 2)
    lamda**2
    >>> Y = Binomial('Y', 2, S.Half)
    >>> factorial_moment(Y, 2)
    1/2
    >>> factorial_moment(Y, 2, Y > 1) # find factorial moment for Y > 1
    2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Factorial_moment
    .. [2] https://mathworld.wolfram.com/FactorialMoment.html
    """
    ...

def median(X, evaluate=..., **kwargs) -> FiniteSet | Set:
    r"""
    Calculuates the median of the probability distribution.

    Explanation
    ===========

    Mathematically, median of Probability distribution is defined as all those
    values of `m` for which the following condition is satisfied

    .. math::
        P(X\leq m) \geq  \frac{1}{2} \text{ and} \text{ } P(X\geq m)\geq \frac{1}{2}

    Parameters
    ==========

    X: The random expression whose median is to be calculated.

    Returns
    =======

    The FiniteSet or an Interval which contains the median of the
    random expression.

    Examples
    ========

    >>> from sympy.stats import Normal, Die, median
    >>> N = Normal('N', 3, 1)
    >>> median(N)
    {3}
    >>> D = Die('D')
    >>> median(D)
    {3, 4}

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Median#Probability_distributions

    """
    ...

def coskewness(X, Y, Z, condition=..., **kwargs):
    r"""
    Calculates the co-skewness of three random variables.

    Explanation
    ===========

    Mathematically Coskewness is defined as

    .. math::
        coskewness(X,Y,Z)=\frac{E[(X-E[X]) * (Y-E[Y]) * (Z-E[Z])]} {\sigma_{X}\sigma_{Y}\sigma_{Z}}

    Parameters
    ==========

    X : RandomSymbol
            Random Variable used to calculate coskewness
    Y : RandomSymbol
            Random Variable used to calculate coskewness
    Z : RandomSymbol
            Random Variable used to calculate coskewness
    condition : Expr containing RandomSymbols
            A conditional expression

    Examples
    ========

    >>> from sympy.stats import coskewness, Exponential, skewness
    >>> from sympy import symbols
    >>> p = symbols('p', positive=True)
    >>> X = Exponential('X', p)
    >>> Y = Exponential('Y', 2*p)
    >>> coskewness(X, Y, Y)
    0
    >>> coskewness(X, Y + X, Y + 2*X)
    16*sqrt(85)/85
    >>> coskewness(X + 2*Y, Y + X, Y + 2*X, X > 3)
    9*sqrt(170)/85
    >>> coskewness(Y, Y, Y) == skewness(Y)
    True
    >>> coskewness(X, Y + p*X, Y + 2*p*X)
    4/(sqrt(1 + 1/(4*p**2))*sqrt(4 + 1/(4*p**2)))

    Returns
    =======

    coskewness : The coskewness of the three random variables

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Coskewness

    """
    ...

P = ...
E = ...
H = ...
