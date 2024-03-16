from typing import Callable, NamedTuple, Sequence, Type
from abc import ABC, abstractmethod
from dataclasses import dataclass
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.relational import Boolean
from sympy.core.symbol import Symbol
from sympy.functions.elementary.exponential import exp

"""Integration method that emulates by-hand techniques.

This module also provides functionality to get the steps used to evaluate a
particular integral, in the ``integral_steps`` function. This will return
nested ``Rule`` s representing the integration rules used.

Each ``Rule`` class represents a (maybe parametrized) integration rule, e.g.
``SinRule`` for integrating ``sin(x)`` and ``ReciprocalSqrtQuadraticRule``
for integrating ``1/sqrt(a+b*x+c*x**2)``. The ``eval`` method returns the
integration result.

The ``manualintegrate`` function computes the integral by calling ``eval``
on the rule returned by ``integral_steps``.

The integrator can be extended with new heuristics and evaluation
techniques. To do so, extend the ``Rule`` class, implement ``eval`` method,
then write a function that accepts an ``IntegralInfo`` object and returns
either a ``Rule`` instance or ``None``. If the new technique requires a new
match, add the key and call to the antiderivative function to integral_steps.
To enable simple substitutions, add the match to find_substitutions.

"""
@dataclass
class Rule(ABC):
    integrand: Expr
    variable: Symbol
    @abstractmethod
    def eval(self) -> Expr:
        ...
    
    @abstractmethod
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class AtomicRule(Rule, ABC):
    """A simple rule that does not depend on other rules"""
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class ConstantRule(AtomicRule):
    """integrate(a, x)  ->  a*x"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class ConstantTimesRule(Rule):
    """integrate(a*f(x), x)  ->  a*integrate(f(x), x)"""
    constant: Expr
    other: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class PowerRule(AtomicRule):
    """integrate(x**a, x)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class NestedPowRule(AtomicRule):
    """integrate((x**a)**b, x)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class AddRule(Rule):
    """integrate(f(x) + g(x), x) -> integrate(f(x), x) + integrate(g(x), x)"""
    substeps: list[Rule]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class URule(Rule):
    """integrate(f(g(x))*g'(x), x) -> integrate(f(u), u), u = g(x)"""
    u_var: Symbol
    u_func: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class PartsRule(Rule):
    """integrate(u(x)*v'(x), x) -> u(x)*v(x) - integrate(u'(x)*v(x), x)"""
    u: Symbol
    dv: Expr
    v_step: Rule
    second_step: Rule | None
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class CyclicPartsRule(Rule):
    """Apply PartsRule multiple times to integrate exp(x)*sin(x)"""
    parts_rules: list[PartsRule]
    coefficient: Expr
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class TrigRule(AtomicRule, ABC):
    ...


@dataclass
class SinRule(TrigRule):
    """integrate(sin(x), x) -> -cos(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class CosRule(TrigRule):
    """integrate(cos(x), x) -> sin(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class SecTanRule(TrigRule):
    """integrate(sec(x)*tan(x), x) -> sec(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class CscCotRule(TrigRule):
    """integrate(csc(x)*cot(x), x) -> -csc(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class Sec2Rule(TrigRule):
    """integrate(sec(x)**2, x) -> tan(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class Csc2Rule(TrigRule):
    """integrate(csc(x)**2, x) -> -cot(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class HyperbolicRule(AtomicRule, ABC):
    ...


@dataclass
class SinhRule(HyperbolicRule):
    """integrate(sinh(x), x) -> cosh(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class CoshRule(HyperbolicRule):
    """integrate(cosh(x), x) -> sinh(x)"""
    def eval(self) -> type[UndefinedFunction]:
        ...
    


@dataclass
class ExpRule(AtomicRule):
    """integrate(a**x, x) -> a**x/ln(a)"""
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ReciprocalRule(AtomicRule):
    """integrate(1/x, x) -> ln(x)"""
    base: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ArcsinRule(AtomicRule):
    """integrate(1/sqrt(1-x**2), x) -> asin(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class ArcsinhRule(AtomicRule):
    """integrate(1/sqrt(1+x**2), x) -> asin(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class ReciprocalSqrtQuadraticRule(AtomicRule):
    """integrate(1/sqrt(a+b*x+c*x**2), x) -> log(2*sqrt(c)*sqrt(a+b*x+c*x**2)+b+2*c*x)/sqrt(c)"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class SqrtQuadraticDenomRule(AtomicRule):
    """integrate(poly(x)/sqrt(a+b*x+c*x**2), x)"""
    a: Expr
    b: Expr
    c: Expr
    coeffs: list[Expr]
    def eval(self) -> Expr:
        ...
    


@dataclass
class SqrtQuadraticRule(AtomicRule):
    """integrate(sqrt(a+b*x+c*x**2), x)"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class AlternativeRule(Rule):
    """Multiple ways to do integration."""
    alternatives: list[Rule]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DontKnowRule(Rule):
    """Leave the integral as is."""
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DerivativeRule(AtomicRule):
    """integrate(f'(x), x) -> f(x)"""
    def eval(self) -> Expr:
        ...
    


@dataclass
class RewriteRule(Rule):
    """Rewrite integrand to another form that is easier to handle."""
    rewritten: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class CompleteSquareRule(RewriteRule):
    """Rewrite a+b*x+c*x**2 to a-b**2/(4*c) + c*(x+b/(2*c))**2"""
    ...


@dataclass
class PiecewiseRule(Rule):
    subfunctions: Sequence[tuple[Rule, bool | Boolean]]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class HeavisideRule(Rule):
    harg: Expr
    ibnd: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DiracDeltaRule(AtomicRule):
    n: Expr
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class TrigSubstitutionRule(Rule):
    theta: Expr
    func: Expr
    rewritten: Expr
    substep: Rule
    restriction: bool | Boolean
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class ArctanRule(AtomicRule):
    """integrate(a/(b*x**2+c), x) -> a/b / sqrt(c/b) * atan(x/sqrt(c/b))"""
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class OrthogonalPolyRule(AtomicRule, ABC):
    n: Expr
    ...


@dataclass
class JacobiRule(OrthogonalPolyRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class GegenbauerRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChebyshevTRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChebyshevURule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LegendreRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class HermiteRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LaguerreRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class AssocLaguerreRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class IRule(AtomicRule, ABC):
    a: Expr
    b: Expr
    ...


@dataclass
class CiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class EiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class SiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ShiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ErfRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class FresnelCRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class FresnelSRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class PolylogRule(AtomicRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class UpperGammaRule(AtomicRule):
    a: Expr
    e: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class EllipticFRule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class EllipticERule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr:
        ...
    


class IntegralInfo(NamedTuple):
    integrand: Expr
    symbol: Symbol
    ...


def manual_diff(f, symbol) -> int | ArrayDerivative | Derivative:
    """Derivative of f in form expected by find_substitutions

    SymPy's derivatives for some trig functions (like cot) are not in a form
    that works well with finding substitutions; this replaces the
    derivatives for those particular forms with something that works better.

    """
    ...

def manual_subs(expr, *args):
    """
    A wrapper for `expr.subs(*args)` with additional logic for substitution
    of invertible functions.
    """
    ...

inverse_trig_functions = ...
def find_substitutions(integrand, symbol, u_var) -> list[Any]:
    ...

def rewriter(condition, rewrite) -> Callable[..., RewriteRule | None]:
    """Strategy that rewrites an integrand."""
    ...

def proxy_rewriter(condition, rewrite) -> Callable[..., RewriteRule | None]:
    """Strategy that rewrites an integrand based on some other criteria."""
    ...

def multiplexer(conditions) -> Callable[..., Any | None]:
    """Apply the rule that matches the condition, else None"""
    ...

def alternatives(*rules) -> Callable[..., Any | AlternativeRule | None]:
    """Strategy that makes an AlternativeRule out of multiple possible results."""
    ...

def constant_rule(integral) -> ConstantRule:
    ...

def power_rule(integral) -> ReciprocalRule | PowerRule | ExpRule | ConstantRule | PiecewiseRule | None:
    ...

def exp_rule(integral) -> ExpRule | None:
    ...

def orthogonal_poly_rule(integral) -> None:
    ...

_special_function_patterns: list[tuple[Type, Expr, Callable | None, tuple]] = ...
_wilds = ...
_symbol = ...
def special_function_rule(integral) -> None:
    ...

def nested_pow_rule(integral: IntegralInfo) -> Rule | None:
    class NoMatch(Exception):
        ...
    
    

def inverse_trig_rule(integral: IntegralInfo, degenerate=...) -> NestedPowRule | Rule | None:
    """
    Set degenerate=False on recursive call where coefficient of quadratic term
    is assumed non-zero.
    """
    ...

def add_rule(integral) -> AddRule | None:
    ...

def mul_rule(integral: IntegralInfo) -> ConstantTimesRule | None:
    ...

def parts_rule(integral) -> ConstantTimesRule | CyclicPartsRule | PartsRule | None:
    ...

def trig_rule(integral) -> SinRule | CosRule | Sec2Rule | Csc2Rule | RewriteRule | None:
    ...

def trig_product_rule(integral: IntegralInfo) -> SecTanRule | CscCotRule | None:
    ...

def quadratic_denom_rule(integral) -> ArctanRule | RewriteRule | PiecewiseRule | URule | ConstantTimesRule | None:
    ...

def sqrt_linear_rule(integral: IntegralInfo) -> PiecewiseRule | URule | None:
    """
    Substitute common (a+b*x)**(1/n)
    """
    ...

def sqrt_quadratic_rule(integral: IntegralInfo, degenerate=...) -> Rule | None:
    ...

def hyperbolic_rule(integral: tuple[Expr, Symbol]) -> SinhRule | CoshRule | RewriteRule | None:
    ...

@cacheit
def make_wilds(symbol) -> tuple[Wild, Wild, Wild, Wild]:
    ...

@cacheit
def sincos_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def tansec_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def cotcsc_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def heaviside_pattern(symbol) -> tuple[Any, Wild, Wild, Wild]:
    ...

def uncurry(func) -> Callable[..., Any]:
    ...

def trig_rewriter(rewrite) -> Callable[..., RewriteRule | None]:
    ...

sincos_botheven_condition = ...
sincos_botheven = ...
sincos_sinodd_condition = ...
sincos_sinodd = ...
sincos_cosodd_condition = ...
sincos_cosodd = ...
tansec_seceven_condition = ...
tansec_seceven = ...
tansec_tanodd_condition = ...
tansec_tanodd = ...
tan_tansquared_condition = ...
tan_tansquared = ...
cotcsc_csceven_condition = ...
cotcsc_csceven = ...
cotcsc_cotodd_condition = ...
cotcsc_cotodd = ...
def trig_sincos_rule(integral) -> None:
    ...

def trig_tansec_rule(integral) -> None:
    ...

def trig_cotcsc_rule(integral) -> None:
    ...

def trig_sindouble_rule(integral) -> DontKnowRule | tuple[Any, Any] | Rule | None:
    ...

def trig_powers_products_rule(integral) -> DontKnowRule | Rule | tuple[Any, Any]:
    ...

def trig_substitution_rule(integral) -> TrigSubstitutionRule | None:
    ...

def heaviside_rule(integral) -> HeavisideRule | None:
    ...

def dirac_delta_rule(integral: IntegralInfo) -> Rule | None:
    ...

def substitution_rule(integral) -> AlternativeRule | None:
    ...

partial_fractions_rule = ...
cancel_rule = ...
distribute_expand_rule = ...
trig_expand_rule = ...
def derivative_rule(integral) -> DerivativeRule | DontKnowRule | ConstantRule:
    ...

def rewrites_rule(integral) -> RewriteRule | None:
    ...

def fallback_rule(integral) -> DontKnowRule:
    ...

_integral_cache: dict[Expr, Expr | None] = ...
_parts_u_cache: dict[Expr, int] = ...
_cache_dummy = ...
def integral_steps(integrand, symbol, **options) -> DontKnowRule | tuple[Any, Any] | Rule:
    """Returns the steps needed to compute an integral.

    Explanation
    ===========

    This function attempts to mirror what a student would do by hand as
    closely as possible.

    SymPy Gamma uses this to provide a step-by-step explanation of an
    integral. The code it uses to format the results of this function can be
    found at
    https://github.com/sympy/sympy_gamma/blob/master/app/logic/intsteps.py.

    Examples
    ========

    >>> from sympy import exp, sin
    >>> from sympy.integrals.manualintegrate import integral_steps
    >>> from sympy.abc import x
    >>> print(repr(integral_steps(exp(x) / (1 + exp(2 * x)), x))) \
    # doctest: +NORMALIZE_WHITESPACE
    URule(integrand=exp(x)/(exp(2*x) + 1), variable=x, u_var=_u, u_func=exp(x),
    substep=ArctanRule(integrand=1/(_u**2 + 1), variable=_u, a=1, b=1, c=1))
    >>> print(repr(integral_steps(sin(x), x))) \
    # doctest: +NORMALIZE_WHITESPACE
    SinRule(integrand=sin(x), variable=x)
    >>> print(repr(integral_steps((x**2 + 3)**2, x))) \
    # doctest: +NORMALIZE_WHITESPACE
    RewriteRule(integrand=(x**2 + 3)**2, variable=x, rewritten=x**4 + 6*x**2 + 9,
    substep=AddRule(integrand=x**4 + 6*x**2 + 9, variable=x,
    substeps=[PowerRule(integrand=x**4, variable=x, base=x, exp=4),
    ConstantTimesRule(integrand=6*x**2, variable=x, constant=6, other=x**2,
    substep=PowerRule(integrand=x**2, variable=x, base=x, exp=2)),
    ConstantRule(integrand=9, variable=x)]))

    Returns
    =======

    rule : Rule
        The first step; most rules have substeps that must also be
        considered. These substeps can be evaluated using ``manualintegrate``
        to obtain a result.

    """
    ...

def manualintegrate(f, var) -> Piecewise | Expr:
    """manualintegrate(f, var)

    Explanation
    ===========

    Compute indefinite integral of a single variable using an algorithm that
    resembles what a student would do by hand.

    Unlike :func:`~.integrate`, var can only be a single symbol.

    Examples
    ========

    >>> from sympy import sin, cos, tan, exp, log, integrate
    >>> from sympy.integrals.manualintegrate import manualintegrate
    >>> from sympy.abc import x
    >>> manualintegrate(1 / x, x)
    log(x)
    >>> integrate(1/x)
    log(x)
    >>> manualintegrate(log(x), x)
    x*log(x) - x
    >>> integrate(log(x))
    x*log(x) - x
    >>> manualintegrate(exp(x) / (1 + exp(2 * x)), x)
    atan(exp(x))
    >>> integrate(exp(x) / (1 + exp(2 * x)))
    RootSum(4*_z**2 + 1, Lambda(_i, _i*log(2*_i + exp(x))))
    >>> manualintegrate(cos(x)**4 * sin(x), x)
    -cos(x)**5/5
    >>> integrate(cos(x)**4 * sin(x), x)
    -cos(x)**5/5
    >>> manualintegrate(cos(x)**4 * sin(x)**3, x)
    cos(x)**7/7 - cos(x)**5/5
    >>> integrate(cos(x)**4 * sin(x)**3, x)
    cos(x)**7/7 - cos(x)**5/5
    >>> manualintegrate(tan(x), x)
    -log(cos(x))
    >>> integrate(tan(x), x)
    -log(cos(x))

    See Also
    ========

    sympy.integrals.integrals.integrate
    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    """
    ...

