from typing import Any, Generator, Literal, NoReturn, Tuple
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.multidimensional import vectorize
from sympy.core.relational import Eq, Equality, Ne, Relational
from sympy.core.symbol import Symbol

r"""
This module contains :py:meth:`~sympy.solvers.ode.dsolve` and different helper
functions that it uses.

:py:meth:`~sympy.solvers.ode.dsolve` solves ordinary differential equations.
See the docstring on the various functions for their uses.  Note that partial
differential equations support is in ``pde.py``.  Note that hint functions
have docstrings describing their various methods, but they are intended for
internal use.  Use ``dsolve(ode, func, hint=hint)`` to solve an ODE using a
specific hint.  See also the docstring on
:py:meth:`~sympy.solvers.ode.dsolve`.

**Functions in this module**

    These are the user functions in this module:

    - :py:meth:`~sympy.solvers.ode.dsolve` - Solves ODEs.
    - :py:meth:`~sympy.solvers.ode.classify_ode` - Classifies ODEs into
      possible hints for :py:meth:`~sympy.solvers.ode.dsolve`.
    - :py:meth:`~sympy.solvers.ode.checkodesol` - Checks if an equation is the
      solution to an ODE.
    - :py:meth:`~sympy.solvers.ode.homogeneous_order` - Returns the
      homogeneous order of an expression.
    - :py:meth:`~sympy.solvers.ode.infinitesimals` - Returns the infinitesimals
      of the Lie group of point transformations of an ODE, such that it is
      invariant.
    - :py:meth:`~sympy.solvers.ode.checkinfsol` - Checks if the given infinitesimals
      are the actual infinitesimals of a first order ODE.

    These are the non-solver helper functions that are for internal use.  The
    user should use the various options to
    :py:meth:`~sympy.solvers.ode.dsolve` to obtain the functionality provided
    by these functions:

    - :py:meth:`~sympy.solvers.ode.ode.odesimp` - Does all forms of ODE
      simplification.
    - :py:meth:`~sympy.solvers.ode.ode.ode_sol_simplicity` - A key function for
      comparing solutions by simplicity.
    - :py:meth:`~sympy.solvers.ode.constantsimp` - Simplifies arbitrary
      constants.
    - :py:meth:`~sympy.solvers.ode.ode.constant_renumber` - Renumber arbitrary
      constants.
    - :py:meth:`~sympy.solvers.ode.ode._handle_Integral` - Evaluate unevaluated
      Integrals.

    See also the docstrings of these functions.

**Currently implemented solver methods**

The following methods are implemented for solving ordinary differential
equations.  See the docstrings of the various hint functions for more
information on each (run ``help(ode)``):

  - 1st order separable differential equations.
  - 1st order differential equations whose coefficients or `dx` and `dy` are
    functions homogeneous of the same order.
  - 1st order exact differential equations.
  - 1st order linear differential equations.
  - 1st order Bernoulli differential equations.
  - Power series solutions for first order differential equations.
  - Lie Group method of solving first order differential equations.
  - 2nd order Liouville differential equations.
  - Power series solutions for second order differential equations
    at ordinary and regular singular points.
  - `n`\th order differential equation that can be solved with algebraic
    rearrangement and integration.
  - `n`\th order linear homogeneous differential equation with constant
    coefficients.
  - `n`\th order linear inhomogeneous differential equation with constant
    coefficients using the method of undetermined coefficients.
  - `n`\th order linear inhomogeneous differential equation with constant
    coefficients using the method of variation of parameters.

**Philosophy behind this module**

This module is designed to make it easy to add new ODE solving methods without
having to mess with the solving code for other methods.  The idea is that
there is a :py:meth:`~sympy.solvers.ode.classify_ode` function, which takes in
an ODE and tells you what hints, if any, will solve the ODE.  It does this
without attempting to solve the ODE, so it is fast.  Each solving method is a
hint, and it has its own function, named ``ode_<hint>``.  That function takes
in the ODE and any match expression gathered by
:py:meth:`~sympy.solvers.ode.classify_ode` and returns a solved result.  If
this result has any integrals in it, the hint function will return an
unevaluated :py:class:`~sympy.integrals.integrals.Integral` class.
:py:meth:`~sympy.solvers.ode.dsolve`, which is the user wrapper function
around all of this, will then call :py:meth:`~sympy.solvers.ode.ode.odesimp` on
the result, which, among other things, will attempt to solve the equation for
the dependent variable (the function we are solving for), simplify the
arbitrary constants in the expression, and evaluate any integrals, if the hint
allows it.

**How to add new solution methods**

If you have an ODE that you want :py:meth:`~sympy.solvers.ode.dsolve` to be
able to solve, try to avoid adding special case code here.  Instead, try
finding a general method that will solve your ODE, as well as others.  This
way, the :py:mod:`~sympy.solvers.ode` module will become more robust, and
unhindered by special case hacks.  WolphramAlpha and Maple's
DETools[odeadvisor] function are two resources you can use to classify a
specific ODE.  It is also better for a method to work with an `n`\th order ODE
instead of only with specific orders, if possible.

To add a new method, there are a few things that you need to do.  First, you
need a hint name for your method.  Try to name your hint so that it is
unambiguous with all other methods, including ones that may not be implemented
yet.  If your method uses integrals, also include a ``hint_Integral`` hint.
If there is more than one way to solve ODEs with your method, include a hint
for each one, as well as a ``<hint>_best`` hint.  Your ``ode_<hint>_best()``
function should choose the best using min with ``ode_sol_simplicity`` as the
key argument.  See
:obj:`~sympy.solvers.ode.single.HomogeneousCoeffBest`, for example.
The function that uses your method will be called ``ode_<hint>()``, so the
hint must only use characters that are allowed in a Python function name
(alphanumeric characters and the underscore '``_``' character).  Include a
function for every hint, except for ``_Integral`` hints
(:py:meth:`~sympy.solvers.ode.dsolve` takes care of those automatically).
Hint names should be all lowercase, unless a word is commonly capitalized
(such as Integral or Bernoulli).  If you have a hint that you do not want to
run with ``all_Integral`` that does not have an ``_Integral`` counterpart (such
as a best hint that would defeat the purpose of ``all_Integral``), you will
need to remove it manually in the :py:meth:`~sympy.solvers.ode.dsolve` code.
See also the :py:meth:`~sympy.solvers.ode.classify_ode` docstring for
guidelines on writing a hint name.

Determine *in general* how the solutions returned by your method compare with
other methods that can potentially solve the same ODEs.  Then, put your hints
in the :py:data:`~sympy.solvers.ode.allhints` tuple in the order that they
should be called.  The ordering of this tuple determines which hints are
default.  Note that exceptions are ok, because it is easy for the user to
choose individual hints with :py:meth:`~sympy.solvers.ode.dsolve`.  In
general, ``_Integral`` variants should go at the end of the list, and
``_best`` variants should go before the various hints they apply to.  For
example, the ``undetermined_coefficients`` hint comes before the
``variation_of_parameters`` hint because, even though variation of parameters
is more general than undetermined coefficients, undetermined coefficients
generally returns cleaner results for the ODEs that it can solve than
variation of parameters does, and it does not require integration, so it is
much faster.

Next, you need to have a match expression or a function that matches the type
of the ODE, which you should put in :py:meth:`~sympy.solvers.ode.classify_ode`
(if the match function is more than just a few lines.  It should match the
ODE without solving for it as much as possible, so that
:py:meth:`~sympy.solvers.ode.classify_ode` remains fast and is not hindered by
bugs in solving code.  Be sure to consider corner cases.  For example, if your
solution method involves dividing by something, make sure you exclude the case
where that division will be 0.

In most cases, the matching of the ODE will also give you the various parts
that you need to solve it.  You should put that in a dictionary (``.match()``
will do this for you), and add that as ``matching_hints['hint'] = matchdict``
in the relevant part of :py:meth:`~sympy.solvers.ode.classify_ode`.
:py:meth:`~sympy.solvers.ode.classify_ode` will then send this to
:py:meth:`~sympy.solvers.ode.dsolve`, which will send it to your function as
the ``match`` argument.  Your function should be named ``ode_<hint>(eq, func,
order, match)`.  If you need to send more information, put it in the ``match``
dictionary.  For example, if you had to substitute in a dummy variable in
:py:meth:`~sympy.solvers.ode.classify_ode` to match the ODE, you will need to
pass it to your function using the `match` dict to access it.  You can access
the independent variable using ``func.args[0]``, and the dependent variable
(the function you are trying to solve for) as ``func.func``.  If, while trying
to solve the ODE, you find that you cannot, raise ``NotImplementedError``.
:py:meth:`~sympy.solvers.ode.dsolve` will catch this error with the ``all``
meta-hint, rather than causing the whole routine to fail.

Add a docstring to your function that describes the method employed.  Like
with anything else in SymPy, you will need to add a doctest to the docstring,
in addition to real tests in ``test_ode.py``.  Try to maintain consistency
with the other hint functions' docstrings.  Add your method to the list at the
top of this docstring.  Also, add your method to ``ode.rst`` in the
``docs/src`` directory, so that the Sphinx docs will pull its docstring into
the main SymPy documentation.  Be sure to make the Sphinx documentation by
running ``make html`` from within the doc directory to verify that the
docstring formats correctly.

If your solution method involves integrating, use :py:obj:`~.Integral` instead of
:py:meth:`~sympy.core.expr.Expr.integrate`.  This allows the user to bypass
hard/slow integration by using the ``_Integral`` variant of your hint.  In
most cases, calling :py:meth:`sympy.core.basic.Basic.doit` will integrate your
solution.  If this is not the case, you will need to write special code in
:py:meth:`~sympy.solvers.ode.ode._handle_Integral`.  Arbitrary constants should be
symbols named ``C1``, ``C2``, and so on.  All solution methods should return
an equality instance.  If you need an arbitrary number of arbitrary constants,
you can use ``constants = numbered_symbols(prefix='C', cls=Symbol, start=1)``.
If it is possible to solve for the dependent function in a general way, do so.
Otherwise, do as best as you can, but do not call solve in your
``ode_<hint>()`` function.  :py:meth:`~sympy.solvers.ode.ode.odesimp` will attempt
to solve the solution for you, so you do not need to do that.  Lastly, if your
ODE has a common simplification that can be applied to your solutions, you can
add a special case in :py:meth:`~sympy.solvers.ode.ode.odesimp` for it.  For
example, solutions returned from the ``1st_homogeneous_coeff`` hints often
have many :obj:`~sympy.functions.elementary.exponential.log` terms, so
:py:meth:`~sympy.solvers.ode.ode.odesimp` calls
:py:meth:`~sympy.simplify.simplify.logcombine` on them (it also helps to write
the arbitrary constant as ``log(C1)`` instead of ``C1`` in this case).  Also
consider common ways that you can rearrange your solution to have
:py:meth:`~sympy.solvers.ode.constantsimp` take better advantage of it.  It is
better to put simplification in :py:meth:`~sympy.solvers.ode.ode.odesimp` than in
your method, because it can then be turned off with the simplify flag in
:py:meth:`~sympy.solvers.ode.dsolve`.  If you have any extraneous
simplification in your function, be sure to only run it using ``if
match.get('simplify', True):``, especially if it can be slow or if it can
reduce the domain of the solution.

Finally, as with every contribution to SymPy, your method will need to be
tested.  Add a test for each method in ``test_ode.py``.  Follow the
conventions there, i.e., test the solver using ``dsolve(eq, f(x),
hint=your_hint)``, and also test the solution using
:py:meth:`~sympy.solvers.ode.checkodesol` (you can put these in a separate
tests and skip/XFAIL if it runs too slow/does not work).  Be sure to call your
hint specifically in :py:meth:`~sympy.solvers.ode.dsolve`, that way the test
will not be broken simply by the introduction of another matching hint.  If your
method works for higher order (>1) ODEs, you will need to run ``sol =
constant_renumber(sol, 'C', 1, order)`` for each solution, where ``order`` is
the order of the ODE.  This is because ``constant_renumber`` renumbers the
arbitrary constants by printing order, which is platform dependent.  Try to
test every corner case of your solver, including a range of orders if it is a
`n`\th order solver, but if your solver is slow, such as if it involves hard
integration, try to keep the test run time down.

Feel free to refactor existing hints to avoid duplicating code or creating
inconsistencies.  If you can show that your method exactly duplicates an
existing method, including in the simplicity and speed of obtaining the
solutions, then you can remove the old, less general method.  The existing
code is tested extensively in ``test_ode.py``, so if anything is broken, one
of those tests will surely fail.

"""
allhints = ...
def get_numbered_constants(eq, num=..., start=..., prefix=...) -> Symbol | tuple[Symbol, ...]:
    """
    Returns a list of constants that do not occur
    in eq already.
    """
    ...

def iter_numbered_constants(eq, start=..., prefix=...) -> Generator[Symbol, Any, NoReturn]:
    """
    Returns an iterator of constants that do not occur
    in eq already.
    """
    ...

def dsolve(eq, func=..., hint=..., simplify=..., ics=..., xi=..., eta=..., x0=..., n=..., **kwargs) -> list[Any] | Any | dict[Any, Any] | Equality | Basic | list[list[Any] | Any] | list[Equality]:
    r"""
    Solves any (supported) kind of ordinary differential equation and
    system of ordinary differential equations.

    For single ordinary differential equation
    =========================================

    It is classified under this when number of equation in ``eq`` is one.
    **Usage**

        ``dsolve(eq, f(x), hint)`` -> Solve ordinary differential equation
        ``eq`` for function ``f(x)``, using method ``hint``.

    **Details**

        ``eq`` can be any supported ordinary differential equation (see the
            :py:mod:`~sympy.solvers.ode` docstring for supported methods).
            This can either be an :py:class:`~sympy.core.relational.Equality`,
            or an expression, which is assumed to be equal to ``0``.

        ``f(x)`` is a function of one variable whose derivatives in that
            variable make up the ordinary differential equation ``eq``.  In
            many cases it is not necessary to provide this; it will be
            autodetected (and an error raised if it could not be detected).

        ``hint`` is the solving method that you want dsolve to use.  Use
            ``classify_ode(eq, f(x))`` to get all of the possible hints for an
            ODE.  The default hint, ``default``, will use whatever hint is
            returned first by :py:meth:`~sympy.solvers.ode.classify_ode`.  See
            Hints below for more options that you can use for hint.

        ``simplify`` enables simplification by
            :py:meth:`~sympy.solvers.ode.ode.odesimp`.  See its docstring for more
            information.  Turn this off, for example, to disable solving of
            solutions for ``func`` or simplification of arbitrary constants.
            It will still integrate with this hint. Note that the solution may
            contain more arbitrary constants than the order of the ODE with
            this option enabled.

        ``xi`` and ``eta`` are the infinitesimal functions of an ordinary
            differential equation. They are the infinitesimals of the Lie group
            of point transformations for which the differential equation is
            invariant. The user can specify values for the infinitesimals. If
            nothing is specified, ``xi`` and ``eta`` are calculated using
            :py:meth:`~sympy.solvers.ode.infinitesimals` with the help of various
            heuristics.

        ``ics`` is the set of initial/boundary conditions for the differential equation.
          It should be given in the form of ``{f(x0): x1, f(x).diff(x).subs(x, x2):
          x3}`` and so on.  For power series solutions, if no initial
          conditions are specified ``f(0)`` is assumed to be ``C0`` and the power
          series solution is calculated about 0.

        ``x0`` is the point about which the power series solution of a differential
          equation is to be evaluated.

        ``n`` gives the exponent of the dependent variable up to which the power series
          solution of a differential equation is to be evaluated.

    **Hints**

        Aside from the various solving methods, there are also some meta-hints
        that you can pass to :py:meth:`~sympy.solvers.ode.dsolve`:

        ``default``:
                This uses whatever hint is returned first by
                :py:meth:`~sympy.solvers.ode.classify_ode`. This is the
                default argument to :py:meth:`~sympy.solvers.ode.dsolve`.

        ``all``:
                To make :py:meth:`~sympy.solvers.ode.dsolve` apply all
                relevant classification hints, use ``dsolve(ODE, func,
                hint="all")``.  This will return a dictionary of
                ``hint:solution`` terms.  If a hint causes dsolve to raise the
                ``NotImplementedError``, value of that hint's key will be the
                exception object raised.  The dictionary will also include
                some special keys:

                - ``order``: The order of the ODE.  See also
                  :py:meth:`~sympy.solvers.deutils.ode_order` in
                  ``deutils.py``.
                - ``best``: The simplest hint; what would be returned by
                  ``best`` below.
                - ``best_hint``: The hint that would produce the solution
                  given by ``best``.  If more than one hint produces the best
                  solution, the first one in the tuple returned by
                  :py:meth:`~sympy.solvers.ode.classify_ode` is chosen.
                - ``default``: The solution that would be returned by default.
                  This is the one produced by the hint that appears first in
                  the tuple returned by
                  :py:meth:`~sympy.solvers.ode.classify_ode`.

        ``all_Integral``:
                This is the same as ``all``, except if a hint also has a
                corresponding ``_Integral`` hint, it only returns the
                ``_Integral`` hint.  This is useful if ``all`` causes
                :py:meth:`~sympy.solvers.ode.dsolve` to hang because of a
                difficult or impossible integral.  This meta-hint will also be
                much faster than ``all``, because
                :py:meth:`~sympy.core.expr.Expr.integrate` is an expensive
                routine.

        ``best``:
                To have :py:meth:`~sympy.solvers.ode.dsolve` try all methods
                and return the simplest one.  This takes into account whether
                the solution is solvable in the function, whether it contains
                any Integral classes (i.e.  unevaluatable integrals), and
                which one is the shortest in size.

        See also the :py:meth:`~sympy.solvers.ode.classify_ode` docstring for
        more info on hints, and the :py:mod:`~sympy.solvers.ode` docstring for
        a list of all supported hints.

    **Tips**

        - You can declare the derivative of an unknown function this way:

            >>> from sympy import Function, Derivative
            >>> from sympy.abc import x # x is the independent variable
            >>> f = Function("f")(x) # f is a function of x
            >>> # f_ will be the derivative of f with respect to x
            >>> f_ = Derivative(f, x)

        - See ``test_ode.py`` for many tests, which serves also as a set of
          examples for how to use :py:meth:`~sympy.solvers.ode.dsolve`.
        - :py:meth:`~sympy.solvers.ode.dsolve` always returns an
          :py:class:`~sympy.core.relational.Equality` class (except for the
          case when the hint is ``all`` or ``all_Integral``).  If possible, it
          solves the solution explicitly for the function being solved for.
          Otherwise, it returns an implicit solution.
        - Arbitrary constants are symbols named ``C1``, ``C2``, and so on.
        - Because all solutions should be mathematically equivalent, some
          hints may return the exact same result for an ODE. Often, though,
          two different hints will return the same solution formatted
          differently.  The two should be equivalent. Also note that sometimes
          the values of the arbitrary constants in two different solutions may
          not be the same, because one constant may have "absorbed" other
          constants into it.
        - Do ``help(ode.ode_<hintname>)`` to get help more information on a
          specific hint, where ``<hintname>`` is the name of a hint without
          ``_Integral``.

    For system of ordinary differential equations
    =============================================

    **Usage**
        ``dsolve(eq, func)`` -> Solve a system of ordinary differential
        equations ``eq`` for ``func`` being list of functions including
        `x(t)`, `y(t)`, `z(t)` where number of functions in the list depends
        upon the number of equations provided in ``eq``.

    **Details**

        ``eq`` can be any supported system of ordinary differential equations
        This can either be an :py:class:`~sympy.core.relational.Equality`,
        or an expression, which is assumed to be equal to ``0``.

        ``func`` holds ``x(t)`` and ``y(t)`` being functions of one variable which
        together with some of their derivatives make up the system of ordinary
        differential equation ``eq``. It is not necessary to provide this; it
        will be autodetected (and an error raised if it could not be detected).

    **Hints**

        The hints are formed by parameters returned by classify_sysode, combining
        them give hints name used later for forming method name.

    Examples
    ========

    >>> from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> dsolve(Derivative(f(x), x, x) + 9*f(x), f(x))
    Eq(f(x), C1*sin(3*x) + C2*cos(3*x))

    >>> eq = sin(x)*cos(f(x)) + cos(x)*sin(f(x))*f(x).diff(x)
    >>> dsolve(eq, hint='1st_exact')
    [Eq(f(x), -acos(C1/cos(x)) + 2*pi), Eq(f(x), acos(C1/cos(x)))]
    >>> dsolve(eq, hint='almost_linear')
    [Eq(f(x), -acos(C1/cos(x)) + 2*pi), Eq(f(x), acos(C1/cos(x)))]
    >>> t = symbols('t')
    >>> x, y = symbols('x, y', cls=Function)
    >>> eq = (Eq(Derivative(x(t),t), 12*t*x(t) + 8*y(t)), Eq(Derivative(y(t),t), 21*x(t) + 7*t*y(t)))
    >>> dsolve(eq)
    [Eq(x(t), C1*x0(t) + C2*x0(t)*Integral(8*exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)**2, t)),
    Eq(y(t), C1*y0(t) + C2*(y0(t)*Integral(8*exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)**2, t) +
    exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)))]
    >>> eq = (Eq(Derivative(x(t),t),x(t)*y(t)*sin(t)), Eq(Derivative(y(t),t),y(t)**2*sin(t)))
    >>> dsolve(eq)
    {Eq(x(t), -exp(C1)/(C2*exp(C1) - cos(t))), Eq(y(t), -1/(C1 - cos(t)))}
    """
    ...

def solve_ics(sols, funcs, constants, ics):
    """
    Solve for the constants given initial conditions

    ``sols`` is a list of solutions.

    ``funcs`` is a list of functions.

    ``constants`` is a list of constants.

    ``ics`` is the set of initial/boundary conditions for the differential
    equation. It should be given in the form of ``{f(x0): x1,
    f(x).diff(x).subs(x, x2):  x3}`` and so on.

    Returns a dictionary mapping constants to values.
    ``solution.subs(constants)`` will replace the constants in ``solution``.

    Example
    =======
    >>> # From dsolve(f(x).diff(x) - f(x), f(x))
    >>> from sympy import symbols, Eq, exp, Function
    >>> from sympy.solvers.ode.ode import solve_ics
    >>> f = Function('f')
    >>> x, C1 = symbols('x C1')
    >>> sols = [Eq(f(x), C1*exp(x))]
    >>> funcs = [f(x)]
    >>> constants = [C1]
    >>> ics = {f(0): 2}
    >>> solved_constants = solve_ics(sols, funcs, constants, ics)
    >>> solved_constants
    {C1: 2}
    >>> sols[0].subs(solved_constants)
    Eq(f(x), 2*exp(x))

    """
    ...

def classify_ode(eq, func=..., dict=..., ics=..., *, prep=..., xi=..., eta=..., n=..., **kwargs):
    r"""
    Returns a tuple of possible :py:meth:`~sympy.solvers.ode.dsolve`
    classifications for an ODE.

    The tuple is ordered so that first item is the classification that
    :py:meth:`~sympy.solvers.ode.dsolve` uses to solve the ODE by default.  In
    general, classifications at the near the beginning of the list will
    produce better solutions faster than those near the end, thought there are
    always exceptions.  To make :py:meth:`~sympy.solvers.ode.dsolve` use a
    different classification, use ``dsolve(ODE, func,
    hint=<classification>)``.  See also the
    :py:meth:`~sympy.solvers.ode.dsolve` docstring for different meta-hints
    you can use.

    If ``dict`` is true, :py:meth:`~sympy.solvers.ode.classify_ode` will
    return a dictionary of ``hint:match`` expression terms. This is intended
    for internal use by :py:meth:`~sympy.solvers.ode.dsolve`.  Note that
    because dictionaries are ordered arbitrarily, this will most likely not be
    in the same order as the tuple.

    You can get help on different hints by executing
    ``help(ode.ode_hintname)``, where ``hintname`` is the name of the hint
    without ``_Integral``.

    See :py:data:`~sympy.solvers.ode.allhints` or the
    :py:mod:`~sympy.solvers.ode` docstring for a list of all supported hints
    that can be returned from :py:meth:`~sympy.solvers.ode.classify_ode`.

    Notes
    =====

    These are remarks on hint names.

    ``_Integral``

        If a classification has ``_Integral`` at the end, it will return the
        expression with an unevaluated :py:class:`~.Integral`
        class in it.  Note that a hint may do this anyway if
        :py:meth:`~sympy.core.expr.Expr.integrate` cannot do the integral,
        though just using an ``_Integral`` will do so much faster.  Indeed, an
        ``_Integral`` hint will always be faster than its corresponding hint
        without ``_Integral`` because
        :py:meth:`~sympy.core.expr.Expr.integrate` is an expensive routine.
        If :py:meth:`~sympy.solvers.ode.dsolve` hangs, it is probably because
        :py:meth:`~sympy.core.expr.Expr.integrate` is hanging on a tough or
        impossible integral.  Try using an ``_Integral`` hint or
        ``all_Integral`` to get it return something.

        Note that some hints do not have ``_Integral`` counterparts. This is
        because :py:func:`~sympy.integrals.integrals.integrate` is not used in
        solving the ODE for those method. For example, `n`\th order linear
        homogeneous ODEs with constant coefficients do not require integration
        to solve, so there is no
        ``nth_linear_homogeneous_constant_coeff_Integrate`` hint. You can
        easily evaluate any unevaluated
        :py:class:`~sympy.integrals.integrals.Integral`\s in an expression by
        doing ``expr.doit()``.

    Ordinals

        Some hints contain an ordinal such as ``1st_linear``.  This is to help
        differentiate them from other hints, as well as from other methods
        that may not be implemented yet. If a hint has ``nth`` in it, such as
        the ``nth_linear`` hints, this means that the method used to applies
        to ODEs of any order.

    ``indep`` and ``dep``

        Some hints contain the words ``indep`` or ``dep``.  These reference
        the independent variable and the dependent function, respectively. For
        example, if an ODE is in terms of `f(x)`, then ``indep`` will refer to
        `x` and ``dep`` will refer to `f`.

    ``subs``

        If a hints has the word ``subs`` in it, it means that the ODE is solved
        by substituting the expression given after the word ``subs`` for a
        single dummy variable.  This is usually in terms of ``indep`` and
        ``dep`` as above.  The substituted expression will be written only in
        characters allowed for names of Python objects, meaning operators will
        be spelled out.  For example, ``indep``/``dep`` will be written as
        ``indep_div_dep``.

    ``coeff``

        The word ``coeff`` in a hint refers to the coefficients of something
        in the ODE, usually of the derivative terms.  See the docstring for
        the individual methods for more info (``help(ode)``).  This is
        contrast to ``coefficients``, as in ``undetermined_coefficients``,
        which refers to the common name of a method.

    ``_best``

        Methods that have more than one fundamental way to solve will have a
        hint for each sub-method and a ``_best`` meta-classification. This
        will evaluate all hints and return the best, using the same
        considerations as the normal ``best`` meta-hint.


    Examples
    ========

    >>> from sympy import Function, classify_ode, Eq
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> classify_ode(Eq(f(x).diff(x), 0), f(x))
    ('nth_algebraic',
    'separable',
    '1st_exact',
    '1st_linear',
    'Bernoulli',
    '1st_homogeneous_coeff_best',
    '1st_homogeneous_coeff_subs_indep_div_dep',
    '1st_homogeneous_coeff_subs_dep_div_indep',
    '1st_power_series', 'lie_group', 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_euler_eq_homogeneous',
    'nth_algebraic_Integral', 'separable_Integral', '1st_exact_Integral',
    '1st_linear_Integral', 'Bernoulli_Integral',
    '1st_homogeneous_coeff_subs_indep_div_dep_Integral',
    '1st_homogeneous_coeff_subs_dep_div_indep_Integral')
    >>> classify_ode(f(x).diff(x, 2) + 3*f(x).diff(x) + 2*f(x) - 4)
    ('factorable', 'nth_linear_constant_coeff_undetermined_coefficients',
    'nth_linear_constant_coeff_variation_of_parameters',
    'nth_linear_constant_coeff_variation_of_parameters_Integral')

    """
    ...

def classify_sysode(eq, funcs=..., **kwargs) -> dict[str, int]:
    r"""
    Returns a dictionary of parameter names and values that define the system
    of ordinary differential equations in ``eq``.
    The parameters are further used in
    :py:meth:`~sympy.solvers.ode.dsolve` for solving that system.

    Some parameter names and values are:

    'is_linear' (boolean), which tells whether the given system is linear.
    Note that "linear" here refers to the operator: terms such as ``x*diff(x,t)`` are
    nonlinear, whereas terms like ``sin(t)*diff(x,t)`` are still linear operators.

    'func' (list) contains the :py:class:`~sympy.core.function.Function`s that
    appear with a derivative in the ODE, i.e. those that we are trying to solve
    the ODE for.

    'order' (dict) with the maximum derivative for each element of the 'func'
    parameter.

    'func_coeff' (dict or Matrix) with the coefficient for each triple ``(equation number,
    function, order)```. The coefficients are those subexpressions that do not
    appear in 'func', and hence can be considered constant for purposes of ODE
    solving. The value of this parameter can also be a  Matrix if the system of ODEs are
    linear first order of the form X' = AX where X is the vector of dependent variables.
    Here, this function returns the coefficient matrix A.

    'eq' (list) with the equations from ``eq``, sympified and transformed into
    expressions (we are solving for these expressions to be zero).

    'no_of_equations' (int) is the number of equations (same as ``len(eq)``).

    'type_of_equation' (string) is an internal classification of the type of
    ODE.

    'is_constant' (boolean), which tells if the system of ODEs is constant coefficient
    or not. This key is temporary addition for now and is in the match dict only when
    the system of ODEs is linear first order constant coefficient homogeneous. So, this
    key's value is True for now if it is available else it does not exist.

    'is_homogeneous' (boolean), which tells if the system of ODEs is homogeneous. Like the
    key 'is_constant', this key is a temporary addition and it is True since this key value
    is available only when the system is linear first order constant coefficient homogeneous.

    References
    ==========
    -https://eqworld.ipmnet.ru/en/solutions/sysode/sode-toc1.htm
    -A. D. Polyanin and A. V. Manzhirov, Handbook of Mathematics for Engineers and Scientists

    Examples
    ========

    >>> from sympy import Function, Eq, symbols, diff
    >>> from sympy.solvers.ode.ode import classify_sysode
    >>> from sympy.abc import t
    >>> f, x, y = symbols('f, x, y', cls=Function)
    >>> k, l, m, n = symbols('k, l, m, n', Integer=True)
    >>> x1 = diff(x(t), t) ; y1 = diff(y(t), t)
    >>> x2 = diff(x(t), t, t) ; y2 = diff(y(t), t, t)
    >>> eq = (Eq(x1, 12*x(t) - 6*y(t)), Eq(y1, 11*x(t) + 3*y(t)))
    >>> classify_sysode(eq)
    {'eq': [-12*x(t) + 6*y(t) + Derivative(x(t), t), -11*x(t) - 3*y(t) + Derivative(y(t), t)], 'func': [x(t), y(t)],
     'func_coeff': {(0, x(t), 0): -12, (0, x(t), 1): 1, (0, y(t), 0): 6, (0, y(t), 1): 0, (1, x(t), 0): -11, (1, x(t), 1): 0, (1, y(t), 0): -3, (1, y(t), 1): 1}, 'is_linear': True, 'no_of_equation': 2, 'order': {x(t): 1, y(t): 1}, 'type_of_equation': None}
    >>> eq = (Eq(diff(x(t),t), 5*t*x(t) + t**2*y(t) + 2), Eq(diff(y(t),t), -t**2*x(t) + 5*t*y(t)))
    >>> classify_sysode(eq)
    {'eq': [-t**2*y(t) - 5*t*x(t) + Derivative(x(t), t) - 2, t**2*x(t) - 5*t*y(t) + Derivative(y(t), t)],
     'func': [x(t), y(t)], 'func_coeff': {(0, x(t), 0): -5*t, (0, x(t), 1): 1, (0, y(t), 0): -t**2, (0, y(t), 1): 0,
     (1, x(t), 0): t**2, (1, x(t), 1): 0, (1, y(t), 0): -5*t, (1, y(t), 1): 1}, 'is_linear': True, 'no_of_equation': 2,
      'order': {x(t): 1, y(t): 1}, 'type_of_equation': None}

    """
    ...

def check_linear_2eq_order1(eq, func, func_coef) -> Literal['type6', 'type7'] | None:
    ...

def check_nonlinear_2eq_order1(eq, func, func_coef) -> Literal['type5', 'type1', 'type2', 'type3', 'type4'] | None:
    ...

def check_nonlinear_2eq_order2(eq, func, func_coef) -> None:
    ...

def check_nonlinear_3eq_order1(eq, func, func_coef):
    ...

def check_nonlinear_3eq_order2(eq, func, func_coef) -> None:
    ...

@vectorize(0)
def odesimp(ode, eq, func, hint) -> list[Eq | Any | Relational | Ne] | list[list[Any] | Any] | Eq | Relational | Ne | list[list[Eq | Any | Relational | Ne] | list[list[Any] | Any] | Any]:
    r"""
    Simplifies solutions of ODEs, including trying to solve for ``func`` and
    running :py:meth:`~sympy.solvers.ode.constantsimp`.

    It may use knowledge of the type of solution that the hint returns to
    apply additional simplifications.

    It also attempts to integrate any :py:class:`~sympy.integrals.integrals.Integral`\s
    in the expression, if the hint is not an ``_Integral`` hint.

    This function should have no effect on expressions returned by
    :py:meth:`~sympy.solvers.ode.dsolve`, as
    :py:meth:`~sympy.solvers.ode.dsolve` already calls
    :py:meth:`~sympy.solvers.ode.ode.odesimp`, but the individual hint functions
    do not call :py:meth:`~sympy.solvers.ode.ode.odesimp` (because the
    :py:meth:`~sympy.solvers.ode.dsolve` wrapper does).  Therefore, this
    function is designed for mainly internal use.

    Examples
    ========

    >>> from sympy import sin, symbols, dsolve, pprint, Function
    >>> from sympy.solvers.ode.ode import odesimp
    >>> x, u2, C1= symbols('x,u2,C1')
    >>> f = Function('f')

    >>> eq = dsolve(x*f(x).diff(x) - f(x) - x*sin(f(x)/x), f(x),
    ... hint='1st_homogeneous_coeff_subs_indep_div_dep_Integral',
    ... simplify=False)
    >>> pprint(eq, wrap_line=False)
                            x
                           ----
                           f(x)
                             /
                            |
                            |   /        1   \
                            |  -|u1 + -------|
                            |   |        /1 \|
                            |   |     sin|--||
                            |   \        \u1//
    log(f(x)) = log(C1) +   |  ---------------- d(u1)
                            |          2
                            |        u1
                            |
                           /

    >>> pprint(odesimp(eq, f(x), 1, {C1},
    ... hint='1st_homogeneous_coeff_subs_indep_div_dep'
    ... )) #doctest: +SKIP
        x
    --------- = C1
       /f(x)\
    tan|----|
       \2*x /

    """
    ...

def ode_sol_simplicity(sol, func, trysolving=...) -> int:
    r"""
    Returns an extended integer representing how simple a solution to an ODE
    is.

    The following things are considered, in order from most simple to least:

    - ``sol`` is solved for ``func``.
    - ``sol`` is not solved for ``func``, but can be if passed to solve (e.g.,
      a solution returned by ``dsolve(ode, func, simplify=False``).
    - If ``sol`` is not solved for ``func``, then base the result on the
      length of ``sol``, as computed by ``len(str(sol))``.
    - If ``sol`` has any unevaluated :py:class:`~sympy.integrals.integrals.Integral`\s,
      this will automatically be considered less simple than any of the above.

    This function returns an integer such that if solution A is simpler than
    solution B by above metric, then ``ode_sol_simplicity(sola, func) <
    ode_sol_simplicity(solb, func)``.

    Currently, the following are the numbers returned, but if the heuristic is
    ever improved, this may change.  Only the ordering is guaranteed.

    +----------------------------------------------+-------------------+
    | Simplicity                                   | Return            |
    +==============================================+===================+
    | ``sol`` solved for ``func``                  | ``-2``            |
    +----------------------------------------------+-------------------+
    | ``sol`` not solved for ``func`` but can be   | ``-1``            |
    +----------------------------------------------+-------------------+
    | ``sol`` is not solved nor solvable for       | ``len(str(sol))`` |
    | ``func``                                     |                   |
    +----------------------------------------------+-------------------+
    | ``sol`` contains an                          | ``oo``            |
    | :obj:`~sympy.integrals.integrals.Integral`   |                   |
    +----------------------------------------------+-------------------+

    ``oo`` here means the SymPy infinity, which should compare greater than
    any integer.

    If you already know :py:meth:`~sympy.solvers.solvers.solve` cannot solve
    ``sol``, you can use ``trysolving=False`` to skip that step, which is the
    only potentially slow step.  For example,
    :py:meth:`~sympy.solvers.ode.dsolve` with the ``simplify=False`` flag
    should do this.

    If ``sol`` is a list of solutions, if the worst solution in the list
    returns ``oo`` it returns that, otherwise it returns ``len(str(sol))``,
    that is, the length of the string representation of the whole list.

    Examples
    ========

    This function is designed to be passed to ``min`` as the key argument,
    such as ``min(listofsolutions, key=lambda i: ode_sol_simplicity(i,
    f(x)))``.

    >>> from sympy import symbols, Function, Eq, tan, Integral
    >>> from sympy.solvers.ode.ode import ode_sol_simplicity
    >>> x, C1, C2 = symbols('x, C1, C2')
    >>> f = Function('f')

    >>> ode_sol_simplicity(Eq(f(x), C1*x**2), f(x))
    -2
    >>> ode_sol_simplicity(Eq(x**2 + f(x), C1), f(x))
    -1
    >>> ode_sol_simplicity(Eq(f(x), C1*Integral(2*x, x)), f(x))
    oo
    >>> eq1 = Eq(f(x)/tan(f(x)/(2*x)), C1)
    >>> eq2 = Eq(f(x)/tan(f(x)/(2*x) + f(x)), C2)
    >>> [ode_sol_simplicity(eq, f(x)) for eq in [eq1, eq2]]
    [28, 35]
    >>> min([eq1, eq2], key=lambda i: ode_sol_simplicity(i, f(x)))
    Eq(f(x)/tan(f(x)/(2*x)), C1)

    """
    ...

@vectorize(0)
def constantsimp(expr, constants) -> list[list[Any] | Any] | Eq | Relational | Ne | Add | Basic | Any:
    r"""
    Simplifies an expression with arbitrary constants in it.

    This function is written specifically to work with
    :py:meth:`~sympy.solvers.ode.dsolve`, and is not intended for general use.

    Simplification is done by "absorbing" the arbitrary constants into other
    arbitrary constants, numbers, and symbols that they are not independent
    of.

    The symbols must all have the same name with numbers after it, for
    example, ``C1``, ``C2``, ``C3``.  The ``symbolname`` here would be
    '``C``', the ``startnumber`` would be 1, and the ``endnumber`` would be 3.
    If the arbitrary constants are independent of the variable ``x``, then the
    independent symbol would be ``x``.  There is no need to specify the
    dependent function, such as ``f(x)``, because it already has the
    independent symbol, ``x``, in it.

    Because terms are "absorbed" into arbitrary constants and because
    constants are renumbered after simplifying, the arbitrary constants in
    expr are not necessarily equal to the ones of the same name in the
    returned result.

    If two or more arbitrary constants are added, multiplied, or raised to the
    power of each other, they are first absorbed together into a single
    arbitrary constant.  Then the new constant is combined into other terms if
    necessary.

    Absorption of constants is done with limited assistance:

    1. terms of :py:class:`~sympy.core.add.Add`\s are collected to try join
       constants so `e^x (C_1 \cos(x) + C_2 \cos(x))` will simplify to `e^x
       C_1 \cos(x)`;

    2. powers with exponents that are :py:class:`~sympy.core.add.Add`\s are
       expanded so `e^{C_1 + x}` will be simplified to `C_1 e^x`.

    Use :py:meth:`~sympy.solvers.ode.ode.constant_renumber` to renumber constants
    after simplification or else arbitrary numbers on constants may appear,
    e.g. `C_1 + C_3 x`.

    In rare cases, a single constant can be "simplified" into two constants.
    Every differential equation solution should have as many arbitrary
    constants as the order of the differential equation.  The result here will
    be technically correct, but it may, for example, have `C_1` and `C_2` in
    an expression, when `C_1` is actually equal to `C_2`.  Use your discretion
    in such situations, and also take advantage of the ability to use hints in
    :py:meth:`~sympy.solvers.ode.dsolve`.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.solvers.ode.ode import constantsimp
    >>> C1, C2, C3, x, y = symbols('C1, C2, C3, x, y')
    >>> constantsimp(2*C1*x, {C1, C2, C3})
    C1*x
    >>> constantsimp(C1 + 2 + x, {C1, C2, C3})
    C1 + x
    >>> constantsimp(C1*C2 + 2 + C2 + C3*x, {C1, C2, C3})
    C1 + C3*x

    """
    ...

def constant_renumber(expr, variables=..., newconstants=...) -> list[Any] | set[Any] | tuple[Any, ...] | Tuple | Basic | Eq | Relational | Ne:
    r"""
    Renumber arbitrary constants in ``expr`` to use the symbol names as given
    in ``newconstants``. In the process, this reorders expression terms in a
    standard way.

    If ``newconstants`` is not provided then the new constant names will be
    ``C1``, ``C2`` etc. Otherwise ``newconstants`` should be an iterable
    giving the new symbols to use for the constants in order.

    The ``variables`` argument is a list of non-constant symbols. All other
    free symbols found in ``expr`` are assumed to be constants and will be
    renumbered. If ``variables`` is not given then any numbered symbol
    beginning with ``C`` (e.g. ``C1``) is assumed to be a constant.

    Symbols are renumbered based on ``.sort_key()``, so they should be
    numbered roughly in the order that they appear in the final, printed
    expression.  Note that this ordering is based in part on hashes, so it can
    produce different results on different machines.

    The structure of this function is very similar to that of
    :py:meth:`~sympy.solvers.ode.constantsimp`.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.solvers.ode.ode import constant_renumber
    >>> x, C1, C2, C3 = symbols('x,C1:4')
    >>> expr = C3 + C2*x + C1*x**2
    >>> expr
    C1*x**2  + C2*x + C3
    >>> constant_renumber(expr)
    C1 + C2*x + C3*x**2

    The ``variables`` argument specifies which are constants so that the
    other symbols will not be renumbered:

    >>> constant_renumber(expr, [C1, x])
    C1*x**2  + C2 + C3*x

    The ``newconstants`` argument is used to specify what symbols to use when
    replacing the constants:

    >>> constant_renumber(expr, [x], newconstants=symbols('E1:4'))
    E1 + E2*x + E3*x**2

    """
    ...

def homogeneous_order(eq, *symbols) -> Any | None:
    r"""
    Returns the order `n` if `g` is homogeneous and ``None`` if it is not
    homogeneous.

    Determines if a function is homogeneous and if so of what order.  A
    function `f(x, y, \cdots)` is homogeneous of order `n` if `f(t x, t y,
    \cdots) = t^n f(x, y, \cdots)`.

    If the function is of two variables, `F(x, y)`, then `f` being homogeneous
    of any order is equivalent to being able to rewrite `F(x, y)` as `G(x/y)`
    or `H(y/x)`.  This fact is used to solve 1st order ordinary differential
    equations whose coefficients are homogeneous of the same order (see the
    docstrings of
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsDepDivIndep` and
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsIndepDivDep`).

    Symbols can be functions, but every argument of the function must be a
    symbol, and the arguments of the function that appear in the expression
    must match those given in the list of symbols.  If a declared function
    appears with different arguments than given in the list of symbols,
    ``None`` is returned.

    Examples
    ========

    >>> from sympy import Function, homogeneous_order, sqrt
    >>> from sympy.abc import x, y
    >>> f = Function('f')
    >>> homogeneous_order(f(x), f(x)) is None
    True
    >>> homogeneous_order(f(x,y), f(y, x), x, y) is None
    True
    >>> homogeneous_order(f(x), f(x), x)
    1
    >>> homogeneous_order(x**2*f(x)/sqrt(x**2+f(x)**2), x, f(x))
    2
    >>> homogeneous_order(x**2+f(x), x, f(x)) is None
    True

    """
    ...

def ode_2nd_power_series_ordinary(eq, func, order, match) -> Eq | Relational | Ne:
    r"""
    Gives a power series solution to a second order homogeneous differential
    equation with polynomial coefficients at an ordinary point. A homogeneous
    differential equation is of the form

    .. math :: P(x)\frac{d^2y}{dx^2} + Q(x)\frac{dy}{dx} + R(x) y(x) = 0

    For simplicity it is assumed that `P(x)`, `Q(x)` and `R(x)` are polynomials,
    it is sufficient that `\frac{Q(x)}{P(x)}` and `\frac{R(x)}{P(x)}` exists at
    `x_{0}`. A recurrence relation is obtained by substituting `y` as `\sum_{n=0}^\infty a_{n}x^{n}`,
    in the differential equation, and equating the nth term. Using this relation
    various terms can be generated.


    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function("f")
    >>> eq = f(x).diff(x, 2) + f(x)
    >>> pprint(dsolve(eq, hint='2nd_power_series_ordinary'))
              / 4    2    \        /     2\
              |x    x     |        |    x |    / 6\
    f(x) = C2*|-- - -- + 1| + C1*x*|1 - --| + O\x /
              \24   2     /        \    6 /


    References
    ==========
    - https://tutorial.math.lamar.edu/Classes/DE/SeriesSolutions.aspx
    - George E. Simmons, "Differential Equations with Applications and
      Historical Notes", p.p 176 - 184

    """
    ...

def ode_2nd_power_series_regular(eq, func, order, match) -> Eq | Relational | Ne | None:
    r"""
    Gives a power series solution to a second order homogeneous differential
    equation with polynomial coefficients at a regular point. A second order
    homogeneous differential equation is of the form

    .. math :: P(x)\frac{d^2y}{dx^2} + Q(x)\frac{dy}{dx} + R(x) y(x) = 0

    A point is said to regular singular at `x0` if `x - x0\frac{Q(x)}{P(x)}`
    and `(x - x0)^{2}\frac{R(x)}{P(x)}` are analytic at `x0`. For simplicity
    `P(x)`, `Q(x)` and `R(x)` are assumed to be polynomials. The algorithm for
    finding the power series solutions is:

    1.  Try expressing `(x - x0)P(x)` and `((x - x0)^{2})Q(x)` as power series
        solutions about x0. Find `p0` and `q0` which are the constants of the
        power series expansions.
    2.  Solve the indicial equation `f(m) = m(m - 1) + m*p0 + q0`, to obtain the
        roots `m1` and `m2` of the indicial equation.
    3.  If `m1 - m2` is a non integer there exists two series solutions. If
        `m1 = m2`, there exists only one solution. If `m1 - m2` is an integer,
        then the existence of one solution is confirmed. The other solution may
        or may not exist.

    The power series solution is of the form `x^{m}\sum_{n=0}^\infty a_{n}x^{n}`. The
    coefficients are determined by the following recurrence relation.
    `a_{n} = -\frac{\sum_{k=0}^{n-1} q_{n-k} + (m + k)p_{n-k}}{f(m + n)}`. For the case
    in which `m1 - m2` is an integer, it can be seen from the recurrence relation
    that for the lower root `m`, when `n` equals the difference of both the
    roots, the denominator becomes zero. So if the numerator is not equal to zero,
    a second series solution exists.


    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function("f")
    >>> eq = x*(f(x).diff(x, 2)) + 2*(f(x).diff(x)) + x*f(x)
    >>> pprint(dsolve(eq, hint='2nd_power_series_regular'))
                                  /   6     4    2    \
                                  |  x     x    x     |
              / 4     2    \   C1*|- --- + -- - -- + 1|
              |x     x     |      \  720   24   2     /    / 6\
    f(x) = C2*|--- - -- + 1| + ------------------------ + O\x /
              \120   6     /              x


    References
    ==========
    - George E. Simmons, "Differential Equations with Applications and
      Historical Notes", p.p 176 - 184

    """
    ...

def ode_1st_power_series(eq, func, order, match) -> Eq | Relational | Ne:
    r"""
    The power series solution is a method which gives the Taylor series expansion
    to the solution of a differential equation.

    For a first order differential equation `\frac{dy}{dx} = h(x, y)`, a power
    series solution exists at a point `x = x_{0}` if `h(x, y)` is analytic at `x_{0}`.
    The solution is given by

    .. math:: y(x) = y(x_{0}) + \sum_{n = 1}^{\infty} \frac{F_{n}(x_{0},b)(x - x_{0})^n}{n!},

    where `y(x_{0}) = b` is the value of y at the initial value of `x_{0}`.
    To compute the values of the `F_{n}(x_{0},b)` the following algorithm is
    followed, until the required number of terms are generated.

    1. `F_1 = h(x_{0}, b)`
    2. `F_{n+1} = \frac{\partial F_{n}}{\partial x} + \frac{\partial F_{n}}{\partial y}F_{1}`

    Examples
    ========

    >>> from sympy import Function, pprint, exp, dsolve
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = exp(x)*(f(x).diff(x)) - f(x)
    >>> pprint(dsolve(eq, hint='1st_power_series'))
                           3       4       5
                       C1*x    C1*x    C1*x     / 6\
    f(x) = C1 + C1*x - ----- + ----- + ----- + O\x /
                         6       24      60


    References
    ==========

    - Travis W. Walker, Analytic power series technique for solving first-order
      differential equations, p.p 17, 18

    """
    ...

def checkinfsol(eq, infinitesimals, func=..., order=...) -> list[Any]:
    r"""
    This function is used to check if the given infinitesimals are the
    actual infinitesimals of the given first order differential equation.
    This method is specific to the Lie Group Solver of ODEs.

    As of now, it simply checks, by substituting the infinitesimals in the
    partial differential equation.


    .. math:: \frac{\partial \eta}{\partial x} + \left(\frac{\partial \eta}{\partial y}
                - \frac{\partial \xi}{\partial x}\right)*h
                - \frac{\partial \xi}{\partial y}*h^{2}
                - \xi\frac{\partial h}{\partial x} - \eta\frac{\partial h}{\partial y} = 0


    where `\eta`, and `\xi` are the infinitesimals and `h(x,y) = \frac{dy}{dx}`

    The infinitesimals should be given in the form of a list of dicts
    ``[{xi(x, y): inf, eta(x, y): inf}]``, corresponding to the
    output of the function infinitesimals. It returns a list
    of values of the form ``[(True/False, sol)]`` where ``sol`` is the value
    obtained after substituting the infinitesimals in the PDE. If it
    is ``True``, then ``sol`` would be 0.

    """
    ...

def sysode_linear_2eq_order1(match_) -> list[Eq | Any | Relational | Ne]:
    ...

def sysode_nonlinear_2eq_order1(match_) -> set[Eq] | list[Any] | set[Any]:
    ...

def sysode_nonlinear_3eq_order1(match_) -> list[Any | Basic] | list[Any | list[Any] | dict[Any, Any] | Equality | Basic | list[list[Any] | Any] | list[Equality]]:
    ...

