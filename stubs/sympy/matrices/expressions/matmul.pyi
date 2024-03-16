from sympy.core.mul import Mul
from sympy.matrices.expressions.matexpr import MatrixExpr

class MatMul(MatrixExpr, Mul):
    """
    A product of matrix expressions

    Examples
    ========

    >>> from sympy import MatMul, MatrixSymbol
    >>> A = MatrixSymbol('A', 5, 4)
    >>> B = MatrixSymbol('B', 4, 3)
    >>> C = MatrixSymbol('C', 3, 6)
    >>> MatMul(A, B, C)
    A*B*C
    """
    is_MatMul = ...
    identity = ...
    def __new__(cls, *args, evaluate=..., check=..., _sympify=...) -> GenericIdentity | Order | object | Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def as_coeff_matrices(self) -> tuple[Any | Order, list[Expr]]:
        ...
    
    def as_coeff_mmul(self) -> tuple[Any | Order, GenericIdentity | Any | Order | object | MatMul]:
        ...
    
    def expand(self, **kwargs) -> object:
        ...
    
    def doit(self, **hints) -> object:
        ...
    
    def args_cnc(self, cset=..., warn=..., **kwargs) -> list[Any]:
        ...
    


def newmul(*args) -> MatMul:
    ...

def any_zeros(mul) -> ZeroMatrix:
    ...

def merge_explicit(matmul) -> MatMul:
    """ Merge explicit MatrixBase arguments

    >>> from sympy import MatrixSymbol, Matrix, MatMul, pprint
    >>> from sympy.matrices.expressions.matmul import merge_explicit
    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = Matrix([[1, 1], [1, 1]])
    >>> C = Matrix([[1, 2], [3, 4]])
    >>> X = MatMul(A, B, C)
    >>> pprint(X)
      [1  1] [1  2]
    A*[    ]*[    ]
      [1  1] [3  4]
    >>> pprint(merge_explicit(X))
      [4  6]
    A*[    ]
      [4  6]

    >>> X = MatMul(B, A, C)
    >>> pprint(X)
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    >>> pprint(merge_explicit(X))
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    """
    ...

def remove_ids(mul) -> MatMul:
    """ Remove Identities from a MatMul

    This is a modified version of sympy.strategies.rm_id.
    This is necesssary because MatMul may contain both MatrixExprs and Exprs
    as args.

    See Also
    ========

    sympy.strategies.rm_id
    """
    ...

def factor_in_front(mul) -> MatMul:
    ...

def combine_powers(mul) -> MatMul:
    r"""Combine consecutive powers with the same base into one, e.g.
    $$A \times A^2 \Rightarrow A^3$$

    This also cancels out the possible matrix inverses using the
    knowledgebase of :class:`~.Inverse`, e.g.,
    $$ Y \times X \times X^{-1} \Rightarrow Y $$
    """
    ...

def combine_permutations(mul) -> MatMul:
    """Refine products of permutation matrices as the products of cycles.
    """
    ...

def combine_one_matrices(mul) -> MatMul:
    """
    Combine products of OneMatrix

    e.g. OneMatrix(2, 3) * OneMatrix(3, 4) -> 3 * OneMatrix(2, 4)
    """
    ...

def distribute_monom(mul) -> GenericZeroMatrix | MatAdd:
    """
    Simplify MatMul expressions but distributing
    rational term to MatMul.

    e.g. 2*(A+B) -> 2*A + 2*B
    """
    ...

rules = ...
canonicalize = ...
def only_squares(*matrices) -> list[Any]:
    """factor matrices only if they are square"""
    ...

def refine_MatMul(expr, assumptions) -> GenericIdentity | Order | object | MatMul:
    """
    >>> from sympy import MatrixSymbol, Q, assuming, refine
    >>> X = MatrixSymbol('X', 2, 2)
    >>> expr = X * X.T
    >>> print(expr)
    X*X.T
    >>> with assuming(Q.orthogonal(X)):
    ...     print(refine(expr))
    I
    """
    ...

