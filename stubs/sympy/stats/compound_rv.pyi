from sympy.stats.rv import Distribution, NamedArgsMixin, PSpace

class CompoundPSpace(PSpace):
    """
    A temporary Probability Space for the Compound Distribution. After
    Marginalization, this returns the corresponding Probability Space of the
    parent distribution.
    """
    def __new__(cls, s, distribution) -> SingleContinuousPSpace | SingleDiscretePSpace | SingleFinitePSpace | Self:
        ...
    
    @property
    def value(self) -> RandomSymbol:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def is_Continuous(self):
        ...
    
    @property
    def is_Finite(self):
        ...
    
    @property
    def is_Discrete(self):
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    @property
    def pdf(self):
        ...
    
    @property
    def set(self):
        ...
    
    @property
    def domain(self) -> SingleContinuousDomain | SingleDiscreteDomain | SingleFiniteDomain:
        ...
    
    def compute_density(self, expr, *, compound_evaluate=..., **kwargs) -> Basic | Lambda | FiniteDensity:
        ...
    
    def compute_cdf(self, expr, *, compound_evaluate=..., **kwargs) -> Lambda | dict[Any, Any]:
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> tuple[Any, ...] | Sum | Order | Any | Piecewise | Basic | Equality | Relational | Ne | Integral | None:
        ...
    
    def probability(self, condition, *, compound_evaluate=..., **kwargs) -> Probability | tuple[Any, ...] | Sum | Order | Any | Piecewise | Basic | Equality | Relational | Ne | int:
        ...
    
    def conditional_space(self, condition, *, compound_evaluate=..., **kwargs) -> ContinuousPSpace | DiscretePSpace | FinitePSpace:
        ...
    


class CompoundDistribution(Distribution, NamedArgsMixin):
    """
    Class for Compound Distributions.

    Parameters
    ==========

    dist : Distribution
        Distribution must contain a random parameter

    Examples
    ========

    >>> from sympy.stats.compound_rv import CompoundDistribution
    >>> from sympy.stats.crv_types import NormalDistribution
    >>> from sympy.stats import Normal
    >>> from sympy.abc import x
    >>> X = Normal('X', 2, 4)
    >>> N = NormalDistribution(X, 4)
    >>> C = CompoundDistribution(N)
    >>> C.set
    Interval(-oo, oo)
    >>> C.pdf(x, evaluate=True).simplify()
    exp(-x**2/64 + x/16 - 1/16)/(8*sqrt(pi))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Compound_probability_distribution

    """
    def __new__(cls, dist) -> ContinuousDistribution | SingleFiniteDistribution | DiscreteDistribution | Self:
        ...
    
    @property
    def set(self):
        ...
    
    @property
    def is_Continuous(self) -> bool:
        ...
    
    @property
    def is_Finite(self) -> bool:
        ...
    
    @property
    def is_Discrete(self) -> bool:
        ...
    
    def pdf(self, x, evaluate=...) -> Basic:
        ...
    


