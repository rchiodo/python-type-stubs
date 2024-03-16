from sympy.assumptions.assume import UndefinedPredicate
from sympy.assumptions.predicates.sets import *
from sympy.assumptions.predicates.calculus import *
from sympy.utilities.decorator import memoize_property

"""Module for querying SymPy objects about assumptions."""
class AssumptionKeys:
    """
    This class contains all the supported keys by ``ask``.
    It should be accessed via the instance ``sympy.Q``.

    """
    @memoize_property
    def hermitian(self) -> UndefinedPredicate | HermitianPredicate:
        ...
    
    @memoize_property
    def antihermitian(self) -> UndefinedPredicate | AntihermitianPredicate:
        ...
    
    @memoize_property
    def real(self) -> UndefinedPredicate | RealPredicate:
        ...
    
    @memoize_property
    def extended_real(self) -> UndefinedPredicate | ExtendedRealPredicate:
        ...
    
    @memoize_property
    def imaginary(self) -> UndefinedPredicate | ImaginaryPredicate:
        ...
    
    @memoize_property
    def complex(self) -> UndefinedPredicate | ComplexPredicate:
        ...
    
    @memoize_property
    def algebraic(self) -> UndefinedPredicate | AlgebraicPredicate:
        ...
    
    @memoize_property
    def transcendental(self) -> UndefinedPredicate | TranscendentalPredicate:
        ...
    
    @memoize_property
    def integer(self) -> UndefinedPredicate | IntegerPredicate:
        ...
    
    @memoize_property
    def noninteger(self) -> UndefinedPredicate | NonIntegerPredicate:
        ...
    
    @memoize_property
    def rational(self) -> UndefinedPredicate | RationalPredicate:
        ...
    
    @memoize_property
    def irrational(self) -> UndefinedPredicate | IrrationalPredicate:
        ...
    
    @memoize_property
    def finite(self) -> UndefinedPredicate | FinitePredicate:
        ...
    
    @memoize_property
    def infinite(self) -> UndefinedPredicate | InfinitePredicate:
        ...
    
    @memoize_property
    def positive_infinite(self) -> UndefinedPredicate | PositiveInfinitePredicate:
        ...
    
    @memoize_property
    def negative_infinite(self) -> UndefinedPredicate | NegativeInfinitePredicate:
        ...
    
    @memoize_property
    def positive(self) -> UndefinedPredicate | PositivePredicate:
        ...
    
    @memoize_property
    def negative(self) -> UndefinedPredicate | NegativePredicate:
        ...
    
    @memoize_property
    def zero(self) -> UndefinedPredicate | ZeroPredicate:
        ...
    
    @memoize_property
    def extended_positive(self) -> UndefinedPredicate | ExtendedPositivePredicate:
        ...
    
    @memoize_property
    def extended_negative(self) -> UndefinedPredicate | ExtendedNegativePredicate:
        ...
    
    @memoize_property
    def nonzero(self) -> UndefinedPredicate | NonZeroPredicate:
        ...
    
    @memoize_property
    def nonpositive(self) -> UndefinedPredicate | NonPositivePredicate:
        ...
    
    @memoize_property
    def nonnegative(self) -> UndefinedPredicate | NonNegativePredicate:
        ...
    
    @memoize_property
    def extended_nonzero(self) -> UndefinedPredicate | ExtendedNonZeroPredicate:
        ...
    
    @memoize_property
    def extended_nonpositive(self) -> UndefinedPredicate | ExtendedNonPositivePredicate:
        ...
    
    @memoize_property
    def extended_nonnegative(self) -> UndefinedPredicate | ExtendedNonNegativePredicate:
        ...
    
    @memoize_property
    def even(self) -> UndefinedPredicate | EvenPredicate:
        ...
    
    @memoize_property
    def odd(self) -> UndefinedPredicate | OddPredicate:
        ...
    
    @memoize_property
    def prime(self) -> UndefinedPredicate | PrimePredicate:
        ...
    
    @memoize_property
    def composite(self) -> UndefinedPredicate | CompositePredicate:
        ...
    
    @memoize_property
    def commutative(self) -> UndefinedPredicate | CommutativePredicate:
        ...
    
    @memoize_property
    def is_true(self) -> UndefinedPredicate | IsTruePredicate:
        ...
    
    @memoize_property
    def symmetric(self) -> UndefinedPredicate | SymmetricPredicate:
        ...
    
    @memoize_property
    def invertible(self) -> UndefinedPredicate | InvertiblePredicate:
        ...
    
    @memoize_property
    def orthogonal(self) -> UndefinedPredicate | OrthogonalPredicate:
        ...
    
    @memoize_property
    def unitary(self) -> UndefinedPredicate | UnitaryPredicate:
        ...
    
    @memoize_property
    def positive_definite(self) -> UndefinedPredicate | PositiveDefinitePredicate:
        ...
    
    @memoize_property
    def upper_triangular(self) -> UndefinedPredicate | UpperTriangularPredicate:
        ...
    
    @memoize_property
    def lower_triangular(self) -> UndefinedPredicate | LowerTriangularPredicate:
        ...
    
    @memoize_property
    def diagonal(self) -> UndefinedPredicate | DiagonalPredicate:
        ...
    
    @memoize_property
    def fullrank(self) -> UndefinedPredicate | FullRankPredicate:
        ...
    
    @memoize_property
    def square(self) -> UndefinedPredicate | SquarePredicate:
        ...
    
    @memoize_property
    def integer_elements(self) -> UndefinedPredicate | IntegerElementsPredicate:
        ...
    
    @memoize_property
    def real_elements(self) -> UndefinedPredicate | RealElementsPredicate:
        ...
    
    @memoize_property
    def complex_elements(self) -> UndefinedPredicate | ComplexElementsPredicate:
        ...
    
    @memoize_property
    def singular(self) -> UndefinedPredicate | SingularPredicate:
        ...
    
    @memoize_property
    def normal(self) -> UndefinedPredicate | NormalPredicate:
        ...
    
    @memoize_property
    def triangular(self) -> UndefinedPredicate | TriangularPredicate:
        ...
    
    @memoize_property
    def unit_triangular(self) -> UndefinedPredicate | UnitTriangularPredicate:
        ...
    
    @memoize_property
    def eq(self) -> UndefinedPredicate | EqualityPredicate:
        ...
    
    @memoize_property
    def ne(self) -> UndefinedPredicate | UnequalityPredicate:
        ...
    
    @memoize_property
    def gt(self) -> UndefinedPredicate | StrictGreaterThanPredicate:
        ...
    
    @memoize_property
    def ge(self) -> UndefinedPredicate | GreaterThanPredicate:
        ...
    
    @memoize_property
    def lt(self) -> UndefinedPredicate | StrictLessThanPredicate:
        ...
    
    @memoize_property
    def le(self) -> UndefinedPredicate | LessThanPredicate:
        ...
    


Q = ...
def ask(proposition, assumptions=..., context=...) -> bool | None:
    """
    Function to evaluate the proposition with assumptions.

    Explanation
    ===========

    This function evaluates the proposition to ``True`` or ``False`` if
    the truth value can be determined. If not, it returns ``None``.

    It should be discerned from :func:`~.refine()` which, when applied to a
    proposition, simplifies the argument to symbolic ``Boolean`` instead of
    Python built-in ``True``, ``False`` or ``None``.

    **Syntax**

        * ask(proposition)
            Evaluate the *proposition* in global assumption context.

        * ask(proposition, assumptions)
            Evaluate the *proposition* with respect to *assumptions* in
            global assumption context.

    Parameters
    ==========

    proposition : Boolean
        Proposition which will be evaluated to boolean value. If this is
        not ``AppliedPredicate``, it will be wrapped by ``Q.is_true``.

    assumptions : Boolean, optional
        Local assumptions to evaluate the *proposition*.

    context : AssumptionsContext, optional
        Default assumptions to evaluate the *proposition*. By default,
        this is ``sympy.assumptions.global_assumptions`` variable.

    Returns
    =======

    ``True``, ``False``, or ``None``

    Raises
    ======

    TypeError : *proposition* or *assumptions* is not valid logical expression.

    ValueError : assumptions are inconsistent.

    Examples
    ========

    >>> from sympy import ask, Q, pi
    >>> from sympy.abc import x, y
    >>> ask(Q.rational(pi))
    False
    >>> ask(Q.even(x*y), Q.even(x) & Q.integer(y))
    True
    >>> ask(Q.prime(4*x), Q.integer(x))
    False

    If the truth value cannot be determined, ``None`` will be returned.

    >>> print(ask(Q.odd(3*x))) # cannot determine unless we know x
    None

    ``ValueError`` is raised if assumptions are inconsistent.

    >>> ask(Q.integer(x), Q.even(x) & Q.odd(x))
    Traceback (most recent call last):
      ...
    ValueError: inconsistent assumptions Q.even(x) & Q.odd(x)

    Notes
    =====

    Relations in assumptions are not implemented (yet), so the following
    will not give a meaningful result.

    >>> ask(Q.positive(x), x > 0)

    It is however a work in progress.

    See Also
    ========

    sympy.assumptions.refine.refine : Simplification using assumptions.
        Proposition is not reduced to ``None`` if the truth value cannot
        be determined.
    """
    ...

def register_handler(key, handler) -> None:
    """
    Register a handler in the ask system. key must be a string and handler a
    class inheriting from AskHandler.

    .. deprecated:: 1.8.
        Use multipledispatch handler instead. See :obj:`~.Predicate`.

    """
    ...

def remove_handler(key, handler) -> None:
    """
    Removes a handler from the ask system.

    .. deprecated:: 1.8.
        Use multipledispatch handler instead. See :obj:`~.Predicate`.

    """
    ...

