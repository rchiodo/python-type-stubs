from sympy.sets.sets import FiniteSet, Interval, ProductSet, Set, Union
from sympy.sets.fancysets import Complexes, Range, Rationals, Reals

_inf_sets = ...
is_subset_sets = ...
@is_subset_sets.register(Set, Set)
def _(a, b) -> None:
    ...

@is_subset_sets.register(Interval, Interval)
def _(a, b) -> Literal[False] | None:
    ...

@is_subset_sets.register(Interval, FiniteSet)
def _(a_interval, b_fs) -> Literal[False] | None:
    ...

@is_subset_sets.register(Interval, Union)
def _(a_interval, b_u) -> Literal[False] | None:
    ...

@is_subset_sets.register(Range, Range)
def _(a, b) -> bool | None:
    ...

@is_subset_sets.register(Range, Interval)
def _(a_range, b_interval) -> bool | None:
    ...

@is_subset_sets.register(Range, FiniteSet)
def _(a_range, b_finiteset) -> bool | None:
    ...

@is_subset_sets.register(Interval, Range)
def _(a_interval, b_range) -> Literal[False] | None:
    ...

@is_subset_sets.register(Interval, Rationals)
def _(a_interval, b_rationals) -> Literal[False] | None:
    ...

@is_subset_sets.register(Range, Complexes)
def _(a, b) -> Literal[True]:
    ...

@is_subset_sets.register(Complexes, Interval)
def _(a, b) -> Literal[False]:
    ...

@is_subset_sets.register(Complexes, Range)
def _(a, b) -> Literal[False]:
    ...

@is_subset_sets.register(Complexes, Rationals)
def _(a, b) -> Literal[False]:
    ...

@is_subset_sets.register(Rationals, Reals)
def _(a, b) -> Literal[True]:
    ...

@is_subset_sets.register(Rationals, Range)
def _(a, b) -> Literal[False]:
    ...

@is_subset_sets.register(ProductSet, FiniteSet)
def _(a_ps, b_fs) -> bool | None:
    ...

