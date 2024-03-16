from sympy.utilities.decorator import doctest_depends_on

flint = ...
__all__ = ['DFM']
@doctest_depends_on(ground_types=['flint'])
class DFM:
    """
    Dense FLINT matrix. This class is a wrapper for matrices from python-flint.

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.matrices.dfm import DFM
    >>> dfm = DFM([[ZZ(1), ZZ(2)], [ZZ(3), ZZ(4)]], (2, 2), ZZ)
    >>> dfm
    [[1, 2], [3, 4]]
    >>> dfm.rep
    [1, 2]
    [3, 4]
    >>> type(dfm.rep)  # doctest: +SKIP
    <class 'flint._flint.fmpz_mat'>

    Usually, the DFM class is not instantiated directly, but is created as the
    internal representation of :class:`~.DomainMatrix`. When
    `SYMPY_GROUND_TYPES` is set to `flint` and `python-flint` is installed, the
    :class:`DFM` class is used automatically as the internal representation of
    :class:`~.DomainMatrix` in dense format if the domain is supported by
    python-flint.

    >>> from sympy.polys.matrices.domainmatrix import DM
    >>> dM = DM([[1, 2], [3, 4]], ZZ)
    >>> dM.rep
    [[1, 2], [3, 4]]

    A :class:`~.DomainMatrix` can be converted to :class:`DFM` by calling the
    :meth:`to_dfm` method:

    >>> dM.to_dfm()
    [[1, 2], [3, 4]]

    """
    fmt = ...
    is_DFM = ...
    is_DDM = ...
    def __new__(cls, rowslist, shape, domain) -> Self:
        """Construct from a nested list."""
        ...
    
    def __str__(self) -> str:
        """Return ``str(self)``."""
        ...
    
    def __repr__(self) -> str:
        """Return ``repr(self)``."""
        ...
    
    def __eq__(self, other) -> bool:
        """Return ``self == other``."""
        ...
    
    @classmethod
    def from_list(cls, rowslist, shape, domain) -> Self:
        """Construct from a nested list."""
        ...
    
    def to_list(self):
        """Convert to a nested list."""
        ...
    
    def copy(self) -> Self:
        """Return a copy of self."""
        ...
    
    def to_ddm(self) -> DDM:
        """Convert to a DDM."""
        ...
    
    def to_sdm(self) -> SDM:
        """Convert to a SDM."""
        ...
    
    def to_dfm(self) -> Self:
        """Return self."""
        ...
    
    def to_dfm_or_ddm(self) -> Self:
        """
        Convert to a :class:`DFM`.

        This :class:`DFM` method exists to parallel the :class:`~.DDM` and
        :class:`~.SDM` methods. For :class:`DFM` it will always return self.

        See Also
        ========

        to_ddm
        to_sdm
        sympy.polys.matrices.domainmatrix.DomainMatrix.to_dfm_or_ddm
        """
        ...
    
    @classmethod
    def from_ddm(cls, ddm) -> Self:
        """Convert from a DDM."""
        ...
    
    @classmethod
    def from_list_flat(cls, elements, shape, domain) -> Self:
        """Inverse of :meth:`to_list_flat`."""
        ...
    
    def to_list_flat(self):
        """Convert to a flat list."""
        ...
    
    def to_flat_nz(self) -> tuple[list[Any], tuple[tuple[tuple[Any, Any], ...], Any]]:
        """Convert to a flat list of non-zeros."""
        ...
    
    @classmethod
    def from_flat_nz(cls, elements, data, domain) -> DFM_dummy:
        """Inverse of :meth:`to_flat_nz`."""
        ...
    
    def to_dod(self) -> dict[Any, Any]:
        """Convert to a DOD."""
        ...
    
    @classmethod
    def from_dod(cls, dod, shape, domain) -> DFM_dummy:
        """Inverse of :meth:`to_dod`."""
        ...
    
    def to_dok(self) -> dict[Any, Any]:
        """Convert to a DOK."""
        ...
    
    def convert_to(self, domain) -> Self | DFM_dummy:
        """Convert to a new domain."""
        ...
    
    def getitem(self, i, j):
        """Get the ``(i, j)``-th entry."""
        ...
    
    def setitem(self, i, j, value) -> None:
        """Set the ``(i, j)``-th entry."""
        ...
    
    def extract(self, rowslist, colslist) -> Self:
        """Extract a submatrix."""
        ...
    
    def extract_slice(self, rowslice, colslice) -> Self:
        """Slice a DFM."""
        ...
    
    def neg(self) -> Self:
        """Negate a DFM matrix."""
        ...
    
    def add(self, other) -> Self:
        """Add two DFM matrices."""
        ...
    
    def sub(self, other) -> Self:
        """Subtract two DFM matrices."""
        ...
    
    def mul(self, other) -> Self:
        """Multiply a DFM matrix from the right by a scalar."""
        ...
    
    def rmul(self, other) -> Self:
        """Multiply a DFM matrix from the left by a scalar."""
        ...
    
    def mul_elementwise(self, other) -> DFM_dummy:
        """Elementwise multiplication of two DFM matrices."""
        ...
    
    def matmul(self, other) -> Self:
        """Multiply two DFM matrices."""
        ...
    
    def __neg__(self) -> Self:
        """Negate a DFM matrix."""
        ...
    
    @classmethod
    def zeros(cls, shape, domain) -> Self:
        """Return a zero DFM matrix."""
        ...
    
    @classmethod
    def ones(cls, shape, domain) -> DFM_dummy:
        """Return a one DFM matrix."""
        ...
    
    @classmethod
    def eye(cls, n, domain) -> DFM_dummy:
        """Return the identity matrix of size n."""
        ...
    
    @classmethod
    def diag(cls, elements, domain) -> DFM_dummy:
        """Return a diagonal matrix."""
        ...
    
    def applyfunc(self, func, domain) -> DFM_dummy:
        """Apply a function to each entry of a DFM matrix."""
        ...
    
    def transpose(self) -> Self:
        """Transpose a DFM matrix."""
        ...
    
    def hstack(self, *others) -> DFM_dummy:
        """Horizontally stack matrices."""
        ...
    
    def vstack(self, *others) -> DFM_dummy:
        """Vertically stack matrices."""
        ...
    
    def diagonal(self) -> list[Any]:
        """Return the diagonal of a DFM matrix."""
        ...
    
    def is_upper(self) -> bool:
        """Return ``True`` if the matrix is upper triangular."""
        ...
    
    def is_lower(self) -> bool:
        """Return ``True`` if the matrix is lower triangular."""
        ...
    
    def is_diagonal(self) -> bool:
        """Return ``True`` if the matrix is diagonal."""
        ...
    
    def is_zero_matrix(self) -> bool:
        """Return ``True`` if the matrix is the zero matrix."""
        ...
    
    def nnz(self) -> int:
        """Return the number of non-zero elements in the matrix."""
        ...
    
    def scc(self) -> list[Any]:
        """Return the strongly connected components of the matrix."""
        ...
    
    @doctest_depends_on(ground_types='flint')
    def det(self):
        """
        Compute the determinant of the matrix using FLINT.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> dfm = M.to_DM().to_dfm()
        >>> dfm
        [[1, 2], [3, 4]]
        >>> dfm.det()
        -2

        Notes
        =====

        Calls the ``.det()`` method of the underlying FLINT matrix.

        For :ref:`ZZ` or :ref:`QQ` this calls ``fmpz_mat_det`` or
        ``fmpq_mat_det`` respectively.

        At the time of writing the implementation of ``fmpz_mat_det`` uses one
        of several algorithms depending on the size of the matrix and bit size
        of the entries. The algorithms used are:

        - Cofactor for very small (up to 4x4) matrices.
        - Bareiss for small (up to 25x25) matrices.
        - Modular algorithms for larger matrices (up to 60x60) or for larger
          matrices with large bit sizes.
        - Modular "accelerated" for larger matrices (60x60 upwards) if the bit
          size is smaller than the dimensions of the matrix.

        The implementation of ``fmpq_mat_det`` clears denominators from each
        row (not the whole matrix) and then calls ``fmpz_mat_det`` and divides
        by the product of the denominators.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.det
            Higher level interface to compute the determinant of a matrix.
        """
        ...
    
    @doctest_depends_on(ground_types='flint')
    def charpoly(self):
        """
        Compute the characteristic polynomial of the matrix using FLINT.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> dfm = M.to_DM().to_dfm()  # need ground types = 'flint'
        >>> dfm
        [[1, 2], [3, 4]]
        >>> dfm.charpoly()
        [1, -5, -2]

        Notes
        =====

        Calls the ``.charpoly()`` method of the underlying FLINT matrix.

        For :ref:`ZZ` or :ref:`QQ` this calls ``fmpz_mat_charpoly`` or
        ``fmpq_mat_charpoly`` respectively.

        At the time of writing the implementation of ``fmpq_mat_charpoly``
        clears a denominator from the whole matrix and then calls
        ``fmpz_mat_charpoly``. The coefficients of the characteristic
        polynomial are then multiplied by powers of the denominator.

        The ``fmpz_mat_charpoly`` method uses a modular algorithm with CRT
        reconstruction. The modular algorithm uses ``nmod_mat_charpoly`` which
        uses Berkowitz for small matrices and non-prime moduli or otherwise
        the Danilevsky method.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.charpoly
            Higher level interface to compute the characteristic polynomial of
            a matrix.
        """
        ...
    
    @doctest_depends_on(ground_types='flint')
    def inv(self) -> Self:
        """
        Compute the inverse of a matrix using FLINT.

        Examples
        ========

        >>> from sympy import Matrix, QQ
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> dfm = M.to_DM().to_dfm().convert_to(QQ)
        >>> dfm
        [[1, 2], [3, 4]]
        >>> dfm.inv()
        [[-2, 1], [3/2, -1/2]]
        >>> dfm.matmul(dfm.inv())
        [[1, 0], [0, 1]]

        Notes
        =====

        Calls the ``.inv()`` method of the underlying FLINT matrix.

        For now this will raise an error if the domain is :ref:`ZZ` but will
        use the FLINT method for :ref:`QQ`.

        The FLINT methods for :ref:`ZZ` and :ref:`QQ` are ``fmpz_mat_inv`` and
        ``fmpq_mat_inv`` respectively. The ``fmpz_mat_inv`` method computes an
        inverse with denominator. This is implemented by calling
        ``fmpz_mat_solve`` (see notes in :meth:`lu_solve` about the algorithm).

        The ``fmpq_mat_inv`` method clears denominators from each row and then
        multiplies those into the rhs identity matrix before calling
        ``fmpz_mat_solve``.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.inv
            Higher level method for computing the inverse of a matrix.
        """
        ...
    
    def lu(self) -> tuple[DFM_dummy, DFM_dummy, list[Any]]:
        """Return the LU decomposition of the matrix."""
        ...
    
    @doctest_depends_on(ground_types='flint')
    def lu_solve(self, rhs) -> DFM_dummy | Self:
        """
        Solve a matrix equation using FLINT.

        Examples
        ========

        >>> from sympy import Matrix, QQ
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> dfm = M.to_DM().to_dfm().convert_to(QQ)
        >>> dfm
        [[1, 2], [3, 4]]
        >>> rhs = Matrix([1, 2]).to_DM().to_dfm().convert_to(QQ)
        >>> dfm.lu_solve(rhs)
        [[0], [1/2]]

        Notes
        =====

        Calls the ``.solve()`` method of the underlying FLINT matrix.

        For now this will raise an error if the domain is :ref:`ZZ` but will
        use the FLINT method for :ref:`QQ`.

        The FLINT methods for :ref:`ZZ` and :ref:`QQ` are ``fmpz_mat_solve``
        and ``fmpq_mat_solve`` respectively. The ``fmpq_mat_solve`` method
        uses one of two algorithms:

        - For small matrices (<25 rows) it clears denominators between the
          matrix and rhs and uses ``fmpz_mat_solve``.
        - For larger matrices it uses ``fmpq_mat_solve_dixon`` which is a
          modular approach with CRT reconstruction over :ref:`QQ`.

        The ``fmpz_mat_solve`` method uses one of four algorithms:

        - For very small (<= 3x3) matrices it uses a Cramer's rule.
        - For small (<= 15x15) matrices it uses a fraction-free LU solve.
        - Otherwise it uses either Dixon or another multimodular approach.

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.lu_solve
            Higher level interface to solve a matrix equation.
        """
        ...
    
    def nullspace(self) -> tuple[DFM_dummy, list[int]]:
        """Return a basis for the nullspace of the matrix."""
        ...
    
    def nullspace_from_rref(self, pivots=...) -> tuple[DFM_dummy, list[int]]:
        """Return a basis for the nullspace of the matrix."""
        ...
    
    def particular(self) -> DFM_dummy:
        """Return a particular solution to the system."""
        ...
    
    @doctest_depends_on(ground_types='flint')
    def lll(self, delta=...) -> Self:
        """Compute LLL-reduced basis using FLINT.

        See :meth:`lll_transform` for more information.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> M.to_DM().to_dfm().lll()
        [[2, 1, 0], [-1, 1, 3]]

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.lll
            Higher level interface to compute LLL-reduced basis.
        lll_transform
            Compute LLL-reduced basis and transform matrix.
        """
        ...
    
    @doctest_depends_on(ground_types='flint')
    def lll_transform(self, delta=...) -> tuple[Self, Self]:
        """Compute LLL-reduced basis and transform using FLINT.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2, 3], [4, 5, 6]]).to_DM().to_dfm()
        >>> M_lll, T = M.lll_transform()
        >>> M_lll
        [[2, 1, 0], [-1, 1, 3]]
        >>> T
        [[-2, 1], [3, -1]]
        >>> T.matmul(M) == M_lll
        True

        See Also
        ========

        sympy.polys.matrices.domainmatrix.DomainMatrix.lll
            Higher level interface to compute LLL-reduced basis.
        lll
            Compute LLL-reduced basis without transform matrix.
        """
        ...
    


