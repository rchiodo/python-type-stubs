from sympy.sets.sets import Set

class PowerSet(Set):
    r"""A symbolic object representing a power set.

    Parameters
    ==========

    arg : Set
        The set to take power of.

    evaluate : bool
        The flag to control evaluation.

        If the evaluation is disabled for finite sets, it can take
        advantage of using subset test as a membership test.

    Notes
    =====

    Power set `\mathcal{P}(S)` is defined as a set containing all the
    subsets of `S`.

    If the set `S` is a finite set, its power set would have
    `2^{\left| S \right|}` elements, where `\left| S \right|` denotes
    the cardinality of `S`.

    Examples
    ========

    >>> from sympy import PowerSet, S, FiniteSet

    A power set of a finite set:

    >>> PowerSet(FiniteSet(1, 2, 3))
    PowerSet({1, 2, 3})

    A power set of an empty set:

    >>> PowerSet(S.EmptySet)
    PowerSet(EmptySet)
    >>> PowerSet(PowerSet(S.EmptySet))
    PowerSet(PowerSet(EmptySet))

    A power set of an infinite set:

    >>> PowerSet(S.Reals)
    PowerSet(Reals)

    Evaluating the power set of a finite set to its explicit form:

    >>> PowerSet(FiniteSet(1, 2, 3)).rewrite(FiniteSet)
    FiniteSet(EmptySet, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3})

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Power_set

    .. [2] https://en.wikipedia.org/wiki/Axiom_of_power_set
    """
    def __new__(cls, arg, evaluate=...) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    def __len__(self) -> Any:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    @property
    def kind(self) -> SetKind:
        ...
    


