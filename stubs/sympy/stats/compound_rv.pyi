from typing import Any, Self
from sympy import Basic, Equality, Integral, Ne, Piecewise, Sum
from sympy.core.function import Lambda
from sympy.core.relational import Relational
from sympy.series.order import Order
from sympy.stats.crv import ContinuousDistribution, ContinuousPSpace, SingleContinuousDomain, SingleContinuousPSpace
from sympy.stats.drv import DiscreteDistribution, DiscretePSpace, SingleDiscreteDomain, SingleDiscretePSpace
from sympy.stats.frv import FiniteDensity, FinitePSpace, SingleFiniteDistribution, SingleFiniteDomain, SingleFinitePSpace
from sympy.stats.rv import Distribution, NamedArgsMixin, PSpace, RandomSymbol
from sympy.stats.symbolic_probability import Probability

class CompoundPSpace(PSpace):
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
    


