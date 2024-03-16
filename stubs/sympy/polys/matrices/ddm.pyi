from sympy.utilities.decorator import doctest_depends_on

"""

Module for the DDM class.

The DDM class is an internal representation used by DomainMatrix. The letters
DDM stand for Dense Domain Matrix. A DDM instance represents a matrix using
elements from a polynomial Domain (e.g. ZZ, QQ, ...) in a dense-matrix
representation.

Basic usage:

    >>> from sympy import ZZ, QQ
    >>> from sympy.polys.matrices.ddm import DDM
    >>> A = DDM([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
    >>> A.shape
    (2, 2)
    >>> A
    [[0, 1], [-1, 0]]
    >>> type(A)
    <class 'sympy.polys.matrices.ddm.DDM'>
    >>> A @ A
    [[-1, 0], [0, -1]]

The ddm_* functions are designed to operate on DDM as well as on an ordinary
list of lists:

    >>> from sympy.polys.matrices.dense import ddm_idet
    >>> ddm_idet(A, QQ)
    1
    >>> ddm_idet([[0, 1], [-1, 0]], QQ)
    1
    >>> A
    [[-1, 0], [0, -1]]

Note that ddm_idet modifies the input matrix in-place. It is recommended to
use the DDM.det method as a friendlier interface to this instead which takes
care of copying the matrix:

    >>> B = DDM([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
    >>> B.det()
    1

Normally DDM would not be used directly and is just part of the internal
representation of DomainMatrix which adds further functionality including e.g.
unifying domains.

The dense format used by DDM is a list of lists of elements e.g. the 2x2
identity matrix is like [[1, 0], [0, 1]]. The DDM class itself is a subclass
of list and its list items are plain lists. Elements are accessed as e.g.
ddm[i][j] where ddm[i] gives the ith row and ddm[i][j] gets the element in the
jth column of that row. Subclassing list makes e.g. iteration and indexing
very efficient. We do not override __getitem__ because it would lose that
benefit.

The core routines are implemented by the ddm_* functions defined in dense.py.
Those functions are intended to be able to operate on a raw list-of-lists
representation of matrices with most functions operating in-place. The DDM
class takes care of copying etc and also stores a Domain object associated
with its elements. This makes it possible to implement things like A + B with
domain checking and also shape checking so that the list of lists
representation is friendlier.

"""
class DDM(list):
    """Dense matrix based on polys domain elements

    This is a list subclass and is a wrapper for a list of lists that supports
    basic matrix arithmetic +, -, *, **.
    """
    fmt = ...
    is_DFM = ...
    is_DDM = ...
    def __init__(self, rowslist, shape, domain) -> None:
        ...
    
    def getitem(self, i, j):
        ...
    
    def setitem(self, i, j, value) -> None:
        ...
    
    def extract_slice(self, slice1, slice2) -> DDM:
        ...
    
    def extract(self, rows, cols) -> DDM:
        ...
    
    @classmethod
    def from_list(cls, rowslist, shape, domain) -> Self:
        """
        Create a :class:`DDM` from a list of lists.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.ddm import DDM
        >>> A = DDM.from_list([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
        >>> A
        [[0, 1], [-1, 0]]
        >>> A == DDM([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
        True

        See Also
        ========

        from_list_flat
        """
        ...
    
    @classmethod
    def from_ddm(cls, other):
        ...
    
    def to_list(self) -> list[Any]:
        """
        Convert to a list of lists.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices.ddm import DDM
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_list()
        [[1, 2], [3, 4]]

        See Also
        ========

        to_list_flat
        """
        ...
    
    def to_list_flat(self) -> list[Any]:
        """
        Convert to a flat list of elements.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices.ddm import DDM
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_list_flat()
        [1, 2, 3, 4]
        >>> A == DDM.from_list_flat(A.to_list_flat(), A.shape, A.domain)
        True

        See Also
        ========

        from_list_flat
        """
        ...
    
    @classmethod
    def from_list_flat(cls, flat, shape, domain) -> Self:
        """
        Create a :class:`DDM` from a flat list of elements.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices.ddm import DDM
        >>> A = DDM.from_list_flat([1, 2, 3, 4], (2, 2), QQ)
        >>> A
        [[1, 2], [3, 4]]
        >>> A == DDM.from_list_flat(A.to_list_flat(), A.shape, A.domain)
        True

        See Also
        ========

        to_list_flat
        """
        ...
    
    def flatiter(self) -> chain[Any]:
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    def to_flat_nz(self) -> tuple[list[Any], tuple[tuple[tuple[Any, Any], ...], Any]]:
        """
        Convert to a flat list of nonzero elements and data.

        Explanation
        ===========

        This is used to operate on a list of the elements of a matrix and then
        reconstruct a matrix using :meth:`from_flat_nz`. Zero elements are
        included in the list but that may change in the future.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> elements, data = A.to_flat_nz()
        >>> elements
        [1, 2, 3, 4]
        >>> A == DDM.from_flat_nz(elements, data, A.domain)
        True

        See Also
        ========

        from_flat_nz
        sympy.polys.matrices.sdm.SDM.to_flat_nz
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_flat_nz
        """
        ...
    
    @classmethod
    def from_flat_nz(cls, elements, data, domain) -> DDM:
        """
        Reconstruct a :class:`DDM` after calling :meth:`to_flat_nz`.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> elements, data = A.to_flat_nz()
        >>> elements
        [1, 2, 3, 4]
        >>> A == DDM.from_flat_nz(elements, data, A.domain)
        True

        See Also
        ========

        to_flat_nz
        sympy.polys.matrices.sdm.SDM.from_flat_nz
        sympy.polys.matrices.domainmatrix.DomainMatrix.from_flat_nz
        """
        ...
    
    def to_dod(self) -> dict[Any, Any]:
        """
        Convert to a dictionary of dictionaries (dod) format.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_dod()
        {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}

        See Also
        ========

        from_dod
        sympy.polys.matrices.sdm.SDM.to_dod
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_dod
        """
        ...
    
    @classmethod
    def from_dod(cls, dod, shape, domain) -> DDM:
        """
        Create a :class:`DDM` from a dictionary of dictionaries (dod) format.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> dod = {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}
        >>> A = DDM.from_dod(dod, (2, 2), QQ)
        >>> A
        [[1, 2], [3, 4]]

        See Also
        ========

        to_dod
        sympy.polys.matrices.sdm.SDM.from_dod
        sympy.polys.matrices.domainmatrix.DomainMatrix.from_dod
        """
        ...
    
    def to_dok(self) -> dict[Any, Any]:
        """
        Convert :class:`DDM` to dictionary of keys (dok) format.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_dok()
        {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}

        See Also
        ========

        from_dok
        sympy.polys.matrices.sdm.SDM.to_dok
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_dok
        """
        ...
    
    @classmethod
    def from_dok(cls, dok, shape, domain) -> DDM:
        """
        Create a :class:`DDM` from a dictionary of keys (dok) format.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> dok = {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}
        >>> A = DDM.from_dok(dok, (2, 2), QQ)
        >>> A
        [[1, 2], [3, 4]]

        See Also
        ========

        to_dok
        sympy.polys.matrices.sdm.SDM.from_dok
        sympy.polys.matrices.domainmatrix.DomainMatrix.from_dok
        """
        ...
    
    def to_ddm(self) -> Self:
        """
        Convert to a :class:`DDM`.

        This just returns ``self`` but exists to parallel the corresponding
        method in other matrix types like :class:`~.SDM`.

        See Also
        ========

        to_sdm
        to_dfm
        to_dfm_or_ddm
        sympy.polys.matrices.sdm.SDM.to_ddm
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_ddm
        """
        ...
    
    def to_sdm(self) -> SDM:
        """
        Convert to a :class:`~.SDM`.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_sdm()
        {0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}
        >>> type(A.to_sdm())
        <class 'sympy.polys.matrices.sdm.SDM'>

        See Also
        ========

        SDM
        sympy.polys.matrices.sdm.SDM.to_ddm
        """
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm(self) -> DFM_dummy:
        """
        Convert to :class:`~.DDM` to :class:`~.DFM`.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_dfm()
        [[1, 2], [3, 4]]
        >>> type(A.to_dfm())
        <class 'sympy.polys.matrices._dfm.DFM'>

        See Also
        ========

        DFM
        sympy.polys.matrices._dfm.DFM.to_ddm
        """
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm_or_ddm(self) -> DFM_dummy | Self:
        """
        Convert to :class:`~.DFM` if possible or otherwise return self.

        Examples
        ========

        >>> from sympy.polys.matrices.ddm import DDM
        >>> from sympy import QQ
        >>> A = DDM([[1, 2], [3, 4]], (2, 2), QQ)
        >>> A.to_dfm_or_ddm()
        [[1, 2], [3, 4]]
        >>> type(A.to_dfm_or_ddm())
        <class 'sympy.polys.matrices._dfm.DFM'>

        See Also
        ========

        to_dfm
        to_ddm
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_dfm_or_ddm
        """
        ...
    
    def convert_to(self, K) -> DDM:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    @classmethod
    def zeros(cls, shape, domain) -> DDM:
        ...
    
    @classmethod
    def ones(cls, shape, domain) -> DDM:
        ...
    
    @classmethod
    def eye(cls, size, domain) -> DDM:
        ...
    
    def copy(self) -> DDM:
        ...
    
    def transpose(self) -> DDM:
        ...
    
    def __add__(a, b) -> NotImplementedType | DDM:
        ...
    
    def __sub__(a, b) -> NotImplementedType | DDM:
        ...
    
    def __neg__(a) -> DDM:
        ...
    
    def __mul__(a, b) -> DDM | NotImplementedType:
        ...
    
    def __rmul__(a, b) -> DDM | NotImplementedType:
        ...
    
    def __matmul__(a, b) -> DDM | NotImplementedType:
        ...
    
    def add(a, b) -> DDM:
        """a + b"""
        ...
    
    def sub(a, b) -> DDM:
        """a - b"""
        ...
    
    def neg(a) -> DDM:
        """-a"""
        ...
    
    def mul(a, b) -> DDM:
        ...
    
    def rmul(a, b) -> DDM:
        ...
    
    def matmul(a, b) -> DDM:
        """a @ b (matrix product)"""
        ...
    
    def mul_elementwise(a, b) -> DDM:
        ...
    
    def hstack(A, *B) -> DDM:
        """Horizontally stacks :py:class:`~.DDM` matrices.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM

        >>> A = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DDM([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.hstack(B)
        [[1, 2, 5, 6], [3, 4, 7, 8]]

        >>> C = DDM([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.hstack(B, C)
        [[1, 2, 5, 6, 9, 10], [3, 4, 7, 8, 11, 12]]
        """
        ...
    
    def vstack(A, *B) -> DDM:
        """Vertically stacks :py:class:`~.DDM` matrices.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM

        >>> A = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DDM([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.vstack(B)
        [[1, 2], [3, 4], [5, 6], [7, 8]]

        >>> C = DDM([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.vstack(B, C)
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        """
        ...
    
    def applyfunc(self, func, domain) -> DDM:
        ...
    
    def nnz(a) -> int:
        """Number of non-zero entries in :py:class:`~.DDM` matrix.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.nnz
        """
        ...
    
    def scc(a) -> list[Any]:
        """Strongly connected components of a square matrix *a*.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM
        >>> A = DDM([[ZZ(1), ZZ(0)], [ZZ(0), ZZ(1)]], (2, 2), ZZ)
        >>> A.scc()
        [[0], [1]]

        See also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.scc

        """
        ...
    
    @classmethod
    def diag(cls, values, domain) -> DDM:
        """Returns a square diagonal matrix with *values* on the diagonal.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices.sdm import DDM
        >>> DDM.diag([ZZ(1), ZZ(2), ZZ(3)], ZZ)
        [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

        See also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.diag
        """
        ...
    
    def rref(a) -> tuple[DDM, list[Any]]:
        """Reduced-row echelon form of a and list of pivots.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.rref
            Higher level interface to this function.
        sympy.polys.matrices.dense.ddm_irref
            The underlying algorithm.
        """
        ...
    
    def rref_den(a) -> tuple[DDM, Any, list[Any]]:
        """Reduced-row echelon form of a with denominator and list of pivots

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.rref_den
            Higher level interface to this function.
        sympy.polys.matrices.dense.ddm_irref_den
            The underlying algorithm.
        """
        ...
    
    def nullspace(a) -> tuple[DDM, list[int]] | tuple[DDM, list[Any]]:
        """Returns a basis for the nullspace of a.

        The domain of the matrix must be a field.

        See Also
        ========

        rref
        sympy.polys.matrices.domainmatrix.DomainMatrix.nullspace
        """
        ...
    
    def nullspace_from_rref(a, pivots=...) -> tuple[DDM, list[int]] | tuple[DDM, list[Any]]:
        """Compute the nullspace of a matrix from its rref.

        The domain of the matrix can be any domain.

        Returns a tuple (basis, nonpivots).

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.nullspace
            The higher level interface to this function.
        """
        ...
    
    def particular(a) -> DDM:
        ...
    
    def det(a):
        """Determinant of a"""
        ...
    
    def inv(a) -> DDM:
        """Inverse of a"""
        ...
    
    def lu(a) -> tuple[DDM, DDM, list[Any]]:
        """L, U decomposition of a"""
        ...
    
    def lu_solve(a, b) -> DDM:
        """x where a*x = b"""
        ...
    
    def charpoly(a) -> list[Any]:
        """Coefficients of characteristic polynomial of a"""
        ...
    
    def is_zero_matrix(self) -> bool:
        """
        Says whether this matrix has all zero entries.
        """
        ...
    
    def is_upper(self) -> bool:
        """
        Says whether this matrix is upper-triangular. True can be returned
        even if the matrix is not square.
        """
        ...
    
    def is_lower(self) -> bool:
        """
        Says whether this matrix is lower-triangular. True can be returned
        even if the matrix is not square.
        """
        ...
    
    def is_diagonal(self) -> bool:
        """
        Says whether this matrix is diagonal. True can be returned even if
        the matrix is not square.
        """
        ...
    
    def diagonal(self) -> list[Any]:
        """
        Returns a list of the elements from the diagonal of the matrix.
        """
        ...
    
    def lll(A, delta=...):
        ...
    
    def lll_transform(A, delta=...) -> tuple[Any, Any | None]:
        ...
    


