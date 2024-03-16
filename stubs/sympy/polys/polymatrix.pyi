class MutablePolyDenseMatrix:
    """
    A mutable matrix of objects from poly module or to operate with them.

    Examples
    ========

    >>> from sympy.polys.polymatrix import PolyMatrix
    >>> from sympy import Symbol, Poly
    >>> x = Symbol('x')
    >>> pm1 = PolyMatrix([[Poly(x**2, x), Poly(-x, x)], [Poly(x**3, x), Poly(-1 + x, x)]])
    >>> v1 = PolyMatrix([[1, 0], [-1, 0]], x)
    >>> pm1*v1
    PolyMatrix([
    [    x**2 + x, 0],
    [x**3 - x + 1, 0]], ring=QQ[x])

    >>> pm1.ring
    ZZ[x]

    >>> v1*pm1
    PolyMatrix([
    [ x**2, -x],
    [-x**2,  x]], ring=QQ[x])

    >>> pm2 = PolyMatrix([[Poly(x**2, x, domain='QQ'), Poly(0, x, domain='QQ'), Poly(1, x, domain='QQ'), \
            Poly(x**3, x, domain='QQ'), Poly(0, x, domain='QQ'), Poly(-x**3, x, domain='QQ')]])
    >>> v2 = PolyMatrix([1, 0, 0, 0, 0, 0], x)
    >>> v2.ring
    QQ[x]
    >>> pm2*v2
    PolyMatrix([[x**2]], ring=QQ[x])

    """
    def __new__(cls, *args, ring=...) -> Self:
        ...
    
    @classmethod
    def from_list(cls, rows, cols, items, gens, ring) -> Self:
        ...
    
    @classmethod
    def from_dm(cls, dm) -> Self:
        ...
    
    def to_Matrix(self):
        ...
    
    @classmethod
    def from_Matrix(cls, other, *gens, ring=...) -> Self:
        ...
    
    def set_gens(self, gens) -> Self:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    def __len__(self):
        ...
    
    def __getitem__(self, key) -> list[Any] | Any | Self:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __add__(self, other) -> Self | NotImplementedType:
        ...
    
    def __sub__(self, other) -> Self | NotImplementedType:
        ...
    
    def __mul__(self, other) -> Self | NotImplementedType:
        ...
    
    def __rmul__(self, other) -> Self | NotImplementedType:
        ...
    
    def __truediv__(self, other) -> NotImplementedType | Self:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def transpose(self) -> Self:
        ...
    
    def row_join(self, other) -> Self:
        ...
    
    def col_join(self, other) -> Self:
        ...
    
    def applyfunc(self, func) -> Self:
        ...
    
    @classmethod
    def eye(cls, n, gens) -> Self:
        ...
    
    @classmethod
    def zeros(cls, m, n, gens) -> Self:
        ...
    
    def rref(self, simplify=..., normalize_last=...) -> tuple[Self, Any]:
        ...
    
    def nullspace(self) -> list[Self]:
        ...
    
    def rank(self):
        ...
    


PolyMatrix = MutablePolyMatrix = MutablePolyDenseMatrix
