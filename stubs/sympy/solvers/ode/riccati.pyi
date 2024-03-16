r"""
This module contains :py:meth:`~sympy.solvers.ode.riccati.solve_riccati`,
a function which gives all rational particular solutions to first order
Riccati ODEs. A general first order Riccati ODE is given by -

.. math:: y' = b_0(x) + b_1(x)w + b_2(x)w^2

where `b_0, b_1` and `b_2` can be arbitrary rational functions of `x`
with `b_2 \ne 0`. When `b_2 = 0`, the equation is not a Riccati ODE
anymore and becomes a Linear ODE. Similarly, when `b_0 = 0`, the equation
is a Bernoulli ODE. The algorithm presented below can find rational
solution(s) to all ODEs with `b_2 \ne 0` that have a rational solution,
or prove that no rational solution exists for the equation.

Background
==========

A Riccati equation can be transformed to its normal form

.. math:: y' + y^2 = a(x)

using the transformation

.. math:: y = -b_2(x) - \frac{b'_2(x)}{2 b_2(x)} - \frac{b_1(x)}{2}

where `a(x)` is given by

.. math:: a(x) = \frac{1}{4}\left(\frac{b_2'}{b_2} + b_1\right)^2 - \frac{1}{2}\left(\frac{b_2'}{b_2} + b_1\right)' - b_0 b_2

Thus, we can develop an algorithm to solve for the Riccati equation
in its normal form, which would in turn give us the solution for
the original Riccati equation.

Algorithm
=========

The algorithm implemented here is presented in the Ph.D thesis
"Rational and Algebraic Solutions of First-Order Algebraic ODEs"
by N. Thieu Vo. The entire thesis can be found here -
https://www3.risc.jku.at/publications/download/risc_5387/PhDThesisThieu.pdf

We have only implemented the Rational Riccati solver (Algorithm 11,
Pg 78-82 in Thesis). Before we proceed towards the implementation
of the algorithm, a few definitions to understand are -

1. Valuation of a Rational Function at `\infty`:
    The valuation of a rational function `p(x)` at `\infty` is equal
    to the difference between the degree of the denominator and the
    numerator of `p(x)`.

    NOTE: A general definition of valuation of a rational function
    at any value of `x` can be found in Pg 63 of the thesis, but
    is not of any interest for this algorithm.

2. Zeros and Poles of a Rational Function:
    Let `a(x) = \frac{S(x)}{T(x)}, T \ne 0` be a rational function
    of `x`. Then -

    a. The Zeros of `a(x)` are the roots of `S(x)`.
    b. The Poles of `a(x)` are the roots of `T(x)`. However, `\infty`
    can also be a pole of a(x). We say that `a(x)` has a pole at
    `\infty` if `a(\frac{1}{x})` has a pole at 0.

Every pole is associated with an order that is equal to the multiplicity
of its appearance as a root of `T(x)`. A pole is called a simple pole if
it has an order 1. Similarly, a pole is called a multiple pole if it has
an order `\ge` 2.

Necessary Conditions
====================

For a Riccati equation in its normal form,

.. math:: y' + y^2 = a(x)

we can define

a. A pole is called a movable pole if it is a pole of `y(x)` and is not
a pole of `a(x)`.
b. Similarly, a pole is called a non-movable pole if it is a pole of both
`y(x)` and `a(x)`.

Then, the algorithm states that a rational solution exists only if -

a. Every pole of `a(x)` must be either a simple pole or a multiple pole
of even order.
b. The valuation of `a(x)` at `\infty` must be even or be `\ge` 2.

This algorithm finds all possible rational solutions for the Riccati ODE.
If no rational solutions are found, it means that no rational solutions
exist.

The algorithm works for Riccati ODEs where the coefficients are rational
functions in the independent variable `x` with rational number coefficients
i.e. in `Q(x)`. The coefficients in the rational function cannot be floats,
irrational numbers, symbols or any other kind of expression. The reasons
for this are -

1. When using symbols, different symbols could take the same value and this
would affect the multiplicity of poles if symbols are present here.

2. An integer degree bound is required to calculate a polynomial solution
to an auxiliary differential equation, which in turn gives the particular
solution for the original ODE. If symbols/floats/irrational numbers are
present, we cannot determine if the expression for the degree bound is an
integer or not.

Solution
========

With these definitions, we can state a general form for the solution of
the equation. `y(x)` must have the form -

.. math:: y(x) = \sum_{i=1}^{n} \sum_{j=1}^{r_i} \frac{c_{ij}}{(x - x_i)^j} + \sum_{i=1}^{m} \frac{1}{x - \chi_i} + \sum_{i=0}^{N} d_i x^i

where `x_1, x_2, \dots, x_n` are non-movable poles of `a(x)`,
`\chi_1, \chi_2, \dots, \chi_m` are movable poles of `a(x)`, and the values
of `N, n, r_1, r_2, \dots, r_n` can be determined from `a(x)`. The
coefficient vectors `(d_0, d_1, \dots, d_N)` and `(c_{i1}, c_{i2}, \dots, c_{i r_i})`
can be determined from `a(x)`. We will have 2 choices each of these vectors
and part of the procedure is figuring out which of the 2 should be used
to get the solution correctly.

Implementation
==============

In this implementation, we use ``Poly`` to represent a rational function
rather than using ``Expr`` since ``Poly`` is much faster. Since we cannot
represent rational functions directly using ``Poly``, we instead represent
a rational function with 2 ``Poly`` objects - one for its numerator and
the other for its denominator.

The code is written to match the steps given in the thesis (Pg 82)

Step 0 : Match the equation -
Find `b_0, b_1` and `b_2`. If `b_2 = 0` or no such functions exist, raise
an error

Step 1 : Transform the equation to its normal form as explained in the
theory section.

Step 2 : Initialize an empty set of solutions, ``sol``.

Step 3 : If `a(x) = 0`, append `\frac{1}/{(x - C1)}` to ``sol``.

Step 4 : If `a(x)` is a rational non-zero number, append `\pm \sqrt{a}`
to ``sol``.

Step 5 : Find the poles and their multiplicities of `a(x)`. Let
the number of poles be `n`. Also find the valuation of `a(x)` at
`\infty` using ``val_at_inf``.

NOTE: Although the algorithm considers `\infty` as a pole, it is
not mentioned if it a part of the set of finite poles. `\infty`
is NOT a part of the set of finite poles. If a pole exists at
`\infty`, we use its multiplicity to find the laurent series of
`a(x)` about `\infty`.

Step 6 : Find `n` c-vectors (one for each pole) and 1 d-vector using
``construct_c`` and ``construct_d``. Now, determine all the ``2**(n + 1)``
combinations of choosing between 2 choices for each of the `n` c-vectors
and 1 d-vector.

NOTE: The equation for `d_{-1}` in Case 4 (Pg 80) has a printinig
mistake. The term `- d_N` must be replaced with `-N d_N`. The same
has been explained in the code as well.

For each of these above combinations, do

Step 8 : Compute `m` in ``compute_m_ybar``. `m` is the degree bound of
the polynomial solution we must find for the auxiliary equation.

Step 9 : In ``compute_m_ybar``, compute ybar as well where ``ybar`` is
one part of y(x) -

.. math:: \overline{y}(x) = \sum_{i=1}^{n} \sum_{j=1}^{r_i} \frac{c_{ij}}{(x - x_i)^j} + \sum_{i=0}^{N} d_i x^i

Step 10 : If `m` is a non-negative integer -

Step 11: Find a polynomial solution of degree `m` for the auxiliary equation.

There are 2 cases possible -

    a. `m` is a non-negative integer: We can solve for the coefficients
    in `p(x)` using Undetermined Coefficients.

    b. `m` is not a non-negative integer: In this case, we cannot find
    a polynomial solution to the auxiliary equation, and hence, we ignore
    this value of `m`.

Step 12 : For each `p(x)` that exists, append `ybar + \frac{p'(x)}{p(x)}`
to ``sol``.

Step 13 : For each solution in ``sol``, apply an inverse transformation,
so that the solutions of the original equation are found using the
solutions of the equation in its normal form.
"""
def riccati_normal(w, x, b1, b2):
    """
    Given a solution `w(x)` to the equation

    .. math:: w'(x) = b_0(x) + b_1(x)*w(x) + b_2(x)*w(x)^2

    and rational function coefficients `b_1(x)` and
    `b_2(x)`, this function transforms the solution to
    give a solution `y(x)` for its corresponding normal
    Riccati ODE

    .. math:: y'(x) + y(x)^2 = a(x)

    using the transformation

    .. math:: y(x) = -b_2(x)*w(x) - b'_2(x)/(2*b_2(x)) - b_1(x)/2
    """
    ...

def riccati_inverse_normal(y, x, b1, b2, bp=...):
    """
    Inverse transforming the solution to the normal
    Riccati ODE to get the solution to the Riccati ODE.
    """
    ...

def riccati_reduced(eq, f, x) -> Literal[False]:
    """
    Convert a Riccati ODE into its corresponding
    normal Riccati ODE.
    """
    ...

def linsolve_dict(eq, syms) -> dict[Any, Any]:
    """
    Get the output of linsolve as a dict
    """
    ...

def match_riccati(eq, f, x) -> tuple[Literal[False], list[Any]] | tuple[Literal[True], list[Any]]:
    """
    A function that matches and returns the coefficients
    if an equation is a Riccati ODE

    Parameters
    ==========

    eq: Equation to be matched
    f: Dependent variable
    x: Independent variable

    Returns
    =======

    match: True if equation is a Riccati ODE, False otherwise
    funcs: [b0, b1, b2] if match is True, [] otherwise. Here,
    b0, b1 and b2 are rational functions which match the equation.
    """
    ...

def val_at_inf(num, den, x):
    ...

def check_necessary_conds(val_inf, muls) -> bool:
    """
    The necessary conditions for a rational solution
    to exist are as follows -

    i) Every pole of a(x) must be either a simple pole
    or a multiple pole of even order.

    ii) The valuation of a(x) at infinity must be even
    or be greater than or equal to 2.

    Here, a simple pole is a pole with multiplicity 1
    and a multiple pole is a pole with multiplicity
    greater than 1.
    """
    ...

def inverse_transform_poly(num, den, x):
    """
    A function to make the substitution
    x -> 1/x in a rational function that
    is represented using Poly objects for
    numerator and denominator.
    """
    ...

def limit_at_inf(num, den, x) -> Literal[0]:
    """
    Find the limit of a rational function
    at oo
    """
    ...

def construct_c_case_1(num, den, x, pole) -> list[list[Any]]:
    ...

def construct_c_case_2(num, den, x, pole, mul) -> list[list[int]] | list[int]:
    ...

def construct_c_case_3() -> list[list[int]]:
    ...

def construct_c(num, den, x, poles, muls) -> list[Any]:
    """
    Helper function to calculate the coefficients
    in the c-vector for each pole.
    """
    ...

def construct_d_case_4(ser, N) -> list[list[int]] | list[int]:
    ...

def construct_d_case_5(ser) -> list[list[int]] | list[int]:
    ...

def construct_d_case_6(num, den, x) -> list[list[Any]]:
    ...

def construct_d(num, den, x, val_inf) -> list[list[int]] | list[int] | list[list[Any]]:
    """
    Helper function to calculate the coefficients
    in the d-vector based on the valuation of the
    function at oo.
    """
    ...

def rational_laurent_series(num, den, x, r, m, n) -> dict[Any, Any]:
    r"""
    The function computes the Laurent series coefficients
    of a rational function.

    Parameters
    ==========

    num: A Poly object that is the numerator of `f(x)`.
    den: A Poly object that is the denominator of `f(x)`.
    x: The variable of expansion of the series.
    r: The point of expansion of the series.
    m: Multiplicity of r if r is a pole of `f(x)`. Should
    be zero otherwise.
    n: Order of the term upto which the series is expanded.

    Returns
    =======

    series: A dictionary that has power of the term as key
    and coefficient of that term as value.

    Below is a basic outline of how the Laurent series of a
    rational function `f(x)` about `x_0` is being calculated -

    1. Substitute `x + x_0` in place of `x`. If `x_0`
    is a pole of `f(x)`, multiply the expression by `x^m`
    where `m` is the multiplicity of `x_0`. Denote the
    the resulting expression as g(x). We do this substitution
    so that we can now find the Laurent series of g(x) about
    `x = 0`.

    2. We can then assume that the Laurent series of `g(x)`
    takes the following form -

    .. math:: g(x) = \frac{num(x)}{den(x)} = \sum_{m = 0}^{\infty} a_m x^m

    where `a_m` denotes the Laurent series coefficients.

    3. Multiply the denominator to the RHS of the equation
    and form a recurrence relation for the coefficients `a_m`.
    """
    ...

def compute_m_ybar(x, poles, choice, N) -> tuple[Any, Any]:
    """
    Helper function to calculate -

    1. m - The degree bound for the polynomial
    solution that must be found for the auxiliary
    differential equation.

    2. ybar - Part of the solution which can be
    computed using the poles, c and d vectors.
    """
    ...

def solve_aux_eq(numa, dena, numy, deny, x, m) -> tuple[Any, dict[Any, Any], Literal[True]] | tuple[Any, Any, Any]:
    """
    Helper function to find a polynomial solution
    of degree m for the auxiliary differential
    equation.
    """
    ...

def remove_redundant_sols(sol1, sol2, x) -> None:
    """
    Helper function to remove redundant
    solutions to the differential equation.
    """
    ...

def get_gen_sol_from_part_sol(part_sols, a, x) -> list[Any]:
    """"
    Helper function which computes the general
    solution for a Riccati ODE from its particular
    solutions.

    There are 3 cases to find the general solution
    from the particular solutions for a Riccati ODE
    depending on the number of particular solution(s)
    we have - 1, 2 or 3.

    For more information, see Section 6 of
    "Methods of Solution of the Riccati Differential Equation"
    by D. R. Haaheim and F. M. Stein
    """
    ...

def solve_riccati(fx, x, b0, b1, b2, gensol=...) -> list[Eq | Any | Relational | Ne]:
    """
    The main function that gives particular/general
    solutions to Riccati ODEs that have atleast 1
    rational particular solution.
    """
    ...

