from sympy.core.function import UndefinedFunction
from sympy.utilities.decorator import deprecated

@deprecated("""\
The `sympy.ntheory.partitions_.npartitions` has been moved to `sympy.functions.combinatorial.numbers.partition`.""", deprecated_since_version="1.13", active_deprecations_target='deprecated-ntheory-symbolic-functions')
def npartitions(n, verbose=...) -> type[UndefinedFunction]:
    """
    Calculate the partition function P(n), i.e. the number of ways that
    n can be written as a sum of positive integers.

    .. deprecated:: 1.13

        The ``npartitions`` function is deprecated. Use :class:`sympy.functions.combinatorial.numbers.partition`
        instead. See its documentation for more information. See
        :ref:`deprecated-ntheory-symbolic-functions` for details.

    P(n) is computed using the Hardy-Ramanujan-Rademacher formula [1]_.


    The correctness of this implementation has been tested through $10^{10}$.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import partition
    >>> partition(25)
    1958

    References
    ==========

    .. [1] https://mathworld.wolfram.com/PartitionFunctionP.html

    """
    ...

