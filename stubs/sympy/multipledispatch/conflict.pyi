class AmbiguityWarning(Warning):
    ...


def supercedes(a, b) -> bool:
    """ A is consistent and strictly more specific than B """
    ...

def consistent(a, b) -> bool:
    """ It is possible for an argument list to satisfy both A and B """
    ...

def ambiguous(a, b) -> bool:
    """ A is consistent with B but neither is strictly more specific """
    ...

def ambiguities(signatures) -> set[tuple[tuple[_T_co, ...], tuple[_T_co, ...]]]:
    """ All signature pairs such that A is ambiguous with B """
    ...

def super_signature(signatures) -> list[type]:
    """ A signature that would break ambiguities """
    ...

def edge(a, b, tie_breaker=...) -> bool:
    """ A should be checked before B

    Tie broken by tie_breaker, defaults to ``hash``
    """
    ...

def ordering(signatures) -> list[Any]:
    """ A sane ordering of signatures to check, first to last

    Topoological sort of edges as given by ``edge`` and ``supercedes``
    """
    ...

