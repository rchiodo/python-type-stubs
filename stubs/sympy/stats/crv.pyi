from sympy.core.cache import cacheit
from sympy.stats.rv import ConditionalDomain, Distribution, NamedArgsMixin, PSpace, ProductDomain, RandomDomain, SingleDomain, SinglePSpace

"""
Continuous Random Variables Module

See Also
========
sympy.stats.crv_types
sympy.stats.rv
sympy.stats.frv
"""
class ContinuousDomain(RandomDomain):
    """
    A domain with continuous support

    Represented using symbols and Intervals.
    """
    is_Continuous = ...
    def as_boolean(self):
        ...
    


class SingleContinuousDomain(ContinuousDomain, SingleDomain):
    """
    A univariate domain with continuous support

    Represented using a single symbol and interval.
    """
    def compute_expectation(self, expr, variables=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def as_boolean(self):
        ...
    


class ProductContinuousDomain(ProductDomain, ContinuousDomain):
    """
    A collection of independent domains with continuous support
    """
    def compute_expectation(self, expr, variables=..., **kwargs):
        ...
    
    def as_boolean(self) -> And:
        ...
    


class ConditionalContinuousDomain(ContinuousDomain, ConditionalDomain):
    """
    A domain with continuous support that has been further restricted by a
    condition such as $x > 3$.
    """
    def compute_expectation(self, expr, variables=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def as_boolean(self) -> And:
        ...
    
    @property
    def set(self):
        ...
    


class ContinuousDistribution(Distribution):
    def __call__(self, *args):
        ...
    


class SingleContinuousDistribution(ContinuousDistribution, NamedArgsMixin):
    """ Continuous distribution of a single variable.

    Explanation
    ===========

    Serves as superclass for Normal/Exponential/UniformDistribution etc....

    Represented by parameters for each of the specific classes.  E.g
    NormalDistribution is represented by a mean and standard deviation.

    Provides methods for pdf, cdf, and sampling.

    See Also
    ========

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
        """ Compute the moment generating function from the PDF.

        Returns a Lambda.
        """
        ...
    
    def moment_generating_function(self, t, **kwargs) -> Basic:
        """ Moment generating function """
        ...
    
    def expectation(self, expr, var, evaluate=..., **kwargs) -> Equality | Relational | Ne | Any | Integral | Literal[0]:
        """ Expectation of expression over distribution """
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
    


class ContinuousPSpace(PSpace):
    """ Continuous Probability Space

    Represents the likelihood of an event space defined over a continuum.

    Represented with a ContinuousDomain and a PDF (Lambda-Like)
    """
    is_Continuous = ...
    is_real = ...
    @property
    def pdf(self):
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs):
        ...
    
    def compute_density(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_cdf(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_quantile(self, expr, **kwargs) -> Lambda:
        ...
    
    def probability(self, condition, **kwargs):
        ...
    
    def where(self, condition) -> SingleContinuousDomain:
        ...
    
    def conditional_space(self, condition, normalize=..., **kwargs) -> ContinuousPSpace:
        ...
    


class SingleContinuousPSpace(ContinuousPSpace, SinglePSpace):
    """
    A continuous probability space over a single univariate variable.

    These consist of a Symbol and a SingleContinuousDistribution

    This class is normally accessed through the various random variable
    functions, Normal, Exponential, Uniform, etc....
    """
    @property
    def set(self):
        ...
    
    @property
    def domain(self) -> SingleContinuousDomain:
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[RandomSymbol, Any]:
        """
        Internal sample method.

        Returns dictionary mapping RandomSymbol to realization value.
        """
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def compute_cdf(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_density(self, expr, **kwargs) -> Basic | Lambda:
        ...
    
    def compute_quantile(self, expr, **kwargs) -> Lambda:
        ...
    


def reduce_rational_inequalities_wrap(condition, var) -> FiniteSet | Union | None:
    ...

