from itertools import combinations
from typing import Any, Self


class Subset:
    _rank_binary = ...
    _rank_lex = ...
    _rank_graycode = ...
    _subset = ...
    _superset = ...
    def __new__(cls, subset, superset) -> Self:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def iterate_binary(self, k) -> Subset:
        ...
    
    def next_binary(self) -> Subset:
        ...
    
    def prev_binary(self) -> Subset:
        ...
    
    def next_lexicographic(self) -> Subset:
        ...
    
    def prev_lexicographic(self) -> Subset:
        ...
    
    def iterate_graycode(self, k) -> Subset:
        ...
    
    def next_gray(self) -> Subset:
        ...
    
    def prev_gray(self) -> Subset:
        ...
    
    @property
    def rank_binary(self) -> int:
        ...
    
    @property
    def rank_lexicographic(self) -> int:
        ...
    
    @property
    def rank_gray(self) -> int:
        ...
    
    @property
    def subset(self) -> None:
        ...
    
    @property
    def size(self) -> int:
        ...
    
    @property
    def superset(self) -> None:
        ...
    
    @property
    def superset_size(self) -> int:
        ...
    
    @property
    def cardinality(self) -> Any:
        ...
    
    @classmethod
    def subset_from_bitlist(self, super_set, bitlist) -> Subset:
        ...
    
    @classmethod
    def bitlist_from_subset(self, subset, superset) -> str:
        ...
    
    @classmethod
    def unrank_binary(self, rank, superset) -> Subset:
        ...
    
    @classmethod
    def unrank_gray(self, rank, superset) -> Subset:
        ...
    
    @classmethod
    def subset_indices(self, subset, superset) -> list[Any]:
        ...
    


def ksubsets(superset, k) -> combinations[Any]:
    ...

