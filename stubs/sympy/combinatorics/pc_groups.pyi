from typing import Any, Literal
from sympy.printing.defaults import DefaultPrinting

class PolycyclicGroup(DefaultPrinting):
    is_group = ...
    is_solvable = ...
    def __init__(self, pc_sequence, pc_series, relative_order, collector=...) -> None:
        """

        Parameters
        ==========

        pc_sequence : list
            A sequence of elements whose classes generate the cyclic factor
            groups of pc_series.
        pc_series : list
            A subnormal sequence of subgroups where each factor group is cyclic.
        relative_order : list
            The orders of factor groups of pc_series.
        collector : Collector
            By default, it is None. Collector class provides the
            polycyclic presentation with various other functionalities.

        """
        ...
    
    def is_prime_order(self) -> bool:
        ...
    
    def length(self) -> int:
        ...
    


class Collector(DefaultPrinting):
    """
    References
    ==========

    .. [1] Holt, D., Eick, B., O'Brien, E.
           "Handbook of Computational Group Theory"
           Section 8.1.3
    """
    def __init__(self, pcgs, pc_series, relative_order, free_group_=..., pc_presentation=...) -> None:
        """

        Most of the parameters for the Collector class are the same as for PolycyclicGroup.
        Others are described below.

        Parameters
        ==========

        free_group_ : tuple
            free_group_ provides the mapping of polycyclic generating
            sequence with the free group elements.
        pc_presentation : dict
            Provides the presentation of polycyclic groups with the
            help of power and conjugate relators.

        See Also
        ========

        PolycyclicGroup

        """
        ...
    
    def minimal_uncollected_subword(self, word) -> tuple[tuple[Any, Any]] | tuple[tuple[Any, Any], tuple[Any, Literal[1, -1]]] | None:
        r"""
        Returns the minimal uncollected subwords.

        Explanation
        ===========

        A word ``v`` defined on generators in ``X`` is a minimal
        uncollected subword of the word ``w`` if ``v`` is a subword
        of ``w`` and it has one of the following form

        * `v = {x_{i+1}}^{a_j}x_i`

        * `v = {x_{i+1}}^{a_j}{x_i}^{-1}`

        * `v = {x_i}^{a_j}`

        for `a_j` not in `\{1, \ldots, s-1\}`. Where, ``s`` is the power
        exponent of the corresponding generator.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics import free_group
        >>> G = SymmetricGroup(4)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> F, x1, x2 = free_group("x1, x2")
        >>> word = x2**2*x1**7
        >>> collector.minimal_uncollected_subword(word)
        ((x2, 2),)

        """
        ...
    
    def relations(self) -> tuple[dict[Any, Any], dict[Any, Any]]:
        """
        Separates the given relators of pc presentation in power and
        conjugate relations.

        Returns
        =======

        (power_rel, conj_rel)
            Separates pc presentation into power and conjugate relations.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> G = SymmetricGroup(3)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> power_rel, conj_rel = collector.relations()
        >>> power_rel
        {x0**2: (), x1**3: ()}
        >>> conj_rel
        {x0**-1*x1*x0: x1**2}

        See Also
        ========

        pc_relators

        """
        ...
    
    def subword_index(self, word, w) -> tuple[Literal[-1], Literal[-1]] | tuple[int, int]:
        """
        Returns the start and ending index of a given
        subword in a word.

        Parameters
        ==========

        word : FreeGroupElement
            word defined on free group elements for a
            polycyclic group.
        w : FreeGroupElement
            subword of a given word, whose starting and
            ending index to be computed.

        Returns
        =======

        (i, j)
            A tuple containing starting and ending index of ``w``
            in the given word.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics import free_group
        >>> G = SymmetricGroup(4)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> F, x1, x2 = free_group("x1, x2")
        >>> word = x2**2*x1**7
        >>> w = x2**2*x1
        >>> collector.subword_index(word, w)
        (0, 3)
        >>> w = x1**7
        >>> collector.subword_index(word, w)
        (2, 9)

        """
        ...
    
    def map_relation(self, w):
        """
        Return a conjugate relation.

        Explanation
        ===========

        Given a word formed by two free group elements, the
        corresponding conjugate relation with those free
        group elements is formed and mapped with the collected
        word in the polycyclic presentation.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics import free_group
        >>> G = SymmetricGroup(3)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> F, x0, x1 = free_group("x0, x1")
        >>> w = x1*x0
        >>> collector.map_relation(w)
        x1**2

        See Also
        ========

        pc_presentation

        """
        ...
    
    def collected_word(self, word):
        r"""
        Return the collected form of a word.

        Explanation
        ===========

        A word ``w`` is called collected, if `w = {x_{i_1}}^{a_1} * \ldots *
        {x_{i_r}}^{a_r}` with `i_1 < i_2< \ldots < i_r` and `a_j` is in
        `\{1, \ldots, {s_j}-1\}`.

        Otherwise w is uncollected.

        Parameters
        ==========

        word : FreeGroupElement
            An uncollected word.

        Returns
        =======

        word
            A collected word of form `w = {x_{i_1}}^{a_1}, \ldots,
            {x_{i_r}}^{a_r}` with `i_1, i_2, \ldots, i_r` and `a_j \in
            \{1, \ldots, {s_j}-1\}`.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics.perm_groups import PermutationGroup
        >>> from sympy.combinatorics import free_group
        >>> G = SymmetricGroup(4)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> F, x0, x1, x2, x3 = free_group("x0, x1, x2, x3")
        >>> word = x3*x2*x1*x0
        >>> collected_word = collector.collected_word(word)
        >>> free_to_perm = {}
        >>> free_group = collector.free_group
        >>> for sym, gen in zip(free_group.symbols, collector.pcgs):
        ...     free_to_perm[sym] = gen
        >>> G1 = PermutationGroup()
        >>> for w in word:
        ...     sym = w[0]
        ...     perm = free_to_perm[sym]
        ...     G1 = PermutationGroup([perm] + G1.generators)
        >>> G2 = PermutationGroup()
        >>> for w in collected_word:
        ...     sym = w[0]
        ...     perm = free_to_perm[sym]
        ...     G2 = PermutationGroup([perm] + G2.generators)

        The two are not identical, but they are equivalent:

        >>> G1.equals(G2), G1 == G2
        (True, False)

        See Also
        ========

        minimal_uncollected_subword

        """
        ...
    
    def pc_relators(self) -> dict[Any, Any]:
        r"""
        Return the polycyclic presentation.

        Explanation
        ===========

        There are two types of relations used in polycyclic
        presentation.

        * Power relations : Power relators are of the form `x_i^{re_i}`,
          where `i \in \{0, \ldots, \mathrm{len(pcgs)}\}`, ``x`` represents polycyclic
          generator and ``re`` is the corresponding relative order.

        * Conjugate relations : Conjugate relators are of the form `x_j^-1x_ix_j`,
          where `j < i \in \{0, \ldots, \mathrm{len(pcgs)}\}`.

        Returns
        =======

        A dictionary with power and conjugate relations as key and
        their collected form as corresponding values.

        Notes
        =====

        Identity Permutation is mapped with empty ``()``.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics.permutations import Permutation
        >>> S = SymmetricGroup(49).sylow_subgroup(7)
        >>> der = S.derived_series()
        >>> G = der[len(der)-2]
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> pcgs = PcGroup.pcgs
        >>> len(pcgs)
        6
        >>> free_group = collector.free_group
        >>> pc_resentation = collector.pc_presentation
        >>> free_to_perm = {}
        >>> for s, g in zip(free_group.symbols, pcgs):
        ...     free_to_perm[s] = g

        >>> for k, v in pc_resentation.items():
        ...     k_array = k.array_form
        ...     if v != ():
        ...        v_array = v.array_form
        ...     lhs = Permutation()
        ...     for gen in k_array:
        ...         s = gen[0]
        ...         e = gen[1]
        ...         lhs = lhs*free_to_perm[s]**e
        ...     if v == ():
        ...         assert lhs.is_identity
        ...         continue
        ...     rhs = Permutation()
        ...     for gen in v_array:
        ...         s = gen[0]
        ...         e = gen[1]
        ...         rhs = rhs*free_to_perm[s]**e
        ...     assert lhs == rhs

        """
        ...
    
    def exponent_vector(self, element) -> list[int]:
        r"""
        Return the exponent vector of length equal to the
        length of polycyclic generating sequence.

        Explanation
        ===========

        For a given generator/element ``g`` of the polycyclic group,
        it can be represented as `g = {x_1}^{e_1}, \ldots, {x_n}^{e_n}`,
        where `x_i` represents polycyclic generators and ``n`` is
        the number of generators in the free_group equal to the length
        of pcgs.

        Parameters
        ==========

        element : Permutation
            Generator of a polycyclic group.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> from sympy.combinatorics.permutations import Permutation
        >>> G = SymmetricGroup(4)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> pcgs = PcGroup.pcgs
        >>> collector.exponent_vector(G[0])
        [1, 0, 0, 0]
        >>> exp = collector.exponent_vector(G[1])
        >>> g = Permutation()
        >>> for i in range(len(exp)):
        ...     g = g*pcgs[i]**exp[i] if exp[i] else g
        >>> assert g == G[1]

        References
        ==========

        .. [1] Holt, D., Eick, B., O'Brien, E.
               "Handbook of Computational Group Theory"
               Section 8.1.1, Definition 8.4

        """
        ...
    
    def depth(self, element) -> int:
        r"""
        Return the depth of a given element.

        Explanation
        ===========

        The depth of a given element ``g`` is defined by
        `\mathrm{dep}[g] = i` if `e_1 = e_2 = \ldots = e_{i-1} = 0`
        and `e_i != 0`, where ``e`` represents the exponent-vector.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> G = SymmetricGroup(3)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> collector.depth(G[0])
        2
        >>> collector.depth(G[1])
        1

        References
        ==========

        .. [1] Holt, D., Eick, B., O'Brien, E.
               "Handbook of Computational Group Theory"
               Section 8.1.1, Definition 8.5

        """
        ...
    
    def leading_exponent(self, element) -> int | None:
        r"""
        Return the leading non-zero exponent.

        Explanation
        ===========

        The leading exponent for a given element `g` is defined
        by `\mathrm{leading\_exponent}[g]` `= e_i`, if `\mathrm{depth}[g] = i`.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> G = SymmetricGroup(3)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> collector.leading_exponent(G[1])
        1

        """
        ...
    
    def induced_pcgs(self, gens) -> list[int]:
        """

        Parameters
        ==========

        gens : list
            A list of generators on which polycyclic subgroup
            is to be defined.

        Examples
        ========

        >>> from sympy.combinatorics.named_groups import SymmetricGroup
        >>> S = SymmetricGroup(8)
        >>> G = S.sylow_subgroup(2)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> gens = [G[0], G[1]]
        >>> ipcgs = collector.induced_pcgs(gens)
        >>> [gen.order() for gen in ipcgs]
        [2, 2, 2]
        >>> G = S.sylow_subgroup(3)
        >>> PcGroup = G.polycyclic_group()
        >>> collector = PcGroup.collector
        >>> gens = [G[0], G[1]]
        >>> ipcgs = collector.induced_pcgs(gens)
        >>> [gen.order() for gen in ipcgs]
        [3]

        """
        ...
    
    def constructive_membership_test(self, ipcgs, g) -> list[int] | Literal[False]:
        """
        Return the exponent vector for induced pcgs.
        """
        ...
    


