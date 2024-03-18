from typing import Any
from sympy import Basic, FiniteSet, Intersection, Piecewise
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.numbers import Integer, Rational
from sympy.sets.sets import Complement, Union
from sympy.stats.frv import SingleFiniteDistribution
from sympy.stats.rv import Density, RandomSymbol

__all__ = ['FiniteRV', 'DiscreteUniform', 'Die', 'Bernoulli', 'Coin', 'Binomial', 'BetaBinomial', 'Hypergeometric', 'Rademacher', 'IdealSoliton', 'RobustSoliton']
def rv(name, cls, *args, **kwargs) -> RandomSymbol:
    ...

class FiniteDistributionHandmade(SingleFiniteDistribution):
    @property
    def dict(self) -> Basic:
        ...
    
    def pmf(self, x) -> Lambda:
        ...
    
    @property
    def set(self) -> set[Any]:
        ...
    
    @staticmethod
    def check(density) -> None:
        ...
    


def FiniteRV(name, density, **kwargs) -> RandomSymbol:
    ...

class DiscreteUniformDistribution(SingleFiniteDistribution):
    @staticmethod
    def check(*args) -> None:
        ...
    
    @property
    def p(self) -> Rational | Integer:
        ...
    
    @property
    @cacheit
    def dict(self) -> dict[Basic, Rational | Any | Integer]:
        ...
    
    @property
    def set(self) -> set[Basic]:
        ...
    
    def pmf(self, x) -> Rational | Integer:
        ...
    


def DiscreteUniform(name, items) -> RandomSymbol:
    ...

class DieDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(sides) -> None:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any | Integer]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def Die(name, sides=...) -> RandomSymbol:
    ...

class BernoulliDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(p, succ, fail) -> None:
        ...
    
    @property
    def set(self) -> set[Any]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def Bernoulli(name, p, succ=..., fail=...) -> RandomSymbol:
    ...

def Coin(name, p=...) -> RandomSymbol:
    ...

class BinomialDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, p, succ, fail) -> None:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    
    @property
    @cacheit
    def dict(self) -> Density | dict[Any, Any | Piecewise]:
        ...
    


def Binomial(name, n, p, succ=..., fail=...) -> RandomSymbol:
    ...

class BetaBinomialDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, alpha, beta) -> None:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any | Integer]:
        ...
    
    def pmf(self, k):
        ...
    


def BetaBinomial(name, n, alpha, beta) -> RandomSymbol:
    ...

class HypergeometricDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, N, m) -> None:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def high(self) -> Piecewise:
        ...
    
    @property
    def low(self) -> Piecewise:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[int]:
        ...
    
    def pmf(self, k):
        ...
    


def Hypergeometric(name, N, m, n) -> RandomSymbol:
    ...

class RademacherDistribution(SingleFiniteDistribution):
    @property
    def set(self) -> set[int]:
        ...
    
    @property
    def pmf(self) -> Lambda:
        ...
    


def Rademacher(name) -> RandomSymbol:
    ...

class IdealSolitonDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(k) -> None:
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def set(self) -> set[Any | Integer]:
        ...
    
    @property
    @cacheit
    def dict(self) -> Density | dict[int, Rational | Any | Integer]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def IdealSoliton(name, k) -> RandomSymbol:
    ...

class RobustSolitonDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(k, delta, c) -> None:
        ...
    
    @property
    def R(self):
        ...
    
    @property
    def Z(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def set(self) -> set[Any | Integer]:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    def pmf(self, x):
        ...
    


def RobustSoliton(name, k, delta, c) -> RandomSymbol:
    r'''
    Create a Finite Random Variable of Robust Soliton Distribution

    Parameters
    ==========

    k : Positive Integer
        Represents the number of input symbols in an LT (Luby Transform) code.
    delta : Positive Rational Number
            Represents the failure probability. Must be in the interval (0,1).
    c : Positive Rational Number
        Constant of proportionality. Values close to 1 are recommended

    Examples
    ========

    >>> from sympy.stats import RobustSoliton, density, P, E
    >>> robSol = RobustSoliton('robSol', 5, 0.5, 0.01)
    >>> density(robSol).dict
    {1: 0.204253668152708, 2: 0.490631107897393, 3: 0.165210624506162, 4: 0.0834387731899302, 5: 0.0505633404760675}
    >>> density(robSol).set
    {1, 2, 3, 4, 5}

    >>> from sympy import Symbol
    >>> k = Symbol('k', positive=True, integer=True)
    >>> c = Symbol('c', positive=True)
    >>> robSol = RobustSoliton('robSol', k, 0.5, c)
    >>> density(robSol).dict
    Density(RobustSolitonDistribution(k, 0.5, c))
    >>> density(robSol).dict.subs(k, 10).subs(c, 0.03).doit()
    {1: 0.116641095387194, 2: 0.467045731687165, 3: 0.159984123349381, 4: 0.0821431680681869, 5: 0.0505765646770100,
    6: 0.0345781523420719, 7: 0.0253132820710503, 8: 0.0194459129233227, 9: 0.0154831166726115, 10: 0.0126733075238887}

    >>> E(robSol.subs(k, 10).subs(c, 0.05))
    2.91358846104106

    >>> P(robSol.subs(k, 4).subs(c, 0.1) > 2)
    0.243650614389834

    Returns
    =======

    RandomSymbol

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Soliton_distribution#Robust_distribution
    .. [2] https://www.inference.org.uk/mackay/itprnn/ps/588.596.pdf
    .. [3] https://pages.cs.wisc.edu/~suman/courses/740/papers/luby02lt.pdf

    '''
    ...

