from collections.abc import MutableSet
from typing import Any, Callable
from sympy.core.basic import Basic
from sympy.core.kind import Kind

"""Module for SymPy containers

    (SymPy objects that store other SymPy objects)

    The containers implemented in this module are subclassed to Basic.
    They are supposed to work seamlessly within the SymPy framework.
"""
class Tuple(Basic):
    """
    Wrapper around the builtin tuple object.

    Explanation
    ===========

    The Tuple is a subclass of Basic, so that it works well in the
    SymPy framework.  The wrapped tuple is available as self.args, but
    you can also access elements or slices with [:] syntax.

    Parameters
    ==========

    sympify : bool
        If ``False``, ``sympify`` is not called on ``args``. This
        can be used for speedups for very large tuples where the
        elements are known to already be SymPy objects.

    Examples
    ========

    >>> from sympy import Tuple, symbols
    >>> a, b, c, d = symbols('a b c d')
    >>> Tuple(a, b, c)[1:]
    (b, c)
    >>> Tuple(a, b, c).subs(a, d)
    (d, b, c)

    """
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def __getitem__(self, i) -> Tuple:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, item) -> bool:
        ...
    
    def __iter__(self) -> Iterator[Basic]:
        ...
    
    def __add__(self, other) -> Tuple | NotImplementedType:
        ...
    
    def __radd__(self, other) -> Tuple | NotImplementedType:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    __rmul__ = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def tuple_count(self, value) -> int:
        """Return number of occurrences of value."""
        ...
    
    def index(self, value, start=..., stop=...) -> int:
        """Searches and returns the first index of the value."""
        ...
    
    @property
    def kind(self) -> TupleKind:
        """
        The kind of a Tuple instance.

        The kind of a Tuple is always of :class:`TupleKind` but
        parametrised by the number of elements and the kind of each element.

        Examples
        ========

        >>> from sympy import Tuple, Matrix
        >>> Tuple(1, 2).kind
        TupleKind(NumberKind, NumberKind)
        >>> Tuple(Matrix([1, 2]), 1).kind
        TupleKind(MatrixKind(NumberKind), NumberKind)
        >>> Tuple(1, 2).kind.element_kind
        (NumberKind, NumberKind)

        See Also
        ========

        sympy.matrices.kind.MatrixKind
        sympy.core.kind.NumberKind
        """
        ...
    


def tuple_wrapper(method) -> Callable[..., Any]:
    """
    Decorator that converts any tuple in the function arguments into a Tuple.

    Explanation
    ===========

    The motivation for this is to provide simple user interfaces.  The user can
    call a function with regular tuples in the argument, and the wrapper will
    convert them to Tuples before handing them to the function.

    Explanation
    ===========

    >>> from sympy.core.containers import tuple_wrapper
    >>> def f(*args):
    ...    return args
    >>> g = tuple_wrapper(f)

    The decorated function g sees only the Tuple argument:

    >>> g(0, (1, 2), 3)
    (0, (1, 2), 3)

    """
    ...

class Dict(Basic):
    """
    Wrapper around the builtin dict object.

    Explanation
    ===========

    The Dict is a subclass of Basic, so that it works well in the
    SymPy framework.  Because it is immutable, it may be included
    in sets, but its values must all be given at instantiation and
    cannot be changed afterwards.  Otherwise it behaves identically
    to the Python dict.

    Examples
    ========

    >>> from sympy import Dict, Symbol

    >>> D = Dict({1: 'one', 2: 'two'})
    >>> for key in D:
    ...    if key == 1:
    ...        print('%s %s' % (key, D[key]))
    1 one

    The args are sympified so the 1 and 2 are Integers and the values
    are Symbols. Queries automatically sympify args so the following work:

    >>> 1 in D
    True
    >>> D.has(Symbol('one')) # searches keys and values
    True
    >>> 'one' in D # not in the keys
    False
    >>> D[1]
    one

    """
    def __new__(cls, *args) -> Self:
        ...
    
    def __getitem__(self, key):
        """x.__getitem__(y) <==> x[y]"""
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def items(self):
        '''Returns a set-like object providing a view on dict's items.
        '''
        ...
    
    def keys(self):
        '''Returns the list of the dict's keys.'''
        ...
    
    def values(self):
        '''Returns the list of the dict's values.'''
        ...
    
    def __iter__(self):
        '''x.__iter__() <==> iter(x)'''
        ...
    
    def __len__(self):
        '''x.__len__() <==> len(x)'''
        ...
    
    def get(self, key, default=...) -> None:
        '''Returns the value for key if the key is in the dictionary.'''
        ...
    
    def __contains__(self, key) -> bool:
        '''D.__contains__(k) -> True if D has a key k, else False'''
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    __hash__: Callable[[Basic], Any] = ...


class OrderedSet(MutableSet):
    def __init__(self, iterable=...) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    def add(self, key) -> None:
        ...
    
    def discard(self, key) -> None:
        ...
    
    def pop(self, last=...):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def intersection(self, other) -> Self:
        ...
    
    def difference(self, other) -> Self:
        ...
    
    def update(self, iterable) -> None:
        ...
    


class TupleKind(Kind):
    """
    TupleKind is a subclass of Kind, which is used to define Kind of ``Tuple``.

    Parameters of TupleKind will be kinds of all the arguments in Tuples, for
    example

    Parameters
    ==========

    args : tuple(element_kind)
       element_kind is kind of element.
       args is tuple of kinds of element

    Examples
    ========

    >>> from sympy import Tuple
    >>> Tuple(1, 2).kind
    TupleKind(NumberKind, NumberKind)
    >>> Tuple(1, 2).kind.element_kind
    (NumberKind, NumberKind)

    See Also
    ========

    sympy.core.kind.NumberKind
    MatrixKind
    sympy.sets.sets.SetKind
    """
    def __new__(cls, *args) -> Self:
        ...
    
    def __repr__(self) -> str:
        ...
    


