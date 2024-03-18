from functools import singledispatch
from typing import Any, Generator, Literal, Self
from sympy import Equality, FiniteSet, Integral, Ne, Piecewise, ProductSet, Sum
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.relational import Relational
from sympy.matrices.expressions.matexpr import MatrixSymbol
from sympy.series.order import Order
from sympy.stats.compound_rv import CompoundPSpace
from sympy.stats.crv import ContinuousPSpace, ProductContinuousDomain
from sympy.stats.drv import DiscretePSpace, ProductDiscreteDomain
from sympy.stats.frv import ConditionalFiniteDomain, FiniteDensity, FinitePSpace, ProductFiniteDomain, ProductFinitePSpace
from sympy.stats.frv_types import BernoulliDistribution
from sympy.stats.joint_rv import JointRandomSymbol
from sympy.stats.stochastic_process import StochasticPSpace
from sympy.stats.symbolic_multivariate_probability import ExpectationMatrix
from sympy.stats.symbolic_probability import Expectation, Probability
from sympy.utilities.decorator import doctest_depends_on

"""
Main Random Variables Module

Defines abstract random variable type.
Contains interfaces for probability space object (PSpace) as well as standard
operators, P, E, sample, density, where, quantile

See Also
========

sympy.stats.crv
sympy.stats.frv
sympy.stats.rv_interface
"""
x = ...
@singledispatch
def is_random(x) -> bool:
    ...

@is_random.register(Basic)
def _(x) -> bool:
    ...

class RandomDomain(Basic):
    """
    Represents a set of variables and the values which they can take.

    See Also
    ========

    sympy.stats.crv.ContinuousDomain
    sympy.stats.frv.FiniteDomain
    """
    is_ProductDomain = ...
    is_Finite = ...
    is_Continuous = ...
    is_Discrete = ...
    def __new__(cls, symbols, *args) -> Self:
        ...
    
    @property
    def symbols(self) -> Basic:
        ...
    
    @property
    def set(self) -> Basic:
        ...
    
    def __contains__(self, other):
        ...
    
    def compute_expectation(self, expr):
        ...
    


class SingleDomain(RandomDomain):
    """
    A single variable and its domain.

    See Also
    ========

    sympy.stats.crv.SingleContinuousDomain
    sympy.stats.frv.SingleFiniteDomain
    """
    def __new__(cls, symbol, set) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    


class MatrixDomain(RandomDomain):
    """
    A Random Matrix variable and its domain.

    """
    def __new__(cls, symbol, set) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    


class ConditionalDomain(RandomDomain):
    """
    A RandomDomain with an attached condition.

    See Also
    ========

    sympy.stats.crv.ConditionalContinuousDomain
    sympy.stats.frv.ConditionalFiniteDomain
    """
    def __new__(cls, fulldomain, condition) -> Self:
        ...
    
    @property
    def symbols(self):
        ...
    
    @property
    def fulldomain(self) -> Basic:
        ...
    
    @property
    def condition(self) -> Basic:
        ...
    
    @property
    def set(self):
        ...
    
    def as_boolean(self) -> And:
        ...
    


class PSpace(Basic):
    """
    A Probability Space.

    Explanation
    ===========

    Probability Spaces encode processes that equal different values
    probabilistically. These underly Random Symbols which occur in SymPy
    expressions and contain the mechanics to evaluate statistical statements.

    See Also
    ========

    sympy.stats.crv.ContinuousPSpace
    sympy.stats.frv.FinitePSpace
    """
    is_Finite: bool = ...
    is_Continuous: bool = ...
    is_Discrete: bool = ...
    is_real: bool = ...
    @property
    def domain(self) -> Basic:
        ...
    
    @property
    def density(self) -> Basic:
        ...
    
    @property
    def values(self) -> frozenset[RandomSymbol]:
        ...
    
    @property
    def symbols(self):
        ...
    
    def where(self, condition):
        ...
    
    def compute_density(self, expr):
        ...
    
    def sample(self, size=..., library=..., seed=...):
        ...
    
    def probability(self, condition):
        ...
    
    def compute_expectation(self, expr):
        ...
    


class SinglePSpace(PSpace):
    """
    Represents the probabilities of a set of random events that can be
    attributed to a single variable/symbol.
    """
    def __new__(cls, s, distribution) -> Self:
        ...
    
    @property
    def value(self) -> RandomSymbol:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    @property
    def pdf(self):
        ...
    


class RandomSymbol(Expr):
    """
    Random Symbols represent ProbabilitySpaces in SymPy Expressions.
    In principle they can take on any value that their symbol can take on
    within the associated PSpace with probability determined by the PSpace
    Density.

    Explanation
    ===========

    Random Symbols contain pspace and symbol properties.
    The pspace property points to the represented Probability Space
    The symbol is a standard SymPy Symbol that is used in that probability space
    for example in defining a density.

    You can form normal SymPy expressions using RandomSymbols and operate on
    those expressions with the Functions

    E - Expectation of a random expression
    P - Probability of a condition
    density - Probability Density of an expression
    given - A new random expression (with new random symbols) given a condition

    An object of the RandomSymbol type should almost never be created by the
    user. They tend to be created instead by the PSpace class's value method.
    Traditionally a user does not even do this but instead calls one of the
    convenience functions Normal, Exponential, Coin, Die, FiniteRV, etc....
    """
    def __new__(cls, symbol, pspace=...) -> RandomSymbol | Self:
        ...
    
    is_finite = ...
    is_symbol = ...
    is_Atom = ...
    _diff_wrt = ...
    pspace = ...
    symbol = ...
    name = ...
    @property
    def is_commutative(self) -> Any:
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


class RandomIndexedSymbol(RandomSymbol):
    def __new__(cls, idx_obj, pspace=...) -> Self:
        ...
    
    symbol = ...
    name = ...
    @property
    def key(self) -> Basic | None:
        ...
    
    @property
    def free_symbols(self) -> set[Basic] | set[Self]:
        ...
    
    @property
    def pspace(self) -> Basic:
        ...
    


class RandomMatrixSymbol(RandomSymbol, MatrixSymbol):
    def __new__(cls, symbol, n, m, pspace=...) -> Self:
        ...
    
    symbol = ...
    pspace = ...


class ProductPSpace(PSpace):
    """
    Abstract class for representing probability spaces with multiple random
    variables.

    See Also
    ========

    sympy.stats.rv.IndependentProductPSpace
    sympy.stats.joint_rv.JointPSpace
    """
    ...


class IndependentProductPSpace(ProductPSpace):
    """
    A probability space resulting from the merger of two independent probability
    spaces.

    Often created using the function, pspace.
    """
    def __new__(cls, *spaces) -> ProductFinitePSpace | Self:
        ...
    
    @property
    def pdf(self) -> Order | Basic:
        ...
    
    @property
    def rs_space_dict(self) -> dict[Any, Any]:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def spaces(self) -> FiniteSet:
        ...
    
    @property
    def values(self) -> frozenset[Any]:
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs):
        ...
    
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    @property
    def density(self):
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[Any, Any]:
        ...
    
    def probability(self, condition, **kwargs) -> Order | Lambda | Probability | tuple[Any, ...] | Sum | Any | Piecewise | Basic | Equality | Relational | Ne | int:
        ...
    
    def compute_density(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_cdf(self, expr, **kwargs):
        ...
    
    def conditional_space(self, condition, normalize=..., **kwargs) -> FinitePSpace | ContinuousPSpace | DiscretePSpace:
        ...
    


class ProductDomain(RandomDomain):
    """
    A domain resulting from the merger of two independent domains.

    See Also
    ========
    sympy.stats.crv.ProductContinuousDomain
    sympy.stats.frv.ProductFiniteDomain
    """
    is_ProductDomain = ...
    def __new__(cls, *domains) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | Self:
        ...
    
    @property
    def sym_domain_dict(self) -> dict[Any, Basic]:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def domains(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def set(self) -> FiniteSet | ProductSet:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    
    def as_boolean(self) -> And:
        ...
    


def random_symbols(expr) -> list[Any]:
    """
    Returns all RandomSymbols within a SymPy Expression.
    """
    ...

def pspace(expr) -> Any | CompoundPSpace | StochasticPSpace | ProductFinitePSpace | IndependentProductPSpace:
    """
    Returns the underlying Probability Space of a random expression.

    For internal use.

    Examples
    ========

    >>> from sympy.stats import pspace, Normal
    >>> X = Normal('X', 0, 1)
    >>> pspace(2*X + 1) == X.pspace
    True
    """
    ...

def sumsets(sets) -> frozenset[Any]:
    """
    Union of sets
    """
    ...

def rs_swap(a, b) -> dict[Any, Any]:
    """
    Build a dictionary to swap RandomSymbols based on their underlying symbol.

    i.e.
    if    ``X = ('x', pspace1)``
    and   ``Y = ('x', pspace2)``
    then ``X`` and ``Y`` match and the key, value pair
    ``{X:Y}`` will appear in the result

    Inputs: collections a and b of random variables which share common symbols
    Output: dict mapping RVs in a to RVs in b
    """
    ...

def given(expr, condition=..., **kwargs) -> Relational | Basic | bool:
    r""" Conditional Random Expression.

    Explanation
    ===========

    From a random expression and a condition on that expression creates a new
    probability space from the condition and returns the same expression on that
    conditional probability space.

    Examples
    ========

    >>> from sympy.stats import given, density, Die
    >>> X = Die('X', 6)
    >>> Y = given(X, X > 3)
    >>> density(Y).dict
    {4: 1/3, 5: 1/3, 6: 1/3}

    Following convention, if the condition is a random symbol then that symbol
    is considered fixed.

    >>> from sympy.stats import Normal
    >>> from sympy import pprint
    >>> from sympy.abc import z

    >>> X = Normal('X', 0, 1)
    >>> Y = Normal('Y', 0, 1)
    >>> pprint(density(X + Y, Y)(z), use_unicode=False)
                    2
           -(-Y + z)
           -----------
      ___       2
    \/ 2 *e
    ------------------
             ____
         2*\/ pi
    """
    ...

def expectation(expr, condition=..., numsamples=..., evaluate=..., **kwargs) -> Basic | Expectation | tuple[Any, ...] | Sum | Order | Any | Piecewise | Equality | Relational | Ne | Integral | ExpectationMatrix | None:
    """
    Returns the expected value of a random expression.

    Parameters
    ==========

    expr : Expr containing RandomSymbols
        The expression of which you want to compute the expectation value
    given : Expr containing RandomSymbols
        A conditional expression. E(X, X>0) is expectation of X given X > 0
    numsamples : int
        Enables sampling and approximates the expectation with this many samples
    evalf : Bool (defaults to True)
        If sampling return a number rather than a complex expression
    evaluate : Bool (defaults to True)
        In case of continuous systems return unevaluated integral

    Examples
    ========

    >>> from sympy.stats import E, Die
    >>> X = Die('X', 6)
    >>> E(X)
    7/2
    >>> E(2*X + 1)
    8

    >>> E(X, X > 3) # Expectation of X given that it is above 3
    5
    """
    ...

def probability(condition, given_condition=..., numsamples=..., evaluate=..., **kwargs) -> Any | BernoulliDistribution | Probability | tuple[Any, ...] | Sum | Order | Piecewise | Basic | Equality | Relational | Ne | Lambda | int | None:
    """
    Probability that a condition is true, optionally given a second condition.

    Parameters
    ==========

    condition : Combination of Relationals containing RandomSymbols
        The condition of which you want to compute the probability
    given_condition : Combination of Relationals containing RandomSymbols
        A conditional expression. P(X > 1, X > 0) is expectation of X > 1
        given X > 0
    numsamples : int
        Enables sampling and approximates the probability with this many samples
    evaluate : Bool (defaults to True)
        In case of continuous systems return unevaluated integral

    Examples
    ========

    >>> from sympy.stats import P, Die
    >>> from sympy import Eq
    >>> X, Y = Die('X', 6), Die('Y', 6)
    >>> P(X > 3)
    1/2
    >>> P(Eq(X, 5), X > 2) # Probability that X == 5 given that X > 2
    1/4
    >>> P(X > Y)
    5/12
    """
    ...

class Density(Basic):
    expr = ...
    def __new__(cls, expr, condition=...) -> Self:
        ...
    
    @property
    def condition(self) -> Basic | None:
        ...
    
    def doit(self, evaluate=..., **kwargs) -> Density | dict[Any, Any] | Lambda | Basic | Any | FiniteDensity | None:
        ...
    


def density(expr, condition=..., evaluate=..., numsamples=..., **kwargs) -> dict[Any, Any] | Density | Lambda | Basic | Any | FiniteDensity | None:
    """
    Probability density of a random expression, optionally given a second
    condition.

    Explanation
    ===========

    This density will take on different forms for different types of
    probability spaces. Discrete variables produce Dicts. Continuous
    variables produce Lambdas.

    Parameters
    ==========

    expr : Expr containing RandomSymbols
        The expression of which you want to compute the density value
    condition : Relational containing RandomSymbols
        A conditional expression. density(X > 1, X > 0) is density of X > 1
        given X > 0
    numsamples : int
        Enables sampling and approximates the density with this many samples

    Examples
    ========

    >>> from sympy.stats import density, Die, Normal
    >>> from sympy import Symbol

    >>> x = Symbol('x')
    >>> D = Die('D', 6)
    >>> X = Normal(x, 0, 1)

    >>> density(D).dict
    {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
    >>> density(2*D).dict
    {2: 1/6, 4: 1/6, 6: 1/6, 8: 1/6, 10: 1/6, 12: 1/6}
    >>> density(X)(x)
    sqrt(2)*exp(-x**2/2)/(2*sqrt(pi))
    """
    ...

def cdf(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any | dict[Any, Any]:
    """
    Cumulative Distribution Function of a random expression.

    optionally given a second condition.

    Explanation
    ===========

    This density will take on different forms for different types of
    probability spaces.
    Discrete variables produce Dicts.
    Continuous variables produce Lambdas.

    Examples
    ========

    >>> from sympy.stats import density, Die, Normal, cdf

    >>> D = Die('D', 6)
    >>> X = Normal('X', 0, 1)

    >>> density(D).dict
    {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
    >>> cdf(D)
    {1: 1/6, 2: 1/3, 3: 1/2, 4: 2/3, 5: 5/6, 6: 1}
    >>> cdf(3*D, D > 2)
    {9: 1/4, 12: 1/2, 15: 3/4, 18: 1}

    >>> cdf(X)
    Lambda(_z, erf(sqrt(2)*_z/2)/2 + 1/2)
    """
    ...

def characteristic_function(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any:
    """
    Characteristic function of a random expression, optionally given a second condition.

    Returns a Lambda.

    Examples
    ========

    >>> from sympy.stats import Normal, DiscreteUniform, Poisson, characteristic_function

    >>> X = Normal('X', 0, 1)
    >>> characteristic_function(X)
    Lambda(_t, exp(-_t**2/2))

    >>> Y = DiscreteUniform('Y', [1, 2, 7])
    >>> characteristic_function(Y)
    Lambda(_t, exp(7*_t*I)/3 + exp(2*_t*I)/3 + exp(_t*I)/3)

    >>> Z = Poisson('Z', 2)
    >>> characteristic_function(Z)
    Lambda(_t, exp(2*exp(_t*I) - 2))
    """
    ...

def moment_generating_function(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any:
    ...

def where(condition, given_condition=..., **kwargs) -> ConditionalFiniteDomain | Any:
    """
    Returns the domain where a condition is True.

    Examples
    ========

    >>> from sympy.stats import where, Die, Normal
    >>> from sympy import And

    >>> D1, D2 = Die('a', 6), Die('b', 6)
    >>> a, b = D1.symbol, D2.symbol
    >>> X = Normal('x', 0, 1)

    >>> where(X**2<1)
    Domain: (-1 < x) & (x < 1)

    >>> where(X**2<1).set
    Interval.open(-1, 1)

    >>> where(And(D1<=D2, D2<3))
    Domain: (Eq(a, 1) & Eq(b, 1)) | (Eq(a, 1) & Eq(b, 2)) | (Eq(a, 2) & Eq(b, 2))
    """
    ...

@doctest_depends_on(modules=('scipy', ))
def sample(expr, condition=..., size=..., library=..., numsamples=..., seed=..., **kwargs) -> list[Any | JointRandomSymbol | Basic] | JointRandomSymbol | Basic:
    """
    A realization of the random expression.

    Parameters
    ==========

    expr : Expression of random variables
        Expression from which sample is extracted
    condition : Expr containing RandomSymbols
        A conditional expression
    size : int, tuple
        Represents size of each sample in numsamples
    library : str
        - 'scipy' : Sample using scipy
        - 'numpy' : Sample using numpy
        - 'pymc'  : Sample using PyMC

        Choose any of the available options to sample from as string,
        by default is 'scipy'
    numsamples : int
        Number of samples, each with size as ``size``.

        .. deprecated:: 1.9

        The ``numsamples`` parameter is deprecated and is only provided for
        compatibility with v1.8. Use a list comprehension or an additional
        dimension in ``size`` instead. See
        :ref:`deprecated-sympy-stats-numsamples` for details.

    seed :
        An object to be used as seed by the given external library for sampling `expr`.
        Following is the list of possible types of object for the supported libraries,

        - 'scipy': int, numpy.random.RandomState, numpy.random.Generator
        - 'numpy': int, numpy.random.RandomState, numpy.random.Generator
        - 'pymc': int

        Optional, by default None, in which case seed settings
        related to the given library will be used.
        No modifications to environment's global seed settings
        are done by this argument.

    Returns
    =======

    sample: float/list/numpy.ndarray
        one sample or a collection of samples of the random expression.

        - sample(X) returns float/numpy.float64/numpy.int64 object.
        - sample(X, size=int/tuple) returns numpy.ndarray object.

    Examples
    ========

    >>> from sympy.stats import Die, sample, Normal, Geometric
    >>> X, Y, Z = Die('X', 6), Die('Y', 6), Die('Z', 6) # Finite Random Variable
    >>> die_roll = sample(X + Y + Z)
    >>> die_roll # doctest: +SKIP
    3
    >>> N = Normal('N', 3, 4) # Continuous Random Variable
    >>> samp = sample(N)
    >>> samp in N.pspace.domain.set
    True
    >>> samp = sample(N, N>0)
    >>> samp > 0
    True
    >>> samp_list = sample(N, size=4)
    >>> [sam in N.pspace.domain.set for sam in samp_list]
    [True, True, True, True]
    >>> sample(N, size = (2,3)) # doctest: +SKIP
    array([[5.42519758, 6.40207856, 4.94991743],
       [1.85819627, 6.83403519, 1.9412172 ]])
    >>> G = Geometric('G', 0.5) # Discrete Random Variable
    >>> samp_list = sample(G, size=3)
    >>> samp_list # doctest: +SKIP
    [1, 3, 2]
    >>> [sam in G.pspace.domain.set for sam in samp_list]
    [True, True, True]
    >>> MN = Normal("MN", [3, 4], [[2, 1], [1, 2]]) # Joint Random Variable
    >>> samp_list = sample(MN, size=4)
    >>> samp_list # doctest: +SKIP
    [array([2.85768055, 3.38954165]),
     array([4.11163337, 4.3176591 ]),
     array([0.79115232, 1.63232916]),
     array([4.01747268, 3.96716083])]
    >>> [tuple(sam) in MN.pspace.domain.set for sam in samp_list]
    [True, True, True, True]

    .. versionchanged:: 1.7.0
        sample used to return an iterator containing the samples instead of value.

    .. versionchanged:: 1.9.0
        sample returns values or array of values instead of an iterator and numsamples is deprecated.

    """
    ...

def quantile(expr, evaluate=..., **kwargs) -> Lambda | Any:
    r"""
    Return the :math:`p^{th}` order quantile of a probability distribution.

    Explanation
    ===========

    Quantile is defined as the value at which the probability of the random
    variable is less than or equal to the given probability.

    .. math::
        Q(p) = \inf\{x \in (-\infty, \infty) : p \le F(x)\}

    Examples
    ========

    >>> from sympy.stats import quantile, Die, Exponential
    >>> from sympy import Symbol, pprint
    >>> p = Symbol("p")

    >>> l = Symbol("lambda", positive=True)
    >>> X = Exponential("x", l)
    >>> quantile(X)(p)
    -log(1 - p)/lambda

    >>> D = Die("d", 6)
    >>> pprint(quantile(D)(p), use_unicode=False)
    /nan  for Or(p > 1, p < 0)
    |
    | 1       for p <= 1/6
    |
    | 2       for p <= 1/3
    |
    < 3       for p <= 1/2
    |
    | 4       for p <= 2/3
    |
    | 5       for p <= 5/6
    |
    \ 6        for p <= 1

    """
    ...

def sample_iter(expr, condition=..., size=..., library=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    """
    Returns an iterator of realizations from the expression given a condition.

    Parameters
    ==========

    expr: Expr
        Random expression to be realized
    condition: Expr, optional
        A conditional expression
    size : int, tuple
        Represents size of each sample in numsamples
    numsamples: integer, optional
        Length of the iterator (defaults to infinity)
    seed :
        An object to be used as seed by the given external library for sampling `expr`.
        Following is the list of possible types of object for the supported libraries,

        - 'scipy': int, numpy.random.RandomState, numpy.random.Generator
        - 'numpy': int, numpy.random.RandomState, numpy.random.Generator
        - 'pymc': int

        Optional, by default None, in which case seed settings
        related to the given library will be used.
        No modifications to environment's global seed settings
        are done by this argument.

    Examples
    ========

    >>> from sympy.stats import Normal, sample_iter
    >>> X = Normal('X', 0, 1)
    >>> expr = X*X + 3
    >>> iterator = sample_iter(expr, numsamples=3) # doctest: +SKIP
    >>> list(iterator) # doctest: +SKIP
    [12, 4, 7]

    Returns
    =======

    sample_iter: iterator object
        iterator object containing the sample/samples of given expr

    See Also
    ========

    sample
    sampling_P
    sampling_E

    """
    ...

def sample_iter_lambdify(expr, condition=..., size=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    ...

def sample_iter_subs(expr, condition=..., size=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    ...

def sampling_P(condition, given_condition=..., library=..., numsamples=..., evalf=..., seed=..., **kwargs):
    """
    Sampling version of P.

    See Also
    ========

    P
    sampling_E
    sampling_density

    """
    ...

def sampling_E(expr, given_condition=..., library=..., numsamples=..., evalf=..., seed=..., **kwargs):
    """
    Sampling version of E.

    See Also
    ========

    P
    sampling_P
    sampling_density
    """
    ...

def sampling_density(expr, given_condition=..., library=..., numsamples=..., seed=..., **kwargs) -> dict[Any, Any]:
    """
    Sampling version of density.

    See Also
    ========
    density
    sampling_P
    sampling_E
    """
    ...

def dependent(a, b) -> Any | bool:
    """
    Dependence of two random expressions.

    Two expressions are independent if knowledge of one does not change
    computations on the other.

    Examples
    ========

    >>> from sympy.stats import Normal, dependent, given
    >>> from sympy import Tuple, Eq

    >>> X, Y = Normal('X', 0, 1), Normal('Y', 0, 1)
    >>> dependent(X, Y)
    False
    >>> dependent(2*X + Y, -Y)
    True
    >>> X, Y = given(Tuple(X, Y), Eq(X + Y, 3))
    >>> dependent(X, Y)
    True

    See Also
    ========

    independent
    """
    ...

def independent(a, b) -> bool:
    """
    Independence of two random expressions.

    Two expressions are independent if knowledge of one does not change
    computations on the other.

    Examples
    ========

    >>> from sympy.stats import Normal, independent, given
    >>> from sympy import Tuple, Eq

    >>> X, Y = Normal('X', 0, 1), Normal('Y', 0, 1)
    >>> independent(X, Y)
    True
    >>> independent(2*X + Y, -Y)
    False
    >>> X, Y = given(Tuple(X, Y), Eq(X + Y, 3))
    >>> independent(X, Y)
    False

    See Also
    ========

    dependent
    """
    ...

def pspace_independent(a, b) -> bool | None:
    """
    Tests for independence between a and b by checking if their PSpaces have
    overlapping symbols. This is a sufficient but not necessary condition for
    independence and is intended to be used internally.

    Notes
    =====

    pspace_independent(a, b) implies independent(a, b)
    independent(a, b) does not imply pspace_independent(a, b)
    """
    ...

def rv_subs(expr, symbols=...):
    """
    Given a random expression replace all random variables with their symbols.

    If symbols keyword is given restrict the swap to only the symbols listed.
    """
    ...

class NamedArgsMixin:
    _argnames: tuple[str, ...] = ...
    def __getattr__(self, attr):
        ...
    


class Distribution(Basic):
    def sample(self, size=..., library=..., seed=...):
        """ A random realization from the distribution """
        ...
    


def sample_stochastic_process(process):
    """
    This function is used to sample from stochastic process.

    Parameters
    ==========

    process: StochasticProcess
        Process used to extract the samples. It must be an instance of
        StochasticProcess

    Examples
    ========

    >>> from sympy.stats import sample_stochastic_process, DiscreteMarkovChain
    >>> from sympy import Matrix
    >>> T = Matrix([[0.5, 0.2, 0.3],[0.2, 0.5, 0.3],[0.2, 0.3, 0.5]])
    >>> Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
    >>> next(sample_stochastic_process(Y)) in Y.state_space
    True
    >>> next(sample_stochastic_process(Y))  # doctest: +SKIP
    0
    >>> next(sample_stochastic_process(Y)) # doctest: +SKIP
    2

    Returns
    =======

    sample: iterator object
        iterator object containing the sample of given process

    """
    ...

