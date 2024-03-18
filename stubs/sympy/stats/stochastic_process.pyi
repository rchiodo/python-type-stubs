from typing import Self
from sympy import Basic
from sympy.stats.crv import ProductContinuousDomain
from sympy.stats.drv import ProductDiscreteDomain
from sympy.stats.frv import ProductFiniteDomain
from sympy.stats.joint_rv import ProductPSpace
from sympy.stats.rv import ProductDomain

class StochasticPSpace(ProductPSpace):
    """
    Represents probability space of stochastic processes
    and their random variables. Contains mechanics to do
    computations for queries of stochastic processes.

    Explanation
    ===========

    Initialized by symbol, the specific process and
    distribution(optional) if the random indexed symbols
    of the process follows any specific distribution, like,
    in Bernoulli Process, each random indexed symbol follows
    Bernoulli distribution. For processes with memory, this
    parameter should not be passed.
    """
    def __new__(cls, sym, process, distribution=...) -> Self:
        ...
    
    @property
    def process(self) -> Basic:
        """
        The associated stochastic process.
        """
        ...
    
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    def probability(self, condition, given_condition=..., evaluate=..., **kwargs):
        """
        Transfers the task of handling queries to the specific stochastic
        process because every process has their own logic of handling such
        queries.
        """
        ...
    
    def compute_expectation(self, expr, condition=..., evaluate=..., **kwargs):
        """
        Transfers the task of handling queries to the specific stochastic
        process because every process has their own logic of handling such
        queries.
        """
        ...
    


