from typing import Any, Generator, Iterator, NoReturn, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.decorators import call_highest_priority
from sympy.core.relational import Eq, Ne, Relational
from sympy.core.singleton import Singleton
from sympy.series.order import Order
from sympy.sets.sets import Complement, FiniteSet, Intersection, Interval, Union

class SeqBase(Basic):
    """Base class for sequences"""
    is_commutative = ...
    _op_priority = ...
    @property
    def gen(self):
        """Returns the generator for the sequence"""
        ...
    
    @property
    def interval(self):
        """The interval on which the sequence is defined"""
        ...
    
    @property
    def start(self):
        """The starting point of the sequence. This point is included"""
        ...
    
    @property
    def stop(self):
        """The ending point of the sequence. This point is included"""
        ...
    
    @property
    def length(self):
        """Length of the sequence"""
        ...
    
    @property
    def variables(self) -> tuple[()]:
        """Returns a tuple of variables that are bounded"""
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        """
        This method returns the symbols in the object, excluding those
        that take on a specific value (i.e. the dummy symbols).

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n, m
        >>> SeqFormula(m*n**2, (n, 0, 5)).free_symbols
        {m}
        """
        ...
    
    @cacheit
    def coeff(self, pt):
        """Returns the coefficient at point pt"""
        ...
    
    def coeff_mul(self, other) -> Order:
        """
        Should be used when ``other`` is not a sequence. Should be
        defined to define custom behaviour.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2).coeff_mul(2)
        SeqFormula(2*n**2, (n, 0, oo))

        Notes
        =====

        '*' defines multiplication of sequences with sequences only.
        """
        ...
    
    def __add__(self, other) -> SeqAdd:
        """Returns the term-wise addition of 'self' and 'other'.

        ``other`` should be a sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) + SeqFormula(n**3)
        SeqFormula(n**3 + n**2, (n, 0, oo))
        """
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    def __sub__(self, other) -> SeqAdd:
        """Returns the term-wise subtraction of ``self`` and ``other``.

        ``other`` should be a sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) - (SeqFormula(n))
        SeqFormula(n**2 - n, (n, 0, oo))
        """
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    def __neg__(self) -> Order:
        """Negates the sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> -SeqFormula(n**2)
        SeqFormula(-n**2, (n, 0, oo))
        """
        ...
    
    def __mul__(self, other) -> SeqMul:
        """Returns the term-wise multiplication of 'self' and 'other'.

        ``other`` should be a sequence. For ``other`` not being a
        sequence see :func:`coeff_mul` method.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) * (SeqFormula(n))
        SeqFormula(n**3, (n, 0, oo))
        """
        ...
    
    @call_highest_priority('__mul__')
    def __rmul__(self, other):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __getitem__(self, index) -> list[Any] | None:
        ...
    
    def find_linear_recurrence(self, n, d=..., gfvar=...) -> list[Any] | tuple[list[Any], None] | tuple[Any | list[Any], Any]:
        r"""
        Finds the shortest linear recurrence that satisfies the first n
        terms of sequence of order `\leq` ``n/2`` if possible.
        If ``d`` is specified, find shortest linear recurrence of order
        `\leq` min(d, n/2) if possible.
        Returns list of coefficients ``[b(1), b(2), ...]`` corresponding to the
        recurrence relation ``x(n) = b(1)*x(n-1) + b(2)*x(n-2) + ...``
        Returns ``[]`` if no recurrence is found.
        If gfvar is specified, also returns ordinary generating function as a
        function of gfvar.

        Examples
        ========

        >>> from sympy import sequence, sqrt, oo, lucas
        >>> from sympy.abc import n, x, y
        >>> sequence(n**2).find_linear_recurrence(10, 2)
        []
        >>> sequence(n**2).find_linear_recurrence(10)
        [3, -3, 1]
        >>> sequence(2**n).find_linear_recurrence(10)
        [2]
        >>> sequence(23*n**4+91*n**2).find_linear_recurrence(10)
        [5, -10, 10, -5, 1]
        >>> sequence(sqrt(5)*(((1 + sqrt(5))/2)**n - (-(1 + sqrt(5))/2)**(-n))/5).find_linear_recurrence(10)
        [1, 1]
        >>> sequence(x+y*(-2)**(-n), (n, 0, oo)).find_linear_recurrence(30)
        [1/2, 1/2]
        >>> sequence(3*5**n + 12).find_linear_recurrence(20,gfvar=x)
        ([6, -5], 3*(5 - 21*x)/((x - 1)*(5*x - 1)))
        >>> sequence(lucas(n)).find_linear_recurrence(15,gfvar=x)
        ([1, 1], (x - 2)/(x**2 + x - 1))
        """
        ...
    


class EmptySequence(SeqBase, metaclass=Singleton):
    """Represents an empty sequence.

    The empty sequence is also available as a singleton as
    ``S.EmptySequence``.

    Examples
    ========

    >>> from sympy import EmptySequence, SeqPer
    >>> from sympy.abc import x
    >>> EmptySequence
    EmptySequence
    >>> SeqPer((1, 2), (x, 0, 10)) + EmptySequence
    SeqPer((1, 2), (x, 0, 10))
    >>> SeqPer((1, 2)) * EmptySequence
    EmptySequence
    >>> EmptySequence.coeff_mul(-1)
    EmptySequence
    """
    @property
    def interval(self):
        ...
    
    @property
    def length(self):
        ...
    
    def coeff_mul(self, coeff) -> Self:
        """See docstring of SeqBase.coeff_mul"""
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    


class SeqExpr(SeqBase):
    """Sequence expression class.

    Various sequences should inherit from this class.

    Examples
    ========

    >>> from sympy.series.sequences import SeqExpr
    >>> from sympy.abc import x
    >>> from sympy import Tuple
    >>> s = SeqExpr(Tuple(1, 2, 3), Tuple(x, 0, 10))
    >>> s.gen
    (1, 2, 3)
    >>> s.interval
    Interval(0, 10)
    >>> s.length
    11

    See Also
    ========

    sympy.series.sequences.SeqPer
    sympy.series.sequences.SeqFormula
    """
    @property
    def gen(self) -> Basic:
        ...
    
    @property
    def interval(self) -> FiniteSet | Interval:
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def variables(self) -> tuple[Any]:
        ...
    


class SeqPer(SeqExpr):
    """
    Represents a periodic sequence.

    The elements are repeated after a given period.

    Examples
    ========

    >>> from sympy import SeqPer, oo
    >>> from sympy.abc import k

    >>> s = SeqPer((1, 2, 3), (0, 5))
    >>> s.periodical
    (1, 2, 3)
    >>> s.period
    3

    For value at a particular point

    >>> s.coeff(3)
    1

    supports slicing

    >>> s[:]
    [1, 2, 3, 1, 2, 3]

    iterable

    >>> list(s)
    [1, 2, 3, 1, 2, 3]

    sequence starts from negative infinity

    >>> SeqPer((1, 2, 3), (-oo, 0))[0:6]
    [1, 2, 3, 1, 2, 3]

    Periodic formulas

    >>> SeqPer((k, k**2, k**3), (k, 0, oo))[0:6]
    [0, 1, 8, 3, 16, 125]

    See Also
    ========

    sympy.series.sequences.SeqFormula
    """
    def __new__(cls, periodical, limits=...) -> Self:
        ...
    
    @property
    def period(self) -> int:
        ...
    
    @property
    def periodical(self) -> Basic:
        ...
    
    def coeff_mul(self, coeff) -> SeqPer:
        """See docstring of SeqBase.coeff_mul"""
        ...
    


class SeqFormula(SeqExpr):
    """
    Represents sequence based on a formula.

    Elements are generated using a formula.

    Examples
    ========

    >>> from sympy import SeqFormula, oo, Symbol
    >>> n = Symbol('n')
    >>> s = SeqFormula(n**2, (n, 0, 5))
    >>> s.formula
    n**2

    For value at a particular point

    >>> s.coeff(3)
    9

    supports slicing

    >>> s[:]
    [0, 1, 4, 9, 16, 25]

    iterable

    >>> list(s)
    [0, 1, 4, 9, 16, 25]

    sequence starts from negative infinity

    >>> SeqFormula(n**2, (-oo, 0))[0:6]
    [0, 1, 4, 9, 16, 25]

    See Also
    ========

    sympy.series.sequences.SeqPer
    """
    def __new__(cls, formula, limits=...) -> Self:
        ...
    
    @property
    def formula(self) -> Basic:
        ...
    
    def coeff_mul(self, coeff) -> SeqFormula:
        """See docstring of SeqBase.coeff_mul"""
        ...
    
    def expand(self, *args, **kwargs) -> SeqFormula:
        ...
    


class RecursiveSeq(SeqBase):
    """
    A finite degree recursive sequence.

    Explanation
    ===========

    That is, a sequence a(n) that depends on a fixed, finite number of its
    previous values. The general form is

        a(n) = f(a(n - 1), a(n - 2), ..., a(n - d))

    for some fixed, positive integer d, where f is some function defined by a
    SymPy expression.

    Parameters
    ==========

    recurrence : SymPy expression defining recurrence
        This is *not* an equality, only the expression that the nth term is
        equal to. For example, if :code:`a(n) = f(a(n - 1), ..., a(n - d))`,
        then the expression should be :code:`f(a(n - 1), ..., a(n - d))`.

    yn : applied undefined function
        Represents the nth term of the sequence as e.g. :code:`y(n)` where
        :code:`y` is an undefined function and `n` is the sequence index.

    n : symbolic argument
        The name of the variable that the recurrence is in, e.g., :code:`n` if
        the recurrence function is :code:`y(n)`.

    initial : iterable with length equal to the degree of the recurrence
        The initial values of the recurrence.

    start : start value of sequence (inclusive)

    Examples
    ========

    >>> from sympy import Function, symbols
    >>> from sympy.series.sequences import RecursiveSeq
    >>> y = Function("y")
    >>> n = symbols("n")
    >>> fib = RecursiveSeq(y(n - 1) + y(n - 2), y(n), n, [0, 1])

    >>> fib.coeff(3) # Value at a particular point
    2

    >>> fib[:6] # supports slicing
    [0, 1, 1, 2, 3, 5]

    >>> fib.recurrence # inspect recurrence
    Eq(y(n), y(n - 2) + y(n - 1))

    >>> fib.degree # automatically determine degree
    2

    >>> for x in zip(range(10), fib) supports iteration
    ...     print(x)
    (0, 0)
    (1, 1)
    (2, 1)
    (3, 2)
    (4, 3)
    (5, 5)
    (6, 8)
    (7, 13)
    (8, 21)
    (9, 34)

    See Also
    ========

    sympy.series.sequences.SeqFormula

    """
    def __new__(cls, recurrence, yn, n, initial=..., start=...) -> Self:
        ...
    
    @property
    def recurrence(self) -> Eq | Relational | Ne:
        """Equation defining recurrence."""
        ...
    
    @property
    def yn(self) -> Basic:
        """Applied function representing the nth term"""
        ...
    
    @property
    def y(self) -> type[Basic]:
        """Undefined function for the nth term of the sequence"""
        ...
    
    @property
    def n(self) -> Basic:
        """Sequence index symbol"""
        ...
    
    @property
    def initial(self) -> Basic:
        """The initial values of the sequence"""
        ...
    
    @property
    def start(self) -> Basic:
        """The starting point of the sequence. This point is included"""
        ...
    
    @property
    def stop(self):
        """The ending point of the sequence. (oo)"""
        ...
    
    @property
    def interval(self) -> tuple[Basic, Any]:
        """Interval on which sequence is defined."""
        ...
    
    def __iter__(self) -> Generator[Any, Any, NoReturn]:
        ...
    


def sequence(seq, limits=...) -> SeqPer | SeqFormula:
    """
    Returns appropriate sequence object.

    Explanation
    ===========

    If ``seq`` is a SymPy sequence, returns :class:`SeqPer` object
    otherwise returns :class:`SeqFormula` object.

    Examples
    ========

    >>> from sympy import sequence
    >>> from sympy.abc import n
    >>> sequence(n**2, (n, 0, 5))
    SeqFormula(n**2, (n, 0, 5))
    >>> sequence((1, 2, 3), (n, 0, 5))
    SeqPer((1, 2, 3), (n, 0, 5))

    See Also
    ========

    sympy.series.sequences.SeqPer
    sympy.series.sequences.SeqFormula
    """
    ...

class SeqExprOp(SeqBase):
    """
    Base class for operations on sequences.

    Examples
    ========

    >>> from sympy.series.sequences import SeqExprOp, sequence
    >>> from sympy.abc import n
    >>> s1 = sequence(n**2, (n, 0, 10))
    >>> s2 = sequence((1, 2, 3), (n, 5, 10))
    >>> s = SeqExprOp(s1, s2)
    >>> s.gen
    (n**2, (1, 2, 3))
    >>> s.interval
    Interval(5, 10)
    >>> s.length
    6

    See Also
    ========

    sympy.series.sequences.SeqAdd
    sympy.series.sequences.SeqMul
    """
    @property
    def gen(self) -> tuple[Any, ...]:
        """Generator for the sequence.

        returns a tuple of generators of all the argument sequences.
        """
        ...
    
    @property
    def interval(self) -> FiniteSet | Intersection | Union | Complement:
        """Sequence is defined on the intersection
        of all the intervals of respective sequences
        """
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def variables(self) -> tuple[Any, ...]:
        """Cumulative of all the bound variables"""
        ...
    
    @property
    def length(self):
        ...
    


class SeqAdd(SeqExprOp):
    """Represents term-wise addition of sequences.

    Rules:
        * The interval on which sequence is defined is the intersection
          of respective intervals of sequences.
        * Anything + :class:`EmptySequence` remains unchanged.
        * Other rules are defined in ``_add`` methods of sequence classes.

    Examples
    ========

    >>> from sympy import EmptySequence, oo, SeqAdd, SeqPer, SeqFormula
    >>> from sympy.abc import n
    >>> SeqAdd(SeqPer((1, 2), (n, 0, oo)), EmptySequence)
    SeqPer((1, 2), (n, 0, oo))
    >>> SeqAdd(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 6, 10)))
    EmptySequence
    >>> SeqAdd(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2, (n, 0, oo)))
    SeqAdd(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
    >>> SeqAdd(SeqFormula(n**3), SeqFormula(n**2))
    SeqFormula(n**3 + n**2, (n, 0, oo))

    See Also
    ========

    sympy.series.sequences.SeqMul
    """
    def __new__(cls, *args, **kwargs) -> SeqAdd | Self:
        ...
    
    @staticmethod
    def reduce(args) -> SeqAdd:
        """Simplify :class:`SeqAdd` using known rules.

        Iterates through all pairs and ask the constituent
        sequences if they can simplify themselves with any other constituent.

        Notes
        =====

        adapted from ``Union.reduce``

        """
        ...
    


class SeqMul(SeqExprOp):
    r"""Represents term-wise multiplication of sequences.

    Explanation
    ===========

    Handles multiplication of sequences only. For multiplication
    with other objects see :func:`SeqBase.coeff_mul`.

    Rules:
        * The interval on which sequence is defined is the intersection
          of respective intervals of sequences.
        * Anything \* :class:`EmptySequence` returns :class:`EmptySequence`.
        * Other rules are defined in ``_mul`` methods of sequence classes.

    Examples
    ========

    >>> from sympy import EmptySequence, oo, SeqMul, SeqPer, SeqFormula
    >>> from sympy.abc import n
    >>> SeqMul(SeqPer((1, 2), (n, 0, oo)), EmptySequence)
    EmptySequence
    >>> SeqMul(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 6, 10)))
    EmptySequence
    >>> SeqMul(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2))
    SeqMul(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
    >>> SeqMul(SeqFormula(n**3), SeqFormula(n**2))
    SeqFormula(n**5, (n, 0, oo))

    See Also
    ========

    sympy.series.sequences.SeqAdd
    """
    def __new__(cls, *args, **kwargs) -> SeqMul | Self:
        ...
    
    @staticmethod
    def reduce(args) -> SeqMul:
        """Simplify a :class:`SeqMul` using known rules.

        Explanation
        ===========

        Iterates through all pairs and ask the constituent
        sequences if they can simplify themselves with any other constituent.

        Notes
        =====

        adapted from ``Union.reduce``

        """
        ...
    


