'''Functions returning normal forms of matrices'''
from typing import Any
from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.matrices.domainscalar import DomainScalar


def smith_normal_form(m) -> DomainMatrix:
    '''
    Return the Smith Normal Form of a matrix `m` over the ring `domain`.
    This will only work if the ring is a principal ideal domain.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DomainMatrix
    >>> from sympy.polys.matrices.normalforms import smith_normal_form
    >>> m = DomainMatrix([[ZZ(12), ZZ(6), ZZ(4)],
    ...                   [ZZ(3), ZZ(9), ZZ(6)],
    ...                   [ZZ(2), ZZ(16), ZZ(14)]], (3, 3), ZZ)
    >>> print(smith_normal_form(m).to_Matrix())
    Matrix([[1, 0, 0], [0, 10, 0], [0, 0, -30]])

    '''
    ...

def add_columns(m, i, j, a, b, c, d) -> None:
    ...

def invariant_factors(m) -> tuple[()] | tuple[Any, ...]:
    '''
    Return the tuple of abelian invariants for a matrix `m`
    (as in the Smith-Normal form)

    References
    ==========

    [1] https://en.wikipedia.org/wiki/Smith_normal_form#Algorithm
    [2] https://web.archive.org/web/20200331143852/https://sierra.nmsu.edu/morandi/notes/SmithNormalForm.pdf

    '''
    ...

def hermite_normal_form(A, *, D=..., check_rank=...) -> DomainMatrix | DomainScalar:
    ...

