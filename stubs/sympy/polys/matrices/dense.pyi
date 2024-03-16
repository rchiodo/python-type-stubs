from typing import Sequence, TypeVar
from sympy.polys.matrices._typing import RingElement

"""

Module for the ddm_* routines for operating on a matrix in list of lists
matrix representation.

These routines are used internally by the DDM class which also provides a
friendlier interface for them. The idea here is to implement core matrix
routines in a way that can be applied to any simple list representation
without the need to use any particular matrix class. For example we can
compute the RREF of a matrix like:

    >>> from sympy.polys.matrices.dense import ddm_irref
    >>> M = [[1, 2, 3], [4, 5, 6]]
    >>> pivots = ddm_irref(M)
    >>> M
    [[1.0, 0.0, -1.0], [0, 1.0, 2.0]]

These are lower-level routines that work mostly in place.The routines at this
level should not need to know what the domain of the elements is but should
ideally document what operations they will use and what functions they need to
be provided with.

The next-level up is the DDM class which uses these routines but wraps them up
with an interface that handles copying etc and keeps track of the Domain of
the elements of the matrix:

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.matrices.ddm import DDM
    >>> M = DDM([[QQ(1), QQ(2), QQ(3)], [QQ(4), QQ(5), QQ(6)]], (2, 3), QQ)
    >>> M
    [[1, 2, 3], [4, 5, 6]]
    >>> Mrref, pivots = M.rref()
    >>> Mrref
    [[1, 0, -1], [0, 1, 2]]

"""
T = TypeVar('T')
R = TypeVar('R', bound=RingElement)
def ddm_transpose(matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    """matrix transpose"""
    ...

def ddm_iadd(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    """a += b"""
    ...

def ddm_isub(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    """a -= b"""
    ...

def ddm_ineg(a: list[list[R]]) -> None:
    """a <-- -a"""
    ...

def ddm_imul(a: list[list[R]], b: R) -> None:
    """a <-- a*b"""
    ...

def ddm_irmul(a: list[list[R]], b: R) -> None:
    """a <-- b*a"""
    ...

def ddm_imatmul(a: list[list[R]], b: Sequence[Sequence[R]], c: Sequence[Sequence[R]]) -> None:
    """a += b @ c"""
    ...

def ddm_irref(a, _partial_pivot=...) -> list[Any]:
    """In-place reduced row echelon form of a matrix.

    Compute the reduced row echelon form of $a$. Modifies $a$ in place and
    returns a list of the pivot columns.

    Uses naive Gauss-Jordan elimination in the ground domain which must be a
    field.

    This routine is only really suitable for use with simple field domains like
    :ref:`GF(p)`, :ref:`QQ` and :ref:`QQ(a)` although even for :ref:`QQ` with
    larger matrices it is possibly more efficient to use fraction free
    approaches.

    This method is not suitable for use with rational function fields
    (:ref:`K(x)`) because the elements will blowup leading to costly gcd
    operations. In this case clearing denominators and using fraction free
    approaches is likely to be more efficient.

    For inexact numeric domains like :ref:`RR` and :ref:`CC` pass
    ``_partial_pivot=True`` to use partial pivoting to control rounding errors.

    Examples
    ========

    >>> from sympy.polys.matrices.dense import ddm_irref
    >>> from sympy import QQ
    >>> M = [[QQ(1), QQ(2), QQ(3)], [QQ(4), QQ(5), QQ(6)]]
    >>> pivots = ddm_irref(M)
    >>> M
    [[1, 0, -1], [0, 1, 2]]
    >>> pivots
    [0, 1]

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.rref
        Higher level interface to this routine.
    ddm_irref_den
        The fraction free version of this routine.
    sdm_irref
        A sparse version of this routine.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Row_echelon_form#Reduced_row_echelon_form
    """
    ...

def ddm_irref_den(a, K) -> tuple[Any, list[Any]]:
    """a  <--  rref(a); return (den, pivots)

    Compute the fraction-free reduced row echelon form (RREF) of $a$. Modifies
    $a$ in place and returns a tuple containing the denominator of the RREF and
    a list of the pivot columns.

    Explanation
    ===========

    The algorithm used is the fraction-free version of Gauss-Jordan elimination
    described as FFGJ in [1]_. Here it is modified to handle zero or missing
    pivots and to avoid redundant arithmetic.

    The domain $K$ must support exact division (``K.exquo``) but does not need
    to be a field. This method is suitable for most exact rings and fields like
    :ref:`ZZ`, :ref:`QQ` and :ref:`QQ(a)`. In the case of :ref:`QQ` or
    :ref:`K(x)` it might be more efficient to clear denominators and use
    :ref:`ZZ` or :ref:`K[x]` instead.

    For inexact domains like :ref:`RR` and :ref:`CC` use ``ddm_irref`` instead.

    Examples
    ========

    >>> from sympy.polys.matrices.dense import ddm_irref_den
    >>> from sympy import ZZ, Matrix
    >>> M = [[ZZ(1), ZZ(2), ZZ(3)], [ZZ(4), ZZ(5), ZZ(6)]]
    >>> den, pivots = ddm_irref_den(M, ZZ)
    >>> M
    [[-3, 0, 3], [0, -3, -6]]
    >>> den
    -3
    >>> pivots
    [0, 1]
    >>> Matrix(M).rref()[0]
    Matrix([
    [1, 0, -1],
    [0, 1,  2]])

    See Also
    ========

    ddm_irref
        A version of this routine that uses field division.
    sdm_irref
        A sparse version of :func:`ddm_irref`.
    sdm_rref_den
        A sparse version of :func:`ddm_irref_den`.
    sympy.polys.matrices.domainmatrix.DomainMatrix.rref_den
        Higher level interface.

    References
    ==========

    .. [1] Fraction-free algorithms for linear and polynomial equations.
        George C. Nakos , Peter R. Turner , Robert M. Williams.
        https://dl.acm.org/doi/10.1145/271130.271133
    """
    ...

def ddm_idet(a, K):
    """a  <--  echelon(a); return det

    Explanation
    ===========

    Compute the determinant of $a$ using the Bareiss fraction-free algorithm.
    The matrix $a$ is modified in place. Its diagonal elements are the
    determinants of the leading principal minors. The determinant of $a$ is
    returned.

    The domain $K$ must support exact division (``K.exquo``). This method is
    suitable for most exact rings and fields like :ref:`ZZ`, :ref:`QQ` and
    :ref:`QQ(a)` but not for inexact domains like :ref:`RR` and :ref:`CC`.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices.ddm import ddm_idet
    >>> a = [[ZZ(1), ZZ(2), ZZ(3)], [ZZ(4), ZZ(5), ZZ(6)], [ZZ(7), ZZ(8), ZZ(9)]]
    >>> a
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> ddm_idet(a, ZZ)
    0
    >>> a
    [[1, 2, 3], [4, -3, -6], [7, -6, 0]]
    >>> [a[i][i] for i in range(len(a))]
    [1, -3, 0]

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.det

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Bareiss_algorithm
    .. [2] https://www.math.usm.edu/perry/Research/Thesis_DRL.pdf
    """
    ...

def ddm_iinv(ainv, a, K) -> None:
    """ainv  <--  inv(a)

    Compute the inverse of a matrix $a$ over a field $K$ using Gauss-Jordan
    elimination. The result is stored in $ainv$.

    Uses division in the ground domain which should be an exact field.

    Examples
    ========

    >>> from sympy.polys.matrices.ddm import ddm_iinv, ddm_imatmul
    >>> from sympy import QQ
    >>> a = [[QQ(1), QQ(2)], [QQ(3), QQ(4)]]
    >>> ainv = [[None, None], [None, None]]
    >>> ddm_iinv(ainv, a, QQ)
    >>> ainv
    [[-2, 1], [3/2, -1/2]]
    >>> result = [[QQ(0), QQ(0)], [QQ(0), QQ(0)]]
    >>> ddm_imatmul(result, a, ainv)
    >>> result
    [[1, 0], [0, 1]]

    See Also
    ========

    ddm_irref: the underlying routine.
    """
    ...

def ddm_ilu_split(L, U, K) -> list[Any]:
    """L, U  <--  LU(U)

    Compute the LU decomposition of a matrix $L$ in place and store the lower
    and upper triangular matrices in $L$ and $U$, respectively. Returns a list
    of row swaps that were performed.

    Uses division in the ground domain which should be an exact field.

    Examples
    ========

    >>> from sympy.polys.matrices.ddm import ddm_ilu_split
    >>> from sympy import QQ
    >>> L = [[QQ(0), QQ(0)], [QQ(0), QQ(0)]]
    >>> U = [[QQ(1), QQ(2)], [QQ(3), QQ(4)]]
    >>> swaps = ddm_ilu_split(L, U, QQ)
    >>> swaps
    []
    >>> L
    [[0, 0], [3, 0]]
    >>> U
    [[1, 2], [0, -2]]

    See Also
    ========

    ddm_ilu
    ddm_ilu_solve
    """
    ...

def ddm_ilu(a) -> list[Any]:
    """a  <--  LU(a)

    Computes the LU decomposition of a matrix in place. Returns a list of
    row swaps that were performed.

    Uses division in the ground domain which should be an exact field.

    This is only suitable for domains like :ref:`GF(p)`, :ref:`QQ`, :ref:`QQ_I`
    and :ref:`QQ(a)`. With a rational function field like :ref:`K(x)` it is
    better to clear denominators and use division-free algorithms. Pivoting is
    used to avoid exact zeros but not for floating point accuracy so :ref:`RR`
    and :ref:`CC` are not suitable (use :func:`ddm_irref` instead).

    Examples
    ========

    >>> from sympy.polys.matrices.dense import ddm_ilu
    >>> from sympy import QQ
    >>> a = [[QQ(1, 2), QQ(1, 3)], [QQ(1, 4), QQ(1, 5)]]
    >>> swaps = ddm_ilu(a)
    >>> swaps
    []
    >>> a
    [[1/2, 1/3], [1/2, 1/30]]

    The same example using ``Matrix``:

    >>> from sympy import Matrix, S
    >>> M = Matrix([[S(1)/2, S(1)/3], [S(1)/4, S(1)/5]])
    >>> L, U, swaps = M.LUdecomposition()
    >>> L
    Matrix([
    [  1, 0],
    [1/2, 1]])
    >>> U
    Matrix([
    [1/2,  1/3],
    [  0, 1/30]])
    >>> swaps
    []

    See Also
    ========

    ddm_irref
    ddm_ilu_solve
    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    """
    ...

def ddm_ilu_solve(x, L, U, swaps, b) -> None:
    """x  <--  solve(L*U*x = swaps(b))

    Solve a linear system, $A*x = b$, given an LU factorization of $A$.

    Uses division in the ground domain which must be a field.

    Modifies $x$ in place.

    Examples
    ========

    Compute the LU decomposition of $A$ (in place):

    >>> from sympy import QQ
    >>> from sympy.polys.matrices.dense import ddm_ilu, ddm_ilu_solve
    >>> A = [[QQ(1), QQ(2)], [QQ(3), QQ(4)]]
    >>> swaps = ddm_ilu(A)
    >>> A
    [[1, 2], [3, -2]]
    >>> L = U = A

    Solve the linear system:

    >>> b = [[QQ(5)], [QQ(6)]]
    >>> x = [[None], [None]]
    >>> ddm_ilu_solve(x, L, U, swaps, b)
    >>> x
    [[-4], [9/2]]

    See Also
    ========

    ddm_ilu
        Compute the LU decomposition of a matrix in place.
    ddm_ilu_split
        Compute the LU decomposition of a matrix and separate $L$ and $U$.
    sympy.polys.matrices.domainmatrix.DomainMatrix.lu_solve
        Higher level interface to this function.
    """
    ...

def ddm_berk(M, K) -> list[list[Any]]:
    """
    Berkowitz algorithm for computing the characteristic polynomial.

    Explanation
    ===========

    The Berkowitz algorithm is a division-free algorithm for computing the
    characteristic polynomial of a matrix over any commutative ring using only
    arithmetic in the coefficient ring.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.polys.matrices.dense import ddm_berk
    >>> from sympy.polys.domains import ZZ
    >>> M = [[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]]
    >>> ddm_berk(M, ZZ)
    [[1], [-5], [-2]]
    >>> Matrix(M).charpoly()
    PurePoly(lambda**2 - 5*lambda - 2, lambda, domain='ZZ')

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.charpoly
        The high-level interface to this function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Samuelson%E2%80%93Berkowitz_algorithm
    """
    ...

