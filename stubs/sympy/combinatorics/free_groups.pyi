from types import NotImplementedType
from typing import Any, Literal, Self
from sympy.core.expr import Expr
from sympy.core.sympify import CantSympify
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public

@public
def free_group(symbols) -> tuple[FreeGroup, *tuple[Any, ...]]:
    ...

@public
def xfree_group(symbols) -> tuple[FreeGroup, Any]:
    ...

@public
def vfree_group(symbols) -> FreeGroup:
    ...

_free_group_cache: dict[int, FreeGroup] = ...
class FreeGroup(DefaultPrinting):
    is_associative = ...
    is_group = ...
    is_FreeGroup = ...
    is_PermutationGroup = ...
    relators: list[Expr] = ...
    def __new__(cls, symbols) -> Self | FreeGroup:
        ...
    
    def clone(self, symbols=...) -> Self:
        ...
    
    def __contains__(self, i) -> Literal[False]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __len__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __getitem__(self, index) -> Self:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def index(self, gen):
        ...
    
    def order(self):
        ...
    
    @property
    def elements(self) -> set[Any]:
        ...
    
    @property
    def rank(self):
        ...
    
    @property
    def is_abelian(self) -> bool:
        ...
    
    @property
    def identity(self):
        ...
    
    def contains(self, g) -> bool:
        ...
    
    def center(self) -> set[Any]:
        ...
    


class FreeGroupElement(CantSympify, DefaultPrinting, tuple):
    is_assoc_word = ...
    def new(self, init) -> Self:
        ...
    
    _hash = ...
    def __hash__(self) -> int:
        ...
    
    def copy(self) -> Self:
        ...
    
    @property
    def is_identity(self) -> bool:
        ...
    
    @property
    def array_form(self) -> tuple[Any, ...]:
        ...
    
    @property
    def letter_form(self) -> tuple[Any, ...]:
        ...
    
    def __getitem__(self, i):
        ...
    
    def index(self, gen) -> int:
        ...
    
    @property
    def letter_form_elm(self) -> list[Any]:
        ...
    
    @property
    def ext_rep(self) -> tuple[Any, ...]:
        ...
    
    def __contains__(self, gen) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __pow__(self, n) -> Self:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    def __truediv__(self, other):
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __add__(self, other) -> NotImplementedType:
        ...
    
    def inverse(self):
        ...
    
    def order(self):
        ...
    
    def commutator(self, other):
        ...
    
    def eliminate_words(self, words, _all=..., inverse=...) -> Self:
        '''
        Replace each subword from the dictionary `words` by words[subword].
        If words is a list, replace the words by the identity.

        '''
        ...
    
    def eliminate_word(self, gen, by=..., _all=..., inverse=...) -> Self:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def exponent_sum(self, gen):
        ...
    
    def generator_count(self, gen):
        ...
    
    def subword(self, from_i, to_j, strict=...):
        ...
    
    def subword_index(self, word, start=...) -> int:
        '''
        Find the index of `word` in `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**2*b*a*b**3
        >>> w.subword_index(a*b*a*b)
        1

        '''
        ...
    
    def is_dependent(self, word) -> bool:
        ...
    
    def is_independent(self, word) -> bool:
        ...
    
    def contains_generators(self) -> set[Any]:
        ...
    
    def cyclic_subword(self, from_i, to_j):
        ...
    
    def cyclic_conjugates(self) -> set[Any]:
        ...
    
    def is_cyclic_conjugate(self, w) -> bool:
        ...
    
    def number_syllables(self) -> int:
        ...
    
    def exponent_syllable(self, i):
        ...
    
    def generator_syllable(self, i):
        ...
    
    def sub_syllables(self, from_i, to_j):
        ...
    
    def substituted_word(self, from_i, to_j, by):
        ...
    
    def is_cyclically_reduced(self) -> Literal[True]:
        ...
    
    def identity_cyclic_reduction(self) -> Self:
        ...
    
    def cyclic_reduction(self, removed=...) -> tuple[Self | Any, Any] | Self:
        ...
    
    def power_of(self, other) -> bool:
        '''
        Check if `self == other**n` for some integer n.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> ((x*y)**2).power_of(x*y)
        True
        >>> (x**-3*y**-2*x**3).power_of(x**-3*y*x**3)
        True

        '''
        ...
    


def letter_form_to_array_form(array_form, group) -> list[Any] | None:
    ...

def zero_mul_simp(l, index) -> None:
    ...

