__all__ = ['diophantine', 'classify_diop']
class DiophantineSolutionSet(set):
    """
    Container for a set of solutions to a particular diophantine equation.

    The base representation is a set of tuples representing each of the solutions.

    Parameters
    ==========

    symbols : list
        List of free symbols in the original equation.
    parameters: list
        List of parameters to be used in the solution.

    Examples
    ========

    Adding solutions:

        >>> from sympy.solvers.diophantine.diophantine import DiophantineSolutionSet
        >>> from sympy.abc import x, y, t, u
        >>> s1 = DiophantineSolutionSet([x, y], [t, u])
        >>> s1
        set()
        >>> s1.add((2, 3))
        >>> s1.add((-1, u))
        >>> s1
        {(-1, u), (2, 3)}
        >>> s2 = DiophantineSolutionSet([x, y], [t, u])
        >>> s2.add((3, 4))
        >>> s1.update(*s2)
        >>> s1
        {(-1, u), (2, 3), (3, 4)}

    Conversion of solutions into dicts:

        >>> list(s1.dict_iterator())
        [{x: -1, y: u}, {x: 2, y: 3}, {x: 3, y: 4}]

    Substituting values:

        >>> s3 = DiophantineSolutionSet([x, y], [t, u])
        >>> s3.add((t**2, t + u))
        >>> s3
        {(t**2, t + u)}
        >>> s3.subs({t: 2, u: 3})
        {(4, 5)}
        >>> s3.subs(t, -1)
        {(1, u - 1)}
        >>> s3.subs(t, 3)
        {(9, u + 3)}

    Evaluation at specific values. Positional arguments are given in the same order as the parameters:

        >>> s3(-2, 3)
        {(4, 1)}
        >>> s3(5)
        {(25, u + 5)}
        >>> s3(None, 2)
        {(t**2, t + 2)}
    """
    def __init__(self, symbols_seq, parameters) -> None:
        ...
    
    def add(self, solution) -> None:
        ...
    
    def update(self, *solutions) -> None:
        ...
    
    def dict_iterator(self) -> Generator[dict[Any, Any], Any, None]:
        ...
    
    def subs(self, *args, **kwargs) -> DiophantineSolutionSet:
        ...
    
    def __call__(self, *args) -> DiophantineSolutionSet:
        ...
    


class DiophantineEquationType:
    """
    Internal representation of a particular diophantine equation type.

    Parameters
    ==========

    equation :
        The diophantine equation that is being solved.
    free_symbols : list (optional)
        The symbols being solved for.

    Attributes
    ==========

    total_degree :
        The maximum of the degrees of all terms in the equation
    homogeneous :
        Does the equation contain a term of degree 0
    homogeneous_order :
        Does the equation contain any coefficient that is in the symbols being solved for
    dimension :
        The number of symbols being solved for
    """
    name: str = ...
    def __init__(self, equation, free_symbols=...) -> None:
        ...
    
    def matches(self) -> Literal[False]:
        """
        Determine whether the given equation can be matched to the particular equation type.
        """
        ...
    
    @property
    def n_parameters(self) -> int:
        ...
    
    @property
    def parameters(self) -> Any:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    
    def pre_solve(self, parameters=...) -> None:
        ...
    


class Univariate(DiophantineEquationType):
    """
    Representation of a univariate diophantine equation.

    A univariate diophantine equation is an equation of the form
    `a_{0} + a_{1}x + a_{2}x^2 + .. + a_{n}x^n = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x` is an integer variable.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Univariate
    >>> from sympy.abc import x
    >>> Univariate((x - 2)*(x - 3)**2).solve() # solves equation (x - 2)*(x - 3)**2 == 0
    {(2,), (3,)}

    """
    name = ...
    def matches(self) -> bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class Linear(DiophantineEquationType):
    """
    Representation of a linear diophantine equation.

    A linear diophantine equation is an equation of the form `a_{1}x_{1} +
    a_{2}x_{2} + .. + a_{n}x_{n} = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x_{1}, x_{2}, ..x_{n}` are integer variables.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Linear
    >>> from sympy.abc import x, y, z
    >>> l1 = Linear(2*x - 3*y - 5)
    >>> l1.matches() # is this equation linear
    True
    >>> l1.solve() # solves equation 2*x - 3*y - 5 == 0
    {(3*t_0 - 5, 2*t_0 - 5)}

    Here x = -3*t_0 - 5 and y = -2*t_0 - 5

    >>> Linear(2*x - 3*y - 4*z -3).solve()
    {(t_0, 2*t_0 + 4*t_1 + 3, -t_0 - 3*t_1 - 3)}

    """
    name = ...
    def matches(self) -> Any:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class BinaryQuadratic(DiophantineEquationType):
    """
    Representation of a binary quadratic diophantine equation.

    A binary quadratic diophantine equation is an equation of the
    form `Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0`, where `A, B, C, D, E,
    F` are integer constants and `x` and `y` are integer variables.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import BinaryQuadratic
    >>> b1 = BinaryQuadratic(x**3 + y**2 + 1)
    >>> b1.matches()
    False
    >>> b2 = BinaryQuadratic(x**2 + y**2 + 2*x + 2*y + 2)
    >>> b2.matches()
    True
    >>> b2.solve()
    {(-1, -1)}

    References
    ==========

    .. [1] Methods to solve Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, [online],
          Available: https://www.alpertron.com.ar/METHODS.HTM
    .. [2] Solving the equation ax^2+ bxy + cy^2 + dx + ey + f= 0, [online],
          Available: https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf

    """
    name = ...
    def matches(self) -> Any | bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class InhomogeneousTernaryQuadratic(DiophantineEquationType):
    """

    Representation of an inhomogeneous ternary quadratic.

    No solver is currently implemented for this equation type.

    """
    name = ...
    def matches(self) -> bool:
        ...
    


class HomogeneousTernaryQuadraticNormal(DiophantineEquationType):
    """
    Representation of a homogeneous ternary quadratic normal diophantine equation.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import HomogeneousTernaryQuadraticNormal
    >>> HomogeneousTernaryQuadraticNormal(4*x**2 - 5*y**2 + z**2).solve()
    {(1, 2, 4)}

    """
    name = ...
    def matches(self) -> bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class HomogeneousTernaryQuadratic(DiophantineEquationType):
    """
    Representation of a homogeneous ternary quadratic diophantine equation.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import HomogeneousTernaryQuadratic
    >>> HomogeneousTernaryQuadratic(x**2 + y**2 - 3*z**2 + x*y).solve()
    {(-1, 2, 1)}
    >>> HomogeneousTernaryQuadratic(3*x**2 + y**2 - 3*z**2 + 5*x*y + y*z).solve()
    {(3, 12, 13)}

    """
    name = ...
    def matches(self) -> bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class InhomogeneousGeneralQuadratic(DiophantineEquationType):
    """

    Representation of an inhomogeneous general quadratic.

    No solver is currently implemented for this equation type.

    """
    name = ...
    def matches(self) -> bool:
        ...
    


class HomogeneousGeneralQuadratic(DiophantineEquationType):
    """

    Representation of a homogeneous general quadratic.

    No solver is currently implemented for this equation type.

    """
    name = ...
    def matches(self) -> bool:
        ...
    


class GeneralSumOfSquares(DiophantineEquationType):
    r"""
    Representation of the diophantine equation

    `x_{1}^2 + x_{2}^2 + . . . + x_{n}^2 - k = 0`.

    Details
    =======

    When `n = 3` if `k = 4^a(8m + 7)` for some `a, m \in Z` then there will be
    no solutions. Refer [1]_ for more details.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralSumOfSquares
    >>> from sympy.abc import a, b, c, d, e
    >>> GeneralSumOfSquares(a**2 + b**2 + c**2 + d**2 + e**2 - 2345).solve()
    {(15, 22, 22, 24, 24)}

    By default only 1 solution is returned. Use the `limit` keyword for more:

    >>> sorted(GeneralSumOfSquares(a**2 + b**2 + c**2 + d**2 + e**2 - 2345).solve(limit=3))
    [(15, 22, 22, 24, 24), (16, 19, 24, 24, 24), (16, 20, 22, 23, 26)]

    References
    ==========

    .. [1] Representing an integer as a sum of three squares, [online],
        Available:
        https://www.proofwiki.org/wiki/Integer_as_Sum_of_Three_Squares
    """
    name = ...
    def matches(self) -> bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class GeneralPythagorean(DiophantineEquationType):
    """
    Representation of the general pythagorean equation,
    `a_{1}^2x_{1}^2 + a_{2}^2x_{2}^2 + . . . + a_{n}^2x_{n}^2 - a_{n + 1}^2x_{n + 1}^2 = 0`.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralPythagorean
    >>> from sympy.abc import a, b, c, d, e, x, y, z, t
    >>> GeneralPythagorean(a**2 + b**2 + c**2 - d**2).solve()
    {(t_0**2 + t_1**2 - t_2**2, 2*t_0*t_2, 2*t_1*t_2, t_0**2 + t_1**2 + t_2**2)}
    >>> GeneralPythagorean(9*a**2 - 4*b**2 + 16*c**2 + 25*d**2 + e**2).solve(parameters=[x, y, z, t])
    {(-10*t**2 + 10*x**2 + 10*y**2 + 10*z**2, 15*t**2 + 15*x**2 + 15*y**2 + 15*z**2, 15*t*x, 12*t*y, 60*t*z)}
    """
    name = ...
    def matches(self) -> Literal[False]:
        ...
    
    @property
    def n_parameters(self) -> int:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


class CubicThue(DiophantineEquationType):
    """
    Representation of a cubic Thue diophantine equation.

    A cubic Thue diophantine equation is a polynomial of the form
    `f(x, y) = r` of degree 3, where `x` and `y` are integers
    and `r` is a rational number.

    No solver is currently implemented for this equation type.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import CubicThue
    >>> c1 = CubicThue(x**3 + y**2 + 1)
    >>> c1.matches()
    True

    """
    name = ...
    def matches(self) -> Any | bool:
        ...
    


class GeneralSumOfEvenPowers(DiophantineEquationType):
    """
    Representation of the diophantine equation

    `x_{1}^e + x_{2}^e + . . . + x_{n}^e - k = 0`

    where `e` is an even, integer power.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralSumOfEvenPowers
    >>> from sympy.abc import a, b
    >>> GeneralSumOfEvenPowers(a**4 + b**4 - (2**4 + 3**4)).solve()
    {(2, 3)}

    """
    name = ...
    def matches(self) -> bool:
        ...
    
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet:
        ...
    


all_diop_classes = ...
diop_known = ...
def diophantine(eq, param=..., syms=..., permute=...):
    """
    Simplify the solution procedure of diophantine equation ``eq`` by
    converting it into a product of terms which should equal zero.

    Explanation
    ===========

    For example, when solving, `x^2 - y^2 = 0` this is treated as
    `(x + y)(x - y) = 0` and `x + y = 0` and `x - y = 0` are solved
    independently and combined. Each term is solved by calling
    ``diop_solve()``. (Although it is possible to call ``diop_solve()``
    directly, one must be careful to pass an equation in the correct
    form and to interpret the output correctly; ``diophantine()`` is
    the public-facing function to use in general.)

    Output of ``diophantine()`` is a set of tuples. The elements of the
    tuple are the solutions for each variable in the equation and
    are arranged according to the alphabetic ordering of the variables.
    e.g. For an equation with two variables, `a` and `b`, the first
    element of the tuple is the solution for `a` and the second for `b`.

    Usage
    =====

    ``diophantine(eq, t, syms)``: Solve the diophantine
    equation ``eq``.
    ``t`` is the optional parameter to be used by ``diop_solve()``.
    ``syms`` is an optional list of symbols which determines the
    order of the elements in the returned tuple.

    By default, only the base solution is returned. If ``permute`` is set to
    True then permutations of the base solution and/or permutations of the
    signs of the values will be returned when applicable.

    Details
    =======

    ``eq`` should be an expression which is assumed to be zero.
    ``t`` is the parameter to be used in the solution.

    Examples
    ========

    >>> from sympy import diophantine
    >>> from sympy.abc import a, b
    >>> eq = a**4 + b**4 - (2**4 + 3**4)
    >>> diophantine(eq)
    {(2, 3)}
    >>> diophantine(eq, permute=True)
    {(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)}

    >>> from sympy.abc import x, y, z
    >>> diophantine(x**2 - y**2)
    {(t_0, -t_0), (t_0, t_0)}

    >>> diophantine(x*(2*x + 3*y - z))
    {(0, n1, n2), (t_0, t_1, 2*t_0 + 3*t_1)}
    >>> diophantine(x**2 + 3*x*y + 4*x)
    {(0, n1), (-3*t_0 - 4, t_0)}

    See Also
    ========

    diop_solve
    sympy.utilities.iterables.permute_signs
    sympy.utilities.iterables.signed_permutations
    """
    ...

def merge_solution(var, var_t, solution) -> tuple[()] | tuple[Any, ...]:
    """
    This is used to construct the full solution from the solutions of sub
    equations.

    Explanation
    ===========

    For example when solving the equation `(x - y)(x^2 + y^2 - z^2) = 0`,
    solutions for each of the equations `x - y = 0` and `x^2 + y^2 - z^2` are
    found independently. Solutions for `x - y = 0` are `(x, y) = (t, t)`. But
    we should introduce a value for z when we output the solution for the
    original equation. This function converts `(t, t)` into `(t, t, n_{1})`
    where `n_{1}` is an integer parameter.
    """
    ...

def diop_solve(eq, param=...) -> tuple[None, ...] | set[Any] | tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | tuple[Any | None, Any | None, Any | None] | set[tuple[int]] | None:
    """
    Solves the diophantine equation ``eq``.

    Explanation
    ===========

    Unlike ``diophantine()``, factoring of ``eq`` is not attempted. Uses
    ``classify_diop()`` to determine the type of the equation and calls
    the appropriate solver function.

    Use of ``diophantine()`` is recommended over other helper functions.
    ``diop_solve()`` can return either a set or a tuple depending on the
    nature of the equation.

    Usage
    =====

    ``diop_solve(eq, t)``: Solve diophantine equation, ``eq`` using ``t``
    as a parameter if needed.

    Details
    =======

    ``eq`` should be an expression which is assumed to be zero.
    ``t`` is a parameter to be used in the solution.

    Examples
    ========

    >>> from sympy.solvers.diophantine import diop_solve
    >>> from sympy.abc import x, y, z, w
    >>> diop_solve(2*x + 3*y - 5)
    (3*t_0 - 5, 5 - 2*t_0)
    >>> diop_solve(4*x + 3*y - 4*z + 5)
    (t_0, 8*t_0 + 4*t_1 + 5, 7*t_0 + 3*t_1 + 5)
    >>> diop_solve(x + 3*y - 4*z + w - 6)
    (t_0, t_0 + t_1, 6*t_0 + 5*t_1 + 4*t_2 - 6, 5*t_0 + 4*t_1 + 3*t_2 - 6)
    >>> diop_solve(x**2 + y**2 - 5)
    {(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)}


    See Also
    ========

    diophantine()
    """
    ...

def classify_diop(eq, _dict=...) -> tuple[Any, dict[Any, Any] | Any, Any]:
    ...

def diop_linear(eq, param=...) -> tuple[None, ...] | None:
    """
    Solves linear diophantine equations.

    A linear diophantine equation is an equation of the form `a_{1}x_{1} +
    a_{2}x_{2} + .. + a_{n}x_{n} = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x_{1}, x_{2}, ..x_{n}` are integer variables.

    Usage
    =====

    ``diop_linear(eq)``: Returns a tuple containing solutions to the
    diophantine equation ``eq``. Values in the tuple is arranged in the same
    order as the sorted variables.

    Details
    =======

    ``eq`` is a linear diophantine equation which is assumed to be zero.
    ``param`` is the parameter to be used in the solution.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_linear
    >>> from sympy.abc import x, y, z
    >>> diop_linear(2*x - 3*y - 5) # solves equation 2*x - 3*y - 5 == 0
    (3*t_0 - 5, 2*t_0 - 5)

    Here x = -3*t_0 - 5 and y = -2*t_0 - 5

    >>> diop_linear(2*x - 3*y - 4*z -3)
    (t_0, 2*t_0 + 4*t_1 + 3, -t_0 - 3*t_1 - 3)

    See Also
    ========

    diop_quadratic(), diop_ternary_quadratic(), diop_general_pythagorean(),
    diop_general_sum_of_squares()
    """
    ...

def base_solution_linear(c, a, b, t=...) -> tuple[Literal[0], Literal[0]] | tuple[Any, Any] | tuple[None, None]:
    """
    Return the base solution for the linear equation, `ax + by = c`.

    Explanation
    ===========

    Used by ``diop_linear()`` to find the base solution of a linear
    Diophantine equation. If ``t`` is given then the parametrized solution is
    returned.

    Usage
    =====

    ``base_solution_linear(c, a, b, t)``: ``a``, ``b``, ``c`` are coefficients
    in `ax + by = c` and ``t`` is the parameter to be used in the solution.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import base_solution_linear
    >>> from sympy.abc import t
    >>> base_solution_linear(5, 2, 3) # equation 2*x + 3*y = 5
    (-5, 5)
    >>> base_solution_linear(0, 5, 7) # equation 5*x + 7*y = 0
    (0, 0)
    >>> base_solution_linear(5, 2, 3, t) # equation 2*x + 3*y = 5
    (3*t - 5, 5 - 2*t)
    >>> base_solution_linear(0, 5, 7, t) # equation 5*x + 7*y = 0
    (7*t, -5*t)
    """
    ...

def diop_univariate(eq) -> set[tuple[int]] | None:
    """
    Solves a univariate diophantine equations.

    Explanation
    ===========

    A univariate diophantine equation is an equation of the form
    `a_{0} + a_{1}x + a_{2}x^2 + .. + a_{n}x^n = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x` is an integer variable.

    Usage
    =====

    ``diop_univariate(eq)``: Returns a set containing solutions to the
    diophantine equation ``eq``.

    Details
    =======

    ``eq`` is a univariate diophantine equation which is assumed to be zero.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_univariate
    >>> from sympy.abc import x
    >>> diop_univariate((x - 2)*(x - 3)**2) # solves equation (x - 2)*(x - 3)**2 == 0
    {(2,), (3,)}

    """
    ...

def divisible(a, b) -> bool:
    """
    Returns `True` if ``a`` is divisible by ``b`` and `False` otherwise.
    """
    ...

def diop_quadratic(eq, param=...) -> set[Any] | None:
    """
    Solves quadratic diophantine equations.

    i.e. equations of the form `Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0`. Returns a
    set containing the tuples `(x, y)` which contains the solutions. If there
    are no solutions then `(None, None)` is returned.

    Usage
    =====

    ``diop_quadratic(eq, param)``: ``eq`` is a quadratic binary diophantine
    equation. ``param`` is used to indicate the parameter to be used in the
    solution.

    Details
    =======

    ``eq`` should be an expression which is assumed to be zero.
    ``param`` is a parameter to be used in the solution.

    Examples
    ========

    >>> from sympy.abc import x, y, t
    >>> from sympy.solvers.diophantine.diophantine import diop_quadratic
    >>> diop_quadratic(x**2 + y**2 + 2*x + 2*y + 2, t)
    {(-1, -1)}

    References
    ==========

    .. [1] Methods to solve Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, [online],
          Available: https://www.alpertron.com.ar/METHODS.HTM
    .. [2] Solving the equation ax^2+ bxy + cy^2 + dx + ey + f= 0, [online],
          Available: https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf

    See Also
    ========

    diop_linear(), diop_ternary_quadratic(), diop_general_sum_of_squares(),
    diop_general_pythagorean()
    """
    ...

def is_solution_quad(var, coeff, u, v) -> NotImplementedType | bool:
    """
    Check whether `(u, v)` is solution to the quadratic binary diophantine
    equation with the variable list ``var`` and coefficient dictionary
    ``coeff``.

    Not intended for use by normal users.
    """
    ...

def diop_DN(D, N, t=...):
    """
    Solves the equation `x^2 - Dy^2 = N`.

    Explanation
    ===========

    Mainly concerned with the case `D > 0, D` is not a perfect square,
    which is the same as the generalized Pell equation. The LMM
    algorithm [1]_ is used to solve this equation.

    Returns one solution tuple, (`x, y)` for each class of the solutions.
    Other solutions of the class can be constructed according to the
    values of ``D`` and ``N``.

    Usage
    =====

    ``diop_DN(D, N, t)``: D and N are integers as in `x^2 - Dy^2 = N` and
    ``t`` is the parameter to be used in the solutions.

    Details
    =======

    ``D`` and ``N`` correspond to D and N in the equation.
    ``t`` is the parameter to be used in the solutions.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_DN
    >>> diop_DN(13, -4) # Solves equation x**2 - 13*y**2 = -4
    [(3, 1), (393, 109), (36, 10)]

    The output can be interpreted as follows: There are three fundamental
    solutions to the equation `x^2 - 13y^2 = -4` given by (3, 1), (393, 109)
    and (36, 10). Each tuple is in the form (x, y), i.e. solution (3, 1) means
    that `x = 3` and `y = 1`.

    >>> diop_DN(986, 1) # Solves equation x**2 - 986*y**2 = 1
    [(49299, 1570)]

    See Also
    ========

    find_DN(), diop_bf_DN()

    References
    ==========

    .. [1] Solving the generalized Pell equation x**2 - D*y**2 = N, John P.
        Robertson, July 31, 2004, Pages 16 - 17. [online], Available:
        https://web.archive.org/web/20160323033128/http://www.jpr2718.org/pell.pdf
    """
    ...

def cornacchia(a: int, b: int, m: int) -> set[tuple[int, int]]:
    r"""
    Solves `ax^2 + by^2 = m` where `\gcd(a, b) = 1 = gcd(a, m)` and `a, b > 0`.

    Explanation
    ===========

    Uses the algorithm due to Cornacchia. The method only finds primitive
    solutions, i.e. ones with `\gcd(x, y) = 1`. So this method cannot be used to
    find the solutions of `x^2 + y^2 = 20` since the only solution to former is
    `(x, y) = (4, 2)` and it is not primitive. When `a = b`, only the
    solutions with `x \leq y` are found. For more details, see the References.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import cornacchia
    >>> cornacchia(2, 3, 35) # equation 2x**2 + 3y**2 = 35
    {(2, 3), (4, 1)}
    >>> cornacchia(1, 1, 25) # equation x**2 + y**2 = 25
    {(4, 3)}

    References
    ===========

    .. [1] A. Nitaj, "L'algorithme de Cornacchia"
    .. [2] Solving the diophantine equation ax**2 + by**2 = m by Cornacchia's
        method, [online], Available:
        http://www.numbertheory.org/php/cornacchia.html

    See Also
    ========

    sympy.utilities.iterables.signed_permutations
    """
    ...

def PQa(P_0, Q_0, D) -> Generator[tuple[Any, Any, Any, Any, Any, Any], Any, NoReturn]:
    r"""
    Returns useful information needed to solve the Pell equation.

    Explanation
    ===========

    There are six sequences of integers defined related to the continued
    fraction representation of `\\frac{P + \sqrt{D}}{Q}`, namely {`P_{i}`},
    {`Q_{i}`}, {`a_{i}`},{`A_{i}`}, {`B_{i}`}, {`G_{i}`}. ``PQa()`` Returns
    these values as a 6-tuple in the same order as mentioned above. Refer [1]_
    for more detailed information.

    Usage
    =====

    ``PQa(P_0, Q_0, D)``: ``P_0``, ``Q_0`` and ``D`` are integers corresponding
    to `P_{0}`, `Q_{0}` and `D` in the continued fraction
    `\\frac{P_{0} + \sqrt{D}}{Q_{0}}`.
    Also it's assumed that `P_{0}^2 == D mod(|Q_{0}|)` and `D` is square free.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import PQa
    >>> pqa = PQa(13, 4, 5) # (13 + sqrt(5))/4
    >>> next(pqa) # (P_0, Q_0, a_0, A_0, B_0, G_0)
    (13, 4, 3, 3, 1, -1)
    >>> next(pqa) # (P_1, Q_1, a_1, A_1, B_1, G_1)
    (-1, 1, 1, 4, 1, 3)

    References
    ==========

    .. [1] Solving the generalized Pell equation x^2 - Dy^2 = N, John P.
        Robertson, July 31, 2004, Pages 4 - 8. https://web.archive.org/web/20160323033128/http://www.jpr2718.org/pell.pdf
    """
    ...

def diop_bf_DN(D, N, t=...) -> list[tuple[Literal[0], Literal[0]]] | list[tuple[Literal[0], Any]] | list[tuple[Any, Any]] | list[Any]:
    r"""
    Uses brute force to solve the equation, `x^2 - Dy^2 = N`.

    Explanation
    ===========

    Mainly concerned with the generalized Pell equation which is the case when
    `D > 0, D` is not a perfect square. For more information on the case refer
    [1]_. Let `(t, u)` be the minimal positive solution of the equation
    `x^2 - Dy^2 = 1`. Then this method requires
    `\sqrt{\\frac{\mid N \mid (t \pm 1)}{2D}}` to be small.

    Usage
    =====

    ``diop_bf_DN(D, N, t)``: ``D`` and ``N`` are coefficients in
    `x^2 - Dy^2 = N` and ``t`` is the parameter to be used in the solutions.

    Details
    =======

    ``D`` and ``N`` correspond to D and N in the equation.
    ``t`` is the parameter to be used in the solutions.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_bf_DN
    >>> diop_bf_DN(13, -4)
    [(3, 1), (-3, 1), (36, 10)]
    >>> diop_bf_DN(986, 1)
    [(49299, 1570)]

    See Also
    ========

    diop_DN()

    References
    ==========

    .. [1] Solving the generalized Pell equation x**2 - D*y**2 = N, John P.
        Robertson, July 31, 2004, Page 15. https://web.archive.org/web/20160323033128/http://www.jpr2718.org/pell.pdf
    """
    ...

def equivalent(u, v, r, s, D, N) -> bool:
    """
    Returns True if two solutions `(u, v)` and `(r, s)` of `x^2 - Dy^2 = N`
    belongs to the same equivalence class and False otherwise.

    Explanation
    ===========

    Two solutions `(u, v)` and `(r, s)` to the above equation fall to the same
    equivalence class iff both `(ur - Dvs)` and `(us - vr)` are divisible by
    `N`. See reference [1]_. No test is performed to test whether `(u, v)` and
    `(r, s)` are actually solutions to the equation. User should take care of
    this.

    Usage
    =====

    ``equivalent(u, v, r, s, D, N)``: `(u, v)` and `(r, s)` are two solutions
    of the equation `x^2 - Dy^2 = N` and all parameters involved are integers.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import equivalent
    >>> equivalent(18, 5, -18, -5, 13, -1)
    True
    >>> equivalent(3, 1, -18, 393, 109, -4)
    False

    References
    ==========

    .. [1] Solving the generalized Pell equation x**2 - D*y**2 = N, John P.
        Robertson, July 31, 2004, Page 12. https://web.archive.org/web/20160323033128/http://www.jpr2718.org/pell.pdf

    """
    ...

def length(P, Q, D) -> int:
    r"""
    Returns the (length of aperiodic part + length of periodic part) of
    continued fraction representation of `\\frac{P + \sqrt{D}}{Q}`.

    It is important to remember that this does NOT return the length of the
    periodic part but the sum of the lengths of the two parts as mentioned
    above.

    Usage
    =====

    ``length(P, Q, D)``: ``P``, ``Q`` and ``D`` are integers corresponding to
    the continued fraction `\\frac{P + \sqrt{D}}{Q}`.

    Details
    =======

    ``P``, ``D`` and ``Q`` corresponds to P, D and Q in the continued fraction,
    `\\frac{P + \sqrt{D}}{Q}`.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import length
    >>> length(-2, 4, 5) # (-2 + sqrt(5))/4
    3
    >>> length(-5, 4, 17) # (-5 + sqrt(17))/4
    4

    See Also
    ========
    sympy.ntheory.continued_fraction.continued_fraction_periodic
    """
    ...

def transformation_to_DN(eq) -> tuple[Any, Any] | tuple[MutableDenseMatrix, MutableDenseMatrix] | None:
    """
    This function transforms general quadratic,
    `ax^2 + bxy + cy^2 + dx + ey + f = 0`
    to more easy to deal with `X^2 - DY^2 = N` form.

    Explanation
    ===========

    This is used to solve the general quadratic equation by transforming it to
    the latter form. Refer to [1]_ for more detailed information on the
    transformation. This function returns a tuple (A, B) where A is a 2 X 2
    matrix and B is a 2 X 1 matrix such that,

    Transpose([x y]) =  A * Transpose([X Y]) + B

    Usage
    =====

    ``transformation_to_DN(eq)``: where ``eq`` is the quadratic to be
    transformed.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import transformation_to_DN
    >>> A, B = transformation_to_DN(x**2 - 3*x*y - y**2 - 2*y + 1)
    >>> A
    Matrix([
    [1/26, 3/26],
    [   0, 1/13]])
    >>> B
    Matrix([
    [-6/13],
    [-4/13]])

    A, B  returned are such that Transpose((x y)) =  A * Transpose((X Y)) + B.
    Substituting these values for `x` and `y` and a bit of simplifying work
    will give an equation of the form `x^2 - Dy^2 = N`.

    >>> from sympy.abc import X, Y
    >>> from sympy import Matrix, simplify
    >>> u = (A*Matrix([X, Y]) + B)[0] # Transformation for x
    >>> u
    X/26 + 3*Y/26 - 6/13
    >>> v = (A*Matrix([X, Y]) + B)[1] # Transformation for y
    >>> v
    Y/13 - 4/13

    Next we will substitute these formulas for `x` and `y` and do
    ``simplify()``.

    >>> eq = simplify((x**2 - 3*x*y - y**2 - 2*y + 1).subs(zip((x, y), (u, v))))
    >>> eq
    X**2/676 - Y**2/52 + 17/13

    By multiplying the denominator appropriately, we can get a Pell equation
    in the standard form.

    >>> eq * 676
    X**2 - 13*Y**2 + 884

    If only the final equation is needed, ``find_DN()`` can be used.

    See Also
    ========

    find_DN()

    References
    ==========

    .. [1] Solving the equation ax^2 + bxy + cy^2 + dx + ey + f = 0,
           John P.Robertson, May 8, 2003, Page 7 - 11.
           https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf
    """
    ...

def find_DN(eq) -> tuple[Any, Any] | None:
    """
    This function returns a tuple, `(D, N)` of the simplified form,
    `x^2 - Dy^2 = N`, corresponding to the general quadratic,
    `ax^2 + bxy + cy^2 + dx + ey + f = 0`.

    Solving the general quadratic is then equivalent to solving the equation
    `X^2 - DY^2 = N` and transforming the solutions by using the transformation
    matrices returned by ``transformation_to_DN()``.

    Usage
    =====

    ``find_DN(eq)``: where ``eq`` is the quadratic to be transformed.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import find_DN
    >>> find_DN(x**2 - 3*x*y - y**2 - 2*y + 1)
    (13, -884)

    Interpretation of the output is that we get `X^2 -13Y^2 = -884` after
    transforming `x^2 - 3xy - y^2 - 2y + 1` using the transformation returned
    by ``transformation_to_DN()``.

    See Also
    ========

    transformation_to_DN()

    References
    ==========

    .. [1] Solving the equation ax^2 + bxy + cy^2 + dx + ey + f = 0,
           John P.Robertson, May 8, 2003, Page 7 - 11.
           https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf
    """
    ...

def check_param(x, y, a, params) -> DiophantineSolutionSet | None:
    """
    If there is a number modulo ``a`` such that ``x`` and ``y`` are both
    integers, then return a parametric representation for ``x`` and ``y``
    else return (None, None).

    Here ``x`` and ``y`` are functions of ``t``.
    """
    ...

def diop_ternary_quadratic(eq, parameterize=...) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | tuple[Any | None, Any | None, Any | None] | None:
    """
    Solves the general quadratic ternary form,
    `ax^2 + by^2 + cz^2 + fxy + gyz + hxz = 0`.

    Returns a tuple `(x, y, z)` which is a base solution for the above
    equation. If there are no solutions, `(None, None, None)` is returned.

    Usage
    =====

    ``diop_ternary_quadratic(eq)``: Return a tuple containing a basic solution
    to ``eq``.

    Details
    =======

    ``eq`` should be an homogeneous expression of degree two in three variables
    and it is assumed to be zero.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import diop_ternary_quadratic
    >>> diop_ternary_quadratic(x**2 + 3*y**2 - z**2)
    (1, 0, 1)
    >>> diop_ternary_quadratic(4*x**2 + 5*y**2 - z**2)
    (1, 0, 2)
    >>> diop_ternary_quadratic(45*x**2 - 7*y**2 - 8*x*y - z**2)
    (28, 45, 105)
    >>> diop_ternary_quadratic(x**2 - 49*y**2 - z**2 + 13*z*y -8*x*y)
    (9, 1, 5)
    """
    ...

def transformation_to_normal(eq) -> MutableDenseMatrix | None:
    """
    Returns the transformation Matrix that converts a general ternary
    quadratic equation ``eq`` (`ax^2 + by^2 + cz^2 + dxy + eyz + fxz`)
    to a form without cross terms: `ax^2 + by^2 + cz^2 = 0`. This is
    not used in solving ternary quadratics; it is only implemented for
    the sake of completeness.
    """
    ...

def parametrize_ternary_quadratic(eq) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | None:
    """
    Returns the parametrized general solution for the ternary quadratic
    equation ``eq`` which has the form
    `ax^2 + by^2 + cz^2 + fxy + gyz + hxz = 0`.

    Examples
    ========

    >>> from sympy import Tuple, ordered
    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import parametrize_ternary_quadratic

    The parametrized solution may be returned with three parameters:

    >>> parametrize_ternary_quadratic(2*x**2 + y**2 - 2*z**2)
    (p**2 - 2*q**2, -2*p**2 + 4*p*q - 4*p*r - 4*q**2, p**2 - 4*p*q + 2*q**2 - 4*q*r)

    There might also be only two parameters:

    >>> parametrize_ternary_quadratic(4*x**2 + 2*y**2 - 3*z**2)
    (2*p**2 - 3*q**2, -4*p**2 + 12*p*q - 6*q**2, 4*p**2 - 8*p*q + 6*q**2)

    Notes
    =====

    Consider ``p`` and ``q`` in the previous 2-parameter
    solution and observe that more than one solution can be represented
    by a given pair of parameters. If `p` and ``q`` are not coprime, this is
    trivially true since the common factor will also be a common factor of the
    solution values. But it may also be true even when ``p`` and
    ``q`` are coprime:

    >>> sol = Tuple(*_)
    >>> p, q = ordered(sol.free_symbols)
    >>> sol.subs([(p, 3), (q, 2)])
    (6, 12, 12)
    >>> sol.subs([(q, 1), (p, 1)])
    (-1, 2, 2)
    >>> sol.subs([(q, 0), (p, 1)])
    (2, -4, 4)
    >>> sol.subs([(q, 1), (p, 0)])
    (-3, -6, 6)

    Except for sign and a common factor, these are equivalent to
    the solution of (1, 2, 2).

    References
    ==========

    .. [1] The algorithmic resolution of Diophantine equations, Nigel P. Smart,
           London Mathematical Society Student Texts 41, Cambridge University
           Press, Cambridge, 1998.

    """
    ...

def diop_ternary_quadratic_normal(eq, parameterize=...) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | tuple[Any | None, Any | None, Any | None] | None:
    """
    Solves the quadratic ternary diophantine equation,
    `ax^2 + by^2 + cz^2 = 0`.

    Explanation
    ===========

    Here the coefficients `a`, `b`, and `c` should be non zero. Otherwise the
    equation will be a quadratic binary or univariate equation. If solvable,
    returns a tuple `(x, y, z)` that satisfies the given equation. If the
    equation does not have integer solutions, `(None, None, None)` is returned.

    Usage
    =====

    ``diop_ternary_quadratic_normal(eq)``: where ``eq`` is an equation of the form
    `ax^2 + by^2 + cz^2 = 0`.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import diop_ternary_quadratic_normal
    >>> diop_ternary_quadratic_normal(x**2 + 3*y**2 - z**2)
    (1, 0, 1)
    >>> diop_ternary_quadratic_normal(4*x**2 + 5*y**2 - z**2)
    (1, 0, 2)
    >>> diop_ternary_quadratic_normal(34*x**2 - 3*y**2 - 301*z**2)
    (4, 9, 1)
    """
    ...

def sqf_normal(a, b, c, steps=...) -> tuple[tuple[Any | Order, ...], tuple[Any, ...], tuple[Any, Any, Any]] | tuple[Any, Any, Any]:
    """
    Return `a', b', c'`, the coefficients of the square-free normal
    form of `ax^2 + by^2 + cz^2 = 0`, where `a', b', c'` are pairwise
    prime.  If `steps` is True then also return three tuples:
    `sq`, `sqf`, and `(a', b', c')` where `sq` contains the square
    factors of `a`, `b` and `c` after removing the `gcd(a, b, c)`;
    `sqf` contains the values of `a`, `b` and `c` after removing
    both the `gcd(a, b, c)` and the square factors.

    The solutions for `ax^2 + by^2 + cz^2 = 0` can be
    recovered from the solutions of `a'x^2 + b'y^2 + c'z^2 = 0`.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import sqf_normal
    >>> sqf_normal(2 * 3**2 * 5, 2 * 5 * 11, 2 * 7**2 * 11)
    (11, 1, 5)
    >>> sqf_normal(2 * 3**2 * 5, 2 * 5 * 11, 2 * 7**2 * 11, True)
    ((3, 1, 7), (5, 55, 11), (11, 1, 5))

    References
    ==========

    .. [1] Legendre's Theorem, Legrange's Descent,
           https://public.csusm.edu/aitken_html/notes/legendre.pdf


    See Also
    ========

    reconstruct()
    """
    ...

def square_factor(a) -> Order:
    r"""
    Returns an integer `c` s.t. `a = c^2k, \ c,k \in Z`. Here `k` is square
    free. `a` can be given as an integer or a dictionary of factors.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import square_factor
    >>> square_factor(24)
    2
    >>> square_factor(-36*3)
    6
    >>> square_factor(1)
    1
    >>> square_factor({3: 2, 2: 1, -1: 1})  # -18
    3

    See Also
    ========
    sympy.ntheory.factor_.core
    """
    ...

def reconstruct(A, B, z):
    """
    Reconstruct the `z` value of an equivalent solution of `ax^2 + by^2 + cz^2`
    from the `z` value of a solution of the square-free normal form of the
    equation, `a'*x^2 + b'*y^2 + c'*z^2`, where `a'`, `b'` and `c'` are square
    free and `gcd(a', b', c') == 1`.
    """
    ...

def ldescent(A, B) -> tuple[Any, Any, Any] | tuple[Literal[1], Literal[1], Literal[0]] | tuple[Literal[1], Literal[0], Literal[1]] | tuple[list[int] | int, Literal[-1], Literal[0]] | tuple[Any, ...] | None:
    """
    Return a non-trivial solution to `w^2 = Ax^2 + By^2` using
    Lagrange's method; return None if there is no such solution.

    Parameters
    ==========

    A : Integer
    B : Integer
        non-zero integer

    Returns
    =======

    (int, int, int) | None : a tuple `(w_0, x_0, y_0)` which is a solution to the above equation.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import ldescent
    >>> ldescent(1, 1) # w^2 = x^2 + y^2
    (1, 1, 0)
    >>> ldescent(4, -7) # w^2 = 4x^2 - 7y^2
    (2, -1, 0)

    This means that `x = -1, y = 0` and `w = 2` is a solution to the equation
    `w^2 = 4x^2 - 7y^2`

    >>> ldescent(5, -1) # w^2 = 5x^2 - y^2
    (2, 1, -1)

    References
    ==========

    .. [1] The algorithmic resolution of Diophantine equations, Nigel P. Smart,
           London Mathematical Society Student Texts 41, Cambridge University
           Press, Cambridge, 1998.
    .. [2] Cremona, J. E., Rusin, D. (2003). Efficient Solution of Rational Conics.
           Mathematics of Computation, 72(243), 1417-1441.
           https://doi.org/10.1090/S0025-5718-02-01480-1
    """
    ...

def descent(A, B) -> tuple[Any, Any, Any] | tuple[Literal[1], Literal[0], Literal[1]] | tuple[Literal[1], Literal[1], Literal[0]] | tuple[Literal[0], Literal[1], Literal[1]] | tuple[Any, ...]:
    """
    Returns a non-trivial solution, (x, y, z), to `x^2 = Ay^2 + Bz^2`
    using Lagrange's descent method with lattice-reduction. `A` and `B`
    are assumed to be valid for such a solution to exist.

    This is faster than the normal Lagrange's descent algorithm because
    the Gaussian reduction is used.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import descent
    >>> descent(3, 1) # x**2 = 3*y**2 + z**2
    (1, 0, 1)

    `(x, y, z) = (1, 0, 1)` is a solution to the above equation.

    >>> descent(41, -113)
    (-16, -3, 1)

    References
    ==========

    .. [1] Cremona, J. E., Rusin, D. (2003). Efficient Solution of Rational Conics.
           Mathematics of Computation, 72(243), 1417-1441.
           https://doi.org/10.1090/S0025-5718-02-01480-1
    """
    ...

def gaussian_reduce(w: int, a: int, b: int) -> tuple[int, int]:
    r"""
    Returns a reduced solution `(x, z)` to the congruence
    `X^2 - aZ^2 \equiv 0 \pmod{b}` so that `x^2 + |a|z^2` is as small as possible.
    Here ``w`` is a solution of the congruence `x^2 \equiv a \pmod{b}`.

    This function is intended to be used only for ``descent()``.

    Explanation
    ===========

    The Gaussian reduction can find the shortest vector for any norm.
    So we define the special norm for the vectors `u = (u_1, u_2)` and `v = (v_1, v_2)` as follows.

    .. math ::
        u \cdot v := (wu_1 + bu_2)(wv_1 + bv_2) + |a|u_1v_1

    Note that, given the mapping `f: (u_1, u_2) \to (wu_1 + bu_2, u_1)`,
    `f((u_1,u_2))` is the solution to `X^2 - aZ^2 \equiv 0 \pmod{b}`.
    In other words, finding the shortest vector in this norm will yield a solution with smaller `X^2 + |a|Z^2`.
    The algorithm starts from basis vectors `(0, 1)` and `(1, 0)`
    (corresponding to solutions `(b, 0)` and `(w, 1)`, respectively) and finds the shortest vector.
    The shortest vector does not necessarily correspond to the smallest solution,
    but since ``descent()`` only wants the smallest possible solution, it is sufficient.

    Parameters
    ==========

    w : int
        ``w`` s.t. `w^2 \equiv a \pmod{b}`
    a : int
        square-free nonzero integer
    b : int
        square-free nonzero integer

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import gaussian_reduce
    >>> from sympy.ntheory.residue_ntheory import sqrt_mod
    >>> a, b = 19, 101
    >>> gaussian_reduce(sqrt_mod(a, b), a, b) # 1**2 - 19*(-4)**2 = -303
    (1, -4)
    >>> a, b = 11, 14
    >>> x, z = gaussian_reduce(sqrt_mod(a, b), a, b)
    >>> (x**2 - a*z**2) % b == 0
    True

    It does not always return the smallest solution.

    >>> a, b = 6, 95
    >>> min_x, min_z = 1, 4
    >>> x, z = gaussian_reduce(sqrt_mod(a, b), a, b)
    >>> (x**2 - a*z**2) % b == 0 and (min_x**2 - a*min_z**2) % b == 0
    True
    >>> min_x**2 + abs(a)*min_z**2 < x**2 + abs(a)*z**2
    True

    References
    ==========

    .. [1] Gaussian lattice Reduction [online]. Available:
           https://web.archive.org/web/20201021115213/http://home.ie.cuhk.edu.hk/~wkshum/wordpress/?p=404
    .. [2] Cremona, J. E., Rusin, D. (2003). Efficient Solution of Rational Conics.
           Mathematics of Computation, 72(243), 1417-1441.
           https://doi.org/10.1090/S0025-5718-02-01480-1
    """
    ...

def holzer(x, y, z, a, b, c) -> tuple[int, ...]:
    r"""
    Simplify the solution `(x, y, z)` of the equation
    `ax^2 + by^2 = cz^2` with `a, b, c > 0` and `z^2 \geq \mid ab \mid` to
    a new reduced solution `(x', y', z')` such that `z'^2 \leq \mid ab \mid`.

    The algorithm is an interpretation of Mordell's reduction as described
    on page 8 of Cremona and Rusin's paper [1]_ and the work of Mordell in
    reference [2]_.

    References
    ==========

    .. [1] Cremona, J. E., Rusin, D. (2003). Efficient Solution of Rational Conics.
           Mathematics of Computation, 72(243), 1417-1441.
           https://doi.org/10.1090/S0025-5718-02-01480-1
    .. [2] Diophantine Equations, L. J. Mordell, page 48.

    """
    ...

def diop_general_pythagorean(eq, param=...) -> None:
    """
    Solves the general pythagorean equation,
    `a_{1}^2x_{1}^2 + a_{2}^2x_{2}^2 + . . . + a_{n}^2x_{n}^2 - a_{n + 1}^2x_{n + 1}^2 = 0`.

    Returns a tuple which contains a parametrized solution to the equation,
    sorted in the same order as the input variables.

    Usage
    =====

    ``diop_general_pythagorean(eq, param)``: where ``eq`` is a general
    pythagorean equation which is assumed to be zero and ``param`` is the base
    parameter used to construct other parameters by subscripting.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_general_pythagorean
    >>> from sympy.abc import a, b, c, d, e
    >>> diop_general_pythagorean(a**2 + b**2 + c**2 - d**2)
    (m1**2 + m2**2 - m3**2, 2*m1*m3, 2*m2*m3, m1**2 + m2**2 + m3**2)
    >>> diop_general_pythagorean(9*a**2 - 4*b**2 + 16*c**2 + 25*d**2 + e**2)
    (10*m1**2  + 10*m2**2  + 10*m3**2 - 10*m4**2, 15*m1**2  + 15*m2**2  + 15*m3**2  + 15*m4**2, 15*m1*m4, 12*m2*m4, 60*m3*m4)
    """
    ...

def diop_general_sum_of_squares(eq, limit=...) -> set[Any] | None:
    r"""
    Solves the equation `x_{1}^2 + x_{2}^2 + . . . + x_{n}^2 - k = 0`.

    Returns at most ``limit`` number of solutions.

    Usage
    =====

    ``general_sum_of_squares(eq, limit)`` : Here ``eq`` is an expression which
    is assumed to be zero. Also, ``eq`` should be in the form,
    `x_{1}^2 + x_{2}^2 + . . . + x_{n}^2 - k = 0`.

    Details
    =======

    When `n = 3` if `k = 4^a(8m + 7)` for some `a, m \in Z` then there will be
    no solutions. Refer to [1]_ for more details.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_general_sum_of_squares
    >>> from sympy.abc import a, b, c, d, e
    >>> diop_general_sum_of_squares(a**2 + b**2 + c**2 + d**2 + e**2 - 2345)
    {(15, 22, 22, 24, 24)}

    Reference
    =========

    .. [1] Representing an integer as a sum of three squares, [online],
        Available:
        https://www.proofwiki.org/wiki/Integer_as_Sum_of_Three_Squares
    """
    ...

def diop_general_sum_of_even_powers(eq, limit=...) -> set[Any] | None:
    """
    Solves the equation `x_{1}^e + x_{2}^e + . . . + x_{n}^e - k = 0`
    where `e` is an even, integer power.

    Returns at most ``limit`` number of solutions.

    Usage
    =====

    ``general_sum_of_even_powers(eq, limit)`` : Here ``eq`` is an expression which
    is assumed to be zero. Also, ``eq`` should be in the form,
    `x_{1}^e + x_{2}^e + . . . + x_{n}^e - k = 0`.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import diop_general_sum_of_even_powers
    >>> from sympy.abc import a, b
    >>> diop_general_sum_of_even_powers(a**4 + b**4 - (2**4 + 3**4))
    {(2, 3)}

    See Also
    ========

    power_representation
    """
    ...

def partition(n, k=..., zeros=...) -> Generator[tuple[Any, ...] | Any, Any, None]:
    """
    Returns a generator that can be used to generate partitions of an integer
    `n`.

    Explanation
    ===========

    A partition of `n` is a set of positive integers which add up to `n`. For
    example, partitions of 3 are 3, 1 + 2, 1 + 1 + 1. A partition is returned
    as a tuple. If ``k`` equals None, then all possible partitions are returned
    irrespective of their size, otherwise only the partitions of size ``k`` are
    returned. If the ``zero`` parameter is set to True then a suitable
    number of zeros are added at the end of every partition of size less than
    ``k``.

    ``zero`` parameter is considered only if ``k`` is not None. When the
    partitions are over, the last `next()` call throws the ``StopIteration``
    exception, so this function should always be used inside a try - except
    block.

    Details
    =======

    ``partition(n, k)``: Here ``n`` is a positive integer and ``k`` is the size
    of the partition which is also positive integer.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import partition
    >>> f = partition(5)
    >>> next(f)
    (1, 1, 1, 1, 1)
    >>> next(f)
    (1, 1, 1, 2)
    >>> g = partition(5, 3)
    >>> next(g)
    (1, 1, 3)
    >>> next(g)
    (1, 2, 2)
    >>> g = partition(5, 3, zeros=True)
    >>> next(g)
    (0, 0, 5)

    """
    ...

def prime_as_sum_of_two_squares(p) -> tuple[int, int] | None:
    """
    Represent a prime `p` as a unique sum of two squares; this can
    only be done if the prime is congruent to 1 mod 4.

    Parameters
    ==========

    p : Integer
        A prime that is congruent to 1 mod 4

    Returns
    =======

    (int, int) | None : Pair of positive integers ``(x, y)`` satisfying ``x**2 + y**2 = p``.
                        None if ``p`` is not congruent to 1 mod 4.

    Raises
    ======

    ValueError
        If ``p`` is not prime number

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import prime_as_sum_of_two_squares
    >>> prime_as_sum_of_two_squares(7)  # can't be done
    >>> prime_as_sum_of_two_squares(5)
    (1, 2)

    Reference
    =========

    .. [1] Representing a number as a sum of four squares, [online],
           Available: https://schorn.ch/lagrange.html

    See Also
    ========

    sum_of_squares

    """
    ...

def sum_of_three_squares(n) -> tuple[Literal[0], Literal[0], Literal[0]] | tuple[Any, ...] | tuple[Literal[0], Literal[0], Any] | None:
    r"""
    Returns a 3-tuple $(a, b, c)$ such that $a^2 + b^2 + c^2 = n$ and
    $a, b, c \geq 0$.

    Returns None if $n = 4^a(8m + 7)$ for some `a, m \in \mathbb{Z}`. See
    [1]_ for more details.

    Parameters
    ==========

    n : Integer
        non-negative integer

    Returns
    =======

    (int, int, int) | None : 3-tuple non-negative integers ``(a, b, c)`` satisfying ``a**2 + b**2 + c**2 = n``.
                             a,b,c are sorted in ascending order. ``None`` if no such ``(a,b,c)``.

    Raises
    ======

    ValueError
        If ``n`` is a negative integer

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import sum_of_three_squares
    >>> sum_of_three_squares(44542)
    (18, 37, 207)

    References
    ==========

    .. [1] Representing a number as a sum of three squares, [online],
        Available: https://schorn.ch/lagrange.html

    See Also
    ========

    power_representation :
        ``sum_of_three_squares(n)`` is one of the solutions output by ``power_representation(n, 2, 3, zeros=True)``

    """
    ...

def sum_of_four_squares(n) -> tuple[Literal[0], Literal[0], Literal[0], Literal[0]] | tuple[Any, ...]:
    r"""
    Returns a 4-tuple `(a, b, c, d)` such that `a^2 + b^2 + c^2 + d^2 = n`.
    Here `a, b, c, d \geq 0`.

    Parameters
    ==========

    n : Integer
        non-negative integer

    Returns
    =======

    (int, int, int, int) : 4-tuple non-negative integers ``(a, b, c, d)`` satisfying ``a**2 + b**2 + c**2 + d**2 = n``.
                           a,b,c,d are sorted in ascending order.

    Raises
    ======

    ValueError
        If ``n`` is a negative integer

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import sum_of_four_squares
    >>> sum_of_four_squares(3456)
    (8, 8, 32, 48)
    >>> sum_of_four_squares(1294585930293)
    (0, 1234, 2161, 1137796)

    References
    ==========

    .. [1] Representing a number as a sum of four squares, [online],
        Available: https://schorn.ch/lagrange.html

    See Also
    ========

    power_representation :
        ``sum_of_four_squares(n)`` is one of the solutions output by ``power_representation(n, 2, 4, zeros=True)``

    """
    ...

def power_representation(n, p, k, zeros=...):
    r"""
    Returns a generator for finding k-tuples of integers,
    `(n_{1}, n_{2}, . . . n_{k})`, such that
    `n = n_{1}^p + n_{2}^p + . . . n_{k}^p`.

    Usage
    =====

    ``power_representation(n, p, k, zeros)``: Represent non-negative number
    ``n`` as a sum of ``k`` ``p``\ th powers. If ``zeros`` is true, then the
    solutions is allowed to contain zeros.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import power_representation

    Represent 1729 as a sum of two cubes:

    >>> f = power_representation(1729, 3, 2)
    >>> next(f)
    (9, 10)
    >>> next(f)
    (1, 12)

    If the flag `zeros` is True, the solution may contain tuples with
    zeros; any such solutions will be generated after the solutions
    without zeros:

    >>> list(power_representation(125, 2, 3, zeros=True))
    [(5, 6, 8), (3, 4, 10), (0, 5, 10), (0, 2, 11)]

    For even `p` the `permute_sign` function can be used to get all
    signed values:

    >>> from sympy.utilities.iterables import permute_signs
    >>> list(permute_signs((1, 12)))
    [(1, 12), (-1, 12), (1, -12), (-1, -12)]

    All possible signed permutations can also be obtained:

    >>> from sympy.utilities.iterables import signed_permutations
    >>> list(signed_permutations((1, 12)))
    [(1, 12), (-1, 12), (1, -12), (-1, -12), (12, 1), (-12, 1), (12, -1), (-12, -1)]
    """
    ...

sum_of_powers = ...
def pow_rep_recursive(n_i, k, n_remaining, terms, p) -> Generator[tuple[Any, ...] | Any, Any, None]:
    ...

def sum_of_squares(n, k, zeros=...) -> Generator[Any, Any, None]:
    """Return a generator that yields the k-tuples of nonnegative
    values, the squares of which sum to n. If zeros is False (default)
    then the solution will not contain zeros. The nonnegative
    elements of a tuple are sorted.

    * If k == 1 and n is square, (n,) is returned.

    * If k == 2 then n can only be written as a sum of squares if
      every prime in the factorization of n that has the form
      4*k + 3 has an even multiplicity. If n is prime then
      it can only be written as a sum of two squares if it is
      in the form 4*k + 1.

    * if k == 3 then n can be written as a sum of squares if it does
      not have the form 4**m*(8*k + 7).

    * all integers can be written as the sum of 4 squares.

    * if k > 4 then n can be partitioned and each partition can
      be written as a sum of 4 squares; if n is not evenly divisible
      by 4 then n can be written as a sum of squares only if the
      an additional partition can be written as sum of squares.
      For example, if k = 6 then n is partitioned into two parts,
      the first being written as a sum of 4 squares and the second
      being written as a sum of 2 squares -- which can only be
      done if the condition above for k = 2 can be met, so this will
      automatically reject certain partitions of n.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import sum_of_squares
    >>> list(sum_of_squares(25, 2))
    [(3, 4)]
    >>> list(sum_of_squares(25, 2, True))
    [(3, 4), (0, 5)]
    >>> list(sum_of_squares(25, 4))
    [(1, 2, 2, 4)]

    See Also
    ========

    sympy.utilities.iterables.signed_permutations
    """
    ...

