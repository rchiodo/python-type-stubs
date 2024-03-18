from typing import Any, Literal, Self
from sympy import Basic, Contains, Equality, FiniteSet, Intersection, Ne, Piecewise, Sum
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.relational import Relational
from sympy.logic.boolalg import Boolean
from sympy.series.order import Order
from sympy.sets.sets import Complement, Union
from sympy.stats.rv import ConditionalDomain, Distribution, NamedArgsMixin, PSpace, ProductDomain, RandomDomain, RandomSymbol, SingleDomain, SinglePSpace
from sympy.stats.symbolic_probability import Probability

class DiscreteDistribution(Distribution):
    def __call__(self, *args):
        ...
    


class SingleDiscreteDistribution(DiscreteDistribution, NamedArgsMixin):
    """ Discrete distribution of a single variable.

    Serves as superclass for PoissonDistribution etc....

    Provides methods for pdf, cdf, and sampling

    See Also:
        sympy.stats.crv_types.*
    """
    set = ...
    def __new__(cls, *args) -> Self:
        ...
    
    @staticmethod
    def check(*args) -> None:
        ...
    
    @cacheit
    def compute_cdf(self, **kwargs) -> Lambda:
        """ Compute the CDF from the PDF.

        Returns a Lambda.
        """
        ...
    
    def cdf(self, x, **kwargs) -> Basic:
        """ Cumulative density function """
        ...
    
    @cacheit
    def compute_characteristic_function(self, **kwargs) -> Lambda:
        """ Compute the characteristic function from the PDF.

        Returns a Lambda.
        """
        ...
    
    def characteristic_function(self, t, **kwargs) -> Basic:
        """ Characteristic function """
        ...
    
    @cacheit
    def compute_moment_generating_function(self, **kwargs) -> Lambda:
        ...
    
    def moment_generating_function(self, t, **kwargs) -> Basic:
        ...
    
    @cacheit
    def compute_quantile(self, **kwargs) -> Lambda:
        """ Compute the Quantile from the PDF.

        Returns a Lambda.
        """
        ...
    
    def quantile(self, x, **kwargs) -> Basic:
        """ Cumulative density function """
        ...
    
    def expectation(self, expr, var, evaluate=..., **kwargs) -> Any | tuple[Any, ...] | Sum | Order | Piecewise | Basic | Equality | Relational | Ne | Literal[0] | None:
        """ Expectation of expression over distribution """
        ...
    
    def __call__(self, *args):
        ...
    


class DiscreteDomain(RandomDomain):
    """
    A domain with discrete support with step size one.
    Represented using symbols and Range.
    """
    is_Discrete = ...


class SingleDiscreteDomain(DiscreteDomain, SingleDomain):
    def as_boolean(self) -> Boolean | Contains:
        ...
    


class ConditionalDiscreteDomain(DiscreteDomain, ConditionalDomain):
    """
    Domain with discrete support of step size one, that is restricted by
    some condition.
    """
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement:
        ...
    


class DiscretePSpace(PSpace):
    is_real = ...
    is_Discrete = ...
    @property
    def pdf(self):
        ...
    
    def where(self, condition) -> SingleDiscreteDomain:
        ...
    
    def probability(self, condition) -> Probability | tuple[Any, ...] | Sum | Order | Any | Piecewise | Basic | Equality | Relational | Ne | int:
        ...
    
    def eval_prob(self, _domain) -> tuple[Any, ...] | Sum | Order | Any | Piecewise | Basic | Equality | Relational | Ne | int | None:
        ...
    
    def conditional_space(self, condition) -> DiscretePSpace:
        ...
    


class ProductDiscreteDomain(ProductDomain, DiscreteDomain):
    def as_boolean(self) -> And:
        ...
    


class SingleDiscretePSpace(DiscretePSpace, SinglePSpace):
    """ Discrete probability space over a single univariate variable """
    is_real = ...
    @property
    def set(self):
        ...
    
    @property
    def domain(self) -> SingleDiscreteDomain:
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[RandomSymbol, Any]:
        """
        Internal sample method.

        Returns dictionary mapping RandomSymbol to realization value.
        """
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> Equality | Relational | Ne | Sum:
        ...
    
    def compute_cdf(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_density(self, expr, **kwargs) -> Basic:
        ...
    
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_quantile(self, expr, **kwargs) -> Lambda:
        ...
    


