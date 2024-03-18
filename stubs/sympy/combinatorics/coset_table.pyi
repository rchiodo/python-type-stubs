from typing import Any, Self
from sympy.printing.defaults import DefaultPrinting

class CosetTable(DefaultPrinting):
    coset_table_max_limit = ...
    coset_table_limit = ...
    max_stack_size = ...
    def __init__(self, fp_grp, subgroup, max_cosets=...) -> None:
        ...
    
    @property
    def omega(self) -> list[int]:
        ...
    
    def copy(self) -> Self:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @property
    def n(self) -> int:
        ...
    
    def is_complete(self) -> bool:
        ...
    
    def define(self, alpha, x, modified=...) -> None:
        ...
    
    def define_c(self, alpha, x) -> None:
        ...
    
    def scan_c(self, alpha, word) -> None:
        ...
    
    def coincidence_c(self, alpha, beta) -> None:
        ...
    
    def scan(self, alpha, word, y=..., fill=..., modified=...) -> None:
        ...
    
    def scan_check(self, alpha, word) -> bool:
        ...
    
    def merge(self, k, lamda, q, w=..., modified=...) -> None:
        ...
    
    def rep(self, k, modified=...):
        ...
    
    def coincidence(self, alpha, beta, w=..., modified=...) -> None:
        ...
    
    def scan_and_fill(self, alpha, word) -> None:
        ...
    
    def scan_and_fill_c(self, alpha, word) -> None:
        ...
    
    def look_ahead(self) -> None:
        ...
    
    def process_deductions(self, R_c_x, R_c_x_inv) -> None:
        ...
    
    def process_deductions_check(self, R_c_x, R_c_x_inv) -> bool:
        ...
    
    def switch(self, beta, gamma) -> None:
        ...
    
    def standardize(self) -> None:
        ...
    
    def compress(self) -> None:
        ...
    
    def conjugates(self, R) -> list[Any]:
        ...
    
    def coset_representative(self, coset) -> None:
        '''
        Compute the coset representative of a given coset.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
        >>> F, x, y = free_group("x, y")
        >>> f = FpGroup(F, [x**3, y**3, x**-1*y**-1*x*y])
        >>> C = coset_enumeration_r(f, [x])
        >>> C.compress()
        >>> C.table
        [[0, 0, 1, 2], [1, 1, 2, 0], [2, 2, 0, 1]]
        >>> C.coset_representative(0)
        <identity>
        >>> C.coset_representative(1)
        y
        >>> C.coset_representative(2)
        y**-1

        '''
        ...
    
    def modified_define(self, alpha, x) -> None:
        ...
    
    def modified_scan(self, alpha, w, y, fill=...) -> None:
        ...
    
    def modified_scan_and_fill(self, alpha, w, y) -> None:
        ...
    
    def modified_merge(self, k, lamda, w, q) -> None:
        ...
    
    def modified_rep(self, k) -> None:
        ...
    
    def modified_coincidence(self, alpha, beta, w) -> None:
        ...
    


def coset_enumeration_r(fp_grp, Y, max_cosets=..., draft=..., incomplete=..., modified=...) -> CosetTable:
    ...

def modified_coset_enumeration_r(fp_grp, Y, max_cosets=..., draft=..., incomplete=...) -> CosetTable:
    ...

def coset_enumeration_c(fp_grp, Y, max_cosets=..., draft=..., incomplete=...) -> CosetTable:
    ...

