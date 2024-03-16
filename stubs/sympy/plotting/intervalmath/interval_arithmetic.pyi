"""
Interval Arithmetic for plotting.
This module does not implement interval arithmetic accurately and
hence cannot be used for purposes other than plotting. If you want
to use interval arithmetic, use mpmath's interval arithmetic.

The module implements interval arithmetic using numpy and
python floating points. The rounding up and down is not handled
and hence this is not an accurate implementation of interval
arithmetic.

The module uses numpy for speed which cannot be achieved with mpmath.
"""
class interval:
    """ Represents an interval containing floating points as start and
    end of the interval
    The is_valid variable tracks whether the interval obtained as the
    result of the function is in the domain and is continuous.
    - True: Represents the interval result of a function is continuous and
            in the domain of the function.
    - False: The interval argument of the function was not in the domain of
             the function, hence the is_valid of the result interval is False
    - None: The function was not continuous over the interval or
            the function's argument interval is partly in the domain of the
            function

    A comparison between an interval and a real number, or a
    comparison between two intervals may return ``intervalMembership``
    of two 3-valued logic values.
    """
    def __init__(self, *args, is_valid=..., **kwargs) -> None:
        ...
    
    @property
    def mid(self) -> float:
        ...
    
    @property
    def width(self) -> float:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __add__(self, other) -> interval | NotImplementedType:
        ...
    
    __radd__ = ...
    def __sub__(self, other) -> interval | NotImplementedType:
        ...
    
    def __rsub__(self, other) -> interval | NotImplementedType:
        ...
    
    def __neg__(self) -> interval:
        ...
    
    def __mul__(self, other) -> interval | NotImplementedType:
        ...
    
    __rmul__ = ...
    def __contains__(self, other) -> bool:
        ...
    
    def __rtruediv__(self, other) -> interval | NotImplementedType:
        ...
    
    def __truediv__(self, other) -> interval | NotImplementedType:
        ...
    
    def __pow__(self, other) -> Self | interval | NotImplementedType:
        ...
    
    def __rpow__(self, other) -> Self | interval | NotImplementedType:
        ...
    
    def __hash__(self) -> int:
        ...
    


