from typing import Any, Literal, Self, Tuple as tTuple
from sympy.core.kind import _UndefinedKind
from sympy.core.mul import Mul
from sympy.core.numbers import Integer, Rational
from sympy.core.operations import AssocOp
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.series.order import Order

class Add(Expr, AssocOp):
    """
    Expression representing addition operation for algebraic group.

    .. deprecated:: 1.7

       Using arguments that aren't subclasses of :class:`~.Expr` in core
       operators (:class:`~.Mul`, :class:`~.Add`, and :class:`~.Pow`) is
       deprecated. See :ref:`non-expr-args-deprecated` for details.

    Every argument of ``Add()`` must be ``Expr``. Infix operator ``+``
    on most scalar objects in SymPy calls this class.

    Another use of ``Add()`` is to represent the structure of abstract
    addition so that its arguments can be substituted to return different
    class. Refer to examples section for this.

    ``Add()`` evaluates the argument unless ``evaluate=False`` is passed.
    The evaluation logic includes:

    1. Flattening
        ``Add(x, Add(y, z))`` -> ``Add(x, y, z)``

    2. Identity removing
        ``Add(x, 0, y)`` -> ``Add(x, y)``

    3. Coefficient collecting by ``.as_coeff_Mul()``
        ``Add(x, 2*x)`` -> ``Mul(3, x)``

    4. Term sorting
        ``Add(y, x, 2)`` -> ``Add(2, x, y)``

    If no argument is passed, identity element 0 is returned. If single
    element is passed, that element is returned.

    Note that ``Add(*args)`` is more efficient than ``sum(args)`` because
    it flattens the arguments. ``sum(a, b, c, ...)`` recursively adds the
    arguments as ``a + (b + (c + ...))``, which has quadratic complexity.
    On the other hand, ``Add(a, b, c, d)`` does not assume nested
    structure, making the complexity linear.

    Since addition is group operation, every argument should have the
    same :obj:`sympy.core.kind.Kind()`.

    Examples
    ========

    >>> from sympy import Add, I
    >>> from sympy.abc import x, y
    >>> Add(x, 1)
    x + 1
    >>> Add(x, x)
    2*x
    >>> 2*x**2 + 3*x + I*y + 2*y + 2*x/5 + 1.0*y + 1
    2*x**2 + 17*x/5 + 3.0*y + I*y + 1

    If ``evaluate=False`` is passed, result is not evaluated.

    >>> Add(1, 2, evaluate=False)
    1 + 2
    >>> Add(x, x, evaluate=False)
    x + x

    ``Add()`` also represents the general structure of addition operation.

    >>> from sympy import MatrixSymbol
    >>> A,B = MatrixSymbol('A', 2,2), MatrixSymbol('B', 2,2)
    >>> expr = Add(x,y).subs({x:A, y:B})
    >>> expr
    A + B
    >>> type(expr)
    <class 'sympy.matrices.expressions.matadd.MatAdd'>

    Note that the printers do not display in args order.

    >>> Add(x, 1)
    x + 1
    >>> Add(x, 1).args
    (1, x)

    See Also
    ========

    MatAdd

    """
    __slots__ = ...
    args: tTuple[Expr, ...]
    is_Add = ...
    _args_type = Expr
    @classmethod
    def flatten(cls, seq):
        """
        Takes the sequence "seq" of nested Adds and returns a flatten list.

        Returns: (commutative_part, noncommutative_part, order_symbols)

        Applies associativity, all terms are commutable with respect to
        addition.

        NB: the removal of 0 is already handled by AssocOp.__new__

        See Also
        ========

        sympy.core.mul.Mul.flatten

        """
        ...
    
    @classmethod
    def class_key(cls) -> tuple[Literal[3], Literal[1], str]:
        ...
    
    @property
    def kind(self) -> _UndefinedKind | Any:
        ...
    
    def could_extract_minus_sign(self) -> bool:
        ...
    
    @cacheit
    def as_coeff_add(self, *deps) -> tuple[Any | Self, tuple[Any, ...]] | tuple[Expr, tuple[Expr, ...]] | tuple[Any, tTuple[Expr, ...]]:
        """
        Returns a tuple (coeff, args) where self is treated as an Add and coeff
        is the Number term and args is a tuple of all other terms.

        Examples
        ========

        >>> from sympy.abc import x
        >>> (7 + 3*x).as_coeff_add()
        (7, (3*x,))
        >>> (7*x).as_coeff_add()
        (0, (7*x,))
        """
        ...
    
    def as_coeff_Add(self, rational=..., deps=...) -> tuple[Expr, Any | Self] | tuple[Any, Self]:
        """
        Efficiently extract the coefficient of a summation.
        """
        ...
    
    def matches(self, expr, repl_dict=..., old=...):
        ...
    
    @cacheit
    def as_two_terms(self) -> tuple[Expr, Any | Self]:
        """Return head and tail of self.

        This is the most efficient way to get the head and tail of an
        expression.

        - if you want only the head, use self.args[0];
        - if you want to process the arguments of the tail then use
          self.as_coef_add() which gives the head and a tuple containing
          the arguments of the tail when treated as an Add.
        - if you want the coefficient when self is treated as a Mul
          then use self.as_coeff_mul()[0]

        >>> from sympy.abc import x, y
        >>> (3*x - 2*y + 5).as_two_terms()
        (5, 3*x - 2*y)
        """
        ...
    
    def as_numer_denom(self) -> tuple[Order, Any] | tuple[Self, Any | Add | Order | Mul] | tuple[Any | Add | Order | Mul, Any | Add | Order | Mul]:
        """
        Decomposes an expression to its numerator part and its
        denominator part.

        Examples
        ========

        >>> from sympy.abc import x, y, z
        >>> (x*y/z).as_numer_denom()
        (x*y, z)
        >>> (x*(y + 1)/y**7).as_numer_denom()
        (x*(y + 1), y**7)

        See Also
        ========

        sympy.core.expr.Expr.as_numer_denom
        """
        ...
    
    _eval_is_real = ...
    _eval_is_extended_real = ...
    _eval_is_complex = ...
    _eval_is_antihermitian = ...
    _eval_is_finite = ...
    _eval_is_hermitian = ...
    _eval_is_integer = ...
    _eval_is_rational = ...
    _eval_is_algebraic = ...
    _eval_is_commutative = ...
    def removeO(self) -> Self:
        ...
    
    def getO(self) -> Self | None:
        ...
    
    @cacheit
    def extract_leading_order(self, symbols, point=...) -> tuple[tuple[Expr, Order], ...]:
        """
        Returns the leading term and its order.

        Examples
        ========

        >>> from sympy.abc import x
        >>> (x + 1 + 1/x**5).extract_leading_order(x)
        ((x**(-5), O(x**(-5))),)
        >>> (1 + x).extract_leading_order(x)
        ((1, O(1)),)
        >>> (x + x**2).extract_leading_order(x)
        ((x, O(x)),)

        """
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Self]:
        """
        Return a tuple representing a complex number.

        Examples
        ========

        >>> from sympy import I
        >>> (7 + 9*I).as_real_imag()
        (7, 9)
        >>> ((1 + I)/(1 - I)).as_real_imag()
        (0, 1)
        >>> ((1 + 2*I)*(1 + 3*I)).as_real_imag()
        (-5, 5)
        """
        ...
    
    def primitive(self) -> tuple[Any, Self] | tuple[Rational | Any | Integer, Any | Self]:
        """
        Return ``(R, self/R)`` where ``R``` is the Rational GCD of ``self```.

        ``R`` is collected only from the leading coefficient of each term.

        Examples
        ========

        >>> from sympy.abc import x, y

        >>> (2*x + 4*y).primitive()
        (2, x + 2*y)

        >>> (2*x/3 + 4*y/9).primitive()
        (2/9, 3*x + 2*y)

        >>> (2*x/3 + 4.2*y).primitive()
        (1/3, 2*x + 12.6*y)

        No subprocessing of term factors is performed:

        >>> ((2 + 2*x)*x + 2).primitive()
        (1, x*(2*x + 2) + 2)

        Recursive processing can be done with the ``as_content_primitive()``
        method:

        >>> ((2 + 2*x)*x + 2).as_content_primitive()
        (2, x*(x + 1) + 1)

        See also: primitive() function in polytools.py

        """
        ...
    
    def as_content_primitive(self, radical=..., clear=...) -> tuple[Any | Integer | Rational, Any | Rational | Integer | Self]:
        """Return the tuple (R, self/R) where R is the positive Rational
        extracted from self. If radical is True (default is False) then
        common radicals will be removed and included as a factor of the
        primitive expression.

        Examples
        ========

        >>> from sympy import sqrt
        >>> (3 + 3*sqrt(2)).as_content_primitive()
        (3, 1 + sqrt(2))

        Radical content can also be factored out of the primitive:

        >>> (2*sqrt(2) + 4*sqrt(10)).as_content_primitive(radical=True)
        (2, sqrt(2)*(1 + 2*sqrt(5)))

        See docstring of Expr.as_content_primitive for more examples.
        """
        ...
    
    def __neg__(self) -> Mul | Order:
        ...
    


add = ...
