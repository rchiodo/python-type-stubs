from types import NotImplementedType
from typing import Any, Literal, Self, Tuple as tTuple, Union as tUnion
from sympy.matrices.dense import MutableDenseMatrix
from sympy.polys.matrices.domainscalar import DomainScalar
from sympy.utilities.decorator import doctest_depends_on
from sympy.polys.domains import Domain
from sympy.polys.matrices.ddm import DDM
from sympy.polys.matrices.sdm import SDM
from sympy.polys.matrices.dfm import DFM, DFM_dummy

"""

Module for the DomainMatrix class.

A DomainMatrix represents a matrix with elements that are in a particular
Domain. Each DomainMatrix internally wraps a DDM which is used for the
lower-level operations. The idea is that the DomainMatrix class provides the
convenience routines for converting between Expr and the poly domains as well
as unifying matrices with different domains.

"""
def DM(rows, domain) -> DomainMatrix:
    """Convenient alias for DomainMatrix.from_list

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DM
    >>> DM([[1, 2], [3, 4]], ZZ)
    DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

    See Also
    ========

    DomainMatrix.from_list
    """
    ...

class DomainMatrix:
    r"""
    Associate Matrix with :py:class:`~.Domain`

    Explanation
    ===========

    DomainMatrix uses :py:class:`~.Domain` for its internal representation
    which makes it faster than the SymPy Matrix class (currently) for many
    common operations, but this advantage makes it not entirely compatible
    with Matrix. DomainMatrix are analogous to numpy arrays with "dtype".
    In the DomainMatrix, each element has a domain such as :ref:`ZZ`
    or  :ref:`QQ(a)`.


    Examples
    ========

    Creating a DomainMatrix from the existing Matrix class:

    >>> from sympy import Matrix
    >>> from sympy.polys.matrices import DomainMatrix
    >>> Matrix1 = Matrix([
    ...    [1, 2],
    ...    [3, 4]])
    >>> A = DomainMatrix.from_Matrix(Matrix1)
    >>> A
    DomainMatrix({0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}, (2, 2), ZZ)

    Directly forming a DomainMatrix:

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DomainMatrix
    >>> A = DomainMatrix([
    ...    [ZZ(1), ZZ(2)],
    ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
    >>> A
    DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

    See Also
    ========

    DDM
    SDM
    Domain
    Poly

    """
    rep: tUnion[SDM, DDM, Any]
    shape: tTuple[int, int]
    domain: Domain
    def __new__(cls, rows, shape, domain, *, fmt=...) -> Self:
        """
        Creates a :py:class:`~.DomainMatrix`.

        Parameters
        ==========

        rows : Represents elements of DomainMatrix as list of lists
        shape : Represents dimension of DomainMatrix
        domain : Represents :py:class:`~.Domain` of DomainMatrix

        Raises
        ======

        TypeError
            If any of rows, shape and domain are not provided

        """
        ...
    
    def __reduce__(self) -> tuple[type[Self], tuple[list[Any] | Any | dict[Any, Any], Any | tuple[Any, Any], Any]]:
        ...
    
    def __getitem__(self, key) -> DomainScalar | Self:
        ...
    
    def getitem_sympy(self, i, j):
        ...
    
    def extract(self, rowslist, colslist) -> Self:
        ...
    
    def __setitem__(self, key, value) -> None:
        ...
    
    @classmethod
    def from_rep(cls, rep) -> Self:
        """Create a new DomainMatrix efficiently from DDM/SDM.

        Examples
        ========

        Create a :py:class:`~.DomainMatrix` with an dense internal
        representation as :py:class:`~.DDM`:

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.polys.matrices.ddm import DDM
        >>> drep = DDM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> dM = DomainMatrix.from_rep(drep)
        >>> dM
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

        Create a :py:class:`~.DomainMatrix` with a sparse internal
        representation as :py:class:`~.SDM`:

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.polys.matrices.sdm import SDM
        >>> from sympy import ZZ
        >>> drep = SDM({0:{1:ZZ(1)},1:{0:ZZ(2)}}, (2, 2), ZZ)
        >>> dM = DomainMatrix.from_rep(drep)
        >>> dM
        DomainMatrix({0: {1: 1}, 1: {0: 2}}, (2, 2), ZZ)

        Parameters
        ==========

        rep: SDM or DDM
            The internal sparse or dense representation of the matrix.

        Returns
        =======

        DomainMatrix
            A :py:class:`~.DomainMatrix` wrapping *rep*.

        Notes
        =====

        This takes ownership of rep as its internal representation. If rep is
        being mutated elsewhere then a copy should be provided to
        ``from_rep``. Only minimal verification or checking is done on *rep*
        as this is supposed to be an efficient internal routine.

        """
        ...
    
    @classmethod
    @doctest_depends_on(ground_types=['python', 'gmpy'])
    def from_list(cls, rows, domain) -> DomainMatrix:
        r"""
        Convert a list of lists into a DomainMatrix

        Parameters
        ==========

        rows: list of lists
            Each element of the inner lists should be either the single arg,
            or tuple of args, that would be passed to the domain constructor
            in order to form an element of the domain. See examples.

        Returns
        =======

        DomainMatrix containing elements defined in rows

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import FF, QQ, ZZ
        >>> A = DomainMatrix.from_list([[1, 0, 1], [0, 0, 1]], ZZ)
        >>> A
        DomainMatrix([[1, 0, 1], [0, 0, 1]], (2, 3), ZZ)
        >>> B = DomainMatrix.from_list([[1, 0, 1], [0, 0, 1]], FF(7))
        >>> B
        DomainMatrix([[1 mod 7, 0 mod 7, 1 mod 7], [0 mod 7, 0 mod 7, 1 mod 7]], (2, 3), GF(7))
        >>> C = DomainMatrix.from_list([[(1, 2), (3, 1)], [(1, 4), (5, 1)]], QQ)
        >>> C
        DomainMatrix([[1/2, 3], [1/4, 5]], (2, 2), QQ)

        See Also
        ========

        from_list_sympy

        """
        ...
    
    @classmethod
    def from_list_sympy(cls, nrows, ncols, rows, **kwargs) -> DomainMatrix:
        r"""
        Convert a list of lists of Expr into a DomainMatrix using construct_domain

        Parameters
        ==========

        nrows: number of rows
        ncols: number of columns
        rows: list of lists

        Returns
        =======

        DomainMatrix containing elements of rows

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.abc import x, y, z
        >>> A = DomainMatrix.from_list_sympy(1, 3, [[x, y, z]])
        >>> A
        DomainMatrix([[x, y, z]], (1, 3), ZZ[x,y,z])

        See Also
        ========

        sympy.polys.constructor.construct_domain, from_dict_sympy

        """
        ...
    
    @classmethod
    def from_dict_sympy(cls, nrows, ncols, elemsdict, **kwargs) -> DomainMatrix:
        """

        Parameters
        ==========

        nrows: number of rows
        ncols: number of cols
        elemsdict: dict of dicts containing non-zero elements of the DomainMatrix

        Returns
        =======

        DomainMatrix containing elements of elemsdict

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.abc import x,y,z
        >>> elemsdict = {0: {0:x}, 1:{1: y}, 2: {2: z}}
        >>> A = DomainMatrix.from_dict_sympy(3, 3, elemsdict)
        >>> A
        DomainMatrix({0: {0: x}, 1: {1: y}, 2: {2: z}}, (3, 3), ZZ[x,y,z])

        See Also
        ========

        from_list_sympy

        """
        ...
    
    @classmethod
    def from_Matrix(cls, M, fmt=..., **kwargs):
        r"""
        Convert Matrix to DomainMatrix

        Parameters
        ==========

        M: Matrix

        Returns
        =======

        Returns DomainMatrix with identical elements as M

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.polys.matrices import DomainMatrix
        >>> M = Matrix([
        ...    [1.0, 3.4],
        ...    [2.4, 1]])
        >>> A = DomainMatrix.from_Matrix(M)
        >>> A
        DomainMatrix({0: {0: 1.0, 1: 3.4}, 1: {0: 2.4, 1: 1.0}}, (2, 2), RR)

        We can keep internal representation as ddm using fmt='dense'
        >>> from sympy import Matrix, QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix.from_Matrix(Matrix([[QQ(1, 2), QQ(3, 4)], [QQ(0, 1), QQ(0, 1)]]), fmt='dense')
        >>> A.rep
        [[1/2, 3/4], [0, 0]]

        See Also
        ========

        Matrix

        """
        ...
    
    @classmethod
    def get_domain(cls, items_sympy, **kwargs) -> tuple[Any, Any]:
        ...
    
    def choose_domain(self, **opts) -> Self:
        """Convert to a domain found by :func:`~.construct_domain`.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> M = DM([[1, 2], [3, 4]], ZZ)
        >>> M
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)
        >>> M.choose_domain(field=True)
        DomainMatrix([[1, 2], [3, 4]], (2, 2), QQ)

        >>> from sympy.abc import x
        >>> M = DM([[1, x], [x**2, x**3]], ZZ[x])
        >>> M.choose_domain(field=True).domain
        ZZ(x)

        Keyword arguments are passed to :func:`~.construct_domain`.

        See Also
        ========

        construct_domain
        convert_to
        """
        ...
    
    def copy(self) -> Self:
        ...
    
    def convert_to(self, K) -> Self:
        r"""
        Change the domain of DomainMatrix to desired domain or field

        Parameters
        ==========

        K : Represents the desired domain or field.
            Alternatively, ``None`` may be passed, in which case this method
            just returns a copy of this DomainMatrix.

        Returns
        =======

        DomainMatrix
            DomainMatrix with the desired domain or field

        Examples
        ========

        >>> from sympy import ZZ, ZZ_I
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.convert_to(ZZ_I)
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ_I)

        """
        ...
    
    def to_sympy(self) -> Self:
        ...
    
    def to_field(self) -> Self:
        r"""
        Returns a DomainMatrix with the appropriate field

        Returns
        =======

        DomainMatrix
            DomainMatrix with the appropriate field

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.to_field()
        DomainMatrix([[1, 2], [3, 4]], (2, 2), QQ)

        """
        ...
    
    def to_sparse(self) -> Self:
        """
        Return a sparse DomainMatrix representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix([[1, 0],[0, 2]], (2, 2), QQ)
        >>> A.rep
        [[1, 0], [0, 2]]
        >>> B = A.to_sparse()
        >>> B.rep
        {0: {0: 1}, 1: {1: 2}}
        """
        ...
    
    def to_dense(self) -> Self:
        """
        Return a dense DomainMatrix representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix({0: {0: 1}, 1: {1: 2}}, (2, 2), QQ)
        >>> A.rep
        {0: {0: 1}, 1: {1: 2}}
        >>> B = A.to_dense()
        >>> B.rep
        [[1, 0], [0, 2]]

        """
        ...
    
    def to_ddm(self) -> DDM:
        """
        Return a :class:`~.DDM` representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix({0: {0: 1}, 1: {1: 2}}, (2, 2), QQ)
        >>> ddm = A.to_ddm()
        >>> ddm
        [[1, 0], [0, 2]]
        >>> type(ddm)
        <class 'sympy.polys.matrices.ddm.DDM'>

        See Also
        ========

        to_sdm
        to_dense
        sympy.polys.matrices.ddm.DDM.to_sdm
        """
        ...
    
    def to_sdm(self) -> SDM:
        """
        Return a :class:`~.SDM` representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix([[1, 0],[0, 2]], (2, 2), QQ)
        >>> sdm = A.to_sdm()
        >>> sdm
        {0: {0: 1}, 1: {1: 2}}
        >>> type(sdm)
        <class 'sympy.polys.matrices.sdm.SDM'>

        See Also
        ========

        to_ddm
        to_sparse
        sympy.polys.matrices.sdm.SDM.to_ddm
        """
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm(self) -> DFM_dummy:
        """
        Return a :class:`~.DFM` representation of *self*.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix([[1, 0],[0, 2]], (2, 2), QQ)
        >>> dfm = A.to_dfm()
        >>> dfm
        [[1, 0], [0, 2]]
        >>> type(dfm)
        <class 'sympy.polys.matrices._dfm.DFM'>

        See Also
        ========

        to_ddm
        to_dense
        DFM
        """
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm_or_ddm(self) -> DFM_dummy | DDM:
        """
        Return a :class:`~.DFM` or :class:`~.DDM` representation of *self*.

        Explanation
        ===========

        The :class:`~.DFM` representation can only be used if the ground types
        are ``flint`` and the ground domain is supported by ``python-flint``.
        This method will return a :class:`~.DFM` representation if possible,
        but will return a :class:`~.DDM` representation otherwise.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> A = DomainMatrix([[1, 0],[0, 2]], (2, 2), QQ)
        >>> dfm = A.to_dfm_or_ddm()
        >>> dfm
        [[1, 0], [0, 2]]
        >>> type(dfm)  # Depends on the ground domain and ground types
        <class 'sympy.polys.matrices._dfm.DFM'>

        See Also
        ========

        to_ddm: Always return a :class:`~.DDM` representation.
        to_dfm: Returns a :class:`~.DFM` representation or raise an error.
        to_dense: Convert internally to a :class:`~.DFM` or :class:`~.DDM`
        DFM: The :class:`~.DFM` dense FLINT matrix representation.
        DDM: The Python :class:`~.DDM` dense domain matrix representation.
        """
        ...
    
    def unify(self, *others, fmt=...) -> tuple[Any, ...]:
        """
        Unifies the domains and the format of self and other
        matrices.

        Parameters
        ==========

        others : DomainMatrix

        fmt: string 'dense', 'sparse' or `None` (default)
            The preferred format to convert to if self and other are not
            already in the same format. If `None` or not specified then no
            conversion if performed.

        Returns
        =======

        Tuple[DomainMatrix]
            Matrices with unified domain and format

        Examples
        ========

        Unify the domain of DomainMatrix that have different domains:

        >>> from sympy import ZZ, QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([[ZZ(1), ZZ(2)]], (1, 2), ZZ)
        >>> B = DomainMatrix([[QQ(1, 2), QQ(2)]], (1, 2), QQ)
        >>> Aq, Bq = A.unify(B)
        >>> Aq
        DomainMatrix([[1, 2]], (1, 2), QQ)
        >>> Bq
        DomainMatrix([[1/2, 2]], (1, 2), QQ)

        Unify the format (dense or sparse):

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)]], (1, 2), ZZ)
        >>> B = DomainMatrix({0:{0: ZZ(1)}}, (2, 2), ZZ)
        >>> B.rep
        {0: {0: 1}}

        >>> A2, B2 = A.unify(B, fmt='dense')
        >>> B2.rep
        [[1, 0], [0, 0]]

        See Also
        ========

        convert_to, to_dense, to_sparse

        """
        ...
    
    def to_Matrix(self) -> MutableDenseMatrix:
        r"""
        Convert DomainMatrix to Matrix

        Returns
        =======

        Matrix
            MutableDenseMatrix for the DomainMatrix

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.to_Matrix()
        Matrix([
            [1, 2],
            [3, 4]])

        See Also
        ========

        from_Matrix

        """
        ...
    
    def to_list(self) -> list[Any]:
        """
        Convert :class:`DomainMatrix` to list of lists.

        See Also
        ========

        from_list
        to_list_flat
        to_flat_nz
        to_dok
        """
        ...
    
    def to_list_flat(self) -> list[Any]:
        """
        Convert :class:`DomainMatrix` to flat list.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> A.to_list_flat()
        [1, 2, 3, 4]

        See Also
        ========

        from_list_flat
        to_list
        to_flat_nz
        to_dok
        """
        ...
    
    @classmethod
    def from_list_flat(cls, elements, shape, domain) -> Self:
        """
        Create :class:`DomainMatrix` from flat list.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> element_list = [ZZ(1), ZZ(2), ZZ(3), ZZ(4)]
        >>> A = DomainMatrix.from_list_flat(element_list, (2, 2), ZZ)
        >>> A
        DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)
        >>> A == A.from_list_flat(A.to_list_flat(), A.shape, A.domain)
        True

        See Also
        ========

        to_list_flat
        """
        ...
    
    def to_flat_nz(self) -> tuple[list[Any], tuple[tuple[tuple[Any, Any], ...], Any]]:
        """
        Convert :class:`DomainMatrix` to list of nonzero elements and data.

        Explanation
        ===========

        Returns a tuple ``(elements, data)`` where ``elements`` is a list of
        elements of the matrix with zeros possibly excluded. The matrix can be
        reconstructed by passing these to :meth:`from_flat_nz`. The idea is to
        be able to modify a flat list of the elements and then create a new
        matrix of the same shape with the modified elements in the same
        positions.

        The format of ``data`` differs depending on whether the underlying
        representation is dense or sparse but either way it represents the
        positions of the elements in the list in a way that
        :meth:`from_flat_nz` can use to reconstruct the matrix. The
        :meth:`from_flat_nz` method should be called on the same
        :class:`DomainMatrix` that was used to call :meth:`to_flat_nz`.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> elements, data = A.to_flat_nz()
        >>> elements
        [1, 2, 3, 4]
        >>> A == A.from_flat_nz(elements, data, A.domain)
        True

        Create a matrix with the elements doubled:

        >>> elements_doubled = [2*x for x in elements]
        >>> A2 = A.from_flat_nz(elements_doubled, data, A.domain)
        >>> A2 == 2*A
        True

        See Also
        ========

        from_flat_nz
        """
        ...
    
    def from_flat_nz(self, elements, data, domain) -> Self:
        """
        Reconstruct :class:`DomainMatrix` after calling :meth:`to_flat_nz`.

        See :meth:`to_flat_nz` for explanation.

        See Also
        ========

        to_flat_nz
        """
        ...
    
    def to_dod(self) -> dict[Any, Any]:
        """
        Convert :class:`DomainMatrix` to dictionary of dictionaries (dod) format.

        Explanation
        ===========

        Returns a dictionary of dictionaries representing the matrix.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[ZZ(1), ZZ(2), ZZ(0)], [ZZ(3), ZZ(0), ZZ(4)]], ZZ)
        >>> A.to_dod()
        {0: {0: 1, 1: 2}, 1: {0: 3, 2: 4}}
        >>> A.to_sparse() == A.from_dod(A.to_dod(), A.shape, A.domain)
        True
        >>> A == A.from_dod_like(A.to_dod())
        True

        See Also
        ========

        from_dod
        from_dod_like
        to_dok
        to_list
        to_list_flat
        to_flat_nz
        sympy.matrices.matrixbase.MatrixBase.todod
        """
        ...
    
    @classmethod
    def from_dod(cls, dod, shape, domain) -> Self:
        """
        Create sparse :class:`DomainMatrix` from dict of dict (dod) format.

        See :meth:`to_dod` for explanation.

        See Also
        ========

        to_dod
        from_dod_like
        """
        ...
    
    def from_dod_like(self, dod, domain=...) -> Self:
        """
        Create :class:`DomainMatrix` like ``self`` from dict of dict (dod) format.

        See :meth:`to_dod` for explanation.

        See Also
        ========

        to_dod
        from_dod
        """
        ...
    
    def to_dok(self) -> dict[tuple[Any, Any], Any] | dict[Any, Any]:
        """
        Convert :class:`DomainMatrix` to dictionary of keys (dok) format.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(0)],
        ...    [ZZ(0), ZZ(4)]], (2, 2), ZZ)
        >>> A.to_dok()
        {(0, 0): 1, (1, 1): 4}

        The matrix can be reconstructed by calling :meth:`from_dok` although
        the reconstructed matrix will always be in sparse format:

        >>> A.to_sparse() == A.from_dok(A.to_dok(), A.shape, A.domain)
        True

        See Also
        ========

        from_dok
        to_list
        to_list_flat
        to_flat_nz
        """
        ...
    
    @classmethod
    def from_dok(cls, dok, shape, domain) -> Self:
        """
        Create :class:`DomainMatrix` from dictionary of keys (dok) format.

        See :meth:`to_dok` for explanation.

        See Also
        ========

        to_dok
        """
        ...
    
    def nnz(self) -> int:
        """
        Number of nonzero elements in the matrix.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[1, 0], [0, 4]], ZZ)
        >>> A.nnz()
        2
        """
        ...
    
    def __repr__(self) -> str:
        ...
    
    def transpose(self) -> Self:
        """Matrix transpose of ``self``"""
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    @property
    def is_zero_matrix(self) -> bool:
        ...
    
    @property
    def is_upper(self) -> bool:
        """
        Says whether this matrix is upper-triangular. True can be returned
        even if the matrix is not square.
        """
        ...
    
    @property
    def is_lower(self) -> bool:
        """
        Says whether this matrix is lower-triangular. True can be returned
        even if the matrix is not square.
        """
        ...
    
    @property
    def is_diagonal(self) -> bool:
        """
        True if the matrix is diagonal.

        Can return true for non-square matrices. A matrix is diagonal if
        ``M[i,j] == 0`` whenever ``i != j``.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> M = DM([[ZZ(1), ZZ(0)], [ZZ(0), ZZ(1)]], ZZ)
        >>> M.is_diagonal
        True

        See Also
        ========

        is_upper
        is_lower
        is_square
        diagonal
        """
        ...
    
    def diagonal(self) -> list[Any]:
        """
        Get the diagonal entries of the matrix as a list.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> M = DM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], ZZ)
        >>> M.diagonal()
        [1, 4]

        See Also
        ========

        is_diagonal
        diag
        """
        ...
    
    @property
    def is_square(self) -> bool:
        """
        True if the matrix is square.
        """
        ...
    
    def rank(self) -> int:
        ...
    
    def hstack(A, *B) -> DomainMatrix:
        r"""Horizontally stack the given matrices.

        Parameters
        ==========

        B: DomainMatrix
            Matrices to stack horizontally.

        Returns
        =======

        DomainMatrix
            DomainMatrix by stacking horizontally.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.hstack(B)
        DomainMatrix([[1, 2, 5, 6], [3, 4, 7, 8]], (2, 4), ZZ)

        >>> C = DomainMatrix([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.hstack(B, C)
        DomainMatrix([[1, 2, 5, 6, 9, 10], [3, 4, 7, 8, 11, 12]], (2, 6), ZZ)

        See Also
        ========

        unify
        """
        ...
    
    def vstack(A, *B) -> DomainMatrix:
        r"""Vertically stack the given matrices.

        Parameters
        ==========

        B: DomainMatrix
            Matrices to stack vertically.

        Returns
        =======

        DomainMatrix
            DomainMatrix by stacking vertically.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix

        >>> A = DomainMatrix([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([[ZZ(5), ZZ(6)], [ZZ(7), ZZ(8)]], (2, 2), ZZ)
        >>> A.vstack(B)
        DomainMatrix([[1, 2], [3, 4], [5, 6], [7, 8]], (4, 2), ZZ)

        >>> C = DomainMatrix([[ZZ(9), ZZ(10)], [ZZ(11), ZZ(12)]], (2, 2), ZZ)
        >>> A.vstack(B, C)
        DomainMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]], (6, 2), ZZ)

        See Also
        ========

        unify
        """
        ...
    
    def applyfunc(self, func, domain=...) -> Self:
        ...
    
    def __add__(A, B) -> NotImplementedType:
        ...
    
    def __sub__(A, B) -> NotImplementedType:
        ...
    
    def __neg__(A) -> Self:
        ...
    
    def __mul__(A, B) -> DomainMatrix | Self | NotImplementedType:
        """A * B"""
        ...
    
    def __rmul__(A, B) -> DomainMatrix | Self | NotImplementedType:
        ...
    
    def __pow__(A, n) -> NotImplementedType | Self:
        """A ** n"""
        ...
    
    def add(A, B) -> Self:
        r"""
        Adds two DomainMatrix matrices of the same Domain

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to add

        Returns
        =======

        DomainMatrix
            DomainMatrix after Addition

        Raises
        ======

        DMShapeError
            If the dimensions of the two DomainMatrix are not equal

        ValueError
            If the domain of the two DomainMatrix are not same

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(4), ZZ(3)],
        ...    [ZZ(2), ZZ(1)]], (2, 2), ZZ)

        >>> A.add(B)
        DomainMatrix([[5, 5], [5, 5]], (2, 2), ZZ)

        See Also
        ========

        sub, matmul

        """
        ...
    
    def sub(A, B) -> Self:
        r"""
        Subtracts two DomainMatrix matrices of the same Domain

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to subtract

        Returns
        =======

        DomainMatrix
            DomainMatrix after Subtraction

        Raises
        ======

        DMShapeError
            If the dimensions of the two DomainMatrix are not equal

        ValueError
            If the domain of the two DomainMatrix are not same

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(4), ZZ(3)],
        ...    [ZZ(2), ZZ(1)]], (2, 2), ZZ)

        >>> A.sub(B)
        DomainMatrix([[-3, -1], [1, 3]], (2, 2), ZZ)

        See Also
        ========

        add, matmul

        """
        ...
    
    def neg(A) -> Self:
        r"""
        Returns the negative of DomainMatrix

        Parameters
        ==========

        A : Represents a DomainMatrix

        Returns
        =======

        DomainMatrix
            DomainMatrix after Negation

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.neg()
        DomainMatrix([[-1, -2], [-3, -4]], (2, 2), ZZ)

        """
        ...
    
    def mul(A, b) -> Self:
        r"""
        Performs term by term multiplication for the second DomainMatrix
        w.r.t first DomainMatrix. Returns a DomainMatrix whose rows are
        list of DomainMatrix matrices created after term by term multiplication.

        Parameters
        ==========

        A, B: DomainMatrix
            matrices to multiply term-wise

        Returns
        =======

        DomainMatrix
            DomainMatrix after term by term multiplication

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> b = ZZ(2)

        >>> A.mul(b)
        DomainMatrix([[2, 4], [6, 8]], (2, 2), ZZ)

        See Also
        ========

        matmul

        """
        ...
    
    def rmul(A, b) -> Self:
        ...
    
    def matmul(A, B) -> Self:
        r"""
        Performs matrix multiplication of two DomainMatrix matrices

        Parameters
        ==========

        A, B: DomainMatrix
            to multiply

        Returns
        =======

        DomainMatrix
            DomainMatrix after multiplication

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)

        >>> A.matmul(B)
        DomainMatrix([[1, 3], [3, 7]], (2, 2), ZZ)

        See Also
        ========

        mul, pow, add, sub

        """
        ...
    
    def scalarmul(A, lamda) -> DomainMatrix | Self:
        ...
    
    def rscalarmul(A, lamda) -> DomainMatrix | Self:
        ...
    
    def mul_elementwise(A, B) -> Self:
        ...
    
    def __truediv__(A, lamda) -> NotImplementedType:
        """ Method for Scalar Division"""
        ...
    
    def pow(A, n) -> Self:
        r"""
        Computes A**n

        Parameters
        ==========

        A : DomainMatrix

        n : exponent for A

        Returns
        =======

        DomainMatrix
            DomainMatrix on computing A**n

        Raises
        ======

        NotImplementedError
            if n is negative.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)

        >>> A.pow(2)
        DomainMatrix([[1, 2], [0, 1]], (2, 2), ZZ)

        See Also
        ========

        matmul

        """
        ...
    
    def scc(self) -> list[Any]:
        """Compute the strongly connected components of a DomainMatrix

        Explanation
        ===========

        A square matrix can be considered as the adjacency matrix for a
        directed graph where the row and column indices are the vertices. In
        this graph if there is an edge from vertex ``i`` to vertex ``j`` if
        ``M[i, j]`` is nonzero. This routine computes the strongly connected
        components of that graph which are subsets of the rows and columns that
        are connected by some nonzero element of the matrix. The strongly
        connected components are useful because many operations such as the
        determinant can be computed by working with the submatrices
        corresponding to each component.

        Examples
        ========

        Find the strongly connected components of a matrix:

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> M = DomainMatrix([[ZZ(1), ZZ(0), ZZ(2)],
        ...                   [ZZ(0), ZZ(3), ZZ(0)],
        ...                   [ZZ(4), ZZ(6), ZZ(5)]], (3, 3), ZZ)
        >>> M.scc()
        [[1], [0, 2]]

        Compute the determinant from the components:

        >>> MM = M.to_Matrix()
        >>> MM
        Matrix([
        [1, 0, 2],
        [0, 3, 0],
        [4, 6, 5]])
        >>> MM[[1], [1]]
        Matrix([[3]])
        >>> MM[[0, 2], [0, 2]]
        Matrix([
        [1, 2],
        [4, 5]])
        >>> MM.det()
        -9
        >>> MM[[1], [1]].det() * MM[[0, 2], [0, 2]].det()
        -9

        The components are given in reverse topological order and represent a
        permutation of the rows and columns that will bring the matrix into
        block lower-triangular form:

        >>> MM[[1, 0, 2], [1, 0, 2]]
        Matrix([
        [3, 0, 0],
        [0, 1, 2],
        [6, 4, 5]])

        Returns
        =======

        List of lists of integers
            Each list represents a strongly connected component.

        See also
        ========

        sympy.matrices.matrixbase.MatrixBase.strongly_connected_components
        sympy.utilities.iterables.strongly_connected_components

        """
        ...
    
    def clear_denoms(self, convert=...) -> tuple[DomainScalar, Self]:
        """
        Clear denominators, but keep the domain unchanged.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[(1,2), (1,3)], [(1,4), (1,5)]], QQ)
        >>> den, Anum = A.clear_denoms()
        >>> den.to_sympy()
        60
        >>> Anum.to_Matrix()
        Matrix([
        [30, 20],
        [15, 12]])
        >>> den * A == Anum
        True

        The numerator matrix will be in the same domain as the original matrix
        unless ``convert`` is set to ``True``:

        >>> A.clear_denoms()[1].domain
        QQ
        >>> A.clear_denoms(convert=True)[1].domain
        ZZ

        The denominator is always in the associated ring:

        >>> A.clear_denoms()[0].domain
        ZZ
        >>> A.domain.get_ring()
        ZZ

        See Also
        ========

        sympy.polys.polytools.Poly.clear_denoms
        clear_denoms_rowwise
        """
        ...
    
    def clear_denoms_rowwise(self, convert=...) -> tuple[Self, Self]:
        """
        Clear denominators from each row of the matrix.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[(1,2), (1,3), (1,4)], [(1,5), (1,6), (1,7)]], QQ)
        >>> den, Anum = A.clear_denoms_rowwise()
        >>> den.to_Matrix()
        Matrix([
        [12,   0],
        [ 0, 210]])
        >>> Anum.to_Matrix()
        Matrix([
        [ 6,  4,  3],
        [42, 35, 30]])

        The denominator matrix is a diagonal matrix with the denominators of
        each row on the diagonal. The invariants are:

        >>> den * A == Anum
        True
        >>> A == den.to_field().inv() * Anum
        True

        The numerator matrix will be in the same domain as the original matrix
        unless ``convert`` is set to ``True``:

        >>> A.clear_denoms_rowwise()[1].domain
        QQ
        >>> A.clear_denoms_rowwise(convert=True)[1].domain
        ZZ

        The domain of the denominator matrix is the associated ring:

        >>> A.clear_denoms_rowwise()[0].domain
        ZZ

        See Also
        ========

        sympy.polys.polytools.Poly.clear_denoms
        clear_denoms
        """
        ...
    
    def cancel_denom(self, denom) -> tuple[Self, Any]:
        """
        Cancel factors between a matrix and a denominator.

        Returns a matrix and denominator on lowest terms.

        Requires ``gcd`` in the ground domain.

        Methods like :meth:`solve_den`, :meth:`inv_den` and :meth:`rref_den`
        return a matrix and denominator but not necessarily on lowest terms.
        Reduction to lowest terms without fractions can be performed with
        :meth:`cancel_denom`.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[2, 2, 0],
        ...         [0, 2, 2],
        ...         [0, 0, 2]], ZZ)
        >>> Minv, den = M.inv_den()
        >>> Minv.to_Matrix()
        Matrix([
        [1, -1,  1],
        [0,  1, -1],
        [0,  0,  1]])
        >>> den
        2
        >>> Minv_reduced, den_reduced = Minv.cancel_denom(den)
        >>> Minv_reduced.to_Matrix()
        Matrix([
        [1, -1,  1],
        [0,  1, -1],
        [0,  0,  1]])
        >>> den_reduced
        2
        >>> Minv_reduced.to_field() / den_reduced == Minv.to_field() / den
        True

        The denominator is made canonical with respect to units (e.g. a
        negative denominator is made positive):

        >>> M = DM([[2, 2, 0]], ZZ)
        >>> den = ZZ(-4)
        >>> M.cancel_denom(den)
        (DomainMatrix([[-1, -1, 0]], (1, 3), ZZ), 2)

        Any factor common to _all_ elements will be cancelled but there can
        still be factors in common between _some_ elements of the matrix and
        the denominator. To cancel factors between each element and the
        denominator, use :meth:`cancel_denom_elementwise` or otherwise convert
        to a field and use division:

        >>> M = DM([[4, 6]], ZZ)
        >>> den = ZZ(12)
        >>> M.cancel_denom(den)
        (DomainMatrix([[2, 3]], (1, 2), ZZ), 6)
        >>> numers, denoms = M.cancel_denom_elementwise(den)
        >>> numers
        DomainMatrix([[1, 1]], (1, 2), ZZ)
        >>> denoms
        DomainMatrix([[3, 2]], (1, 2), ZZ)
        >>> M.to_field() / den
        DomainMatrix([[1/3, 1/2]], (1, 2), QQ)

        See Also
        ========

        solve_den
        inv_den
        rref_den
        cancel_denom_elementwise
        """
        ...
    
    def cancel_denom_elementwise(self, denom) -> tuple[Self, Self]:
        """
        Cancel factors between the elements of a matrix and a denominator.

        Returns a matrix of numerators and matrix of denominators.

        Requires ``gcd`` in the ground domain.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[2, 3], [4, 12]], ZZ)
        >>> denom = ZZ(6)
        >>> numers, denoms = M.cancel_denom_elementwise(denom)
        >>> numers.to_Matrix()
        Matrix([
        [1, 1],
        [2, 2]])
        >>> denoms.to_Matrix()
        Matrix([
        [3, 2],
        [3, 1]])
        >>> M_frac = (M.to_field() / denom).to_Matrix()
        >>> M_frac
        Matrix([
        [1/3, 1/2],
        [2/3,   2]])
        >>> denoms_inverted = denoms.to_Matrix().applyfunc(lambda e: 1/e)
        >>> numers.to_Matrix().multiply_elementwise(denoms_inverted) == M_frac
        True

        Use :meth:`cancel_denom` to cancel factors between the matrix and the
        denominator while preserving the form of a matrix with a scalar
        denominator.

        See Also
        ========

        cancel_denom
        """
        ...
    
    def content(self):
        """
        Return the gcd of the elements of the matrix.

        Requires ``gcd`` in the ground domain.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[2, 4], [4, 12]], ZZ)
        >>> M.content()
        2

        See Also
        ========

        primitive
        cancel_denom
        """
        ...
    
    def primitive(self) -> tuple[Any, Self]:
        """
        Factor out gcd of the elements of a matrix.

        Requires ``gcd`` in the ground domain.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[2, 4], [4, 12]], ZZ)
        >>> content, M_primitive = M.primitive()
        >>> content
        2
        >>> M_primitive
        DomainMatrix([[1, 2], [2, 6]], (2, 2), ZZ)
        >>> content * M_primitive == M
        True
        >>> M_primitive.content() == ZZ(1)
        True

        See Also
        ========

        content
        cancel_denom
        """
        ...
    
    def rref(self, *, method=...) -> tuple[Any, tuple[Any, ...]]:
        r"""
        Returns reduced-row echelon form (RREF) and list of pivots.

        If the domain is not a field then it will be converted to a field. See
        :meth:`rref_den` for the fraction-free version of this routine that
        returns RREF with denominator instead.

        The domain must either be a field or have an associated fraction field
        (see :meth:`to_field`).

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [QQ(2), QQ(-1), QQ(0)],
        ...     [QQ(-1), QQ(2), QQ(-1)],
        ...     [QQ(0), QQ(0), QQ(2)]], (3, 3), QQ)

        >>> rref_matrix, rref_pivots = A.rref()
        >>> rref_matrix
        DomainMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], (3, 3), QQ)
        >>> rref_pivots
        (0, 1, 2)

        Parameters
        ==========

        method : str, optional (default: 'auto')
            The method to use to compute the RREF. The default is ``'auto'``,
            which will attempt to choose the fastest method. The other options
            are:

            - ``A.rref(method='GJ')`` uses Gauss-Jordan elimination with
              division. If the domain is not a field then it will be converted
              to a field with :meth:`to_field` first and RREF will be computed
              by inverting the pivot elements in each row. This is most
              efficient for very sparse matrices or for matrices whose elements
              have complex denominators.

            - ``A.rref(method='FF')`` uses fraction-free Gauss-Jordan
              elimination. Elimination is performed using exact division
              (``exquo``) to control the growth of the coefficients. In this
              case the current domain is always used for elimination but if
              the domain is not a field then it will be converted to a field
              at the end and divided by the denominator. This is most efficient
              for dense matrices or for matrices with simple denominators.

            - ``A.rref(method='CD')`` clears the denominators before using
              fraction-free Gauss-Jordan elimination in the assoicated ring.
              This is most efficient for dense matrices with very simple
              denominators.

            - ``A.rref(method='GJ_dense')``, ``A.rref(method='FF_dense')``, and
              ``A.rref(method='CD_dense')`` are the same as the above methods
              except that the dense implementations of the algorithms are used.
              By default ``A.rref(method='auto')`` will usually choose the
              sparse implementations for RREF.

            Regardless of which algorithm is used the returned matrix will
            always have the same format (sparse or dense) as the input and its
            domain will always be the field of fractions of the input domain.

        Returns
        =======

        (DomainMatrix, list)
            reduced-row echelon form and list of pivots for the DomainMatrix

        See Also
        ========

        rref_den
            RREF with denominator
        sympy.polys.matrices.sdm.sdm_irref
            Sparse implementation of ``method='GJ'``.
        sympy.polys.matrices.sdm.sdm_rref_den
            Sparse implementation of ``method='FF'`` and ``method='CD'``.
        sympy.polys.matrices.dense.ddm_irref
            Dense implementation of ``method='GJ'``.
        sympy.polys.matrices.dense.ddm_irref_den
            Dense implementation of ``method='FF'`` and ``method='CD'``.
        clear_denoms
            Clear denominators from a matrix, used by ``method='CD'`` and
            by ``method='GJ'`` when the original domain is not a field.

        """
        ...
    
    def rref_den(self, *, method=..., keep_domain=...) -> tuple[Any, Any, tuple[Any, ...]]:
        r"""
        Returns reduced-row echelon form with denominator and list of pivots.

        Requires exact division in the ground domain (``exquo``).

        Examples
        ========

        >>> from sympy import ZZ, QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [ZZ(2), ZZ(-1), ZZ(0)],
        ...     [ZZ(-1), ZZ(2), ZZ(-1)],
        ...     [ZZ(0), ZZ(0), ZZ(2)]], (3, 3), ZZ)

        >>> A_rref, denom, pivots = A.rref_den()
        >>> A_rref
        DomainMatrix([[6, 0, 0], [0, 6, 0], [0, 0, 6]], (3, 3), ZZ)
        >>> denom
        6
        >>> pivots
        (0, 1, 2)
        >>> A_rref.to_field() / denom
        DomainMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], (3, 3), QQ)
        >>> A_rref.to_field() / denom == A.convert_to(QQ).rref()[0]
        True

        Parameters
        ==========

        method : str, optional (default: 'auto')
            The method to use to compute the RREF. The default is ``'auto'``,
            which will attempt to choose the fastest method. The other options
            are:

            - ``A.rref(method='FF')`` uses fraction-free Gauss-Jordan
              elimination. Elimination is performed using exact division
              (``exquo``) to control the growth of the coefficients. In this
              case the current domain is always used for elimination and the
              result is always returned as a matrix over the current domain.
              This is most efficient for dense matrices or for matrices with
              simple denominators.

            - ``A.rref(method='CD')`` clears denominators before using
              fraction-free Gauss-Jordan elimination in the assoicated ring.
              The result will be converted back to the original domain unless
              ``keep_domain=False`` is passed in which case the result will be
              over the ring used for elimination. This is most efficient for
              dense matrices with very simple denominators.

            - ``A.rref(method='GJ')`` uses Gauss-Jordan elimination with
              division. If the domain is not a field then it will be converted
              to a field with :meth:`to_field` first and RREF will be computed
              by inverting the pivot elements in each row. The result is
              converted back to the original domain by clearing denominators
              unless ``keep_domain=False`` is passed in which case the result
              will be over the field used for elimination. This is most
              efficient for very sparse matrices or for matrices whose elements
              have complex denominators.

            - ``A.rref(method='GJ_dense')``, ``A.rref(method='FF_dense')``, and
              ``A.rref(method='CD_dense')`` are the same as the above methods
              except that the dense implementations of the algorithms are used.
              By default ``A.rref(method='auto')`` will usually choose the
              sparse implementations for RREF.

            Regardless of which algorithm is used the returned matrix will
            always have the same format (sparse or dense) as the input and if
            ``keep_domain=True`` its domain will always be the same as the
            input.

        keep_domain : bool, optional
            If True (the default), the domain of the returned matrix and
            denominator are the same as the domain of the input matrix. If
            False, the domain of the returned matrix might be changed to an
            associated ring or field if the algorithm used a different domain.
            This is useful for efficiency if the caller does not need the
            result to be in the original domain e.g. it avoids clearing
            denominators in the case of ``A.rref(method='GJ')``.

        Returns
        =======

        (DomainMatrix, scalar, list)
            Reduced-row echelon form, denominator and list of pivot indices.

        See Also
        ========

        rref
            RREF without denominator for field domains.
        sympy.polys.matrices.sdm.sdm_irref
            Sparse implementation of ``method='GJ'``.
        sympy.polys.matrices.sdm.sdm_rref_den
            Sparse implementation of ``method='FF'`` and ``method='CD'``.
        sympy.polys.matrices.dense.ddm_irref
            Dense implementation of ``method='GJ'``.
        sympy.polys.matrices.dense.ddm_irref_den
            Dense implementation of ``method='FF'`` and ``method='CD'``.
        clear_denoms
            Clear denominators from a matrix, used by ``method='CD'``.

        """
        ...
    
    def columnspace(self) -> Self:
        r"""
        Returns the columnspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The columns of this matrix form a basis for the columnspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.columnspace()
        DomainMatrix([[1], [2]], (2, 1), QQ)

        """
        ...
    
    def rowspace(self) -> Self:
        r"""
        Returns the rowspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The rows of this matrix form a basis for the rowspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> A.rowspace()
        DomainMatrix([[1, -1]], (1, 2), QQ)

        """
        ...
    
    def nullspace(self, divide_last=...):
        r"""
        Returns the nullspace for the DomainMatrix

        Returns
        =======

        DomainMatrix
            The rows of this matrix form a basis for the nullspace.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([
        ...    [QQ(2), QQ(-2)],
        ...    [QQ(4), QQ(-4)]], QQ)
        >>> A.nullspace()
        DomainMatrix([[1, 1]], (1, 2), QQ)

        The returned matrix is a basis for the nullspace:

        >>> A_null = A.nullspace().transpose()
        >>> A * A_null
        DomainMatrix([[0], [0]], (2, 1), QQ)
        >>> rows, cols = A.shape
        >>> nullity = rows - A.rank()
        >>> A_null.shape == (cols, nullity)
        True

        Nullspace can also be computed for non-field rings. If the ring is not
        a field then division is not used. Setting ``divide_last`` to True will
        raise an error in this case:

        >>> from sympy import ZZ
        >>> B = DM([[6, -3],
        ...         [4, -2]], ZZ)
        >>> B.nullspace()
        DomainMatrix([[3, 6]], (1, 2), ZZ)
        >>> B.nullspace(divide_last=True)
        Traceback (most recent call last):
        ...
        DMNotAField: Cannot normalize vectors over a non-field

        Over a ring with ``gcd`` defined the nullspace can potentially be
        reduced with :meth:`primitive`:

        >>> B.nullspace().primitive()
        (3, DomainMatrix([[1, 2]], (1, 2), ZZ))

        A matrix over a ring can often be normalized by converting it to a
        field but it is often a bad idea to do so:

        >>> from sympy.abc import a, b, c
        >>> from sympy import Matrix
        >>> M = Matrix([[        a*b,       b + c,        c],
        ...             [      a - b,         b*c,     c**2],
        ...             [a*b + a - b, b*c + b + c, c**2 + c]])
        >>> M.to_DM().domain
        ZZ[a,b,c]
        >>> M.to_DM().nullspace().to_Matrix().transpose()
        Matrix([
        [                             c**3],
        [            -a*b*c**2 + a*c - b*c],
        [a*b**2*c - a*b - a*c + b**2 + b*c]])

        The unnormalized form here is nicer than the normalized form that
        spreads a large denominator throughout the matrix:

        >>> M.to_DM().to_field().nullspace(divide_last=True).to_Matrix().transpose()
        Matrix([
        [                   c**3/(a*b**2*c - a*b - a*c + b**2 + b*c)],
        [(-a*b*c**2 + a*c - b*c)/(a*b**2*c - a*b - a*c + b**2 + b*c)],
        [                                                          1]])

        Parameters
        ==========

        divide_last : bool, optional
            If False (the default), the vectors are not normalized and the RREF
            is computed using :meth:`rref_den` and the denominator is
            discarded. If True, then each row is divided by its final element;
            the domain must be a field in this case.

        See Also
        ========

        nullspace_from_rref
        rref
        rref_den
        rowspace
        """
        ...
    
    def nullspace_from_rref(self, pivots=...) -> Self:
        """
        Compute nullspace from rref and pivots.

        The domain of the matrix can be any domain.

        The matrix must be in reduced row echelon form already. Otherwise the
        result will be incorrect. Use :meth:`rref` or :meth:`rref_den` first
        to get the reduced row echelon form or use :meth:`nullspace` instead.

        See Also
        ========

        nullspace
        rref
        rref_den
        sympy.polys.matrices.sdm.SDM.nullspace_from_rref
        sympy.polys.matrices.ddm.DDM.nullspace_from_rref
        """
        ...
    
    def inv(self) -> Self:
        r"""
        Finds the inverse of the DomainMatrix if exists

        Returns
        =======

        DomainMatrix
            DomainMatrix after inverse

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        DMNonSquareMatrixError
            If the DomainMatrix is not a not Square DomainMatrix

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [QQ(2), QQ(-1), QQ(0)],
        ...     [QQ(-1), QQ(2), QQ(-1)],
        ...     [QQ(0), QQ(0), QQ(2)]], (3, 3), QQ)
        >>> A.inv()
        DomainMatrix([[2/3, 1/3, 1/6], [1/3, 2/3, 1/3], [0, 0, 1/2]], (3, 3), QQ)

        See Also
        ========

        neg

        """
        ...
    
    def det(self):
        r"""
        Returns the determinant of a square :class:`DomainMatrix`.

        Returns
        =======

        determinant: DomainElement
            Determinant of the matrix.

        Raises
        ======

        ValueError
            If the domain of DomainMatrix is not a Field

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.det()
        -2

        """
        ...
    
    def adj_det(self) -> tuple[Any, Any]:
        """
        Adjugate and determinant of a square :class:`DomainMatrix`.

        Returns
        =======

        (adjugate, determinant) : (DomainMatrix, DomainScalar)
            The adjugate matrix and determinant of this matrix.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([
        ...     [ZZ(1), ZZ(2)],
        ...     [ZZ(3), ZZ(4)]], ZZ)
        >>> adjA, detA = A.adj_det()
        >>> adjA
        DomainMatrix([[4, -2], [-3, 1]], (2, 2), ZZ)
        >>> detA
        -2

        See Also
        ========

        adjugate
            Returns only the adjugate matrix.
        det
            Returns only the determinant.
        inv_den
            Returns a matrix/denominator pair representing the inverse matrix
            but perhaps differing from the adjugate and determinant by a common
            factor.
        """
        ...
    
    def adjugate(self):
        """
        Adjugate of a square :class:`DomainMatrix`.

        The adjugate matrix is the transpose of the cofactor matrix and is
        related to the inverse by::

            adj(A) = det(A) * A.inv()

        Unlike the inverse matrix the adjugate matrix can be computed and
        expressed without division or fractions in the ground domain.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], ZZ)
        >>> A.adjugate()
        DomainMatrix([[4, -2], [-3, 1]], (2, 2), ZZ)

        Returns
        =======

        DomainMatrix
            The adjugate matrix of this matrix with the same domain.

        See Also
        ========

        adj_det
        """
        ...
    
    def inv_den(self, method=...) -> tuple[Any, Any]:
        """
        Return the inverse as a :class:`DomainMatrix` with denominator.

        Returns
        =======

        (inv, den) : (:class:`DomainMatrix`, :class:`~.DomainElement`)
            The inverse matrix and its denominator.

        This is more or less equivalent to :meth:`adj_det` except that ``inv``
        and ``den`` are not guaranteed to be the adjugate and inverse. The
        ratio ``inv/den`` is equivalent to ``adj/det`` but some factors
        might be cancelled between ``inv`` and ``den``. In simple cases this
        might just be a minus sign so that ``(inv, den) == (-adj, -det)`` but
        factors more complicated than ``-1`` can also be cancelled.
        Cancellation is not guaranteed to be complete so ``inv`` and ``den``
        may not be on lowest terms. The denominator ``den`` will be zero if and
        only if the determinant is zero.

        If the actual adjugate and determinant are needed, use :meth:`adj_det`
        instead. If the intention is to compute the inverse matrix or solve a
        system of equations then :meth:`inv_den` is more efficient.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...     [ZZ(2), ZZ(-1), ZZ(0)],
        ...     [ZZ(-1), ZZ(2), ZZ(-1)],
        ...     [ZZ(0), ZZ(0), ZZ(2)]], (3, 3), ZZ)
        >>> Ainv, den = A.inv_den()
        >>> den
        6
        >>> Ainv
        DomainMatrix([[4, 2, 1], [2, 4, 2], [0, 0, 3]], (3, 3), ZZ)
        >>> A * Ainv == den * A.eye(A.shape, A.domain).to_dense()
        True

        Parameters
        ==========

        method : str, optional
            The method to use to compute the inverse. Can be one of ``None``,
            ``'rref'`` or ``'charpoly'``. If ``None`` then the method is
            chosen automatically (see :meth:`solve_den` for details).

        See Also
        ========

        inv
        det
        adj_det
        solve_den
        """
        ...
    
    def solve_den(self, b, method=...) -> tuple[Any, Any]:
        """
        Solve matrix equation $Ax = b$ without fractions in the ground domain.

        Examples
        ========

        Solve a matrix equation over the integers:

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], ZZ)
        >>> b = DM([[ZZ(5)], [ZZ(6)]], ZZ)
        >>> xnum, xden = A.solve_den(b)
        >>> xden
        -2
        >>> xnum
        DomainMatrix([[8], [-9]], (2, 1), ZZ)
        >>> A * xnum == xden * b
        True

        Solve a matrix equation over a polynomial ring:

        >>> from sympy import ZZ
        >>> from sympy.abc import x, y, z, a, b
        >>> R = ZZ[x, y, z, a, b]
        >>> M = DM([[x*y, x*z], [y*z, x*z]], R)
        >>> b = DM([[a], [b]], R)
        >>> M.to_Matrix()
        Matrix([
        [x*y, x*z],
        [y*z, x*z]])
        >>> b.to_Matrix()
        Matrix([
        [a],
        [b]])
        >>> xnum, xden = M.solve_den(b)
        >>> xden
        x**2*y*z - x*y*z**2
        >>> xnum.to_Matrix()
        Matrix([
        [ a*x*z - b*x*z],
        [-a*y*z + b*x*y]])
        >>> M * xnum == xden * b
        True

        The solution can be expressed over a fraction field which will cancel
        gcds between the denominator and the elements of the numerator:

        >>> xsol = xnum.to_field() / xden
        >>> xsol.to_Matrix()
        Matrix([
        [           (a - b)/(x*y - y*z)],
        [(-a*z + b*x)/(x**2*z - x*z**2)]])
        >>> (M * xsol).to_Matrix() == b.to_Matrix()
        True

        When solving a large system of equations this cancellation step might
        be a lot slower than :func:`solve_den` itself. The solution can also be
        expressed as a ``Matrix`` without attempting any polynomial
        cancellation between the numerator and denominator giving a less
        simplified result more quickly:

        >>> xsol_uncancelled = xnum.to_Matrix() / xnum.domain.to_sympy(xden)
        >>> xsol_uncancelled
        Matrix([
        [ (a*x*z - b*x*z)/(x**2*y*z - x*y*z**2)],
        [(-a*y*z + b*x*y)/(x**2*y*z - x*y*z**2)]])
        >>> from sympy import cancel
        >>> cancel(xsol_uncancelled) == xsol.to_Matrix()
        True

        Parameters
        ==========

        self : :class:`DomainMatrix`
            The ``m x n`` matrix $A$ in the equation $Ax = b$. Underdetermined
            systems are not supported so ``m >= n``: $A$ should be square or
            have more rows than columns.
        b : :class:`DomainMatrix`
            The ``n x m`` matrix $b$ for the rhs.
        cp : list of :class:`~.DomainElement`, optional
            The characteristic polynomial of the matrix $A$. If not given, it
            will be computed using :meth:`charpoly`.
        method: str, optional
            The method to use for solving the system. Can be one of ``None``,
            ``'charpoly'`` or ``'rref'``. If ``None`` (the default) then the
            method will be chosen automatically.

            The ``charpoly`` method uses :meth:`solve_den_charpoly` and can
            only be used if the matrix is square. This method is division free
            and can be used with any domain.

            The ``rref`` method is fraction free but requires exact division
            in the ground domain (``exquo``). This is also suitable for most
            domains. This method can be used with overdetermined systems (more
            equations than unknowns) but not underdetermined systems as a
            unique solution is sought.

        Returns
        =======

        (xnum, xden) : (DomainMatrix, DomainElement)
            The solution of the equation $Ax = b$ as a pair consisting of an
            ``n x m`` matrix numerator ``xnum`` and a scalar denominator
            ``xden``.

        The solution $x$ is given by ``x = xnum / xden``. The division free
        invariant is ``A * xnum == xden * b``. If $A$ is square then the
        denominator ``xden`` will be a divisor of the determinant $det(A)$.

        Raises
        ======

        DMNonInvertibleMatrixError
            If the system $Ax = b$ does not have a unique solution.

        See Also
        ========

        solve_den_charpoly
        solve_den_rref
        inv_den
        """
        ...
    
    def solve_den_rref(self, b) -> tuple[Any, Any]:
        """
        Solve matrix equation $Ax = b$ using fraction-free RREF

        Solves the matrix equation $Ax = b$ for $x$ and returns the solution
        as a numerator/denominator pair.

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], ZZ)
        >>> b = DM([[ZZ(5)], [ZZ(6)]], ZZ)
        >>> xnum, xden = A.solve_den_rref(b)
        >>> xden
        -2
        >>> xnum
        DomainMatrix([[8], [-9]], (2, 1), ZZ)
        >>> A * xnum == xden * b
        True

        See Also
        ========

        solve_den
        solve_den_charpoly
        """
        ...
    
    def solve_den_charpoly(self, b, cp=..., check=...) -> tuple[Any, Any]:
        """
        Solve matrix equation $Ax = b$ using the characteristic polynomial.

        This method solves the square matrix equation $Ax = b$ for $x$ using
        the characteristic polynomial without any division or fractions in the
        ground domain.

        Examples
        ========

        Solve a matrix equation over the integers:

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], ZZ)
        >>> b = DM([[ZZ(5)], [ZZ(6)]], ZZ)
        >>> xnum, detA = A.solve_den_charpoly(b)
        >>> detA
        -2
        >>> xnum
        DomainMatrix([[8], [-9]], (2, 1), ZZ)
        >>> A * xnum == detA * b
        True

        Parameters
        ==========

        self : DomainMatrix
            The ``n x n`` matrix `A` in the equation `Ax = b`. Must be square
            and invertible.
        b : DomainMatrix
            The ``n x m`` matrix `b` for the rhs.
        cp : list, optional
            The characteristic polynomial of the matrix `A` if known. If not
            given, it will be computed using :meth:`charpoly`.
        check : bool, optional
            If ``True`` (the default) check that the determinant is not zero
            and raise an error if it is. If ``False`` then if the determinant
            is zero the return value will be equal to ``(A.adjugate()*b, 0)``.

        Returns
        =======

        (xnum, detA) : (DomainMatrix, DomainElement)
            The solution of the equation `Ax = b` as a matrix numerator and
            scalar denominator pair. The denominator is equal to the
            determinant of `A` and the numerator is ``adj(A)*b``.

        The solution $x$ is given by ``x = xnum / detA``. The division free
        invariant is ``A * xnum == detA * b``.

        If ``b`` is the identity matrix, then ``xnum`` is the adjugate matrix
        and we have ``A * adj(A) == detA * I``.

        See Also
        ========

        solve_den
            Main frontend for solving matrix equations with denominator.
        solve_den_rref
            Solve matrix equations using fraction-free RREF.
        inv_den
            Invert a matrix using the characteristic polynomial.
        """
        ...
    
    def adj_poly_det(self, cp=...) -> tuple[list[Any] | Any, Any]:
        """
        Return the polynomial $p$ such that $p(A) = adj(A)$ and also the
        determinant of $A$.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[QQ(1), QQ(2)], [QQ(3), QQ(4)]], QQ)
        >>> p, detA = A.adj_poly_det()
        >>> p
        [-1, 5]
        >>> p_A = A.eval_poly(p)
        >>> p_A
        DomainMatrix([[4, -2], [-3, 1]], (2, 2), QQ)
        >>> p[0]*A**1 + p[1]*A**0 == p_A
        True
        >>> p_A == A.adjugate()
        True
        >>> A * A.adjugate() == detA * A.eye(A.shape, A.domain).to_dense()
        True

        See Also
        ========

        adjugate
        eval_poly
        adj_det
        """
        ...
    
    def eval_poly(self, p) -> Self:
        """
        Evaluate polynomial function of a matrix $p(A)$.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[QQ(1), QQ(2)], [QQ(3), QQ(4)]], QQ)
        >>> p = [QQ(1), QQ(2), QQ(3)]
        >>> p_A = A.eval_poly(p)
        >>> p_A
        DomainMatrix([[12, 14], [21, 33]], (2, 2), QQ)
        >>> p_A == p[0]*A**2 + p[1]*A + p[2]*A**0
        True

        See Also
        ========

        eval_poly_mul
        """
        ...
    
    def eval_poly_mul(self, p, B):
        r"""
        Evaluate polynomial matrix product $p(A) \times B$.

        Evaluate the polynomial matrix product $p(A) \times B$ using Horner's
        method without creating the matrix $p(A)$ explicitly. If $B$ is a
        column matrix then this method will only use matrix-vector multiplies
        and no matrix-matrix multiplies are needed.

        If $B$ is square or wide or if $A$ can be represented in a simpler
        domain than $B$ then it might be faster to evaluate $p(A)$ explicitly
        (see :func:`eval_poly`) and then multiply with $B$.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DM
        >>> A = DM([[QQ(1), QQ(2)], [QQ(3), QQ(4)]], QQ)
        >>> b = DM([[QQ(5)], [QQ(6)]], QQ)
        >>> p = [QQ(1), QQ(2), QQ(3)]
        >>> p_A_b = A.eval_poly_mul(p, b)
        >>> p_A_b
        DomainMatrix([[144], [303]], (2, 1), QQ)
        >>> p_A_b == p[0]*A**2*b + p[1]*A*b + p[2]*b
        True
        >>> A.eval_poly_mul(p, b) == A.eval_poly(p)*b
        True

        See Also
        ========

        eval_poly
        solve_den_charpoly
        """
        ...
    
    def lu(self) -> tuple[Self, Self, list[Any] | Any]:
        r"""
        Returns Lower and Upper decomposition of the DomainMatrix

        Returns
        =======

        (L, U, exchange)
            L, U are Lower and Upper decomposition of the DomainMatrix,
            exchange is the list of indices of rows exchanged in the
            decomposition.

        Raises
        ======

        ValueError
            If the domain of DomainMatrix not a Field

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(-1)],
        ...    [QQ(2), QQ(-2)]], (2, 2), QQ)
        >>> L, U, exchange = A.lu()
        >>> L
        DomainMatrix([[1, 0], [2, 1]], (2, 2), QQ)
        >>> U
        DomainMatrix([[1, -1], [0, 0]], (2, 2), QQ)
        >>> exchange
        []

        See Also
        ========

        lu_solve

        """
        ...
    
    def lu_solve(self, rhs) -> Self:
        r"""
        Solver for DomainMatrix x in the A*x = B

        Parameters
        ==========

        rhs : DomainMatrix B

        Returns
        =======

        DomainMatrix
            x in A*x = B

        Raises
        ======

        DMShapeError
            If the DomainMatrix A and rhs have different number of rows

        ValueError
            If the domain of DomainMatrix A not a Field

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [QQ(1), QQ(2)],
        ...    [QQ(3), QQ(4)]], (2, 2), QQ)
        >>> B = DomainMatrix([
        ...    [QQ(1), QQ(1)],
        ...    [QQ(0), QQ(1)]], (2, 2), QQ)

        >>> A.lu_solve(B)
        DomainMatrix([[-2, -1], [3/2, 1]], (2, 2), QQ)

        See Also
        ========

        lu

        """
        ...
    
    def charpoly(self) -> list[Any]:
        r"""
        Characteristic polynomial of a square matrix.

        Computes the characteristic polynomial in a fully expanded form using
        division free arithmetic. If a factorization of the characteristic
        polynomial is needed then it is more efficient to call
        :meth:`charpoly_factor_list` than calling :meth:`charpoly` and then
        factorizing the result.

        Returns
        =======

        list: list of DomainElement
            coefficients of the characteristic polynomial

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)

        >>> A.charpoly()
        [1, -5, -2]

        See Also
        ========

        charpoly_factor_list
            Compute the factorisation of the characteristic polynomial.
        charpoly_factor_blocks
            A partial factorisation of the characteristic polynomial that can
            be computed more efficiently than either the full factorisation or
            the fully expanded polynomial.
        """
        ...
    
    def charpoly_factor_list(self) -> list[Any]:
        """
        Full factorization of the characteristic polynomial.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[6, -1, 0, 0],
        ...         [9, 12, 0, 0],
        ...         [0,  0, 1, 2],
        ...         [0,  0, 5, 6]], ZZ)

        Compute the factorization of the characteristic polynomial:

        >>> M.charpoly_factor_list()
        [([1, -9], 2), ([1, -7, -4], 1)]

        Use :meth:`charpoly` to get the unfactorized characteristic polynomial:

        >>> M.charpoly()
        [1, -25, 203, -495, -324]

        The same calculations with ``Matrix``:

        >>> M.to_Matrix().charpoly().as_expr()
        lambda**4 - 25*lambda**3 + 203*lambda**2 - 495*lambda - 324
        >>> M.to_Matrix().charpoly().as_expr().factor()
        (lambda - 9)**2*(lambda**2 - 7*lambda - 4)

        Returns
        =======

        list: list of pairs (factor, multiplicity)
            A full factorization of the characteristic polynomial.

        See Also
        ========

        charpoly
            Expanded form of the characteristic polynomial.
        charpoly_factor_blocks
            A partial factorisation of the characteristic polynomial that can
            be computed more efficiently.
        """
        ...
    
    def charpoly_factor_blocks(self) -> list[Any]:
        """
        Partial factorisation of the characteristic polynomial.

        This factorisation arises from a block structure of the matrix (if any)
        and so the factors are not guaranteed to be irreducible. The
        :meth:`charpoly_factor_blocks` method is the most efficient way to get
        a representation of the characteristic polynomial but the result is
        neither fully expanded nor fully factored.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import ZZ
        >>> M = DM([[6, -1, 0, 0],
        ...         [9, 12, 0, 0],
        ...         [0,  0, 1, 2],
        ...         [0,  0, 5, 6]], ZZ)

        This computes a partial factorization using only the block structure of
        the matrix to reveal factors:

        >>> M.charpoly_factor_blocks()
        [([1, -18, 81], 1), ([1, -7, -4], 1)]

        These factors correspond to the two diagonal blocks in the matrix:

        >>> DM([[6, -1], [9, 12]], ZZ).charpoly()
        [1, -18, 81]
        >>> DM([[1, 2], [5, 6]], ZZ).charpoly()
        [1, -7, -4]

        Use :meth:`charpoly_factor_list` to get a complete factorization into
        irreducibles:

        >>> M.charpoly_factor_list()
        [([1, -9], 2), ([1, -7, -4], 1)]

        Use :meth:`charpoly` to get the expanded characteristic polynomial:

        >>> M.charpoly()
        [1, -25, 203, -495, -324]

        Returns
        =======

        list: list of pairs (factor, multiplicity)
            A partial factorization of the characteristic polynomial.

        See Also
        ========

        charpoly
            Compute the fully expanded characteristic polynomial.
        charpoly_factor_list
            Compute a full factorization of the characteristic polynomial.
        """
        ...
    
    def charpoly_base(self) -> list[Any]:
        """
        Base case for :meth:`charpoly_factor_blocks` after block decomposition.

        This method is used internally by :meth:`charpoly_factor_blocks` as the
        base case for computing the characteristic polynomial of a block. It is
        more efficient to call :meth:`charpoly_factor_blocks`, :meth:`charpoly`
        or :meth:`charpoly_factor_list` rather than call this method directly.

        This will use either the dense or the sparse implementation depending
        on the sparsity of the matrix and will clear denominators if possible
        before calling :meth:`charpoly_berk` to compute the characteristic
        polynomial using the Berkowitz algorithm.

        See Also
        ========

        charpoly
        charpoly_factor_list
        charpoly_factor_blocks
        charpoly_berk
        """
        ...
    
    def charpoly_berk(self) -> list[Any]:
        """Compute the characteristic polynomial using the Berkowitz algorithm.

        This method directly calls the underlying implementation of the
        Berkowitz algorithm (:meth:`sympy.polys.matrices.dense.ddm_berk` or
        :meth:`sympy.polys.matrices.sdm.sdm_berk`).

        This is used by :meth:`charpoly` and other methods as the base case for
        for computing the characteristic polynomial. However those methods will
        apply other optimizations such as block decomposition, clearing
        denominators and converting between dense and sparse representations
        before calling this method. It is more efficient to call those methods
        instead of this one but this method is provided for direct access to
        the Berkowitz algorithm.

        Examples
        ========

        >>> from sympy.polys.matrices import DM
        >>> from sympy import QQ
        >>> M = DM([[6, -1, 0, 0],
        ...         [9, 12, 0, 0],
        ...         [0,  0, 1, 2],
        ...         [0,  0, 5, 6]], QQ)
        >>> M.charpoly_berk()
        [1, -25, 203, -495, -324]

        See Also
        ========

        charpoly
        charpoly_base
        charpoly_factor_list
        charpoly_factor_blocks
        sympy.polys.matrices.dense.ddm_berk
        sympy.polys.matrices.sdm.sdm_berk
        """
        ...
    
    @classmethod
    def eye(cls, shape, domain) -> Self:
        r"""
        Return identity matrix of size n or shape (m, n).

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.eye(3, QQ)
        DomainMatrix({0: {0: 1}, 1: {1: 1}, 2: {2: 1}}, (3, 3), QQ)

        """
        ...
    
    @classmethod
    def diag(cls, diagonal, domain, shape=...) -> Self:
        r"""
        Return diagonal matrix with entries from ``diagonal``.

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import ZZ
        >>> DomainMatrix.diag([ZZ(5), ZZ(6)], ZZ)
        DomainMatrix({0: {0: 5}, 1: {1: 6}}, (2, 2), ZZ)

        """
        ...
    
    @classmethod
    def zeros(cls, shape, domain, *, fmt=...) -> Self:
        """Returns a zero DomainMatrix of size shape, belonging to the specified domain

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.zeros((2, 3), QQ)
        DomainMatrix({}, (2, 3), QQ)

        """
        ...
    
    @classmethod
    def ones(cls, shape, domain) -> Self:
        """Returns a DomainMatrix of 1s, of size shape, belonging to the specified domain

        Examples
        ========

        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy import QQ
        >>> DomainMatrix.ones((2,3), QQ)
        DomainMatrix([[1, 1, 1], [1, 1, 1]], (2, 3), QQ)

        """
        ...
    
    def __eq__(A, B) -> bool:
        r"""
        Checks for two DomainMatrix matrices to be equal or not

        Parameters
        ==========

        A, B: DomainMatrix
            to check equality

        Returns
        =======

        Boolean
            True for equal, else False

        Raises
        ======

        NotImplementedError
            If B is not a DomainMatrix

        Examples
        ========

        >>> from sympy import ZZ
        >>> from sympy.polys.matrices import DomainMatrix
        >>> A = DomainMatrix([
        ...    [ZZ(1), ZZ(2)],
        ...    [ZZ(3), ZZ(4)]], (2, 2), ZZ)
        >>> B = DomainMatrix([
        ...    [ZZ(1), ZZ(1)],
        ...    [ZZ(0), ZZ(1)]], (2, 2), ZZ)
        >>> A.__eq__(A)
        True
        >>> A.__eq__(B)
        False

        """
        ...
    
    def unify_eq(A, B) -> Literal[False]:
        ...
    
    def lll(A, delta=...) -> DomainMatrix:
        """
        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.
        See [1]_ and [2]_.

        Parameters
        ==========

        delta : QQ, optional
            The Lovász parameter. Must be in the interval (0.25, 1), with larger
            values producing a more reduced basis. The default is 0.75 for
            historical reasons.

        Returns
        =======

        The reduced basis as a DomainMatrix over ZZ.

        Throws
        ======

        DMValueError: if delta is not in the range (0.25, 1)
        DMShapeError: if the matrix is not of shape (m, n) with m <= n
        DMDomainError: if the matrix domain is not ZZ
        DMRankError: if the matrix contains linearly dependent rows

        Examples
        ========

        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.polys.matrices import DM
        >>> x = DM([[1, 0, 0, 0, -20160],
        ...         [0, 1, 0, 0, 33768],
        ...         [0, 0, 1, 0, 39578],
        ...         [0, 0, 0, 1, 47757]], ZZ)
        >>> y = DM([[10, -3, -2, 8, -4],
        ...         [3, -9, 8, 1, -11],
        ...         [-3, 13, -9, -3, -9],
        ...         [-12, -7, -11, 9, -1]], ZZ)
        >>> assert x.lll(delta=QQ(5, 6)) == y

        Notes
        =====

        The implementation is derived from the Maple code given in Figures 4.3
        and 4.4 of [3]_ (pp.68-69). It uses the efficient method of only calculating
        state updates as they are required.

        See also
        ========

        lll_transform

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm
        .. [2] https://web.archive.org/web/20221029115428/https://web.cs.elte.hu/~lovasz/scans/lll.pdf
        .. [3] Murray R. Bremner, "Lattice Basis Reduction: An Introduction to the LLL Algorithm and Its Applications"

        """
        ...
    
    def lll_transform(A, delta=...) -> tuple[DomainMatrix, DomainMatrix]:
        """
        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm
        and returns the reduced basis and transformation matrix.

        Explanation
        ===========

        Parameters, algorithm and basis are the same as for :meth:`lll` except that
        the return value is a tuple `(B, T)` with `B` the reduced basis and
        `T` a transformation matrix. The original basis `A` is transformed to
        `B` with `T*A == B`. If only `B` is needed then :meth:`lll` should be
        used as it is a little faster.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.polys.matrices import DM
        >>> X = DM([[1, 0, 0, 0, -20160],
        ...         [0, 1, 0, 0, 33768],
        ...         [0, 0, 1, 0, 39578],
        ...         [0, 0, 0, 1, 47757]], ZZ)
        >>> B, T = X.lll_transform(delta=QQ(5, 6))
        >>> T * X == B
        True

        See also
        ========

        lll

        """
        ...
    


