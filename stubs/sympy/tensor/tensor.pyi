from types import NotImplementedType
from typing import Any, Callable, Generator, Literal, LiteralString, Self
from abc import ABC, abstractmethod
from sympy import ImmutableDenseNDimArray, ImmutableSparseNDimArray, Indexed, MutableDenseNDimArray
from sympy.combinatorics.permutations import Perm
from sympy.core import Basic, Expr
from sympy.core.containers import Tuple
from sympy.core.sympify import CantSympify
from sympy.core.operations import AssocOp
from sympy.matrices import Matrix
from sympy.tensor.array.expressions.array_expressions import ArrayContraction, ArrayElement, ArrayTensorProduct, PermuteDims, ZeroArray
from sympy.utilities.decorator import deprecated, memoize_property

"""
This module defines tensors with abstract index notation.

The abstract index notation has been first formalized by Penrose.

Tensor indices are formal objects, with a tensor type; there is no
notion of index range, it is only possible to assign the dimension,
used to trace the Kronecker delta; the dimension can be a Symbol.

The Einstein summation convention is used.
The covariant indices are indicated with a minus sign in front of the index.

For instance the tensor ``t = p(a)*A(b,c)*q(-c)`` has the index ``c``
contracted.

A tensor expression ``t`` can be called; called with its
indices in sorted order it is equal to itself:
in the above example ``t(a, b) == t``;
one can call ``t`` with different indices; ``t(c, d) == p(c)*A(d,a)*q(-a)``.

The contracted indices are dummy indices, internally they have no name,
the indices being represented by a graph-like structure.

Tensors are put in canonical form using ``canon_bp``, which uses
the Butler-Portugal algorithm for canonicalization using the monoterm
symmetries of the tensors.

If there is a (anti)symmetric metric, the indices can be raised and
lowered when the tensor is put in canonical form.
"""
def deprecate_data() -> None:
    ...

def deprecate_fun_eval() -> None:
    ...

def deprecate_call() -> None:
    ...

class _IndexStructure(CantSympify):
    """
    This class handles the indices (free and dummy ones). It contains the
    algorithms to manage the dummy indices replacements and contractions of
    free indices under multiplications of tensor expressions, as well as stuff
    related to canonicalization sorting, getting the permutation of the
    expression and so on. It also includes tools to get the ``TensorIndex``
    objects corresponding to the given index structure.
    """
    def __init__(self, free, dum, index_types, indices, canon_bp=...) -> None:
        ...
    
    @staticmethod
    def from_indices(*indices) -> _IndexStructure:
        """
        Create a new ``_IndexStructure`` object from a list of ``indices``.

        Explanation
        ===========

        ``indices``     ``TensorIndex`` objects, the indices. Contractions are
                        detected upon construction.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, _IndexStructure
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2, m3 = tensor_indices('m0,m1,m2,m3', Lorentz)
        >>> _IndexStructure.from_indices(m0, m1, -m1, m3)
        _IndexStructure([(m0, 0), (m3, 3)], [(1, 2)], [Lorentz, Lorentz, Lorentz, Lorentz])
        """
        ...
    
    @staticmethod
    def from_components_free_dum(components, free, dum) -> _IndexStructure:
        ...
    
    def get_indices(self):
        """
        Get a list of indices, creating new tensor indices to complete dummy indices.
        """
        ...
    
    @staticmethod
    def generate_indices_from_free_dum_index_types(free, dum, index_types) -> list[Any]:
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        """
        Get a list of free indices.
        """
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> _IndexStructure:
        """
        Returns a ``_IndexStructure`` instance corresponding to the permutation ``g``.

        Explanation
        ===========

        ``g``  permutation corresponding to the tensor in the representation
        used in canonicalization

        ``is_canon_bp``   if True, then ``g`` is the permutation
        corresponding to the canonical form of the tensor
        """
        ...
    
    def indices_canon_args(self) -> tuple[Perm, list[Any], list[Any]]:
        """
        Returns ``(g, dummies, msym, v)``, the entries of ``canonicalize``

        See ``canonicalize`` in ``tensor_can.py`` in combinatorics module.
        """
        ...
    


def components_canon_args(components) -> list[Any]:
    ...

class _TensorDataLazyEvaluator(CantSympify):
    """
    EXPERIMENTAL: do not rely on this class, it may change without deprecation
    warnings in future versions of SymPy.

    Explanation
    ===========

    This object contains the logic to associate components data to a tensor
    expression. Components data are set via the ``.data`` property of tensor
    expressions, is stored inside this class as a mapping between the tensor
    expression and the ``ndarray``.

    Computations are executed lazily: whereas the tensor expressions can have
    contractions, tensor products, and additions, components data are not
    computed until they are accessed by reading the ``.data`` property
    associated to the tensor expression.
    """
    _substitutions_dict: dict[Any, Any] = ...
    _substitutions_dict_tensmul: dict[Any, Any] = ...
    def __getitem__(self, key) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @staticmethod
    def data_contract_dum(ndarray_list, dum, ext_rank) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | ImmutableDenseNDimArray | Any:
        ...
    
    def data_tensorhead_from_tensmul(self, data, tensmul, tensorhead) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | ImmutableDenseNDimArray | Any | None:
        """
        This method is used when assigning components data to a ``TensMul``
        object, it converts components data to a fully contravariant ndarray,
        which is then stored according to the ``TensorHead`` key.
        """
        ...
    
    def data_from_tensor(self, tensor) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | ImmutableDenseNDimArray | Any | None:
        """
        This method corrects the components data to the right signature
        (covariant/contravariant) using the metric associated with each
        ``TensorIndexType``.
        """
        ...
    
    def __setitem__(self, key, value) -> None:
        """
        Set the components data of a tensor object/expression.

        Explanation
        ===========

        Components data are transformed to the all-contravariant form and stored
        with the corresponding ``TensorHead`` object. If a ``TensorHead`` object
        cannot be uniquely identified, it will raise an error.
        """
        ...
    
    def __delitem__(self, key) -> None:
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    def add_metric_data(self, metric, data) -> None:
        """
        Assign data to the ``metric`` tensor. The metric tensor behaves in an
        anomalous way when raising and lowering indices.

        Explanation
        ===========

        A fully covariant metric is the inverse transpose of the fully
        contravariant metric (it is meant matrix inverse). If the metric is
        symmetric, the transpose is not necessary and mixed
        covariant/contravariant metrics are Kronecker deltas.
        """
        ...
    
    @staticmethod
    def inverse_matrix(ndarray) -> MutableDenseNDimArray:
        ...
    
    @staticmethod
    def inverse_transpose_matrix(ndarray) -> MutableDenseNDimArray:
        ...
    
    @staticmethod
    def add_rearrange_tensmul_parts(new_tensmul, old_tensmul) -> None:
        ...
    
    @staticmethod
    def parse_data(data) -> MutableDenseNDimArray:
        """
        Transform ``data`` to array. The parameter ``data`` may
        contain data in various formats, e.g. nested lists, SymPy ``Matrix``,
        and so on.

        Examples
        ========

        >>> from sympy.tensor.tensor import _TensorDataLazyEvaluator
        >>> _TensorDataLazyEvaluator.parse_data([1, 3, -6, 12])
        [1, 3, -6, 12]

        >>> _TensorDataLazyEvaluator.parse_data([[1, 2], [4, 7]])
        [[1, 2], [4, 7]]
        """
        ...
    


_tensor_data_substitution_dict = ...
class _TensorManager:
    """
    Class to manage tensor properties.

    Notes
    =====

    Tensors belong to tensor commutation groups; each group has a label
    ``comm``; there are predefined labels:

    ``0``   tensors commuting with any other tensor

    ``1``   tensors anticommuting among themselves

    ``2``   tensors not commuting, apart with those with ``comm=0``

    Other groups can be defined using ``set_comm``; tensors in those
    groups commute with those with ``comm=0``; by default they
    do not commute with any other group.
    """
    def __init__(self) -> None:
        ...
    
    @property
    def comm(self) -> list[dict[Any, Any]]:
        ...
    
    def comm_symbols2i(self, i) -> int:
        """
        Get the commutation group number corresponding to ``i``.

        ``i`` can be a symbol or a number or a string.

        If ``i`` is not already defined its commutation group number
        is set.
        """
        ...
    
    def comm_i2symbol(self, i) -> int:
        """
        Returns the symbol corresponding to the commutation group number.
        """
        ...
    
    def set_comm(self, i, j, c) -> None:
        """
        Set the commutation parameter ``c`` for commutation groups ``i, j``.

        Parameters
        ==========

        i, j : symbols representing commutation groups

        c  :  group commutation number

        Notes
        =====

        ``i, j`` can be symbols, strings or numbers,
        apart from ``0, 1`` and ``2`` which are reserved respectively
        for commuting, anticommuting tensors and tensors not commuting
        with any other group apart with the commuting tensors.
        For the remaining cases, use this method to set the commutation rules;
        by default ``c=None``.

        The group commutation number ``c`` is assigned in correspondence
        to the group commutation symbols; it can be

        0        commuting

        1        anticommuting

        None     no commutation property

        Examples
        ========

        ``G`` and ``GH`` do not commute with themselves and commute with
        each other; A is commuting.

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, TensorManager, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz')
        >>> i0,i1,i2,i3,i4 = tensor_indices('i0:5', Lorentz)
        >>> A = TensorHead('A', [Lorentz])
        >>> G = TensorHead('G', [Lorentz], TensorSymmetry.no_symmetry(1), 'Gcomm')
        >>> GH = TensorHead('GH', [Lorentz], TensorSymmetry.no_symmetry(1), 'GHcomm')
        >>> TensorManager.set_comm('Gcomm', 'GHcomm', 0)
        >>> (GH(i1)*G(i0)).canon_bp()
        G(i0)*GH(i1)
        >>> (G(i1)*G(i0)).canon_bp()
        G(i1)*G(i0)
        >>> (G(i1)*A(i0)).canon_bp()
        A(i0)*G(i1)
        """
        ...
    
    def set_comms(self, *args) -> None:
        """
        Set the commutation group numbers ``c`` for symbols ``i, j``.

        Parameters
        ==========

        args : sequence of ``(i, j, c)``
        """
        ...
    
    def get_comm(self, i, j):
        """
        Return the commutation parameter for commutation group numbers ``i, j``

        see ``_TensorManager.set_comm``
        """
        ...
    
    def clear(self) -> None:
        """
        Clear the TensorManager.
        """
        ...
    


TensorManager = ...
class TensorIndexType(Basic):
    """
    A TensorIndexType is characterized by its name and its metric.

    Parameters
    ==========

    name : name of the tensor type
    dummy_name : name of the head of dummy indices
    dim : dimension, it can be a symbol or an integer or ``None``
    eps_dim : dimension of the epsilon tensor
    metric_symmetry : integer that denotes metric symmetry or ``None`` for no metric
    metric_name : string with the name of the metric tensor

    Attributes
    ==========

    ``metric`` : the metric tensor
    ``delta`` : ``Kronecker delta``
    ``epsilon`` : the ``Levi-Civita epsilon`` tensor
    ``data`` : (deprecated) a property to add ``ndarray`` values, to work in a specified basis.

    Notes
    =====

    The possible values of the ``metric_symmetry`` parameter are:

        ``1``   :   metric tensor is fully symmetric
        ``0``   :   metric tensor possesses no index symmetry
        ``-1``  :   metric tensor is fully antisymmetric
        ``None``:   there is no metric tensor (metric equals to ``None``)

    The metric is assumed to be symmetric by default. It can also be set
    to a custom tensor by the ``.set_metric()`` method.

    If there is a metric the metric is used to raise and lower indices.

    In the case of non-symmetric metric, the following raising and
    lowering conventions will be adopted:

    ``psi(a) = g(a, b)*psi(-b); chi(-a) = chi(b)*g(-b, -a)``

    From these it is easy to find:

    ``g(-a, b) = delta(-a, b)``

    where ``delta(-a, b) = delta(b, -a)`` is the ``Kronecker delta``
    (see ``TensorIndex`` for the conventions on indices).
    For antisymmetric metrics there is also the following equality:

    ``g(a, -b) = -delta(a, -b)``

    If there is no metric it is not possible to raise or lower indices;
    e.g. the index of the defining representation of ``SU(N)``
    is 'covariant' and the conjugate representation is
    'contravariant'; for ``N > 2`` they are linearly independent.

    ``eps_dim`` is by default equal to ``dim``, if the latter is an integer;
    else it can be assigned (for use in naive dimensional regularization);
    if ``eps_dim`` is not an integer ``epsilon`` is ``None``.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> Lorentz.metric
    metric(Lorentz,Lorentz)
    """
    def __new__(cls, name, dummy_name=..., dim=..., eps_dim=..., metric_symmetry=..., metric_name=..., **kwargs) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def dummy_name(self):
        ...
    
    @property
    def dim(self) -> Basic:
        ...
    
    @property
    def eps_dim(self) -> Basic:
        ...
    
    @memoize_property
    def metric(self) -> TensorHead | None:
        ...
    
    @memoize_property
    def delta(self) -> TensorHead:
        ...
    
    @memoize_property
    def epsilon(self) -> TensorHead | None:
        ...
    
    def set_metric(self, tensor) -> None:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    @deprecated("""
        The TensorIndexType.get_kronecker_delta() method is deprecated. Use
        the TensorIndexType.delta attribute instead.
        """, deprecated_since_version="1.5", active_deprecations_target="deprecated-tensorindextype-methods")
    def get_kronecker_delta(self) -> TensorHead:
        ...
    
    @deprecated("""
        The TensorIndexType.get_epsilon() method is deprecated. Use
        the TensorIndexType.epsilon attribute instead.
        """, deprecated_since_version="1.5", active_deprecations_target="deprecated-tensorindextype-methods")
    def get_epsilon(self) -> TensorHead | None:
        ...
    


class TensorIndex(Basic):
    """
    Represents a tensor index

    Parameters
    ==========

    name : name of the index, or ``True`` if you want it to be automatically assigned
    tensor_index_type : ``TensorIndexType`` of the index
    is_up :  flag for contravariant index (is_up=True by default)

    Attributes
    ==========

    ``name``
    ``tensor_index_type``
    ``is_up``

    Notes
    =====

    Tensor indices are contracted with the Einstein summation convention.

    An index can be in contravariant or in covariant form; in the latter
    case it is represented prepending a ``-`` to the index name. Adding
    ``-`` to a covariant (is_up=False) index makes it contravariant.

    Dummy indices have a name with head given by
    ``tensor_inde_type.dummy_name`` with underscore and a number.

    Similar to ``symbols`` multiple contravariant indices can be created
    at once using ``tensor_indices(s, typ)``, where ``s`` is a string
    of names.


    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, TensorIndex, TensorHead, tensor_indices
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> mu = TensorIndex('mu', Lorentz, is_up=False)
    >>> nu, rho = tensor_indices('nu, rho', Lorentz)
    >>> A = TensorHead('A', [Lorentz, Lorentz])
    >>> A(mu, nu)
    A(-mu, nu)
    >>> A(-mu, -rho)
    A(mu, -rho)
    >>> A(mu, -mu)
    A(-L_0, L_0)
    """
    def __new__(cls, name, tensor_index_type, is_up=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def tensor_index_type(self) -> Basic:
        ...
    
    @property
    def is_up(self) -> Basic:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __neg__(self) -> TensorIndex:
        ...
    


def tensor_indices(s, typ) -> TensorIndex | list[TensorIndex]:
    """
    Returns list of tensor indices given their names and their types.

    Parameters
    ==========

    s : string of comma separated names of indices

    typ : ``TensorIndexType`` of the indices

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> a, b, c, d = tensor_indices('a,b,c,d', Lorentz)
    """
    ...

class TensorSymmetry(Basic):
    """
    Monoterm symmetry of a tensor (i.e. any symmetric or anti-symmetric
    index permutation). For the relevant terminology see ``tensor_can.py``
    section of the combinatorics module.

    Parameters
    ==========

    bsgs : tuple ``(base, sgs)`` BSGS of the symmetry of the tensor

    Attributes
    ==========

    ``base`` : base of the BSGS
    ``generators`` : generators of the BSGS
    ``rank`` : rank of the tensor

    Notes
    =====

    A tensor can have an arbitrary monoterm symmetry provided by its BSGS.
    Multiterm symmetries, like the cyclic symmetry of the Riemann tensor
    (i.e., Bianchi identity), are not covered. See combinatorics module for
    information on how to generate BSGS for a general index permutation group.
    Simple symmetries can be generated using built-in methods.

    See Also
    ========

    sympy.combinatorics.tensor_can.get_symmetric_group_sgs

    Examples
    ========

    Define a symmetric tensor of rank 2

    >>> from sympy.tensor.tensor import TensorIndexType, TensorSymmetry, get_symmetric_group_sgs, TensorHead
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> sym = TensorSymmetry(get_symmetric_group_sgs(2))
    >>> T = TensorHead('T', [Lorentz]*2, sym)

    Note, that the same can also be done using built-in TensorSymmetry methods

    >>> sym2 = TensorSymmetry.fully_symmetric(2)
    >>> sym == sym2
    True
    """
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def generators(self) -> Basic:
        ...
    
    @property
    def rank(self):
        ...
    
    @classmethod
    def fully_symmetric(cls, rank) -> TensorSymmetry:
        """
        Returns a fully symmetric (antisymmetric if ``rank``<0)
        TensorSymmetry object for ``abs(rank)`` indices.
        """
        ...
    
    @classmethod
    def direct_product(cls, *args) -> TensorSymmetry:
        """
        Returns a TensorSymmetry object that is being a direct product of
        fully (anti-)symmetric index permutation groups.

        Notes
        =====

        Some examples for different values of ``(*args)``:
        ``(1)``         vector, equivalent to ``TensorSymmetry.fully_symmetric(1)``
        ``(2)``         tensor with 2 symmetric indices, equivalent to ``.fully_symmetric(2)``
        ``(-2)``        tensor with 2 antisymmetric indices, equivalent to ``.fully_symmetric(-2)``
        ``(2, -2)``     tensor with the first 2 indices commuting and the last 2 anticommuting
        ``(1, 1, 1)``   tensor with 3 indices without any symmetry
        """
        ...
    
    @classmethod
    def riemann(cls) -> TensorSymmetry:
        """
        Returns a monotorem symmetry of the Riemann tensor
        """
        ...
    
    @classmethod
    def no_symmetry(cls, rank) -> TensorSymmetry:
        """
        TensorSymmetry object for ``rank`` indices with no symmetry
        """
        ...
    


@deprecated("""
    The tensorsymmetry() function is deprecated. Use the TensorSymmetry
    constructor instead.
    """, deprecated_since_version="1.5", active_deprecations_target="deprecated-tensorsymmetry")
def tensorsymmetry(*args) -> TensorSymmetry:
    """
    Returns a ``TensorSymmetry`` object. This method is deprecated, use
    ``TensorSymmetry.direct_product()`` or ``.riemann()`` instead.

    Explanation
    ===========

    One can represent a tensor with any monoterm slot symmetry group
    using a BSGS.

    ``args`` can be a BSGS
    ``args[0]``    base
    ``args[1]``    sgs

    Usually tensors are in (direct products of) representations
    of the symmetric group;
    ``args`` can be a list of lists representing the shapes of Young tableaux

    Notes
    =====

    For instance:
    ``[[1]]``       vector
    ``[[1]*n]``     symmetric tensor of rank ``n``
    ``[[n]]``       antisymmetric tensor of rank ``n``
    ``[[2, 2]]``    monoterm slot symmetry of the Riemann tensor
    ``[[1],[1]]``   vector*vector
    ``[[2],[1],[1]`` (antisymmetric tensor)*vector*vector

    Notice that with the shape ``[2, 2]`` we associate only the monoterm
    symmetries of the Riemann tensor; this is an abuse of notation,
    since the shape ``[2, 2]`` corresponds usually to the irreducible
    representation characterized by the monoterm symmetries and by the
    cyclic symmetry.
    """
    ...

@deprecated("TensorType is deprecated. Use tensor_heads() instead.", deprecated_since_version="1.5", active_deprecations_target="deprecated-tensortype")
class TensorType(Basic):
    """
    Class of tensor types. Deprecated, use tensor_heads() instead.

    Parameters
    ==========

    index_types : list of ``TensorIndexType`` of the tensor indices
    symmetry : ``TensorSymmetry`` of the tensor

    Attributes
    ==========

    ``index_types``
    ``symmetry``
    ``types`` : list of ``TensorIndexType`` without repetitions
    """
    is_commutative = ...
    def __new__(cls, index_types, symmetry, **kw_args) -> Self:
        ...
    
    @property
    def index_types(self) -> Basic:
        ...
    
    @property
    def symmetry(self) -> Basic:
        ...
    
    @property
    def types(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, s, comm=...) -> TensorHead | list[TensorHead]:
        """
        Return a TensorHead object or a list of TensorHead objects.

        Parameters
        ==========

        s : name or string of names.

        comm : Commutation group.

        see ``_TensorManager.set_comm``
        """
        ...
    


@deprecated("""
    The tensorhead() function is deprecated. Use tensor_heads() instead.
    """, deprecated_since_version="1.5", active_deprecations_target="deprecated-tensorhead")
def tensorhead(name, typ, sym=..., comm=...) -> TensorHead:
    """
    Function generating tensorhead(s). This method is deprecated,
    use TensorHead constructor or tensor_heads() instead.

    Parameters
    ==========

    name : name or sequence of names (as in ``symbols``)

    typ :  index types

    sym :  same as ``*args`` in ``tensorsymmetry``

    comm : commutation group number
    see ``_TensorManager.set_comm``
    """
    ...

class TensorHead(Basic):
    """
    Tensor head of the tensor.

    Parameters
    ==========

    name : name of the tensor
    index_types : list of TensorIndexType
    symmetry : TensorSymmetry of the tensor
    comm : commutation group number

    Attributes
    ==========

    ``name``
    ``index_types``
    ``rank`` : total number of indices
    ``symmetry``
    ``comm`` : commutation group

    Notes
    =====

    Similar to ``symbols`` multiple TensorHeads can be created using
    ``tensorhead(s, typ, sym=None, comm=0)`` function, where ``s``
    is the string of names and ``sym`` is the monoterm tensor symmetry
    (see ``tensorsymmetry``).

    A ``TensorHead`` belongs to a commutation group, defined by a
    symbol on number ``comm`` (see ``_TensorManager.set_comm``);
    tensors in a commutation group have the same commutation properties;
    by default ``comm`` is ``0``, the group of the commuting tensors.

    Examples
    ========

    Define a fully antisymmetric tensor of rank 2:

    >>> from sympy.tensor.tensor import TensorIndexType, TensorHead, TensorSymmetry
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> asym2 = TensorSymmetry.fully_symmetric(-2)
    >>> A = TensorHead('A', [Lorentz, Lorentz], asym2)

    Examples with ndarray values, the components data assigned to the
    ``TensorHead`` object are assumed to be in a fully-contravariant
    representation. In case it is necessary to assign components data which
    represents the values of a non-fully covariant tensor, see the other
    examples.

    >>> from sympy.tensor.tensor import tensor_indices
    >>> from sympy import diag
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> i0, i1 = tensor_indices('i0:2', Lorentz)

    Specify a replacement dictionary to keep track of the arrays to use for
    replacements in the tensorial expression. The ``TensorIndexType`` is
    associated to the metric used for contractions (in fully covariant form):

    >>> repl = {Lorentz: diag(1, -1, -1, -1)}

    Let's see some examples of working with components with the electromagnetic
    tensor:

    >>> from sympy import symbols
    >>> Ex, Ey, Ez, Bx, By, Bz = symbols('E_x E_y E_z B_x B_y B_z')
    >>> c = symbols('c', positive=True)

    Let's define `F`, an antisymmetric tensor:

    >>> F = TensorHead('F', [Lorentz, Lorentz], asym2)

    Let's update the dictionary to contain the matrix to use in the
    replacements:

    >>> repl.update({F(-i0, -i1): [
    ... [0, Ex/c, Ey/c, Ez/c],
    ... [-Ex/c, 0, -Bz, By],
    ... [-Ey/c, Bz, 0, -Bx],
    ... [-Ez/c, -By, Bx, 0]]})

    Now it is possible to retrieve the contravariant form of the Electromagnetic
    tensor:

    >>> F(i0, i1).replace_with_arrays(repl, [i0, i1])
    [[0, -E_x/c, -E_y/c, -E_z/c], [E_x/c, 0, -B_z, B_y], [E_y/c, B_z, 0, -B_x], [E_z/c, -B_y, B_x, 0]]

    and the mixed contravariant-covariant form:

    >>> F(i0, -i1).replace_with_arrays(repl, [i0, -i1])
    [[0, E_x/c, E_y/c, E_z/c], [E_x/c, 0, B_z, -B_y], [E_y/c, -B_z, 0, B_x], [E_z/c, B_y, -B_x, 0]]

    Energy-momentum of a particle may be represented as:

    >>> from sympy import symbols
    >>> P = TensorHead('P', [Lorentz], TensorSymmetry.no_symmetry(1))
    >>> E, px, py, pz = symbols('E p_x p_y p_z', positive=True)
    >>> repl.update({P(i0): [E, px, py, pz]})

    The contravariant and covariant components are, respectively:

    >>> P(i0).replace_with_arrays(repl, [i0])
    [E, p_x, p_y, p_z]
    >>> P(-i0).replace_with_arrays(repl, [-i0])
    [E, -p_x, -p_y, -p_z]

    The contraction of a 1-index tensor by itself:

    >>> expr = P(i0)*P(-i0)
    >>> expr.replace_with_arrays(repl, [])
    E**2 - p_x**2 - p_y**2 - p_z**2
    """
    is_commutative = ...
    def __new__(cls, name, index_types, symmetry=..., comm=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def index_types(self) -> list[Any]:
        ...
    
    @property
    def symmetry(self) -> Basic:
        ...
    
    @property
    def rank(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def commutes_with(self, other):
        """
        Returns ``0`` if ``self`` and ``other`` commute, ``1`` if they anticommute.

        Returns ``None`` if ``self`` and ``other`` neither commute nor anticommute.
        """
        ...
    
    def __call__(self, *indices, **kw_args) -> TensExpr:
        """
        Returns a tensor with indices.

        Explanation
        ===========

        There is a special behavior in case of indices denoted by ``True``,
        they are considered auto-matrix indices, their slots are automatically
        filled, and confer to the tensor the behavior of a matrix or vector
        upon multiplication with another tensor containing auto-matrix indices
        of the same ``TensorIndexType``. This means indices get summed over the
        same way as in matrix multiplication. For matrix behavior, define two
        auto-matrix indices, for vector behavior define just one.

        Indices can also be strings, in which case the attribute
        ``index_types`` is used to convert them to proper ``TensorIndex``.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorSymmetry, TensorHead
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> a, b = tensor_indices('a,b', Lorentz)
        >>> A = TensorHead('A', [Lorentz]*2, TensorSymmetry.no_symmetry(2))
        >>> t = A(a, -b)
        >>> t
        A(a, -b)

        """
        ...
    
    def __pow__(self, other):
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    


def tensor_heads(s, index_types, symmetry=..., comm=...) -> TensorHead | list[TensorHead]:
    """
    Returns a sequence of TensorHeads from a string `s`
    """
    ...

class TensExpr(Expr, ABC):
    """
    Abstract base class for tensor expressions

    Notes
    =====

    A tensor expression is an expression formed by tensors;
    currently the sums of tensors are distributed.

    A ``TensExpr`` can be a ``TensAdd`` or a ``TensMul``.

    ``TensMul`` objects are formed by products of component tensors,
    and include a coefficient, which is a SymPy expression.


    In the internal representation contracted indices are represented
    by ``(ipos1, ipos2, icomp1, icomp2)``, where ``icomp1`` is the position
    of the component tensor with contravariant index, ``ipos1`` is the
    slot which the index occupies in that component tensor.

    Contracted indices are therefore nameless in the internal representation.
    """
    _op_priority = ...
    is_commutative = ...
    def __neg__(self):
        ...
    
    def __abs__(self):
        ...
    
    def __add__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __radd__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __sub__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __rsub__(self, other) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def __mul__(self, other) -> TensExpr | TensMul:
        """
        Multiply two tensors using Einstein summation convention.

        Explanation
        ===========

        If the two tensors have an index in common, one contravariant
        and the other covariant, in their product the indices are summed

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t1 = p(m0)
        >>> t2 = q(-m0)
        >>> t1*t2
        p(L_0)*q(-L_0)
        """
        ...
    
    def __rmul__(self, other) -> TensExpr | TensMul:
        ...
    
    def __truediv__(self, other) -> TensExpr | TensMul:
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __pow__(self, other):
        ...
    
    def __rpow__(self, other):
        ...
    
    @property
    @abstractmethod
    def nocoeff(self):
        ...
    
    @property
    @abstractmethod
    def coeff(self):
        ...
    
    @abstractmethod
    def get_indices(self):
        ...
    
    @abstractmethod
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    def fun_eval(self, *index_tuples):
        ...
    
    def get_matrix(self) -> Matrix:
        """
        DEPRECATED: do not use.

        Returns ndarray components data as a matrix, if components data are
        available and ndarray dimension does not exceed 2.
        """
        ...
    
    def expand(self, **hints) -> Self:
        ...
    
    def replace_with_arrays(self, replacement_dict, indices=...) -> ArrayElement | Indexed | ImmutableSparseNDimArray | ImmutableDenseNDimArray | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims:
        """
        Replace the tensorial expressions with arrays. The final array will
        correspond to the N-dimensional array with indices arranged according
        to ``indices``.

        Parameters
        ==========

        replacement_dict
            dictionary containing the replacement rules for tensors.
        indices
            the index order with respect to which the array is read. The
            original index order will be used if no value is passed.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices
        >>> from sympy.tensor.tensor import TensorHead
        >>> from sympy import symbols, diag

        >>> L = TensorIndexType("L")
        >>> i, j = tensor_indices("i j", L)
        >>> A = TensorHead("A", [L])
        >>> A(i).replace_with_arrays({A(i): [1, 2]}, [i])
        [1, 2]

        Since 'indices' is optional, we can also call replace_with_arrays by
        this way if no specific index order is needed:

        >>> A(i).replace_with_arrays({A(i): [1, 2]})
        [1, 2]

        >>> expr = A(i)*A(j)
        >>> expr.replace_with_arrays({A(i): [1, 2]})
        [[1, 2], [2, 4]]

        For contractions, specify the metric of the ``TensorIndexType``, which
        in this case is ``L``, in its covariant form:

        >>> expr = A(i)*A(-i)
        >>> expr.replace_with_arrays({A(i): [1, 2], L: diag(1, -1)})
        -3

        Symmetrization of an array:

        >>> H = TensorHead("H", [L, L])
        >>> a, b, c, d = symbols("a b c d")
        >>> expr = H(i, j)/2 + H(j, i)/2
        >>> expr.replace_with_arrays({H(i, j): [[a, b], [c, d]]})
        [[a, b/2 + c/2], [b/2 + c/2, d]]

        Anti-symmetrization of an array:

        >>> expr = H(i, j)/2 - H(j, i)/2
        >>> repl = {H(i, j): [[a, b], [c, d]]}
        >>> expr.replace_with_arrays(repl)
        [[0, b/2 - c/2], [-b/2 + c/2, 0]]

        The same expression can be read as the transpose by inverting ``i`` and
        ``j``:

        >>> expr.replace_with_arrays(repl, [j, i])
        [[0, -b/2 + c/2], [b/2 - c/2, 0]]
        """
        ...
    


class TensAdd(TensExpr, AssocOp):
    """
    Sum of tensors.

    Parameters
    ==========

    free_args : list of the free indices

    Attributes
    ==========

    ``args`` : tuple of addends
    ``rank`` : rank of the tensor
    ``free_args`` : list of the free indices in sorted order

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_heads, tensor_indices
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> a, b = tensor_indices('a,b', Lorentz)
    >>> p, q = tensor_heads('p,q', [Lorentz])
    >>> t = p(a) + q(a); t
    p(a) + q(a)

    Examples with components data added to the tensor expression:

    >>> from sympy import symbols, diag
    >>> x, y, z, t = symbols("x y z t")
    >>> repl = {}
    >>> repl[Lorentz] = diag(1, -1, -1, -1)
    >>> repl[p(a)] = [1, 2, 3, 4]
    >>> repl[q(a)] = [x, y, z, t]

    The following are: 2**2 - 3**2 - 2**2 - 7**2 ==> -58

    >>> expr = p(a) + q(a)
    >>> expr.replace_with_arrays(repl, [a])
    [x + 1, y + 2, z + 3, t + 4]
    """
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> Self:
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        ...
    
    @memoize_property
    def rank(self) -> Literal[0]:
        ...
    
    @memoize_property
    def free_args(self) -> list[Any]:
        ...
    
    @memoize_property
    def free_indices(self) -> list[TensorIndex] | set[Any]:
        ...
    
    def doit(self, **hints) -> Basic | TensExpr | TensMul | Expr | Self:
        ...
    
    def get_indices(self) -> list[Any]:
        ...
    
    def __call__(self, *indices) -> Self | Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    def canon_bp(self) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        """
        Canonicalize using the Butler-Portugal algorithm for canonicalization
        under monoterm symmetries.
        """
        ...
    
    def equals(self, other) -> bool | NotImplementedType:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    def contract_delta(self, delta) -> TensMul | TensExpr | Basic | Expr | TensAdd:
        ...
    
    def contract_metric(self, g) -> TensMul | TensExpr | Basic | Expr | TensAdd:
        """
        Raise or lower indices with the metric ``g``.

        Parameters
        ==========

        g :  metric

        contract_all : if True, eliminate all ``g`` which are contracted

        Notes
        =====

        see the ``TensorIndexType`` docstring for the contraction conventions
        """
        ...
    
    def substitute_indices(self, *index_tuples) -> Basic | TensExpr | TensMul | Expr | TensAdd:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    


class Tensor(TensExpr):
    """
    Base tensor class, i.e. this represents a tensor, the single unit to be
    put into an expression.

    Explanation
    ===========

    This object is usually created from a ``TensorHead``, by attaching indices
    to it. Indices preceded by a minus sign are considered contravariant,
    otherwise covariant.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead
    >>> Lorentz = TensorIndexType("Lorentz", dummy_name="L")
    >>> mu, nu = tensor_indices('mu nu', Lorentz)
    >>> A = TensorHead("A", [Lorentz, Lorentz])
    >>> A(mu, -nu)
    A(mu, -nu)
    >>> A(mu, -mu)
    A(L_0, -L_0)

    It is also possible to use symbols instead of inidices (appropriate indices
    are then generated automatically).

    >>> from sympy import Symbol
    >>> x = Symbol('x')
    >>> A(x, mu)
    A(x, mu)
    >>> A(x, -x)
    A(L_0, -L_0)

    """
    is_commutative = ...
    _index_structure: _IndexStructure = ...
    args: tuple[TensorHead, Tuple]
    def __new__(cls, tensor_head, indices, *, is_canon_bp=..., **kw_args) -> Self:
        ...
    
    @property
    def free(self):
        ...
    
    @property
    def dum(self):
        ...
    
    @property
    def ext_rank(self):
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self):
        ...
    
    @property
    def component(self):
        ...
    
    @property
    def components(self):
        ...
    
    @property
    def head(self) -> TensorHead:
        ...
    
    @property
    def indices(self) -> Tuple:
        ...
    
    @property
    def free_indices(self) -> set[TensorIndex]:
        ...
    
    @property
    def index_types(self) -> list[Any]:
        ...
    
    @property
    def rank(self) -> int:
        ...
    
    def doit(self, **hints) -> TensExpr:
        ...
    
    @property
    def free_in_args(self) -> list[tuple[Any, Any, Literal[0]]]:
        ...
    
    @property
    def dum_in_args(self) -> list[tuple[Any, Any, Literal[0], Literal[0]]]:
        ...
    
    @property
    def free_args(self) -> list[Any]:
        ...
    
    def commutes_with(self, other) -> type[NotImplementedError] | Literal[0]:
        """
        :param other:
        :return:
            0  commute
            1  anticommute
            None  neither commute nor anticommute
        """
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> TensExpr:
        """
        Returns the tensor corresponding to the permutation ``g``.

        For further details, see the method in ``TIDS`` with the same name.
        """
        ...
    
    def canon_bp(self) -> Self | TensExpr:
        ...
    
    def split(self) -> list[Self]:
        ...
    
    def sorted_components(self) -> Self:
        ...
    
    def get_indices(self) -> list[TensorIndex]:
        """
        Get a list of indices, corresponding to those of the tensor.
        """
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        """
        Get a list of free indices, corresponding to those of the tensor.
        """
        ...
    
    def as_base_exp(self) -> tuple[Self, Any]:
        ...
    
    def substitute_indices(self, *index_tuples) -> TensExpr:
        """
        Return a tensor with free indices substituted according to ``index_tuples``.

        ``index_types`` list of tuples ``(old_index, new_index)``.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> i, j, k, l = tensor_indices('i,j,k,l', Lorentz)
        >>> A, B = tensor_heads('A,B', [Lorentz]*2, TensorSymmetry.fully_symmetric(2))
        >>> t = A(i, k)*B(-k, -j); t
        A(i, L_0)*B(-L_0, -j)
        >>> t.substitute_indices((i, k),(-j, l))
        A(k, L_0)*B(-L_0, l)
        """
        ...
    
    def __call__(self, *indices) -> Self | TensExpr:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data) -> None:
        ...
    
    @data.deleter
    def data(self) -> None:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def contract_metric(self, g) -> Self:
        ...
    
    def contract_delta(self, metric) -> Self:
        ...
    


class TensMul(TensExpr, AssocOp):
    """
    Product of tensors.

    Parameters
    ==========

    coeff : SymPy coefficient of the tensor
    args

    Attributes
    ==========

    ``components`` : list of ``TensorHead`` of the component tensors
    ``types`` : list of nonrepeated ``TensorIndexType``
    ``free`` : list of ``(ind, ipos, icomp)``, see Notes
    ``dum`` : list of ``(ipos1, ipos2, icomp1, icomp2)``, see Notes
    ``ext_rank`` : rank of the tensor counting the dummy indices
    ``rank`` : rank of the tensor
    ``coeff`` : SymPy coefficient of the tensor
    ``free_args`` : list of the free indices in sorted order
    ``is_canon_bp`` : ``True`` if the tensor in in canonical form

    Notes
    =====

    ``args[0]``   list of ``TensorHead`` of the component tensors.

    ``args[1]``   list of ``(ind, ipos, icomp)``
    where ``ind`` is a free index, ``ipos`` is the slot position
    of ``ind`` in the ``icomp``-th component tensor.

    ``args[2]`` list of tuples representing dummy indices.
    ``(ipos1, ipos2, icomp1, icomp2)`` indicates that the contravariant
    dummy index is the ``ipos1``-th slot position in the ``icomp1``-th
    component tensor; the corresponding covariant index is
    in the ``ipos2`` slot position in the ``icomp2``-th component tensor.

    """
    identity = ...
    _index_structure: _IndexStructure = ...
    def __new__(cls, *args, **kw_args) -> Self:
        ...
    
    index_types = ...
    free = ...
    dum = ...
    free_indices = ...
    rank = ...
    ext_rank = ...
    def doit(self, **hints) -> TensExpr | Self:
        ...
    
    @staticmethod
    def from_data(coeff, components, free, dum, **kw_args) -> TensExpr | TensMul:
        ...
    
    @property
    def free_args(self) -> list[Any]:
        ...
    
    @property
    def components(self) -> list[Any]:
        ...
    
    @property
    def free_in_args(self) -> list[tuple[Any, Any, Any]]:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> TensExpr | Self:
        ...
    
    @property
    def dum_in_args(self) -> list[tuple[Any, Any, Any, Any]]:
        ...
    
    def equals(self, other):
        ...
    
    def get_indices(self):
        """
        Returns the list of indices of the tensor.

        Explanation
        ===========

        The indices are listed in the order in which they appear in the
        component tensors.
        The dummy indices are given a name which does not collide with
        the names of the free indices.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m1)*g(m0,m2)
        >>> t.get_indices()
        [m1, m0, m2]
        >>> t2 = p(m1)*g(-m1, m2)
        >>> t2.get_indices()
        [L_0, -L_0, m2]
        """
        ...
    
    def get_free_indices(self) -> list[TensorIndex]:
        """
        Returns the list of free indices of the tensor.

        Explanation
        ===========

        The indices are listed in the order in which they appear in the
        component tensors.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m1)*g(m0,m2)
        >>> t.get_free_indices()
        [m1, m0, m2]
        >>> t2 = p(m1)*g(-m1, m2)
        >>> t2.get_free_indices()
        [m2]
        """
        ...
    
    def split(self) -> list[Self] | list[Any]:
        """
        Returns a list of tensors, whose product is ``self``.

        Explanation
        ===========

        Dummy indices contracted among different tensor components
        become free indices with the same name as the one used to
        represent the dummy indices.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> a, b, c, d = tensor_indices('a,b,c,d', Lorentz)
        >>> A, B = tensor_heads('A,B', [Lorentz]*2, TensorSymmetry.fully_symmetric(2))
        >>> t = A(a,b)*B(-b,c)
        >>> t
        A(a, L_0)*B(-L_0, c)
        >>> t.split()
        [A(a, L_0), B(-L_0, c)]
        """
        ...
    
    def __neg__(self) -> TensExpr | TensMul:
        ...
    
    def __getitem__(self, item) -> Any | ArrayElement | Indexed | ImmutableDenseNDimArray | Basic:
        ...
    
    def sorted_components(self) -> TensExpr | TensMul:
        """
        Returns a tensor product with sorted components.
        """
        ...
    
    def perm2tensor(self, g, is_canon_bp=...) -> TensExpr | TensMul:
        """
        Returns the tensor corresponding to the permutation ``g``

        For further details, see the method in ``TIDS`` with the same name.
        """
        ...
    
    def canon_bp(self) -> Self | TensMul | TensExpr:
        """
        Canonicalize using the Butler-Portugal algorithm for canonicalization
        under monoterm symmetries.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> A = TensorHead('A', [Lorentz]*2, TensorSymmetry.fully_symmetric(-2))
        >>> t = A(m0,-m1)*A(m1,-m0)
        >>> t.canon_bp()
        -A(L_0, L_1)*A(-L_0, -L_1)
        >>> t = A(m0,-m1)*A(m1,-m2)*A(m2,-m0)
        >>> t.canon_bp()
        0
        """
        ...
    
    def contract_delta(self, delta):
        ...
    
    def contract_metric(self, g):
        """
        Raise or lower indices with the metric ``g``.

        Parameters
        ==========

        g : metric

        Notes
        =====

        See the ``TensorIndexType`` docstring for the contraction conventions.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m0)*q(m1)*g(-m0, -m1)
        >>> t.canon_bp()
        metric(L_0, L_1)*p(-L_0)*q(-L_1)
        >>> t.contract_metric(g).canon_bp()
        p(L_0)*q(-L_0)
        """
        ...
    
    def substitute_indices(self, *index_tuples) -> TensExpr | TensMul:
        ...
    
    def __call__(self, *indices) -> Self | TensExpr | TensMul:
        ...
    
    @property
    def data(self) -> Any | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | Indexed | ImmutableDenseNDimArray | None:
        ...
    
    @data.setter
    def data(self, data):
        ...
    
    @data.deleter
    def data(self):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None] | Any:
        ...
    


class TensorElement(TensExpr):
    """
    Tensor with evaluated components.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, TensorHead, TensorSymmetry
    >>> from sympy import symbols
    >>> L = TensorIndexType("L")
    >>> i, j, k = symbols("i j k")
    >>> A = TensorHead("A", [L, L], TensorSymmetry.fully_symmetric(2))
    >>> A(i, j).get_free_indices()
    [i, j]

    If we want to set component ``i`` to a specific value, use the
    ``TensorElement`` class:

    >>> from sympy.tensor.tensor import TensorElement
    >>> te = TensorElement(A(i, j), {i: 2})

    As index ``i`` has been accessed (``{i: 2}`` is the evaluation of its 3rd
    element), the free indices will only contain ``j``:

    >>> te.get_free_indices()
    [j]
    """
    def __new__(cls, expr, index_map) -> TensExpr | Tensor | Self:
        ...
    
    @property
    def free(self) -> list[tuple[Any, int]]:
        ...
    
    @property
    def dum(self) -> list[Any]:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def index_map(self) -> Basic:
        ...
    
    @property
    def coeff(self):
        ...
    
    @property
    def nocoeff(self) -> Self:
        ...
    
    def get_free_indices(self):
        ...
    
    def get_indices(self):
        ...
    


class WildTensorHead(TensorHead):
    """
    A wild object that is used to create ``WildTensor`` instances

    Explanation
    ===========

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorHead, TensorIndex, WildTensorHead, TensorIndexType
    >>> R3 = TensorIndexType('R3', dim=3)
    >>> p = TensorIndex('p', R3)
    >>> q = TensorIndex('q', R3)

    A WildTensorHead can be created without specifying a ``TensorIndexType``

    >>> W = WildTensorHead("W")

    Calling it with a ``TensorIndex`` creates a ``WildTensor`` instance.

    >>> type(W(p))
    <class 'sympy.tensor.tensor.WildTensor'>

    The ``TensorIndexType`` is automatically detected from the index that is passed

    >>> W(p).component
    W(R3)

    Calling it with no indices returns an object that can match tensors with any number of indices.

    >>> K = TensorHead('K', [R3])
    >>> Q = TensorHead('Q', [R3, R3])
    >>> W().matches(K(p))
    {W: K(p)}
    >>> W().matches(Q(p,q))
    {W: Q(p, q)}

    If you want to ignore the order of indices while matching, pass ``unordered_indices=True``.

    >>> U = WildTensorHead("U", unordered_indices=True)
    >>> W(p,q).matches(Q(q,p))
    >>> U(p,q).matches(Q(q,p))
    {U(R3,R3): _WildTensExpr(Q(q, p))}

    Parameters
    ==========
    name : name of the tensor
    unordered_indices : whether the order of the indices matters for matching
        (default: False)

    See also
    ========
    ``WildTensor``
    ``TensorHead``

    """
    def __new__(cls, name, index_types=..., symmetry=..., comm=..., unordered_indices=...) -> Self:
        ...
    
    def __call__(self, *indices, **kwargs) -> TensExpr:
        ...
    


class WildTensor(Tensor):
    """
    A wild object which matches ``Tensor`` instances

    Explanation
    ===========
    This is instantiated by attaching indices to a ``WildTensorHead`` instance.

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorHead, TensorIndex, WildTensorHead, TensorIndexType
    >>> W = WildTensorHead("W")
    >>> R3 = TensorIndexType('R3', dim=3)
    >>> p = TensorIndex('p', R3)
    >>> q = TensorIndex('q', R3)
    >>> K = TensorHead('K', [R3])
    >>> Q = TensorHead('Q', [R3, R3])

    Matching also takes the indices into account
    >>> W(p).matches(K(p))
    {W(R3): _WildTensExpr(K(p))}
    >>> W(p).matches(K(q))
    >>> W(p).matches(K(-p))

    If you want to match objects with any number of indices, just use a ``WildTensor`` with no indices.
    >>> W().matches(K(p))
    {W: K(p)}
    >>> W().matches(Q(p,q))
    {W: Q(p, q)}

    See Also
    ========
    ``WildTensorHead``
    ``Tensor``

    """
    def __new__(cls, tensor_head, indices, **kw_args) -> Tensor | Self:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    


class WildTensorIndex(TensorIndex):
    """
    A wild object that matches TensorIndex instances.

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorIndex, TensorIndexType, WildTensorIndex
    >>> R3 = TensorIndexType('R3', dim=3)
    >>> p = TensorIndex("p", R3)

    By default, covariant indices only match with covariant indices (and
    similarly for contravariant)

    >>> q = WildTensorIndex("q", R3)
    >>> (q).matches(p)
    {q: p}
    >>> (q).matches(-p)

    If you want matching to ignore whether the index is co/contra-variant, set
    ignore_updown=True

    >>> r = WildTensorIndex("r", R3, ignore_updown=True)
    >>> (r).matches(-p)
    {r: -p}
    >>> (r).matches(p)
    {r: p}

    Parameters
    ==========
    name : name of the index (string), or ``True`` if you want it to be
        automatically assigned
    tensor_index_type : ``TensorIndexType`` of the index
    is_up :  flag for contravariant index (is_up=True by default)
    ignore_updown : bool, Whether this should match both co- and contra-variant
        indices (default:False)
    """
    def __new__(cls, name, tensor_index_type, is_up=..., ignore_updown=...) -> Self:
        ...
    
    @property
    def ignore_updown(self) -> Basic:
        ...
    
    def __neg__(self) -> WildTensorIndex:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    


class _WildTensExpr(Basic):
    """
    INTERNAL USE ONLY

    This is an object that helps with replacement of WildTensors in expressions.
    When this object is set as the tensor_head of a WildTensor, it replaces the
    WildTensor by a TensExpr (passed when initializing this object).

    Examples
    ========
    >>> from sympy.tensor.tensor import WildTensorHead, TensorIndex, TensorHead, TensorIndexType
    >>> W = WildTensorHead("W")
    >>> R3 = TensorIndexType('R3', dim=3)
    >>> p = TensorIndex('p', R3)
    >>> q = TensorIndex('q', R3)
    >>> K = TensorHead('K', [R3])
    >>> print( ( K(p) ).replace( W(p), W(q)*W(-q)*W(p) ) )
    K(R_0)*K(-R_0)*K(p)

    """
    def __init__(self, expr) -> None:
        ...
    
    def __call__(self, *indices) -> TensExpr:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def __abs__(self):
        ...
    
    def __add__(self, other) -> Self:
        ...
    
    def __radd__(self, other) -> Self:
        ...
    
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __mul__(self, other):
        ...
    
    def __rmul__(self, other):
        ...
    
    def __truediv__(self, other):
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __pow__(self, other):
        ...
    
    def __rpow__(self, other):
        ...
    


def canon_bp(p):
    """
    Butler-Portugal canonicalization. See ``tensor_can.py`` from the
    combinatorics module for the details.
    """
    ...

def tensor_mul(*a) -> TensExpr | TensMul:
    """
    product of tensors
    """
    ...

def riemann_cyclic_replace(t_r):
    """
    replace Riemann tensor with an equivalent expression

    ``R(m,n,p,q) -> 2/3*R(m,n,p,q) - 1/3*R(m,q,n,p) + 1/3*R(m,p,n,q)``

    """
    ...

def riemann_cyclic(t2) -> TensMul | TensExpr | Basic | Expr | TensAdd:
    """
    Replace each Riemann tensor with an equivalent expression
    satisfying the cyclic identity.

    This trick is discussed in the reference guide to Cadabra.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, riemann_cyclic, TensorSymmetry
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> i, j, k, l = tensor_indices('i,j,k,l', Lorentz)
    >>> R = TensorHead('R', [Lorentz]*4, TensorSymmetry.riemann())
    >>> t = R(i,j,k,l)*(R(-i,-j,-k,-l) - 2*R(-i,-k,-j,-l))
    >>> riemann_cyclic(t)
    0
    """
    ...

def get_lines(ex, index_type) -> tuple[list[Any], list[Any], list[int]]:
    """
    Returns ``(lines, traces, rest)`` for an index type,
    where ``lines`` is the list of list of positions of a matrix line,
    ``traces`` is the list of list of traced matrix lines,
    ``rest`` is the rest of the elements of the tensor.
    """
    ...

def get_free_indices(t) -> tuple[()] | list[TensorIndex]:
    ...

def get_indices(t) -> tuple[()]:
    ...

def get_dummy_indices(t) -> tuple[()] | list[Any]:
    ...

def get_index_structure(t) -> _IndexStructure:
    ...

def get_coeff(t):
    ...

def contract_metric(t, g):
    ...

def perm2tensor(t, g, is_canon_bp=...) -> TensExpr | TensMul:
    """
    Returns the tensor corresponding to the permutation ``g``

    For further details, see the method in ``TIDS`` with the same name.
    """
    ...

def substitute_indices(t, *index_tuples):
    ...

def get_postprocessor(cls) -> Callable[..., Any]:
    ...

