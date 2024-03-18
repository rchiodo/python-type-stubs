from typing import Any, Self
from sympy import Basic, Equality, FiniteSet, Indexed, Integral, Ne, ProductSet, Sum
from sympy.core.expr import Expr
from sympy.core.function import Lambda
from sympy.core.relational import Relational
from sympy.stats.crv import ProductContinuousDomain, SingleContinuousPSpace
from sympy.stats.drv import ProductDiscreteDomain, SingleDiscretePSpace
from sympy.stats.frv import ProductFiniteDomain
from sympy.stats.rv import Distribution, NamedArgsMixin, ProductDomain, ProductPSpace, RandomSymbol, SingleDomain

"""
Joint Random Variables Module

See Also
========
sympy.stats.rv
sympy.stats.frv
sympy.stats.crv
sympy.stats.drv
"""
class JointPSpace(ProductPSpace):
    """
    Represents a joint probability space. Represented using symbols for
    each component and a distribution.
    """
    def __new__(cls, sym, dist) -> SingleContinuousPSpace | SingleDiscretePSpace | Self:
        ...
    
    @property
    def set(self) -> Basic | FiniteSet | ProductSet:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    @property
    def value(self) -> RandomSymbol | JointRandomSymbol:
        ...
    
    @property
    def component_count(self) -> Expr:
        ...
    
    @property
    def pdf(self):
        ...
    
    @property
    def domain(self) -> SingleDomain | ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    def component_domain(self, index):
        ...
    
    def marginal_distribution(self, *indices) -> Lambda:
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def where(self, condition):
        ...
    
    def compute_density(self, expr):
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[RandomSymbol, Any]:
        """
        Internal sample method

        Returns dictionary mapping RandomSymbol to realization value.
        """
        ...
    
    def probability(self, condition):
        ...
    


class SampleJointScipy:
    """Returns the sample from scipy of the given distribution"""
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


class SampleJointNumpy:
    """Returns the sample from numpy of the given distribution"""
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


class SampleJointPymc:
    """Returns the sample from pymc of the given distribution"""
    def __new__(cls, dist, size, seed=...) -> None:
        ...
    


_get_sample_class_jrv = ...
class JointDistribution(Distribution, NamedArgsMixin):
    """
    Represented by the random variables part of the joint distribution.
    Contains methods for PDF, CDF, sampling, marginal densities, etc.
    """
    _argnames = ...
    def __new__(cls, *args) -> Self:
        ...
    
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    @property
    def pdf(self):
        ...
    
    def cdf(self, other) -> Equality | Relational | Ne | Integral | Sum:
        ...
    
    def sample(self, size=..., library=..., seed=...):
        """ A random realization from the distribution """
        ...
    
    def __call__(self, *args):
        ...
    


class JointRandomSymbol(RandomSymbol):
    """
    Representation of random symbols with joint probability distributions
    to allow indexing."
    """
    def __getitem__(self, key) -> Indexed | None:
        ...
    


class MarginalDistribution(Distribution):
    """
    Represents the marginal distribution of a joint probability space.

    Initialised using a probability distribution and random variables(or
    their indexed components) which should be a part of the resultant
    distribution.
    """
    def __new__(cls, dist, *rvs) -> Self:
        ...
    
    def check(self) -> None:
        ...
    
    @property
    def set(self) -> FiniteSet | ProductSet:
        ...
    
    @property
    def symbols(self) -> set[Any]:
        ...
    
    def pdf(self, *x) -> Basic:
        ...
    
    def compute_pdf(self, expr, rvs) -> Equality | Relational | Ne | Integral | Sum:
        ...
    
    def marginalise_out(self, expr, rv) -> Equality | Relational | Ne | Integral | Sum:
        ...
    
    def __call__(self, *args) -> Basic:
        ...
    


