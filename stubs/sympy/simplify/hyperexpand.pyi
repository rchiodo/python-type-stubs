from sympy.core import Expr

"""
Expand Hypergeometric (and Meijer G) functions into named
special functions.

The algorithm for doing this uses a collection of lookup tables of
hypergeometric functions, and various of their properties, to expand
many hypergeometric functions in terms of special functions.

It is based on the following paper:
      Kelly B. Roach.  Meijer G Function Representations.
      In: Proceedings of the 1997 International Symposium on Symbolic and
      Algebraic Computation, pages 205-211, New York, 1997. ACM.

It is described in great(er) detail in the Sphinx documentation.
"""
def add_formulae(formulae) -> None:
    """ Create our knowledge base. """
    ...

def add_meijerg_formulae(formulae) -> None:
    ...

def make_simp(z) -> Callable[..., Any]:
    """ Create a function that simplifies rational functions in ``z``. """
    ...

def debug(*args) -> None:
    ...

class Hyper_Function(Expr):
    """ A generalized hypergeometric function. """
    def __new__(cls, ap, bq) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Any, Any]:
        ...
    
    @property
    def sizes(self) -> tuple[int, int]:
        ...
    
    @property
    def gamma(self) -> int:
        """
        Number of upper parameters that are negative integers

        This is a transformation invariant.
        """
        ...
    
    def __call__(self, arg) -> type[UndefinedFunction]:
        ...
    
    def build_invariants(self) -> tuple[int, tuple[tuple[Any, int], ...], tuple[tuple[Any, int], ...]]:
        """
        Compute the invariant vector.

        Explanation
        ===========

        The invariant vector is:
            (gamma, ((s1, n1), ..., (sk, nk)), ((t1, m1), ..., (tr, mr)))
        where gamma is the number of integer a < 0,
              s1 < ... < sk
              nl is the number of parameters a_i congruent to sl mod 1
              t1 < ... < tr
              ml is the number of parameters b_i congruent to tl mod 1

        If the index pair contains parameters, then this is not truly an
        invariant, since the parameters cannot be sorted uniquely mod1.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import Hyper_Function
        >>> from sympy import S
        >>> ap = (S.Half, S.One/3, S(-1)/2, -2)
        >>> bq = (1, 2)

        Here gamma = 1,
             k = 3, s1 = 0, s2 = 1/3, s3 = 1/2
                    n1 = 1, n2 = 1,   n2 = 2
             r = 1, t1 = 0
                    m1 = 2:

        >>> Hyper_Function(ap, bq).build_invariants()
        (1, ((0, 1), (1/3, 1), (1/2, 2)), ((0, 2),))
        """
        ...
    
    def difficulty(self, func) -> Literal[-1, 0]:
        """ Estimate how many steps it takes to reach ``func`` from self.
            Return -1 if impossible. """
        ...
    


class G_Function(Expr):
    """ A Meijer G-function. """
    def __new__(cls, an, ap, bm, bq) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def __call__(self, z) -> type[UndefinedFunction]:
        ...
    
    def compute_buckets(self) -> tuple[dict[Any, list[Any]], ...]:
        """
        Compute buckets for the fours sets of parameters.

        Explanation
        ===========

        We guarantee that any two equal Mod objects returned are actually the
        same, and that the buckets are sorted by real part (an and bq
        descendending, bm and ap ascending).

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import G_Function
        >>> from sympy.abc import y
        >>> from sympy import S

        >>> a, b = [1, 3, 2, S(3)/2], [1 + y, y, 2, y + 3]
        >>> G_Function(a, b, [2], [y]).compute_buckets()
        ({0: [3, 2, 1], 1/2: [3/2]},
        {0: [2], y: [y, y + 1, y + 3]}, {0: [2]}, {y: [y]})

        """
        ...
    
    @property
    def signature(self) -> tuple[int, int, int, int]:
        ...
    


_x = ...
class Formula:
    """
    This class represents hypergeometric formulae.

    Explanation
    ===========

    Its data members are:
    - z, the argument
    - closed_form, the closed form expression
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (see _compute_basis)

    Examples
    ========

    >>> from sympy.abc import a, b, z
    >>> from sympy.simplify.hyperexpand import Formula, Hyper_Function
    >>> func = Hyper_Function((a/2, a/3 + b, (1+a)/2), (a, b, (a+b)/7))
    >>> f = Formula(func, z, None, [a, b])

    """
    def __init__(self, func, z, res, symbols, B=..., C=..., M=...) -> None:
        ...
    
    @property
    def closed_form(self):
        ...
    
    def find_instantiations(self, func) -> list[Any]:
        """
        Find substitutions of the free symbols that match ``func``.

        Return the substitution dictionaries as a list. Note that the returned
        instantiations need not actually match, or be valid!

        """
        ...
    


class FormulaCollection:
    """ A collection of formulae to use as origins. """
    def __init__(self) -> None:
        """ Doing this globally at module init time is a pain ... """
        ...
    
    def lookup_origin(self, func) -> Formula | None:
        """
        Given the suitable target ``func``, try to find an origin in our
        knowledge base.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import (FormulaCollection,
        ...     Hyper_Function)
        >>> f = FormulaCollection()
        >>> f.lookup_origin(Hyper_Function((), ())).closed_form
        exp(_z)
        >>> f.lookup_origin(Hyper_Function([1], ())).closed_form
        HyperRep_power1(-1, _z)

        >>> from sympy import S
        >>> i = Hyper_Function([S('1/4'), S('3/4 + 4')], [S.Half])
        >>> f.lookup_origin(i).closed_form
        HyperRep_sqrts1(-1/4, _z)
        """
        ...
    


class MeijerFormula:
    """
    This class represents a Meijer G-function formula.

    Its data members are:
    - z, the argument
    - symbols, the free symbols (parameters) in the formula
    - func, the function
    - B, C, M (c/f ordinary Formula)
    """
    def __init__(self, an, ap, bm, bq, z, symbols, B, C, M, matcher) -> None:
        ...
    
    @property
    def closed_form(self):
        ...
    
    def try_instantiate(self, func) -> MeijerFormula | None:
        """
        Try to instantiate the current formula to (almost) match func.
        This uses the _matcher passed on init.
        """
        ...
    


class MeijerFormulaCollection:
    """
    This class holds a collection of meijer g formulae.
    """
    def __init__(self) -> None:
        ...
    
    def lookup_origin(self, func) -> None:
        """ Try to find a formula that matches func. """
        ...
    


class Operator:
    """
    Base class for operators to be applied to our functions.

    Explanation
    ===========

    These operators are differential operators. They are by convention
    expressed in the variable D = z*d/dz (although this base class does
    not actually care).
    Note that when the operator is applied to an object, we typically do
    *not* blindly differentiate but instead use a different representation
    of the z*d/dz operator (see make_derivative_operator).

    To subclass from this, define a __init__ method that initializes a
    self._poly variable. This variable stores a polynomial. By convention
    the generator is z*d/dz, and acts to the right of all coefficients.

    Thus this poly
        x**2 + 2*z*x + 1
    represents the differential operator
        (z*d/dz)**2 + 2*z**2*d/dz.

    This class is used only in the implementation of the hypergeometric
    function expansion algorithm.
    """
    def apply(self, obj, op):
        """
        Apply ``self`` to the object ``obj``, where the generator is ``op``.

        Examples
        ========

        >>> from sympy.simplify.hyperexpand import Operator
        >>> from sympy.polys.polytools import Poly
        >>> from sympy.abc import x, y, z
        >>> op = Operator()
        >>> op._poly = Poly(x**2 + z*x + y, x)
        >>> op.apply(z**7, lambda f: f.diff(z))
        y*z**7 + 7*z**7 + 42*z**5
        """
        ...
    


class MultOperator(Operator):
    """ Simply multiply by a "constant" """
    def __init__(self, p) -> None:
        ...
    


class ShiftA(Operator):
    """ Increment an upper index. """
    def __init__(self, ai) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ShiftB(Operator):
    """ Decrement a lower index. """
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class UnShiftA(Operator):
    """ Decrement an upper index. """
    def __init__(self, ap, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class UnShiftB(Operator):
    """ Increment a lower index. """
    def __init__(self, ap, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftA(Operator):
    """ Increment an upper b index. """
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftB(Operator):
    """ Decrement an upper a index. """
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftC(Operator):
    """ Increment a lower b index. """
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerShiftD(Operator):
    """ Decrement a lower a index. """
    def __init__(self, bi) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftA(Operator):
    """ Decrement an upper b index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftB(Operator):
    """ Increment an upper a index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftC(Operator):
    """ Decrement a lower b index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class MeijerUnShiftD(Operator):
    """ Increment a lower a index. """
    def __init__(self, an, ap, bm, bq, i, z) -> None:
        """ Note: i counts from zero! """
        ...
    
    def __str__(self) -> str:
        ...
    


class ReduceOrder(Operator):
    """ Reduce Order by cancelling an upper and a lower index. """
    def __new__(cls, ai, bj) -> Self | None:
        """ For convenience if reduction is not possible, return None. """
        ...
    
    @classmethod
    def meijer_minus(cls, b, a) -> Self | None:
        ...
    
    @classmethod
    def meijer_plus(cls, a, b) -> Self | None:
        ...
    
    def __str__(self) -> str:
        ...
    


def reduce_order(func) -> tuple[Hyper_Function, list[Any]]:
    """
    Given the hypergeometric function ``func``, find a sequence of operators to
    reduces order as much as possible.

    Explanation
    ===========

    Return (newfunc, [operators]), where applying the operators to the
    hypergeometric function newfunc yields func.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import reduce_order, Hyper_Function
    >>> reduce_order(Hyper_Function((1, 2), (3, 4)))
    (Hyper_Function((1, 2), (3, 4)), [])
    >>> reduce_order(Hyper_Function((1,), (1,)))
    (Hyper_Function((), ()), [<Reduce order by cancelling upper 1 with lower 1.>])
    >>> reduce_order(Hyper_Function((2, 4), (3, 3)))
    (Hyper_Function((2,), (3,)), [<Reduce order by cancelling
    upper 4 with lower 3.>])
    """
    ...

def reduce_order_meijer(func) -> tuple[G_Function, list[Any]]:
    """
    Given the Meijer G function parameters, ``func``, find a sequence of
    operators that reduces order as much as possible.

    Return newfunc, [operators].

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import (reduce_order_meijer,
    ...                                         G_Function)
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 2]))[0]
    G_Function((4, 3), (5, 6), (3, 4), (2, 1))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [3, 4], [1, 8]))[0]
    G_Function((3,), (5, 6), (3, 4), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [1, 5]))[0]
    G_Function((3,), (), (), (1,))
    >>> reduce_order_meijer(G_Function([3, 4], [5, 6], [7, 5], [5, 3]))[0]
    G_Function((), (), (), ())
    """
    ...

def make_derivative_operator(M, z) -> Callable[..., Any]:
    """ Create a derivative operator, to be passed to Operator.apply. """
    ...

def apply_operators(obj, ops, op):
    """
    Apply the list of operators ``ops`` to object ``obj``, substituting
    ``op`` for the generator.
    """
    ...

def devise_plan(target, origin, z) -> list[Any]:
    """
    Devise a plan (consisting of shift and un-shift operators) to be applied
    to the hypergeometric function ``target`` to yield ``origin``.
    Returns a list of operators.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import devise_plan, Hyper_Function
    >>> from sympy.abc import z

    Nothing to do:

    >>> devise_plan(Hyper_Function((1, 2), ()), Hyper_Function((1, 2), ()), z)
    []
    >>> devise_plan(Hyper_Function((), (1, 2)), Hyper_Function((), (1, 2)), z)
    []

    Very simple plans:

    >>> devise_plan(Hyper_Function((2,), ()), Hyper_Function((1,), ()), z)
    [<Increment upper 1.>]
    >>> devise_plan(Hyper_Function((), (2,)), Hyper_Function((), (1,)), z)
    [<Increment lower index #0 of [], [1].>]

    Several buckets:

    >>> from sympy import S
    >>> devise_plan(Hyper_Function((1, S.Half), ()),
    ...             Hyper_Function((2, S('3/2')), ()), z) #doctest: +NORMALIZE_WHITESPACE
    [<Decrement upper index #0 of [3/2, 1], [].>,
    <Decrement upper index #0 of [2, 3/2], [].>]

    A slightly more complicated plan:

    >>> devise_plan(Hyper_Function((1, 3), ()), Hyper_Function((2, 2), ()), z)
    [<Increment upper 2.>, <Decrement upper index #0 of [2, 2], [].>]

    Another more complicated plan: (note that the ap have to be shifted first!)

    >>> devise_plan(Hyper_Function((1, -1), (2,)), Hyper_Function((3, -2), (4,)), z)
    [<Decrement lower 3.>, <Decrement lower 4.>,
    <Decrement upper index #1 of [-1, 2], [4].>,
    <Decrement upper index #1 of [-1, 3], [4].>, <Increment upper -2.>]
    """
    ...

def try_shifted_sum(func, z) -> tuple[Hyper_Function, list[Any], Any | int] | None:
    """ Try to recognise a hypergeometric sum that starts from k > 0. """
    ...

def try_polynomial(func, z) -> None:
    """ Recognise polynomial cases. Returns None if not such a case.
        Requires order to be fully reduced. """
    ...

def try_lerchphi(func) -> Formula | None:
    """
    Try to find an expression for Hyper_Function ``func`` in terms of Lerch
    Transcendents.

    Return None if no such expression can be found.
    """
    ...

def build_hypergeometric_formula(func) -> Formula:
    """
    Create a formula object representing the hypergeometric function ``func``.

    """
    ...

def hyperexpand_special(ap, bq, z) -> type[UndefinedFunction]:
    """
    Try to find a closed-form expression for hyper(ap, bq, z), where ``z``
    is supposed to be a "special" value, e.g. 1.

    This function tries various of the classical summation formulae
    (Gauss, Saalschuetz, etc).
    """
    ...

_collection = ...
def devise_plan_meijer(fro, to, z) -> list[Any]:
    """
    Find operators to convert G-function ``fro`` into G-function ``to``.

    Explanation
    ===========

    It is assumed that ``fro`` and ``to`` have the same signatures, and that in fact
    any corresponding pair of parameters differs by integers, and a direct path
    is possible. I.e. if there are parameters a1 b1 c1  and a2 b2 c2 it is
    assumed that a1 can be shifted to a2, etc. The only thing this routine
    determines is the order of shifts to apply, nothing clever will be tried.
    It is also assumed that ``fro`` is suitable.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import (devise_plan_meijer,
    ...                                         G_Function)
    >>> from sympy.abc import z

    Empty plan:

    >>> devise_plan_meijer(G_Function([1], [2], [3], [4]),
    ...                    G_Function([1], [2], [3], [4]), z)
    []

    Very simple plans:

    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([1], [], [], []), z)
    [<Increment upper a index #0 of [0], [], [], [].>]
    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([-1], [], [], []), z)
    [<Decrement upper a=0.>]
    >>> devise_plan_meijer(G_Function([], [1], [], []),
    ...                    G_Function([], [2], [], []), z)
    [<Increment lower a index #0 of [], [1], [], [].>]

    Slightly more complicated plans:

    >>> devise_plan_meijer(G_Function([0], [], [], []),
    ...                    G_Function([2], [], [], []), z)
    [<Increment upper a index #0 of [1], [], [], [].>,
    <Increment upper a index #0 of [0], [], [], [].>]
    >>> devise_plan_meijer(G_Function([0], [], [0], []),
    ...                    G_Function([-1], [], [1], []), z)
    [<Increment upper b=0.>, <Decrement upper a=0.>]

    Order matters:

    >>> devise_plan_meijer(G_Function([0], [], [0], []),
    ...                    G_Function([1], [], [1], []), z)
    [<Increment upper a index #0 of [0], [], [1], [].>, <Increment upper b=0.>]
    """
    ...

_meijercollection = ...
def hyperexpand(f, allow_hyper=..., rewrite=..., place=...):
    """
    Expand hypergeometric functions. If allow_hyper is True, allow partial
    simplification (that is a result different from input,
    but still containing hypergeometric functions).

    If a G-function has expansions both at zero and at infinity,
    ``place`` can be set to ``0`` or ``zoo`` to indicate the
    preferred choice.

    Examples
    ========

    >>> from sympy.simplify.hyperexpand import hyperexpand
    >>> from sympy.functions import hyper
    >>> from sympy.abc import z
    >>> hyperexpand(hyper([], [], z))
    exp(z)

    Non-hyperegeometric parts of the expression and hypergeometric expressions
    that are not recognised are left unchanged:

    >>> hyperexpand(1 + hyper([1, 1, 1], [], z))
    hyper((1, 1, 1), (), z) + 1
    """
    ...

