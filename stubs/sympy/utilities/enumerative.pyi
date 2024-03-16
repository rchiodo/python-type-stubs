"""
Algorithms and classes to support enumerative combinatorics.

Currently just multiset partitions, but more could be added.

Terminology (following Knuth, algorithm 7.1.2.5M TAOCP)
*multiset* aaabbcccc has a *partition* aaabc | bccc

The submultisets, aaabc and bccc of the partition are called
*parts*, or sometimes *vectors*.  (Knuth notes that multiset
partitions can be thought of as partitions of vectors of integers,
where the ith element of the vector gives the multiplicity of
element i.)

The values a, b and c are *components* of the multiset.  These
correspond to elements of a set, but in a multiset can be present
with a multiplicity greater than 1.

The algorithm deserves some explanation.

Think of the part aaabc from the multiset above.  If we impose an
ordering on the components of the multiset, we can represent a part
with a vector, in which the value of the first element of the vector
corresponds to the multiplicity of the first component in that
part. Thus, aaabc can be represented by the vector [3, 1, 1].  We
can also define an ordering on parts, based on the lexicographic
ordering of the vector (leftmost vector element, i.e., the element
with the smallest component number, is the most significant), so
that [3, 1, 1] > [3, 1, 0] and [3, 1, 1] > [2, 1, 4].  The ordering
on parts can be extended to an ordering on partitions: First, sort
the parts in each partition, left-to-right in decreasing order. Then
partition A is greater than partition B if A's leftmost/greatest
part is greater than B's leftmost part.  If the leftmost parts are
equal, compare the second parts, and so on.

In this ordering, the greatest partition of a given multiset has only
one part.  The least partition is the one in which the components
are spread out, one per part.

The enumeration algorithms in this file yield the partitions of the
argument multiset in decreasing order.  The main data structure is a
stack of parts, corresponding to the current partition.  An
important invariant is that the parts on the stack are themselves in
decreasing order.  This data structure is decremented to find the
next smaller partition.  Most often, decrementing the partition will
only involve adjustments to the smallest parts at the top of the
stack, much as adjacent integers *usually* differ only in their last
few digits.

Knuth's algorithm uses two main operations on parts:

Decrement - change the part so that it is smaller in the
  (vector) lexicographic order, but reduced by the smallest amount possible.
  For example, if the multiset has vector [5,
  3, 1], and the bottom/greatest part is [4, 2, 1], this part would
  decrement to [4, 2, 0], while [4, 0, 0] would decrement to [3, 3,
  1].  A singleton part is never decremented -- [1, 0, 0] is not
  decremented to [0, 3, 1].  Instead, the decrement operator needs
  to fail for this case.  In Knuth's pseudocode, the decrement
  operator is step m5.

Spread unallocated multiplicity - Once a part has been decremented,
  it cannot be the rightmost part in the partition.  There is some
  multiplicity that has not been allocated, and new parts must be
  created above it in the stack to use up this multiplicity.  To
  maintain the invariant that the parts on the stack are in
  decreasing order, these new parts must be less than or equal to
  the decremented part.
  For example, if the multiset is [5, 3, 1], and its most
  significant part has just been decremented to [5, 3, 0], the
  spread operation will add a new part so that the stack becomes
  [[5, 3, 0], [0, 0, 1]].  If the most significant part (for the
  same multiset) has been decremented to [2, 0, 0] the stack becomes
  [[2, 0, 0], [2, 0, 0], [1, 3, 1]].  In the pseudocode, the spread
  operation for one part is step m2.  The complete spread operation
  is a loop of steps m2 and m3.

In order to facilitate the spread operation, Knuth stores, for each
component of each part, not just the multiplicity of that component
in the part, but also the total multiplicity available for this
component in this part or any lesser part above it on the stack.

One added twist is that Knuth does not represent the part vectors as
arrays. Instead, he uses a sparse representation, in which a
component of a part is represented as a component number (c), plus
the multiplicity of the component in that part (v) as well as the
total multiplicity available for that component (u).  This saves
time that would be spent skipping over zeros.

"""
class PartComponent:
    """Internal class used in support of the multiset partitions
    enumerators and the associated visitor functions.

    Represents one component of one part of the current partition.

    A stack of these, plus an auxiliary frame array, f, represents a
    partition of the multiset.

    Knuth's pseudocode makes c, u, and v separate arrays.
    """
    __slots__ = ...
    def __init__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        "for debug/algorithm animation purposes"
        ...
    
    def __eq__(self, other) -> bool:
        """Define  value oriented equality, which is useful for testers"""
        ...
    
    def __ne__(self, other) -> bool:
        """Defined for consistency with __eq__"""
        ...
    


def multiset_partitions_taocp(multiplicities) -> Generator[list[Any], Any, None]:
    """Enumerates partitions of a multiset.

    Parameters
    ==========

    multiplicities
         list of integer multiplicities of the components of the multiset.

    Yields
    ======

    state
        Internal data structure which encodes a particular partition.
        This output is then usually processed by a visitor function
        which combines the information from this data structure with
        the components themselves to produce an actual partition.

        Unless they wish to create their own visitor function, users will
        have little need to look inside this data structure.  But, for
        reference, it is a 3-element list with components:

        f
            is a frame array, which is used to divide pstack into parts.

        lpart
            points to the base of the topmost part.

        pstack
            is an array of PartComponent objects.

        The ``state`` output offers a peek into the internal data
        structures of the enumeration function.  The client should
        treat this as read-only; any modification of the data
        structure will cause unpredictable (and almost certainly
        incorrect) results.  Also, the components of ``state`` are
        modified in place at each iteration.  Hence, the visitor must
        be called at each loop iteration.  Accumulating the ``state``
        instances and processing them later will not work.

    Examples
    ========

    >>> from sympy.utilities.enumerative import list_visitor
    >>> from sympy.utilities.enumerative import multiset_partitions_taocp
    >>> # variables components and multiplicities represent the multiset 'abb'
    >>> components = 'ab'
    >>> multiplicities = [1, 2]
    >>> states = multiset_partitions_taocp(multiplicities)
    >>> list(list_visitor(state, components) for state in states)
    [[['a', 'b', 'b']],
    [['a', 'b'], ['b']],
    [['a'], ['b', 'b']],
    [['a'], ['b'], ['b']]]

    See Also
    ========

    sympy.utilities.iterables.multiset_partitions: Takes a multiset
        as input and directly yields multiset partitions.  It
        dispatches to a number of functions, including this one, for
        implementation.  Most users will find it more convenient to
        use than multiset_partitions_taocp.

    """
    ...

def factoring_visitor(state, primes) -> list[Any]:
    """Use with multiset_partitions_taocp to enumerate the ways a
    number can be expressed as a product of factors.  For this usage,
    the exponents of the prime factors of a number are arguments to
    the partition enumerator, while the corresponding prime factors
    are input here.

    Examples
    ========

    To enumerate the factorings of a number we can think of the elements of the
    partition as being the prime factors and the multiplicities as being their
    exponents.

    >>> from sympy.utilities.enumerative import factoring_visitor
    >>> from sympy.utilities.enumerative import multiset_partitions_taocp
    >>> from sympy import factorint
    >>> primes, multiplicities = zip(*factorint(24).items())
    >>> primes
    (2, 3)
    >>> multiplicities
    (3, 1)
    >>> states = multiset_partitions_taocp(multiplicities)
    >>> list(factoring_visitor(state, primes) for state in states)
    [[24], [8, 3], [12, 2], [4, 6], [4, 2, 3], [6, 2, 2], [2, 2, 2, 3]]
    """
    ...

def list_visitor(state, components) -> list[Any]:
    """Return a list of lists to represent the partition.

    Examples
    ========

    >>> from sympy.utilities.enumerative import list_visitor
    >>> from sympy.utilities.enumerative import multiset_partitions_taocp
    >>> states = multiset_partitions_taocp([1, 2, 1])
    >>> s = next(states)
    >>> list_visitor(s, 'abc')  # for multiset 'a b b c'
    [['a', 'b', 'b', 'c']]
    >>> s = next(states)
    >>> list_visitor(s, [1, 2, 3])  # for multiset '1 2 2 3
    [[1, 2, 2], [3]]
    """
    ...

class MultisetPartitionTraverser:
    """
    Has methods to ``enumerate`` and ``count`` the partitions of a multiset.

    This implements a refactored and extended version of Knuth's algorithm
    7.1.2.5M [AOCP]_."

    The enumeration methods of this class are generators and return
    data structures which can be interpreted by the same visitor
    functions used for the output of ``multiset_partitions_taocp``.

    Examples
    ========

    >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
    >>> m = MultisetPartitionTraverser()
    >>> m.count_partitions([4,4,4,2])
    127750
    >>> m.count_partitions([3,3,3])
    686

    See Also
    ========

    multiset_partitions_taocp
    sympy.utilities.iterables.multiset_partitions

    References
    ==========

    .. [AOCP] Algorithm 7.1.2.5M in Volume 4A, Combinatoral Algorithms,
           Part 1, of The Art of Computer Programming, by Donald Knuth.

    .. [Factorisatio] On a Problem of Oppenheim concerning
           "Factorisatio Numerorum" E. R. Canfield, Paul Erdos, Carl
           Pomerance, JOURNAL OF NUMBER THEORY, Vol. 17, No. 1. August
           1983.  See section 7 for a description of an algorithm
           similar to Knuth's.

    .. [Yorgey] Generating Multiset Partitions, Brent Yorgey, The
           Monad.Reader, Issue 8, September 2007.

    """
    def __init__(self) -> None:
        ...
    
    def db_trace(self, msg) -> None:
        """Useful for understanding/debugging the algorithms.  Not
        generally activated in end-user code."""
        ...
    
    def decrement_part(self, part) -> bool:
        """Decrements part (a subrange of pstack), if possible, returning
        True iff the part was successfully decremented.

        If you think of the v values in the part as a multi-digit
        integer (least significant digit on the right) this is
        basically decrementing that integer, but with the extra
        constraint that the leftmost digit cannot be decremented to 0.

        Parameters
        ==========

        part
           The part, represented as a list of PartComponent objects,
           which is to be decremented.

        """
        ...
    
    def decrement_part_small(self, part, ub) -> bool:
        """Decrements part (a subrange of pstack), if possible, returning
        True iff the part was successfully decremented.

        Parameters
        ==========

        part
            part to be decremented (topmost part on the stack)

        ub
            the maximum number of parts allowed in a partition
            returned by the calling traversal.

        Notes
        =====

        The goal of this modification of the ordinary decrement method
        is to fail (meaning that the subtree rooted at this part is to
        be skipped) when it can be proved that this part can only have
        child partitions which are larger than allowed by ``ub``. If a
        decision is made to fail, it must be accurate, otherwise the
        enumeration will miss some partitions.  But, it is OK not to
        capture all the possible failures -- if a part is passed that
        should not be, the resulting too-large partitions are filtered
        by the enumeration one level up.  However, as is usual in
        constrained enumerations, failing early is advantageous.

        The tests used by this method catch the most common cases,
        although this implementation is by no means the last word on
        this problem.  The tests include:

        1) ``lpart`` must be less than ``ub`` by at least 2.  This is because
           once a part has been decremented, the partition
           will gain at least one child in the spread step.

        2) If the leading component of the part is about to be
           decremented, check for how many parts will be added in
           order to use up the unallocated multiplicity in that
           leading component, and fail if this number is greater than
           allowed by ``ub``.  (See code for the exact expression.)  This
           test is given in the answer to Knuth's problem 7.2.1.5.69.

        3) If there is *exactly* enough room to expand the leading
           component by the above test, check the next component (if
           it exists) once decrementing has finished.  If this has
           ``v == 0``, this next component will push the expansion over the
           limit by 1, so fail.
        """
        ...
    
    def decrement_part_large(self, part, amt, lb) -> bool | None:
        """Decrements part, while respecting size constraint.

        A part can have no children which are of sufficient size (as
        indicated by ``lb``) unless that part has sufficient
        unallocated multiplicity.  When enforcing the size constraint,
        this method will decrement the part (if necessary) by an
        amount needed to ensure sufficient unallocated multiplicity.

        Returns True iff the part was successfully decremented.

        Parameters
        ==========

        part
            part to be decremented (topmost part on the stack)

        amt
            Can only take values 0 or 1.  A value of 1 means that the
            part must be decremented, and then the size constraint is
            enforced.  A value of 0 means just to enforce the ``lb``
            size constraint.

        lb
            The partitions produced by the calling enumeration must
            have more parts than this value.

        """
        ...
    
    def decrement_part_range(self, part, lb, ub) -> bool | None:
        """Decrements part (a subrange of pstack), if possible, returning
        True iff the part was successfully decremented.

        Parameters
        ==========

        part
            part to be decremented (topmost part on the stack)

        ub
            the maximum number of parts allowed in a partition
            returned by the calling traversal.

        lb
            The partitions produced by the calling enumeration must
            have more parts than this value.

        Notes
        =====

        Combines the constraints of _small and _large decrement
        methods.  If returns success, part has been decremented at
        least once, but perhaps by quite a bit more if needed to meet
        the lb constraint.
        """
        ...
    
    def spread_part_multiplicity(self) -> bool:
        """Returns True if a new part has been created, and
        adjusts pstack, f and lpart as needed.

        Notes
        =====

        Spreads unallocated multiplicity from the current top part
        into a new part created above the current on the stack.  This
        new part is constrained to be less than or equal to the old in
        terms of the part ordering.

        This call does nothing (and returns False) if the current top
        part has no unallocated multiplicity.

        """
        ...
    
    def top_part(self) -> list[PartComponent]:
        """Return current top part on the stack, as a slice of pstack.

        """
        ...
    
    def enum_all(self, multiplicities) -> Generator[list[Any], Any, None]:
        """Enumerate the partitions of a multiset.

        Examples
        ========

        >>> from sympy.utilities.enumerative import list_visitor
        >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
        >>> m = MultisetPartitionTraverser()
        >>> states = m.enum_all([2,2])
        >>> list(list_visitor(state, 'ab') for state in states)
        [[['a', 'a', 'b', 'b']],
        [['a', 'a', 'b'], ['b']],
        [['a', 'a'], ['b', 'b']],
        [['a', 'a'], ['b'], ['b']],
        [['a', 'b', 'b'], ['a']],
        [['a', 'b'], ['a', 'b']],
        [['a', 'b'], ['a'], ['b']],
        [['a'], ['a'], ['b', 'b']],
        [['a'], ['a'], ['b'], ['b']]]

        See Also
        ========

        multiset_partitions_taocp:
            which provides the same result as this method, but is
            about twice as fast.  Hence, enum_all is primarily useful
            for testing.  Also see the function for a discussion of
            states and visitors.

        """
        ...
    
    def enum_small(self, multiplicities, ub) -> Generator[list[Any], Any, None]:
        """Enumerate multiset partitions with no more than ``ub`` parts.

        Equivalent to enum_range(multiplicities, 0, ub)

        Parameters
        ==========

        multiplicities
             list of multiplicities of the components of the multiset.

        ub
            Maximum number of parts

        Examples
        ========

        >>> from sympy.utilities.enumerative import list_visitor
        >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
        >>> m = MultisetPartitionTraverser()
        >>> states = m.enum_small([2,2], 2)
        >>> list(list_visitor(state, 'ab') for state in states)
        [[['a', 'a', 'b', 'b']],
        [['a', 'a', 'b'], ['b']],
        [['a', 'a'], ['b', 'b']],
        [['a', 'b', 'b'], ['a']],
        [['a', 'b'], ['a', 'b']]]

        The implementation is based, in part, on the answer given to
        exercise 69, in Knuth [AOCP]_.

        See Also
        ========

        enum_all, enum_large, enum_range

        """
        ...
    
    def enum_large(self, multiplicities, lb) -> Generator[list[Any], Any, None]:
        """Enumerate the partitions of a multiset with lb < num(parts)

        Equivalent to enum_range(multiplicities, lb, sum(multiplicities))

        Parameters
        ==========

        multiplicities
            list of multiplicities of the components of the multiset.

        lb
            Number of parts in the partition must be greater than
            this lower bound.


        Examples
        ========

        >>> from sympy.utilities.enumerative import list_visitor
        >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
        >>> m = MultisetPartitionTraverser()
        >>> states = m.enum_large([2,2], 2)
        >>> list(list_visitor(state, 'ab') for state in states)
        [[['a', 'a'], ['b'], ['b']],
        [['a', 'b'], ['a'], ['b']],
        [['a'], ['a'], ['b', 'b']],
        [['a'], ['a'], ['b'], ['b']]]

        See Also
        ========

        enum_all, enum_small, enum_range

        """
        ...
    
    def enum_range(self, multiplicities, lb, ub) -> Generator[list[Any], Any, None]:
        """Enumerate the partitions of a multiset with
        ``lb < num(parts) <= ub``.

        In particular, if partitions with exactly ``k`` parts are
        desired, call with ``(multiplicities, k - 1, k)``.  This
        method generalizes enum_all, enum_small, and enum_large.

        Examples
        ========

        >>> from sympy.utilities.enumerative import list_visitor
        >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
        >>> m = MultisetPartitionTraverser()
        >>> states = m.enum_range([2,2], 1, 2)
        >>> list(list_visitor(state, 'ab') for state in states)
        [[['a', 'a', 'b'], ['b']],
        [['a', 'a'], ['b', 'b']],
        [['a', 'b', 'b'], ['a']],
        [['a', 'b'], ['a', 'b']]]

        """
        ...
    
    def count_partitions_slow(self, multiplicities) -> int:
        """Returns the number of partitions of a multiset whose elements
        have the multiplicities given in ``multiplicities``.

        Primarily for comparison purposes.  It follows the same path as
        enumerate, and counts, rather than generates, the partitions.

        See Also
        ========

        count_partitions
            Has the same calling interface, but is much faster.

        """
        ...
    
    def count_partitions(self, multiplicities) -> int:
        """Returns the number of partitions of a multiset whose components
        have the multiplicities given in ``multiplicities``.

        For larger counts, this method is much faster than calling one
        of the enumerators and counting the result.  Uses dynamic
        programming to cut down on the number of nodes actually
        explored.  The dictionary used in order to accelerate the
        counting process is stored in the ``MultisetPartitionTraverser``
        object and persists across calls.  If the user does not
        expect to call ``count_partitions`` for any additional
        multisets, the object should be cleared to save memory.  On
        the other hand, the cache built up from one count run can
        significantly speed up subsequent calls to ``count_partitions``,
        so it may be advantageous not to clear the object.

        Examples
        ========

        >>> from sympy.utilities.enumerative import MultisetPartitionTraverser
        >>> m = MultisetPartitionTraverser()
        >>> m.count_partitions([9,8,2])
        288716
        >>> m.count_partitions([2,2])
        9
        >>> del m

        Notes
        =====

        If one looks at the workings of Knuth's algorithm M [AOCP]_, it
        can be viewed as a traversal of a binary tree of parts.  A
        part has (up to) two children, the left child resulting from
        the spread operation, and the right child from the decrement
        operation.  The ordinary enumeration of multiset partitions is
        an in-order traversal of this tree, and with the partitions
        corresponding to paths from the root to the leaves. The
        mapping from paths to partitions is a little complicated,
        since the partition would contain only those parts which are
        leaves or the parents of a spread link, not those which are
        parents of a decrement link.

        For counting purposes, it is sufficient to count leaves, and
        this can be done with a recursive in-order traversal.  The
        number of leaves of a subtree rooted at a particular part is a
        function only of that part itself, so memoizing has the
        potential to speed up the counting dramatically.

        This method follows a computational approach which is similar
        to the hypothetical memoized recursive function, but with two
        differences:

        1) This method is iterative, borrowing its structure from the
           other enumerations and maintaining an explicit stack of
           parts which are in the process of being counted.  (There
           may be multisets which can be counted reasonably quickly by
           this implementation, but which would overflow the default
           Python recursion limit with a recursive implementation.)

        2) Instead of using the part data structure directly, a more
           compact key is constructed.  This saves space, but more
           importantly coalesces some parts which would remain
           separate with physical keys.

        Unlike the enumeration functions, there is currently no _range
        version of count_partitions.  If someone wants to stretch
        their brain, it should be possible to construct one by
        memoizing with a histogram of counts rather than a single
        count, and combining the histograms.
        """
        ...
    


def part_key(part) -> tuple[Any, ...]:
    """Helper for MultisetPartitionTraverser.count_partitions that
    creates a key for ``part``, that only includes information which can
    affect the count for that part.  (Any irrelevant information just
    reduces the effectiveness of dynamic programming.)

    Notes
    =====

    This member function is a candidate for future exploration. There
    are likely symmetries that can be exploited to coalesce some
    ``part_key`` values, and thereby save space and improve
    performance.

    """
    ...

