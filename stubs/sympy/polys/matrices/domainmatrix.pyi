from types import NotImplementedType
from typing import Any, Literal, Self, Tuple as tTuple, Union as tUnion
from sympy.matrices.dense import MutableDenseMatrix
from sympy.polys.matrices.domainscalar import DomainScalar
from sympy.utilities.decorator import doctest_depends_on
from sympy.polys.domains import Domain
from sympy.polys.matrices.ddm import DDM
from sympy.polys.matrices.sdm import SDM
from sympy.polys.matrices.dfm import DFM, DFM_dummy

def DM(rows, domain) -> DomainMatrix:
    ...

class DomainMatrix:
    rep: tUnion[SDM, DDM, Any]
    shape: tTuple[int, int]
    domain: Domain
    def __new__(cls, rows, shape, domain, *, fmt=...) -> Self:
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
        ...
    
    @classmethod
    @doctest_depends_on(ground_types=['python', 'gmpy'])
    def from_list(cls, rows, domain) -> DomainMatrix:
        ...
    
    @classmethod
    def from_list_sympy(cls, nrows, ncols, rows, **kwargs) -> DomainMatrix:
        ...
    
    @classmethod
    def from_dict_sympy(cls, nrows, ncols, elemsdict, **kwargs) -> DomainMatrix:
        ...
    
    @classmethod
    def from_Matrix(cls, M, fmt=..., **kwargs):
        ...
    
    @classmethod
    def get_domain(cls, items_sympy, **kwargs) -> tuple[Any, Any]:
        ...
    
    def choose_domain(self, **opts) -> Self:
        ...
    
    def copy(self) -> Self:
        ...
    
    def convert_to(self, K) -> Self:
        ...
    
    def to_sympy(self) -> Self:
        ...
    
    def to_field(self) -> Self:
        ...
    
    def to_sparse(self) -> Self:
        ...
    
    def to_dense(self) -> Self:
        ...
    
    def to_ddm(self) -> DDM:
        ...
    
    def to_sdm(self) -> SDM:
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm(self) -> DFM_dummy:
        ...
    
    @doctest_depends_on(ground_types=['flint'])
    def to_dfm_or_ddm(self) -> DFM_dummy | DDM:
        ...
    
    def unify(self, *others, fmt=...) -> tuple[Any, ...]:
        ...
    
    def to_Matrix(self) -> MutableDenseMatrix:
        ...
    
    def to_list(self) -> list[Any]:
        ...
    
    def to_list_flat(self) -> list[Any]:
        ...
    
    @classmethod
    def from_list_flat(cls, elements, shape, domain) -> Self:
        ...
    
    def to_flat_nz(self) -> tuple[list[Any], tuple[tuple[tuple[Any, Any], ...], Any]]:
        ...
    
    def from_flat_nz(self, elements, data, domain) -> Self:
        ...
    
    def to_dod(self) -> dict[Any, Any]:
        ...
    
    @classmethod
    def from_dod(cls, dod, shape, domain) -> Self:
        ...
    
    def from_dod_like(self, dod, domain=...) -> Self:
        ...
    
    def to_dok(self) -> dict[tuple[Any, Any], Any] | dict[Any, Any]:
        ...
    
    @classmethod
    def from_dok(cls, dok, shape, domain) -> Self:
        ...
    
    def nnz(self) -> int:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def transpose(self) -> Self:
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    @property
    def is_zero_matrix(self) -> bool:
        ...
    
    @property
    def is_upper(self) -> bool:
        ...
    
    @property
    def is_lower(self) -> bool:
        ...
    
    @property
    def is_diagonal(self) -> bool:
        ...
    
    def diagonal(self) -> list[Any]:
        ...
    
    @property
    def is_square(self) -> bool:
        ...
    
    def rank(self) -> int:
        ...
    
    def hstack(A, *B) -> DomainMatrix:
        ...
    
    def vstack(A, *B) -> DomainMatrix:
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
        ...
    
    def __rmul__(A, B) -> DomainMatrix | Self | NotImplementedType:
        ...
    
    def __pow__(A, n) -> NotImplementedType | Self:
        ...
    
    def add(A, B) -> Self:
        ...
    
    def sub(A, B) -> Self:
        ...
    
    def neg(A) -> Self:
        ...
    
    def mul(A, b) -> Self:
        ...
    
    def rmul(A, b) -> Self:
        ...
    
    def matmul(A, B) -> Self:
        ...
    
    def scalarmul(A, lamda) -> DomainMatrix | Self:
        ...
    
    def rscalarmul(A, lamda) -> DomainMatrix | Self:
        ...
    
    def mul_elementwise(A, B) -> Self:
        ...
    
    def __truediv__(A, lamda) -> NotImplementedType:
        ...
    
    def pow(A, n) -> Self:
        ...
    
    def scc(self) -> list[Any]:
        ...
    
    def clear_denoms(self, convert=...) -> tuple[DomainScalar, Self]:
        ...
    
    def clear_denoms_rowwise(self, convert=...) -> tuple[Self, Self]:
        ...
    
    def cancel_denom(self, denom) -> tuple[Self, Any]:
        ...
    
    def cancel_denom_elementwise(self, denom) -> tuple[Self, Self]:
        ...
    
    def content(self):
        ...
    
    def primitive(self) -> tuple[Any, Self]:
        ...
    
    def rref(self, *, method=...) -> tuple[Any, tuple[Any, ...]]:
        ...
    
    def rref_den(self, *, method=..., keep_domain=...) -> tuple[Any, Any, tuple[Any, ...]]:
        ...
    
    def columnspace(self) -> Self:
        ...
    
    def rowspace(self) -> Self:
        ...
    
    def nullspace(self, divide_last=...):
        ...
    
    def nullspace_from_rref(self, pivots=...) -> Self:
        ...
    
    def inv(self) -> Self:
        ...
    
    def det(self):
        ...
    
    def adj_det(self) -> tuple[Any, Any]:
        ...
    
    def adjugate(self):
        ...
    
    def inv_den(self, method=...) -> tuple[Any, Any]:
        ...
    
    def solve_den(self, b, method=...) -> tuple[Any, Any]:
        ...
    
    def solve_den_rref(self, b) -> tuple[Any, Any]:
        ...
    
    def solve_den_charpoly(self, b, cp=..., check=...) -> tuple[Any, Any]:
        ...
    
    def adj_poly_det(self, cp=...) -> tuple[list[Any] | Any, Any]:
        ...
    
    def eval_poly(self, p) -> Self:
        ...
    
    def eval_poly_mul(self, p, B):
        ...
    
    def lu(self) -> tuple[Self, Self, list[Any] | Any]:
        ...
    
    def lu_solve(self, rhs) -> Self:
        ...
    
    def charpoly(self) -> list[Any]:
        ...
    
    def charpoly_factor_list(self) -> list[Any]:
        ...
    
    def charpoly_factor_blocks(self) -> list[Any]:
        ...
    
    def charpoly_base(self) -> list[Any]:
        ...
    
    def charpoly_berk(self) -> list[Any]:
        ...
    
    @classmethod
    def eye(cls, shape, domain) -> Self:
        ...
    
    @classmethod
    def diag(cls, diagonal, domain, shape=...) -> Self:
        ...
    
    @classmethod
    def zeros(cls, shape, domain, *, fmt=...) -> Self:
        ...
    
    @classmethod
    def ones(cls, shape, domain) -> Self:
        ...
    
    def __eq__(A, B) -> bool:
        ...
    
    def unify_eq(A, B) -> Literal[False]:
        ...
    
    def lll(A, delta=...) -> DomainMatrix:
        ...
    
    def lll_transform(A, delta=...) -> tuple[DomainMatrix, DomainMatrix]:
        ...
    


