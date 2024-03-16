from sympy.core.facts import FactKB

"""
This module contains the machinery handling assumptions.
Do also consider the guide :ref:`assumptions-guide`.

All symbolic objects have assumption attributes that can be accessed via
``.is_<assumption name>`` attribute.

Assumptions determine certain properties of symbolic objects and can
have 3 possible values: ``True``, ``False``, ``None``.  ``True`` is returned if the
object has the property and ``False`` is returned if it does not or cannot
(i.e. does not make sense):

    >>> from sympy import I
    >>> I.is_algebraic
    True
    >>> I.is_real
    False
    >>> I.is_prime
    False

When the property cannot be determined (or when a method is not
implemented) ``None`` will be returned. For example,  a generic symbol, ``x``,
may or may not be positive so a value of ``None`` is returned for ``x.is_positive``.

By default, all symbolic values are in the largest set in the given context
without specifying the property. For example, a symbol that has a property
being integer, is also real, complex, etc.

Here follows a list of possible assumption names:

.. glossary::

    commutative
        object commutes with any other object with
        respect to multiplication operation. See [12]_.

    complex
        object can have only values from the set
        of complex numbers. See [13]_.

    imaginary
        object value is a number that can be written as a real
        number multiplied by the imaginary unit ``I``.  See
        [3]_.  Please note that ``0`` is not considered to be an
        imaginary number, see
        `issue #7649 <https://github.com/sympy/sympy/issues/7649>`_.

    real
        object can have only values from the set
        of real numbers.

    extended_real
        object can have only values from the set
        of real numbers, ``oo`` and ``-oo``.

    integer
        object can have only values from the set
        of integers.

    odd
    even
        object can have only values from the set of
        odd (even) integers [2]_.

    prime
        object is a natural number greater than 1 that has
        no positive divisors other than 1 and itself.  See [6]_.

    composite
        object is a positive integer that has at least one positive
        divisor other than 1 or the number itself.  See [4]_.

    zero
        object has the value of 0.

    nonzero
        object is a real number that is not zero.

    rational
        object can have only values from the set
        of rationals.

    algebraic
        object can have only values from the set
        of algebraic numbers [11]_.

    transcendental
        object can have only values from the set
        of transcendental numbers [10]_.

    irrational
        object value cannot be represented exactly by :class:`~.Rational`, see [5]_.

    finite
    infinite
        object absolute value is bounded (arbitrarily large).
        See [7]_, [8]_, [9]_.

    negative
    nonnegative
        object can have only negative (nonnegative)
        values [1]_.

    positive
    nonpositive
        object can have only positive (nonpositive) values.

    extended_negative
    extended_nonnegative
    extended_positive
    extended_nonpositive
    extended_nonzero
        as without the extended part, but also including infinity with
        corresponding sign, e.g., extended_positive includes ``oo``

    hermitian
    antihermitian
        object belongs to the field of Hermitian
        (antihermitian) operators.

Examples
========

    >>> from sympy import Symbol
    >>> x = Symbol('x', real=True); x
    x
    >>> x.is_real
    True
    >>> x.is_complex
    True

See Also
========

.. seealso::

    :py:class:`sympy.core.numbers.ImaginaryUnit`
    :py:class:`sympy.core.numbers.Zero`
    :py:class:`sympy.core.numbers.One`
    :py:class:`sympy.core.numbers.Infinity`
    :py:class:`sympy.core.numbers.NegativeInfinity`
    :py:class:`sympy.core.numbers.ComplexInfinity`

Notes
=====

The fully-resolved assumptions for any SymPy expression
can be obtained as follows:

    >>> from sympy.core.assumptions import assumptions
    >>> x = Symbol('x',positive=True)
    >>> assumptions(x + I)
    {'commutative': True, 'complex': True, 'composite': False, 'even':
    False, 'extended_negative': False, 'extended_nonnegative': False,
    'extended_nonpositive': False, 'extended_nonzero': False,
    'extended_positive': False, 'extended_real': False, 'finite': True,
    'imaginary': False, 'infinite': False, 'integer': False, 'irrational':
    False, 'negative': False, 'noninteger': False, 'nonnegative': False,
    'nonpositive': False, 'nonzero': False, 'odd': False, 'positive':
    False, 'prime': False, 'rational': False, 'real': False, 'zero':
    False}

Developers Notes
================

The current (and possibly incomplete) values are stored
in the ``obj._assumptions dictionary``; queries to getter methods
(with property decorators) or attributes of objects/classes
will return values and update the dictionary.

    >>> eq = x**2 + I
    >>> eq._assumptions
    {}
    >>> eq.is_finite
    True
    >>> eq._assumptions
    {'finite': True, 'infinite': False}

For a :class:`~.Symbol`, there are two locations for assumptions that may
be of interest. The ``assumptions0`` attribute gives the full set of
assumptions derived from a given set of initial assumptions. The
latter assumptions are stored as ``Symbol._assumptions_orig``

    >>> Symbol('x', prime=True, even=True)._assumptions_orig
    {'even': True, 'prime': True}

The ``_assumptions_orig`` are not necessarily canonical nor are they filtered
in any way: they records the assumptions used to instantiate a Symbol and (for
storage purposes) represent a more compact representation of the assumptions
needed to recreate the full set in ``Symbol.assumptions0``.


References
==========

.. [1] https://en.wikipedia.org/wiki/Negative_number
.. [2] https://en.wikipedia.org/wiki/Parity_%28mathematics%29
.. [3] https://en.wikipedia.org/wiki/Imaginary_number
.. [4] https://en.wikipedia.org/wiki/Composite_number
.. [5] https://en.wikipedia.org/wiki/Irrational_number
.. [6] https://en.wikipedia.org/wiki/Prime_number
.. [7] https://en.wikipedia.org/wiki/Finite
.. [8] https://docs.python.org/3/library/math.html#math.isfinite
.. [9] https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html
.. [10] https://en.wikipedia.org/wiki/Transcendental_number
.. [11] https://en.wikipedia.org/wiki/Algebraic_number
.. [12] https://en.wikipedia.org/wiki/Commutative_property
.. [13] https://en.wikipedia.org/wiki/Complex_number

"""
_assume_rules = ...
_assume_defined = ...
_assume_defined = ...
def assumptions(expr, _check=...) -> dict[Any, Any]:
    """return the T/F assumptions of ``expr``"""
    ...

def common_assumptions(exprs, check=...) -> dict[Any, Any]:
    """return those assumptions which have the same True or False
    value for all the given expressions.

    Examples
    ========

    >>> from sympy.core import common_assumptions
    >>> from sympy import oo, pi, sqrt
    >>> common_assumptions([-4, 0, sqrt(2), 2, pi, oo])
    {'commutative': True, 'composite': False,
    'extended_real': True, 'imaginary': False, 'odd': False}

    By default, all assumptions are tested; pass an iterable of the
    assumptions to limit those that are reported:

    >>> common_assumptions([0, 1, 2], ['positive', 'integer'])
    {'integer': True}
    """
    ...

def failing_assumptions(expr, **assumptions) -> dict[Any, Any]:
    """
    Return a dictionary containing assumptions with values not
    matching those of the passed assumptions.

    Examples
    ========

    >>> from sympy import failing_assumptions, Symbol

    >>> x = Symbol('x', positive=True)
    >>> y = Symbol('y')
    >>> failing_assumptions(6*x + y, positive=True)
    {'positive': None}

    >>> failing_assumptions(x**2 - 1, positive=True)
    {'positive': None}

    If *expr* satisfies all of the assumptions, an empty dictionary is returned.

    >>> failing_assumptions(x**2, positive=True)
    {}

    """
    ...

def check_assumptions(expr, against=..., **assume) -> bool | None:
    """
    Checks whether assumptions of ``expr`` match the T/F assumptions
    given (or possessed by ``against``). True is returned if all
    assumptions match; False is returned if there is a mismatch and
    the assumption in ``expr`` is not None; else None is returned.

    Explanation
    ===========

    *assume* is a dict of assumptions with True or False values

    Examples
    ========

    >>> from sympy import Symbol, pi, I, exp, check_assumptions
    >>> check_assumptions(-5, integer=True)
    True
    >>> check_assumptions(pi, real=True, integer=False)
    True
    >>> check_assumptions(pi, negative=True)
    False
    >>> check_assumptions(exp(I*pi/7), real=False)
    True
    >>> x = Symbol('x', positive=True)
    >>> check_assumptions(2*x + 1, positive=True)
    True
    >>> check_assumptions(-2*x - 5, positive=True)
    False

    To check assumptions of *expr* against another variable or expression,
    pass the expression or variable as ``against``.

    >>> check_assumptions(2*x + 1, x)
    True

    To see if a number matches the assumptions of an expression, pass
    the number as the first argument, else its specific assumptions
    may not have a non-None value in the expression:

    >>> check_assumptions(x, 3)
    >>> check_assumptions(3, x)
    True

    ``None`` is returned if ``check_assumptions()`` could not conclude.

    >>> check_assumptions(2*x - 1, x)

    >>> z = Symbol('z')
    >>> check_assumptions(z, real=True)

    See Also
    ========

    failing_assumptions

    """
    ...

class StdFactKB(FactKB):
    """A FactKB specialized for the built-in rules

    This is the only kind of FactKB that Basic objects should use.
    """
    def __init__(self, facts=...) -> None:
        ...
    
    def copy(self) -> Self:
        ...
    
    @property
    def generator(self) -> dict[Any, Any]:
        ...
    


def as_property(fact):
    """Convert a fact name to the name of the corresponding property"""
    ...

def make_property(fact) -> property:
    """Create the automagic property corresponding to a fact."""
    ...

class ManagedProperties(type):
    def __init__(cls, *args, **kwargs) -> None:
        ...
    


