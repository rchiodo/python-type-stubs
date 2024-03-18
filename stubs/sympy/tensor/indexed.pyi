from typing import Any, Self, Tuple
from sympy import Basic, MatrixBase, NDimArray
from sympy.core import Expr
from sympy.utilities.iterables import NotIterable

r"""Module that defines indexed objects.

The classes ``IndexedBase``, ``Indexed``, and ``Idx`` represent a
matrix element ``M[i, j]`` as in the following diagram::

       1) The Indexed class represents the entire indexed object.
                  |
               ___|___
              '       '
               M[i, j]
              /   \__\______
              |             |
              |             |
              |     2) The Idx class represents indices; each Idx can
              |        optionally contain information about its range.
              |
        3) IndexedBase represents the 'stem' of an indexed object, here `M`.
           The stem used by itself is usually taken to represent the entire
           array.

There can be any number of indices on an Indexed object.  No
transformation properties are implemented in these Base objects, but
implicit contraction of repeated indices is supported.

Note that the support for complicated (i.e. non-atomic) integer
expressions as indices is limited.  (This should be improved in
future releases.)

Examples
========

To express the above matrix element example you would write:

>>> from sympy import symbols, IndexedBase, Idx
>>> M = IndexedBase('M')
>>> i, j = symbols('i j', cls=Idx)
>>> M[i, j]
M[i, j]

Repeated indices in a product implies a summation, so to express a
matrix-vector product in terms of Indexed objects:

>>> x = IndexedBase('x')
>>> M[i, j]*x[j]
M[i, j]*x[j]

If the indexed objects will be converted to component based arrays, e.g.
with the code printers or the autowrap framework, you also need to provide
(symbolic or numerical) dimensions.  This can be done by passing an
optional shape parameter to IndexedBase upon construction:

>>> dim1, dim2 = symbols('dim1 dim2', integer=True)
>>> A = IndexedBase('A', shape=(dim1, 2*dim1, dim2))
>>> A.shape
(dim1, 2*dim1, dim2)
>>> A[i, j, 3].shape
(dim1, 2*dim1, dim2)

If an IndexedBase object has no shape information, it is assumed that the
array is as large as the ranges of its indices:

>>> n, m = symbols('n m', integer=True)
>>> i = Idx('i', m)
>>> j = Idx('j', n)
>>> M[i, j].shape
(m, n)
>>> M[i, j].ranges
[(0, m - 1), (0, n - 1)]

The above can be compared with the following:

>>> A[i, 2, j].shape
(dim1, 2*dim1, dim2)
>>> A[i, 2, j].ranges
[(0, m - 1), None, (0, n - 1)]

To analyze the structure of indexed expressions, you can use the methods
get_indices() and get_contraction_structure():

>>> from sympy.tensor import get_indices, get_contraction_structure
>>> get_indices(A[i, j, j])
({i}, {})
>>> get_contraction_structure(A[i, j, j])
{(j,): {A[i, j, j]}}

See the appropriate docstrings for a detailed explanation of the output.
"""
class IndexException(Exception):
    ...


class Indexed(Expr):
    """Represents a mathematical object with indices.

    >>> from sympy import Indexed, IndexedBase, Idx, symbols
    >>> i, j = symbols('i j', cls=Idx)
    >>> Indexed('A', i, j)
    A[i, j]

    It is recommended that ``Indexed`` objects be created by indexing ``IndexedBase``:
    ``IndexedBase('A')[i, j]`` instead of ``Indexed(IndexedBase('A'), i, j)``.

    >>> A = IndexedBase('A')
    >>> a_ij = A[i, j]           # Prefer this,
    >>> b_ij = Indexed(A, i, j)  # over this.
    >>> a_ij == b_ij
    True

    """
    is_Indexed = ...
    is_symbol = ...
    is_Atom = ...
    def __new__(cls, base, *args, **kw_args) -> Self:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def assumptions0(self) -> dict[Any, Any]:
        ...
    
    @property
    def base(self) -> Basic:
        """Returns the ``IndexedBase`` of the ``Indexed`` object.

        Examples
        ========

        >>> from sympy import Indexed, IndexedBase, Idx, symbols
        >>> i, j = symbols('i j', cls=Idx)
        >>> Indexed('A', i, j).base
        A
        >>> B = IndexedBase('B')
        >>> B == B[i, j].base
        True

        """
        ...
    
    @property
    def indices(self) -> tuple[Basic, ...]:
        """
        Returns the indices of the ``Indexed`` object.

        Examples
        ========

        >>> from sympy import Indexed, Idx, symbols
        >>> i, j = symbols('i j', cls=Idx)
        >>> Indexed('A', i, j).indices
        (i, j)

        """
        ...
    
    @property
    def rank(self) -> int:
        """
        Returns the rank of the ``Indexed`` object.

        Examples
        ========

        >>> from sympy import Indexed, Idx, symbols
        >>> i, j, k, l, m = symbols('i:m', cls=Idx)
        >>> Indexed('A', i, j).rank
        2
        >>> q = Indexed('A', i, j, k, l, m)
        >>> q.rank
        5
        >>> q.rank == len(q.indices)
        True

        """
        ...
    
    @property
    def shape(self) -> Tuple:
        """Returns a list with dimensions of each index.

        Dimensions is a property of the array, not of the indices.  Still, if
        the ``IndexedBase`` does not define a shape attribute, it is assumed
        that the ranges of the indices correspond to the shape of the array.

        >>> from sympy import IndexedBase, Idx, symbols
        >>> n, m = symbols('n m', integer=True)
        >>> i = Idx('i', m)
        >>> j = Idx('j', m)
        >>> A = IndexedBase('A', shape=(n, n))
        >>> B = IndexedBase('B')
        >>> A[i, j].shape
        (n, n)
        >>> B[i, j].shape
        (m, m)
        """
        ...
    
    @property
    def ranges(self) -> list[Any]:
        """Returns a list of tuples with lower and upper range of each index.

        If an index does not define the data members upper and lower, the
        corresponding slot in the list contains ``None`` instead of a tuple.

        Examples
        ========

        >>> from sympy import Indexed,Idx, symbols
        >>> Indexed('A', Idx('i', 2), Idx('j', 4), Idx('k', 8)).ranges
        [(0, 1), (0, 3), (0, 7)]
        >>> Indexed('A', Idx('i', 3), Idx('j', 3), Idx('k', 3)).ranges
        [(0, 2), (0, 2), (0, 2)]
        >>> x, y, z = symbols('x y z', integer=True)
        >>> Indexed('A', x, y, z).ranges
        [None, None, None]

        """
        ...
    
    @property
    def free_symbols(self) -> set[Self | Basic] | set[Basic]:
        ...
    
    @property
    def expr_free_symbols(self) -> set[Self]:
        ...
    


class IndexedBase(Expr, NotIterable):
    """Represent the base or stem of an indexed object

    The IndexedBase class represent an array that contains elements. The main purpose
    of this class is to allow the convenient creation of objects of the Indexed
    class.  The __getitem__ method of IndexedBase returns an instance of
    Indexed.  Alone, without indices, the IndexedBase class can be used as a
    notation for e.g. matrix equations, resembling what you could do with the
    Symbol class.  But, the IndexedBase class adds functionality that is not
    available for Symbol instances:

      -  An IndexedBase object can optionally store shape information.  This can
         be used in to check array conformance and conditions for numpy
         broadcasting.  (TODO)
      -  An IndexedBase object implements syntactic sugar that allows easy symbolic
         representation of array operations, using implicit summation of
         repeated indices.
      -  The IndexedBase object symbolizes a mathematical structure equivalent
         to arrays, and is recognized as such for code generation and automatic
         compilation and wrapping.

    >>> from sympy.tensor import IndexedBase, Idx
    >>> from sympy import symbols
    >>> A = IndexedBase('A'); A
    A
    >>> type(A)
    <class 'sympy.tensor.indexed.IndexedBase'>

    When an IndexedBase object receives indices, it returns an array with named
    axes, represented by an Indexed object:

    >>> i, j = symbols('i j', integer=True)
    >>> A[i, j, 2]
    A[i, j, 2]
    >>> type(A[i, j, 2])
    <class 'sympy.tensor.indexed.Indexed'>

    The IndexedBase constructor takes an optional shape argument.  If given,
    it overrides any shape information in the indices. (But not the index
    ranges!)

    >>> m, n, o, p = symbols('m n o p', integer=True)
    >>> i = Idx('i', m)
    >>> j = Idx('j', n)
    >>> A[i, j].shape
    (m, n)
    >>> B = IndexedBase('B', shape=(o, p))
    >>> B[i, j].shape
    (o, p)

    Assumptions can be specified with keyword arguments the same way as for Symbol:

    >>> A_real = IndexedBase('A', real=True)
    >>> A_real.is_real
    True
    >>> A != A_real
    True

    Assumptions can also be inherited if a Symbol is used to initialize the IndexedBase:

    >>> I = symbols('I', integer=True)
    >>> C_inherit = IndexedBase(I)
    >>> C_explicit = IndexedBase('I', integer=True)
    >>> C_inherit == C_explicit
    True
    """
    is_symbol = ...
    is_Atom = ...
    def __new__(cls, label, shape=..., *, offset=..., strides=..., **kw_args) -> MatrixBase | NDimArray | Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def assumptions0(self) -> dict[Any, Any]:
        ...
    
    def __getitem__(self, indices, **kw_args) -> Indexed:
        ...
    
    @property
    def shape(self):
        """Returns the shape of the ``IndexedBase`` object.

        Examples
        ========

        >>> from sympy import IndexedBase, Idx
        >>> from sympy.abc import x, y
        >>> IndexedBase('A', shape=(x, y)).shape
        (x, y)

        Note: If the shape of the ``IndexedBase`` is specified, it will override
        any shape information given by the indices.

        >>> A = IndexedBase('A', shape=(x, y))
        >>> B = IndexedBase('B')
        >>> i = Idx('i', 2)
        >>> j = Idx('j', 1)
        >>> A[i, j].shape
        (x, y)
        >>> B[i, j].shape
        (2, 1)

        """
        ...
    
    @property
    def strides(self):
        """Returns the strided scheme for the ``IndexedBase`` object.

        Normally this is a tuple denoting the number of
        steps to take in the respective dimension when traversing
        an array. For code generation purposes strides='C' and
        strides='F' can also be used.

        strides='C' would mean that code printer would unroll
        in row-major order and 'F' means unroll in column major
        order.

        """
        ...
    
    @property
    def offset(self):
        """Returns the offset for the ``IndexedBase`` object.

        This is the value added to the resulting index when the
        2D Indexed object is unrolled to a 1D form. Used in code
        generation.

        Examples
        ==========
        >>> from sympy.printing import ccode
        >>> from sympy.tensor import IndexedBase, Idx
        >>> from sympy import symbols
        >>> l, m, n, o = symbols('l m n o', integer=True)
        >>> A = IndexedBase('A', strides=(l, m, n), offset=o)
        >>> i, j, k = map(Idx, 'ijk')
        >>> ccode(A[i, j, k])
        'A[l*i + m*j + n*k + o]'

        """
        ...
    
    @property
    def label(self) -> Basic:
        """Returns the label of the ``IndexedBase`` object.

        Examples
        ========

        >>> from sympy import IndexedBase
        >>> from sympy.abc import x, y
        >>> IndexedBase('A', shape=(x, y)).label
        A

        """
        ...
    


class Idx(Expr):
    """Represents an integer index as an ``Integer`` or integer expression.

    There are a number of ways to create an ``Idx`` object.  The constructor
    takes two arguments:

    ``label``
        An integer or a symbol that labels the index.
    ``range``
        Optionally you can specify a range as either

        * ``Symbol`` or integer: This is interpreted as a dimension. Lower and
          upper bounds are set to ``0`` and ``range - 1``, respectively.
        * ``tuple``: The two elements are interpreted as the lower and upper
          bounds of the range, respectively.

    Note: bounds of the range are assumed to be either integer or infinite (oo
    and -oo are allowed to specify an unbounded range). If ``n`` is given as a
    bound, then ``n.is_integer`` must not return false.

    For convenience, if the label is given as a string it is automatically
    converted to an integer symbol.  (Note: this conversion is not done for
    range or dimension arguments.)

    Examples
    ========

    >>> from sympy import Idx, symbols, oo
    >>> n, i, L, U = symbols('n i L U', integer=True)

    If a string is given for the label an integer ``Symbol`` is created and the
    bounds are both ``None``:

    >>> idx = Idx('qwerty'); idx
    qwerty
    >>> idx.lower, idx.upper
    (None, None)

    Both upper and lower bounds can be specified:

    >>> idx = Idx(i, (L, U)); idx
    i
    >>> idx.lower, idx.upper
    (L, U)

    When only a single bound is given it is interpreted as the dimension
    and the lower bound defaults to 0:

    >>> idx = Idx(i, n); idx.lower, idx.upper
    (0, n - 1)
    >>> idx = Idx(i, 4); idx.lower, idx.upper
    (0, 3)
    >>> idx = Idx(i, oo); idx.lower, idx.upper
    (0, oo)

    """
    is_integer = ...
    is_finite = ...
    is_real = ...
    is_symbol = ...
    is_Atom = ...
    _diff_wrt = ...
    def __new__(cls, label, range=..., **kw_args) -> Self:
        ...
    
    @property
    def label(self) -> Basic:
        """Returns the label (Integer or integer expression) of the Idx object.

        Examples
        ========

        >>> from sympy import Idx, Symbol
        >>> x = Symbol('x', integer=True)
        >>> Idx(x).label
        x
        >>> j = Symbol('j', integer=True)
        >>> Idx(j).label
        j
        >>> Idx(j + 1).label
        j + 1

        """
        ...
    
    @property
    def lower(self) -> None:
        """Returns the lower bound of the ``Idx``.

        Examples
        ========

        >>> from sympy import Idx
        >>> Idx('j', 2).lower
        0
        >>> Idx('j', 5).lower
        0
        >>> Idx('j').lower is None
        True

        """
        ...
    
    @property
    def upper(self) -> None:
        """Returns the upper bound of the ``Idx``.

        Examples
        ========

        >>> from sympy import Idx
        >>> Idx('j', 2).upper
        1
        >>> Idx('j', 5).upper
        4
        >>> Idx('j').upper is None
        True

        """
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


