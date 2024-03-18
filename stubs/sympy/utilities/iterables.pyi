from collections import defaultdict
from itertools import chain, combinations, combinations_with_replacement, permutations, product
from typing import Any, Generator, Iterator, Literal, Never, NoReturn
from sympy import Basic, Symbol
from sympy.utilities.decorator import deprecated

def is_palindromic(s, i=..., j=...) -> bool:
    ...

def flatten(iterable, levels=..., cls=...) -> list[Any]:
    ...

def unflatten(iter, n=...) -> list[Any]:
    ...

def reshape(seq, how) -> Any:
    ...

def group(seq, multiple=...) -> list[list[Any]] | list[tuple[Any, int]]:
    ...

def iproduct(*iterables) -> Generator[tuple[()] | tuple[Any] | tuple[Any, Any] | Any, Any, None]:
    '''
    Cartesian product of iterables.

    Generator of the Cartesian product of iterables. This is analogous to
    itertools.product except that it works with infinite iterables and will
    yield any item from the infinite product eventually.

    Examples
    ========

    >>> from sympy.utilities.iterables import iproduct
    >>> sorted(iproduct([1,2], [3,4]))
    [(1, 3), (1, 4), (2, 3), (2, 4)]

    With an infinite iterator:

    >>> from sympy import S
    >>> (3,) in iproduct(S.Integers)
    True
    >>> (3, 4) in iproduct(S.Integers, S.Integers)
    True

    .. seealso::

       `itertools.product
       <https://docs.python.org/3/library/itertools.html#itertools.product>`_
    '''
    ...

def multiset(seq) -> dict[Any, int]:
    ...

def ibin(n, bits=..., str=...) -> list[int] | Iterator[Never] | permutations[Any] | Iterator[tuple[()]] | product[tuple[Any, ...]] | str | Generator[str, None, None]:
    ...

def variations(seq, n, repetition=...) -> Iterator[Never] | permutations[Any] | Iterator[tuple[()]] | product[tuple[Any, ...]]:
    ...

def subsets(seq, k=..., repetition=...) -> chain[tuple[Any, ...]] | combinations[Any] | combinations_with_replacement[Any]:
    ...

def filter_symbols(iterator, exclude) -> Generator[Any, Any, None]:
    ...

def numbered_symbols(prefix=..., cls=..., start=..., exclude=..., *args, **assumptions) -> Generator[Symbol | Any, Any, NoReturn]:
    ...

def capture(func) -> str:
    ...

def sift(seq, keyfunc, binary=...) -> defaultdict[Any, list[Any]] | tuple[list[Any], list[Any]]:
    ...

def take(iter, n) -> list[Any]:
    ...

def dict_merge(*dicts) -> dict[Any, Any]:
    ...

def common_prefix(*seqs) -> list[Any]:
    ...

def common_suffix(*seqs) -> list[Any]:
    ...

def prefixes(seq) -> Generator[Any, Any, None]:
    ...

def postfixes(seq) -> Generator[Any, Any, None]:
    ...

def topological_sort(graph, key=...) -> list[Any]:
    ...

def strongly_connected_components(G) -> list[Any]:
    ...

def connected_components(G) -> list[Any]:
    ...

def rotate_left(x, y) -> list[Any]:
    ...

def rotate_right(x, y) -> list[Any]:
    ...

def least_rotation(x, key=...) -> int:
    '''
    Returns the number of steps of left rotation required to
    obtain lexicographically minimal string/list/tuple, etc.

    Examples
    ========

    >>> from sympy.utilities.iterables import least_rotation, rotate_left
    >>> a = [3, 1, 5, 1, 2]
    >>> least_rotation(a)
    3
    >>> rotate_left(a, _)
    [1, 2, 3, 1, 5]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation

    '''
    ...

def multiset_combinations(m, n, g=...) -> Generator[Any | list[Any], Any, None]:
    ...

def multiset_permutations(m, size=..., g=...) -> Generator[list[Any | int] | Any, Any, None]:
    ...

def multiset_partitions(multiset, m=...) -> Generator[list[list[int]] | list[list[Any]] | list[list[str] | Any] | list[Any], Any, None]:
    ...

def partitions(n, m=..., k=..., size=...) -> Generator[tuple[Literal[0], dict[Any, Any]] | tuple[int, dict[int, int]] | dict[int, int], Any, None]:
    ...

def ordered_partitions(n, m=..., sort=...) -> Generator[Any | list[Any], Any, None]:
    ...

def binary_partitions(n) -> Generator[Any | list[Any], Any, None]:
    ...

def has_dups(seq) -> bool:
    ...

def has_variety(seq) -> bool:
    ...

def uniq(seq, result=...) -> Generator[Any, Any, None]:
    ...

def generate_bell(n) -> Generator[tuple[Literal[0]] | tuple[Literal[0], Literal[1]] | tuple[Literal[1], Literal[0]] | Any | tuple[int, ...], Any, None]:
    ...

def generate_involutions(n) -> Generator[tuple[int, ...], Any, None]:
    ...

def multiset_derangements(s) -> Generator[list[Any] | list[None] | Any, Any, None]:
    ...

def random_derangement(t, choice=..., strict=...) -> str | list[None] | list[Any]:
    ...

def generate_derangements(s) -> Generator[list[Any] | list[None], Any, None]:
    ...

def necklaces(n, k, free=...) -> Generator[tuple[Any, ...], Any, None]:
    ...

def bracelets(n, k) -> Generator[tuple[Any, ...], Any, None]:
    ...

def generate_oriented_forest(n) -> Generator[list[int], Any, None]:
    ...

def minlex(seq, directed=..., key=...) -> tuple[Any, ...] | list[Any]:
    ...

def runs(seq, op=...) -> list[Any]:
    ...

def sequence_partitions(l, n, /) -> Generator[list[Any] | Any, Any, None]:
    ...

def sequence_partitions_empty(l, n, /) -> Generator[list[Any] | Any, Any, None]:
    ...

def kbins(l, k, ordered=...) -> Generator[list[Any] | Any | list[list[Any | int]] | list[list[int]] | list[list[Any]] | list[list[str] | Any], Any, None]:
    ...

def permute_signs(t) -> Generator[Any, Any, None]:
    ...

def signed_permutations(t) -> Generator[Any, None, None]:
    ...

def rotations(s, dir=...) -> Generator[list[Any], Any, None]:
    ...

def roundrobin(*iterables) -> Generator[Any, Any, None]:
    ...

class NotIterable:
    ...


def iterable(i, exclude=...) -> bool:
    ...

def is_sequence(i, include=...) -> bool:
    ...

def postorder_traversal(node, keys=...) -> Generator[Any | Basic, Any, None]:
    ...

def interactive_traversal(expr) -> Basic:
    ...

def default_sort_key(*args, **kwargs) -> tuple[tuple[Literal[5], Literal[0], str], tuple[int, tuple[Any, ...]], Any, Any] | tuple[tuple[Literal[10, 0], Literal[0], str | Any], tuple[int, tuple[Any, ...]] | tuple[Literal[1], tuple[str]], Any, Any]:
    ...

def ordered(*args, **kwargs) -> Generator[Any, Any, None]:
    ...

