from typing import Any, Generator, Literal, Self
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.pc_groups import PolycyclicGroup
from sympy.combinatorics.permutations import Permutation
from sympy.core import Basic
from sympy.core.function import UndefinedFunction

rmul = ...
_af_new = ...
class PermutationGroup(Basic):
    is_group = ...
    def __new__(cls, *args, dups=..., **kwargs) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __getitem__(self, i):
        ...
    
    def __contains__(self, i) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def __mul__(self, other) -> Coset | PermutationGroup:
        ...
    
    @property
    def base(self) -> list[Any]:
        ...
    
    def baseswap(self, base, strong_gens, pos, randomized=..., transversals=..., basic_orbits=..., strong_gens_distr=...) -> tuple[Any, Any | list[Any]]:
        ...
    
    @property
    def basic_orbits(self) -> list[list[Any]]:
        ...
    
    @property
    def basic_stabilizers(self) -> list[Any]:
        ...
    
    @property
    def basic_transversals(self) -> list[None] | None:
        ...
    
    def composition_series(self) -> list[Any]:
        ...
    
    def coset_transversal(self, H) -> list[Any | Basic | list[Any] | Permutation] | list[Permutation]:
        ...
    
    def coset_table(self, H) -> list[Any] | None:
        ...
    
    def center(self) -> Self | PermutationGroup | None:
        ...
    
    def centralizer(self, other) -> Self | PermutationGroup | None:
        ...
    
    def commutator(self, G, H) -> PermutationGroup | None:
        ...
    
    def coset_factor(self, g, factor_index=...) -> list[Any]:
        ...
    
    def generator_product(self, g, original=...) -> list[Any]:
        r'''
        Return a list of strong generators `[s1, \dots, sn]`
        s.t `g = sn \times \dots \times s1`. If ``original=True``, make the
        list contain only the original group generators

        '''
        ...
    
    def coset_rank(self, g) -> int | None:
        ...
    
    def coset_unrank(self, rank, af=...) -> list[Any] | Permutation | None:
        ...
    
    @property
    def degree(self):
        ...
    
    @property
    def identity(self) -> Permutation:
        '''
        Return the identity element of the permutation group.

        '''
        ...
    
    @property
    def elements(self) -> set[Any | Basic | list[Any] | Permutation]:
        ...
    
    def derived_series(self) -> list[Self]:
        ...
    
    def derived_subgroup(self) -> PermutationGroup | None:
        ...
    
    def generate(self, method=..., af=...) -> Generator[Any | Basic | list[Any] | Permutation, Any, None] | Generator[list[int] | Permutation | list[Any], Any, None]:
        ...
    
    def generate_dimino(self, af=...) -> Generator[list[int] | Permutation | list[Any], Any, None]:
        ...
    
    def generate_schreier_sims(self, af=...) -> Generator[Any | Basic | list[Any] | Permutation, Any, None]:
        ...
    
    @property
    def generators(self) -> list[Basic]:
        ...
    
    def contains(self, g, strict=...) -> bool:
        ...
    
    @property
    def is_perfect(self) -> bool:
        ...
    
    @property
    def is_abelian(self) -> bool:
        ...
    
    def abelian_invariants(self) -> list[Any]:
        ...
    
    def is_elementary(self, p) -> bool:
        ...
    
    def is_alt_sym(self, eps=..., _random_prec=...) -> bool:
        ...
    
    @property
    def is_nilpotent(self) -> bool:
        ...
    
    def is_normal(self, gr, strict=...) -> bool:
        ...
    
    def is_primitive(self, randomized=...) -> bool:
        ...
    
    def minimal_blocks(self, randomized=...) -> list[Any] | Literal[False]:
        '''
        For a transitive group, return the list of all minimal
        block systems. If a group is intransitive, return `False`.

        Examples
        ========
        >>> from sympy.combinatorics import Permutation, PermutationGroup
        >>> from sympy.combinatorics.named_groups import DihedralGroup
        >>> DihedralGroup(6).minimal_blocks()
        [[0, 1, 0, 1, 0, 1], [0, 1, 2, 0, 1, 2]]
        >>> G = PermutationGroup(Permutation(1,2,5))
        >>> G.minimal_blocks()
        False

        See Also
        ========

        minimal_block, is_transitive, is_primitive

        '''
        ...
    
    @property
    def is_solvable(self) -> bool:
        ...
    
    def is_subgroup(self, G, strict=...) -> bool:
        ...
    
    @property
    def is_polycyclic(self) -> bool:
        ...
    
    def is_transitive(self, strict=...) -> bool:
        ...
    
    @property
    def is_trivial(self) -> bool:
        ...
    
    def lower_central_series(self) -> list[Self]:
        ...
    
    @property
    def max_div(self) -> Literal[1] | None:
        ...
    
    def minimal_block(self, points) -> list[Any] | Literal[False]:
        ...
    
    def conjugacy_class(self, x) -> set[Any]:
        ...
    
    def conjugacy_classes(self) -> list[set[Permutation]]:
        ...
    
    def normal_closure(self, other, k=...) -> PermutationGroup | None:
        ...
    
    def orbit(self, alpha, action=...) -> set[Any] | set[tuple[Any, ...]] | None:
        ...
    
    def orbit_rep(self, alpha, beta, schreier_vector=...) -> Permutation | Literal[False]:
        ...
    
    def orbit_transversal(self, alpha, pairs=...) -> list[tuple[Any, Permutation]] | list[tuple[Any, list[int]]] | tuple[list[tuple[Any, Permutation]] | list[tuple[Any, list[int]]], dict[Any, list[Any]]] | list[list[int]] | tuple[list[list[int]], dict[Any, list[Any]]] | list[Permutation] | tuple[list[Permutation], dict[Any, list[Any]]]:
        ...
    
    def orbits(self, rep=...) -> list[Any]:
        ...
    
    def order(self) -> int | type[UndefinedFunction]:
        ...
    
    def index(self, H) -> None:
        ...
    
    @property
    def is_symmetric(self) -> bool:
        ...
    
    @property
    def is_alternating(self) -> bool:
        ...
    
    @property
    def is_cyclic(self) -> bool:
        ...
    
    @property
    def is_dihedral(self) -> bool:
        ...
    
    def pointwise_stabilizer(self, points, incremental=...) -> PermutationGroup:
        ...
    
    def make_perm(self, n, seed=...) -> Permutation:
        ...
    
    def random(self, af=...) -> list[Any] | Permutation | None:
        ...
    
    def random_pr(self, gen_count=..., iterations=..., _random_prec=...) -> Permutation:
        ...
    
    def random_stab(self, alpha, schreier_vector=..., _random_prec=...) -> Permutation:
        ...
    
    def schreier_sims(self) -> None:
        ...
    
    def schreier_sims_incremental(self, base=..., gens=..., slp_dict=...) -> tuple[Any | list[Any], list[Basic] | Any, dict[Basic | Any, list[Basic | Any]]] | tuple[Any | list[Any], list[Basic] | Any] | tuple[Any | list[Any], list[Basic | Any], dict[Any, Any]] | tuple[Any | list[Any], list[Basic | Any]]:
        ...
    
    def schreier_sims_random(self, base=..., gens=..., consec_succ=..., _random_prec=...) -> tuple[Any | list[Any], list[Any]]:
        ...
    
    def schreier_vector(self, alpha):
        ...
    
    def stabilizer(self, alpha) -> PermGroup:
        ...
    
    @property
    def strong_gens(self) -> list[Basic] | list[Basic | Any]:
        ...
    
    def subgroup(self, gens) -> PermutationGroup:
        ...
    
    def subgroup_search(self, prop, base=..., strong_gens=..., tests=..., init_subgroup=...) -> PermutationGroup:
        ...
    
    @property
    def transitivity_degree(self) -> int:
        ...
    
    def sylow_subgroup(self, p) -> PermutationGroup | Self:
        '''
        Return a p-Sylow subgroup of the group.

        The algorithm is described in [1], Chapter 4, Section 7

        Examples
        ========
        >>> from sympy.combinatorics.named_groups import DihedralGroup
        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics.named_groups import AlternatingGroup

        >>> D = DihedralGroup(6)
        >>> S = D.sylow_subgroup(2)
        >>> S.order()
        4
        >>> G = SymmetricGroup(6)
        >>> S = G.sylow_subgroup(5)
        >>> S.order()
        5

        >>> G1 = AlternatingGroup(3)
        >>> G2 = AlternatingGroup(5)
        >>> G3 = AlternatingGroup(9)

        >>> S1 = G1.sylow_subgroup(3)
        >>> S2 = G2.sylow_subgroup(3)
        >>> S3 = G3.sylow_subgroup(3)

        >>> len1 = len(S1.lower_central_series())
        >>> len2 = len(S2.lower_central_series())
        >>> len3 = len(S3.lower_central_series())

        >>> len1 == len2
        True
        >>> len1 < len3
        True

        '''
        ...
    
    def strong_presentation(self) -> FpGroup | tuple[Any, Any] | tuple[Any | list[Any], Any | list[Any]]:
        '''
        Return a strong finite presentation of group. The generators
        of the returned group are in the same order as the strong
        generators of group.

        The algorithm is based on Sims' Verify algorithm described
        in [1], Chapter 6.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import DihedralGroup
        >>> P = DihedralGroup(4)
        >>> G = P.strong_presentation()
        >>> P.order() == G.order()
        True

        See Also
        ========

        presentation, _verify

        '''
        ...
    
    def presentation(self, eliminate_gens=...) -> FpGroup | tuple[Any, Any] | tuple[Any | list[Any], Any | list[Any]] | Any:
        '''
        Return an `FpGroup` presentation of the group.

        The algorithm is described in [1], Chapter 6.1.

        '''
        ...
    
    def polycyclic_group(self) -> PolycyclicGroup:
        ...
    


PermGroup = PermutationGroup
class SymmetricPermutationGroup(Basic):
    def __new__(cls, deg) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __contains__(self, i) -> bool:
        ...
    
    def order(self) -> type[UndefinedFunction]:
        ...
    
    @property
    def degree(self) -> Basic:
        ...
    
    @property
    def identity(self) -> Permutation:
        '''
        Return the identity element of the SymmetricPermutationGroup.

        Examples
        ========

        >>> from sympy.combinatorics import SymmetricPermutationGroup
        >>> G = SymmetricPermutationGroup(4)
        >>> G.identity()
        (3)

        '''
        ...
    


class Coset(Basic):
    def __new__(cls, g, H, G=..., dir=...) -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @property
    def is_left_coset(self) -> bool:
        ...
    
    @property
    def is_right_coset(self) -> bool:
        ...
    
    def as_list(self) -> list[Any]:
        ...
    


