from sympy.external.gmpy import MPQ
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.utilities import public

"""Implementation of :class:`RationalField` class. """
@public
class RationalField(Field, CharacteristicZero, SimpleDomain):
    r"""Abstract base class for the domain :ref:`QQ`.

    The :py:class:`RationalField` class represents the field of rational
    numbers $\mathbb{Q}$ as a :py:class:`~.Domain` in the domain system.
    :py:class:`RationalField` is a superclass of
    :py:class:`PythonRationalField` and :py:class:`GMPYRationalField` one of
    which will be the implementation for :ref:`QQ` depending on whether either
    of ``gmpy`` or ``gmpy2`` is installed or not.

    See also
    ========

    Domain
    """
    rep = ...
    alias = ...
    is_QQ = ...
    is_Numerical = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    dtype = MPQ
    zero = dtype(0)
    one = dtype(1)
    tp = type(one)
    def __init__(self) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        """Returns ``True`` if two domains are equivalent. """
        ...
    
    def __hash__(self) -> int:
        """Returns hash code of ``self``. """
        ...
    
    def get_ring(self) -> Any:
        """Returns ring associated with ``self``. """
        ...
    
    def to_sympy(self, a) -> Rational | Integer:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> PythonMPQ:
        """Convert SymPy's Integer to ``dtype``. """
        ...
    
    def algebraic_field(self, *extension, alias=...) -> Any:
        r"""Returns an algebraic field, i.e. `\mathbb{Q}(\alpha, \ldots)`.

        Parameters
        ==========

        *extension : One or more :py:class:`~.Expr`
            Generators of the extension. These should be expressions that are
            algebraic over `\mathbb{Q}`.

        alias : str, :py:class:`~.Symbol`, None, optional (default=None)
            If provided, this will be used as the alias symbol for the
            primitive element of the returned :py:class:`~.AlgebraicField`.

        Returns
        =======

        :py:class:`~.AlgebraicField`
            A :py:class:`~.Domain` representing the algebraic field extension.

        Examples
        ========

        >>> from sympy import QQ, sqrt
        >>> QQ.algebraic_field(sqrt(2))
        QQ<sqrt(2)>
        """
        ...
    
    def from_AlgebraicField(K1, a, K0) -> None:
        """Convert a :py:class:`~.ANP` object to :ref:`QQ`.

        See :py:meth:`~.Domain.convert`
        """
        ...
    
    def from_ZZ(K1, a, K0) -> PythonMPQ:
        """Convert a Python ``int`` object to ``dtype``. """
        ...
    
    def from_ZZ_python(K1, a, K0) -> PythonMPQ:
        """Convert a Python ``int`` object to ``dtype``. """
        ...
    
    def from_QQ(K1, a, K0) -> PythonMPQ:
        """Convert a Python ``Fraction`` object to ``dtype``. """
        ...
    
    def from_QQ_python(K1, a, K0) -> PythonMPQ:
        """Convert a Python ``Fraction`` object to ``dtype``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0) -> PythonMPQ:
        """Convert a GMPY ``mpz`` object to ``dtype``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
        ...
    
    def from_GaussianRationalField(K1, a, K0) -> PythonMPQ | None:
        """Convert a ``GaussianElement`` object to ``dtype``. """
        ...
    
    def from_RealField(K1, a, K0) -> PythonMPQ:
        """Convert a mpmath ``mpf`` object to ``dtype``. """
        ...
    
    def exquo(self, a, b) -> NotImplementedType | Self:
        """Exact quotient of ``a`` and ``b``, implies ``__truediv__``.  """
        ...
    
    def quo(self, a, b) -> NotImplementedType | Self:
        """Quotient of ``a`` and ``b``, implies ``__truediv__``. """
        ...
    
    def rem(self, a, b) -> dtype:
        """Remainder of ``a`` and ``b``, implies nothing.  """
        ...
    
    def div(self, a, b) -> tuple[NotImplementedType | Self, dtype]:
        """Division of ``a`` and ``b``, implies ``__truediv__``. """
        ...
    
    def numer(self, a):
        """Returns numerator of ``a``. """
        ...
    
    def denom(self, a):
        """Returns denominator of ``a``. """
        ...
    
    def is_square(self, a) -> Literal[False]:
        """Return ``True`` if ``a`` is a square.

        Explanation
        ===========
        A rational number is a square if and only if there exists
        a rational number ``b`` such that ``b * b == a``.
        """
        ...
    
    def exsqrt(self, a) -> PythonMPQ | None:
        """Non-negative square root of ``a`` if ``a`` is a square.

        See also
        ========
        is_square
        """
        ...
    


QQ = ...
