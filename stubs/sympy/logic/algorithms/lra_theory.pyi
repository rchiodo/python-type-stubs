"""Implements "A Fast Linear-Arithmetic Solver for DPLL(T)"

The LRASolver class defined in this file can be used
in conjunction with a SAT solver to check the
satisfiability of formulas involving inequalities.

Here's an example of how that would work:

    Suppose you want to check the satisfiability of
    the following formula:

    >>> from sympy.core.relational import Eq
    >>> from sympy.abc import x, y
    >>> f = ((x > 0) | (x < 0)) & (Eq(x, 0) | Eq(y, 1)) & (~Eq(y, 1) | Eq(1, 2))

    First a preprocessing step should be done on f. During preprocessing,
    f should be checked for any predicates such as `Q.prime` that can't be
    handled. Also unequality like `~Eq(y, 1)` should be split.

    I should mention that the paper says to split both equalities and
    unequality, but this implementation only requires that unequality
    be split.

    >>> f = ((x > 0) | (x < 0)) & (Eq(x, 0) | Eq(y, 1)) & ((y < 1) | (y > 1) | Eq(1, 2))

    Then an LRASolver instance needs to be initialized with this formula.

    >>> from sympy.assumptions.cnf import CNF, EncodedCNF
    >>> from sympy.assumptions.ask import Q
    >>> from sympy.logic.algorithms.lra_theory import LRASolver
    >>> cnf = CNF.from_prop(f)
    >>> enc = EncodedCNF()
    >>> enc.add_from_cnf(cnf)
    >>> lra, conflicts = LRASolver.from_encoded_cnf(enc)

    Any immediate one-lital conflicts clauses will be detected here.
    In this example, `~Eq(1, 2)` is one such conflict clause. We'll
    want to add it to `f` so that the SAT solver is forced to
    assign Eq(1, 2) to False.

    >>> f = f & ~Eq(1, 2)

    Now that the one-literal conflict clauses have been added
    and an lra object has been initialized, we can pass `f`
    to a SAT solver. The SAT solver will give us a satisfying
    assignment such as:

    (1 = 2): False
    (y = 1): True
    (y < 1): True
    (y > 1): True
    (x = 0): True
    (x < 0): True
    (x > 0): True

    Next you would pass this assignment to the LRASolver
    which will be able to determine that this particular
    assignment is satisfiable or not.

    Note that since EncodedCNF is inherently non-deterministic,
    the int each predicate is encoded as is not consistent. As a
    result, the code bellow likely does not reflect the assignment
    given above.

    >>> lra.assert_lit(-1) #doctest: +SKIP
    >>> lra.assert_lit(2) #doctest: +SKIP
    >>> lra.assert_lit(3) #doctest: +SKIP
    >>> lra.assert_lit(4) #doctest: +SKIP
    >>> lra.assert_lit(5) #doctest: +SKIP
    >>> lra.assert_lit(6) #doctest: +SKIP
    >>> lra.assert_lit(7) #doctest: +SKIP
    >>> is_sat, conflict_or_assignment = lra.check()

    As the particular assignment suggested is not satisfiable,
    the LRASolver will return unsat and a conflict clause when
    given that assignment. The conflict clause will always be
    minimal, but there can be multiple minimal conflict clauses.
    One possible conflict clause could be `~(x < 0) | ~(x > 0)`.

    We would then add whatever conflict clause is given to
    `f` to prevent the SAT solver from coming up with an
    assignment with the same conflicting literals. In this case,
    the conflict clause `~(x < 0) | ~(x > 0)` would prevent
    any assignment where both (x < 0) and (x > 0) were both
    true.

    The SAT solver would then find another assignment
    and we would check that assignment with the LRASolver
    and so on. Eventually either a satisfying assignment
    that the SAT solver and LRASolver agreed on would be found
    or enough conflict clauses would be added so that the
    boolean formula was unsatisfiable.


This implementation is based on [1]_, which includes a
detailed explanation of the algorithm and pseudocode
for the most important functions.

[1]_ also explains how backtracking and theory propagation
could be implemented to speed up the current implementation,
but these are not currently implemented.

TODO:
 - Handle non-rational real numbers
 - Handle positive and negative infinity
 - Implement backtracking and theory proposition
 - Simplify matrix by removing unused variables using Gaussian elimination

References
==========

.. [1] Dutertre, B., de Moura, L.:
       A Fast Linear-Arithmetic Solver for DPLL(T)
       https://link.springer.com/chapter/10.1007/11817963_11
"""
class UnhandledInput(Exception):
    """
    Raised while creating an LRASolver if non-linearity
    or non-rational numbers are present.
    """
    ...


ALLOWED_PRED = ...
HANDLE_NEGATION = ...
class LRASolver:
    """
    Linear Arithmetic Solver for DPLL(T) implemented with an algorithm based on
    the Dual Simplex method. Uses Bland's pivoting rule to avoid cycling.

    References
    ==========

    .. [1] Dutertre, B., de Moura, L.:
           A Fast Linear-Arithmetic Solver for DPLL(T)
           https://link.springer.com/chapter/10.1007/11817963_11
    """
    def __init__(self, A, slack_variables, nonslack_variables, enc_to_boundary, s_subs, testing_mode) -> None:
        """
        Use the "from_encoded_cnf" method to create a new LRASolver.
        """
        ...
    
    @staticmethod
    def from_encoded_cnf(encoded_cnf, testing_mode=...) -> tuple[LRASolver, list[Any]]:
        """
        Creates an LRASolver from an EncodedCNF object
        and a list of conflict clauses for propositions
        that can be simplified to True or False.

        Parameters
        ==========

        encoded_cnf : EncodedCNF

        testing_mode : bool
            Setting testing_mode to True enables some slow assert statements
            and sorting to reduce nonterministic behavior.

        Returns
        =======

        (lra, conflicts)

        lra : LRASolver

        conflicts : list
            Contains a one-literal conflict clause for each proposition
            that can be simplified to True or False.

        Example
        =======

        >>> from sympy.core.relational import Eq
        >>> from sympy.assumptions.cnf import CNF, EncodedCNF
        >>> from sympy.assumptions.ask import Q
        >>> from sympy.logic.algorithms.lra_theory import LRASolver
        >>> from sympy.abc import x, y, z
        >>> phi = (x >= 0) & ((x + y <= 2) | (x + 2 * y - z >= 6))
        >>> phi = phi & (Eq(x + y, 2) | (x + 2 * y - z > 4))
        >>> phi = phi & Q.gt(2, 1)
        >>> cnf = CNF.from_prop(phi)
        >>> enc = EncodedCNF()
        >>> enc.from_cnf(cnf)
        >>> lra, conflicts = LRASolver.from_encoded_cnf(enc, testing_mode=True)
        >>> lra #doctest: +SKIP
        <sympy.logic.algorithms.lra_theory.LRASolver object at 0x7fdcb0e15b70>
        >>> conflicts #doctest: +SKIP
        [[4]]
        """
        ...
    
    def reset_bounds(self) -> None:
        """
        Resets the state of the LRASolver to before
        anything was asserted.
        """
        ...
    
    def assert_lit(self, enc_constraint) -> tuple[Literal[False], list[Any]] | None:
        """
        Assert a literal representing a constraint
        and update the internal state accordingly.

        Note that due to peculiarities of this implementation
        asserting ~(x > 0) will assert (x <= 0) but asserting
        ~Eq(x, 0) will not do anything.

        Parameters
        ==========

        enc_constraint : int
            A mapping of encodings to constraints
            can be found in `self.enc_to_boundary`.

        Returns
        =======

        None or (False, explanation)

        explanation : set of ints
            A conflict clause that "explains" why
            the literals asserted so far are unsatisfiable.
        """
        ...
    
    def check(self) -> tuple[Literal[True], dict[Any, Any]] | tuple[Literal[False], list[Any]]:
        """
        Searches for an assignment that satisfies all constraints
        or determines that no such assignment exists and gives
        a minimal conflict clause that "explains" why the
        constraints are unsatisfiable.

        Returns
        =======

        (True, assignment) or (False, explanation)

        assignment : dict of LRAVariables to values
            Assigned values are tuples that represent a rational number
            plus some infinatesimal delta.

        explanation : set of ints
        """
        ...
    


class Boundary:
    """
    Represents an upper or lower bound or an equality between a symbol
    and some constant.
    """
    def __init__(self, var, const, upper, equality, strict=...) -> None:
        ...
    
    @staticmethod
    def from_upper(var) -> tuple[Boundary, Literal[-1, 1]]:
        ...
    
    @staticmethod
    def from_lower(var) -> tuple[Boundary, Literal[-1, 1]]:
        ...
    
    def get_negated(self) -> Boundary:
        ...
    
    def get_inequality(self) -> Eq | Relational | Ne:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class LRARational:
    """
    Represents a rational plus or minus some amount
    of arbitrary small deltas.
    """
    def __init__(self, rational, delta) -> None:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __add__(self, other) -> LRARational:
        ...
    
    def __sub__(self, other) -> LRARational:
        ...
    
    def __mul__(self, other) -> LRARational:
        ...
    
    def __getitem__(self, index) -> Any:
        ...
    
    def __repr__(self) -> str:
        ...
    


class LRAVariable:
    """
    Object to keep track of upper and lower bounds
    on `self.var`.
    """
    def __init__(self, var) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


