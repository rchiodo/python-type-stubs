from sympy.integrals.integrals import Integral

"""
The Risch Algorithm for transcendental function integration.

The core algorithms for the Risch algorithm are here.  The subproblem
algorithms are in the rde.py and prde.py files for the Risch
Differential Equation solver and the parametric problems solvers,
respectively.  All important information concerning the differential extension
for an integrand is stored in a DifferentialExtension object, which in the code
is usually called DE.  Throughout the code and Inside the DifferentialExtension
object, the conventions/attribute names are that the base domain is QQ and each
differential extension is x, t0, t1, ..., tn-1 = DE.t. DE.x is the variable of
integration (Dx == 1), DE.D is a list of the derivatives of
x, t1, t2, ..., tn-1 = t, DE.T is the list [x, t1, t2, ..., tn-1], DE.t is the
outer-most variable of the differential extension at the given level (the level
can be adjusted using DE.increment_level() and DE.decrement_level()),
k is the field C(x, t0, ..., tn-2), where C is the constant field.  The
numerator of a fraction is denoted by a and the denominator by
d.  If the fraction is named f, fa == numer(f) and fd == denom(f).
Fractions are returned as tuples (fa, fd).  DE.d and DE.t are used to
represent the topmost derivation and extension variable, respectively.
The docstring of a function signifies whether an argument is in k[t], in
which case it will just return a Poly in t, or in k(t), in which case it
will return the fraction (fa, fd). Other variable names probably come
from the names used in Bronstein's book.
"""
def integer_powers(exprs) -> list[tuple[Any, Any]]:
    """
    Rewrites a list of expressions as integer multiples of each other.

    Explanation
    ===========

    For example, if you have [x, x/2, x**2 + 1, 2*x/3], then you can rewrite
    this as [(x/6) * 6, (x/6) * 3, (x**2 + 1) * 1, (x/6) * 4]. This is useful
    in the Risch integration algorithm, where we must write exp(x) + exp(x/2)
    as (exp(x/2))**2 + exp(x/2), but not as exp(x) + sqrt(exp(x)) (this is
    because only the transcendental case is implemented and we therefore cannot
    integrate algebraic extensions). The integer multiples returned by this
    function for each term are the smallest possible (their content equals 1).

    Returns a list of tuples where the first element is the base term and the
    second element is a list of `(item, factor)` terms, where `factor` is the
    integer multiplicative factor that must multiply the base term to obtain
    the original item.

    The easiest way to understand this is to look at an example:

    >>> from sympy.abc import x
    >>> from sympy.integrals.risch import integer_powers
    >>> integer_powers([x, x/2, x**2 + 1, 2*x/3])
    [(x/6, [(x, 6), (x/2, 3), (2*x/3, 4)]), (x**2 + 1, [(x**2 + 1, 1)])]

    We can see how this relates to the example at the beginning of the
    docstring.  It chose x/6 as the first base term.  Then, x can be written as
    (x/2) * 2, so we get (0, 2), and so on. Now only element (x**2 + 1)
    remains, and there are no other terms that can be written as a rational
    multiple of that, so we get that it can be written as (x**2 + 1) * 1.

    """
    ...

class DifferentialExtension:
    """
    A container for all the information relating to a differential extension.

    Explanation
    ===========

    The attributes of this object are (see also the docstring of __init__):

    - f: The original (Expr) integrand.
    - x: The variable of integration.
    - T: List of variables in the extension.
    - D: List of derivations in the extension; corresponds to the elements of T.
    - fa: Poly of the numerator of the integrand.
    - fd: Poly of the denominator of the integrand.
    - Tfuncs: Lambda() representations of each element of T (except for x).
      For back-substitution after integration.
    - backsubs: A (possibly empty) list of further substitutions to be made on
      the final integral to make it look more like the integrand.
    - exts:
    - extargs:
    - cases: List of string representations of the cases of T.
    - t: The top level extension variable, as defined by the current level
      (see level below).
    - d: The top level extension derivation, as defined by the current
      derivation (see level below).
    - case: The string representation of the case of self.d.
    (Note that self.T and self.D will always contain the complete extension,
    regardless of the level.  Therefore, you should ALWAYS use DE.t and DE.d
    instead of DE.T[-1] and DE.D[-1].  If you want to have a list of the
    derivations or variables only up to the current level, use
    DE.D[:len(DE.D) + DE.level + 1] and DE.T[:len(DE.T) + DE.level + 1].  Note
    that, in particular, the derivation() function does this.)

    The following are also attributes, but will probably not be useful other
    than in internal use:
    - newf: Expr form of fa/fd.
    - level: The number (between -1 and -len(self.T)) such that
      self.T[self.level] == self.t and self.D[self.level] == self.d.
      Use the methods self.increment_level() and self.decrement_level() to change
      the current level.
    """
    __slots__ = ...
    def __init__(self, f=..., x=..., handle_first=..., dummy=..., extension=..., rewrite_complex=...) -> None:
        """
        Tries to build a transcendental extension tower from ``f`` with respect to ``x``.

        Explanation
        ===========

        If it is successful, creates a DifferentialExtension object with, among
        others, the attributes fa, fd, D, T, Tfuncs, and backsubs such that
        fa and fd are Polys in T[-1] with rational coefficients in T[:-1],
        fa/fd == f, and D[i] is a Poly in T[i] with rational coefficients in
        T[:i] representing the derivative of T[i] for each i from 1 to len(T).
        Tfuncs is a list of Lambda objects for back replacing the functions
        after integrating.  Lambda() is only used (instead of lambda) to make
        them easier to test and debug. Note that Tfuncs corresponds to the
        elements of T, except for T[0] == x, but they should be back-substituted
        in reverse order.  backsubs is a (possibly empty) back-substitution list
        that should be applied on the completed integral to make it look more
        like the original integrand.

        If it is unsuccessful, it raises NotImplementedError.

        You can also create an object by manually setting the attributes as a
        dictionary to the extension keyword argument.  You must include at least
        D.  Warning, any attribute that is not given will be set to None. The
        attributes T, t, d, cases, case, x, and level are set automatically and
        do not need to be given.  The functions in the Risch Algorithm will NOT
        check to see if an attribute is None before using it.  This also does not
        check to see if the extension is valid (non-algebraic) or even if it is
        self-consistent.  Therefore, this should only be used for
        testing/debugging purposes.
        """
        ...
    
    def __getattr__(self, attr) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def reset(self) -> None:
        """
        Reset self to an initial state.  Used by __init__.
        """
        ...
    
    def indices(self, extension) -> list[int]:
        """
        Parameters
        ==========

        extension : str
            Represents a valid extension type.

        Returns
        =======

        list: A list of indices of 'exts' where extension of
            type 'extension' is present.

        Examples
        ========

        >>> from sympy.integrals.risch import DifferentialExtension
        >>> from sympy import log, exp
        >>> from sympy.abc import x
        >>> DE = DifferentialExtension(log(x) + exp(x), x, handle_first='exp')
        >>> DE.indices('log')
        [2]
        >>> DE.indices('exp')
        [1]

        """
        ...
    
    def increment_level(self) -> None:
        """
        Increment the level of self.

        Explanation
        ===========

        This makes the working differential extension larger.  self.level is
        given relative to the end of the list (-1, -2, etc.), so we do not need
        do worry about it when building the extension.
        """
        ...
    
    def decrement_level(self) -> None:
        """
        Decrease the level of self.

        Explanation
        ===========

        This makes the working differential extension smaller.  self.level is
        given relative to the end of the list (-1, -2, etc.), so we do not need
        do worry about it when building the extension.
        """
        ...
    


def update_sets(seq, atoms, func) -> list[Any]:
    ...

class DecrementLevel:
    """
    A context manager for decrementing the level of a DifferentialExtension.
    """
    __slots__ = ...
    def __init__(self, DE) -> None:
        ...
    
    def __enter__(self) -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        ...
    


class NonElementaryIntegralException(Exception):
    """
    Exception used by subroutines within the Risch algorithm to indicate to one
    another that the function being integrated does not have an elementary
    integral in the given differential field.
    """
    ...


def gcdex_diophantine(a, b, c) -> tuple[Any, Any]:
    """
    Extended Euclidean Algorithm, Diophantine version.

    Explanation
    ===========

    Given ``a``, ``b`` in K[x] and ``c`` in (a, b), the ideal generated by ``a`` and
    ``b``, return (s, t) such that s*a + t*b == c and either s == 0 or s.degree()
    < b.degree().
    """
    ...

def frac_in(f, t, *, cancel=..., **kwargs) -> tuple[Any, Any]:
    """
    Returns the tuple (fa, fd), where fa and fd are Polys in t.

    Explanation
    ===========

    This is a common idiom in the Risch Algorithm functions, so we abstract
    it out here. ``f`` should be a basic expression, a Poly, or a tuple (fa, fd),
    where fa and fd are either basic expressions or Polys, and f == fa/fd.
    **kwargs are applied to Poly.
    """
    ...

def as_poly_1t(p, t, z):
    """
    (Hackish) way to convert an element ``p`` of K[t, 1/t] to K[t, z].

    In other words, ``z == 1/t`` will be a dummy variable that Poly can handle
    better.

    See issue 5131.

    Examples
    ========

    >>> from sympy import random_poly
    >>> from sympy.integrals.risch import as_poly_1t
    >>> from sympy.abc import x, z

    >>> p1 = random_poly(x, 10, -10, 10)
    >>> p2 = random_poly(x, 10, -10, 10)
    >>> p = p1 + p2.subs(x, 1/x)
    >>> as_poly_1t(p, x, z).as_expr().subs(z, 1/x) == p
    True
    """
    ...

def derivation(p, DE, coefficientD=..., basic=...) -> Any | Literal[0]:
    """
    Computes Dp.

    Explanation
    ===========

    Given the derivation D with D = d/dx and p is a polynomial in t over
    K(x), return Dp.

    If coefficientD is True, it computes the derivation kD
    (kappaD), which is defined as kD(sum(ai*Xi**i, (i, 0, n))) ==
    sum(Dai*Xi**i, (i, 1, n)) (Definition 3.2.2, page 80).  X in this case is
    T[-1], so coefficientD computes the derivative just with respect to T[:-1],
    with T[-1] treated as a constant.

    If ``basic=True``, the returns a Basic expression.  Elements of D can still be
    instances of Poly.
    """
    ...

def get_case(d, t) -> Literal['base', 'primitive', 'exp', 'tan', 'other_nonlinear', 'other_linear']:
    """
    Returns the type of the derivation d.

    Returns one of {'exp', 'tan', 'base', 'primitive', 'other_linear',
    'other_nonlinear'}.
    """
    ...

def splitfactor(p, DE, coefficientD=..., z=...) -> tuple[Any, Any]:
    """
    Splitting factorization.

    Explanation
    ===========

    Given a derivation D on k[t] and ``p`` in k[t], return (p_n, p_s) in
    k[t] x k[t] such that p = p_n*p_s, p_s is special, and each square
    factor of p_n is normal.

    Page. 100
    """
    ...

def splitfactor_sqf(p, DE, coefficientD=..., z=..., basic=...) -> tuple[tuple[tuple[Any, Literal[1]]], tuple[()]] | tuple[tuple[Any, ...], tuple[Any, ...]]:
    """
    Splitting Square-free Factorization.

    Explanation
    ===========

    Given a derivation D on k[t] and ``p`` in k[t], returns (N1, ..., Nm)
    and (S1, ..., Sm) in k[t]^m such that p =
    (N1*N2**2*...*Nm**m)*(S1*S2**2*...*Sm**m) is a splitting
    factorization of ``p`` and the Ni and Si are square-free and coprime.
    """
    ...

def canonical_representation(a, d, DE) -> tuple[Any, tuple[Any, Any], tuple[Any, Any]]:
    """
    Canonical Representation.

    Explanation
    ===========

    Given a derivation D on k[t] and f = a/d in k(t), return (f_p, f_s,
    f_n) in k[t] x k(t) x k(t) such that f = f_p + f_s + f_n is the
    canonical representation of f (f_p is a polynomial, f_s is reduced
    (has a special denominator), and f_n is simple (has a normal
    denominator).
    """
    ...

def hermite_reduce(a, d, DE) -> tuple[tuple[Any, Any], tuple[Any, Any], tuple[Any, Any]]:
    """
    Hermite Reduction - Mack's Linear Version.

    Given a derivation D on k(t) and f = a/d in k(t), returns g, h, r in
    k(t) such that f = Dg + h + r, h is simple, and r is reduced.

    """
    ...

def polynomial_reduce(p, DE) -> tuple[Any, Any]:
    """
    Polynomial Reduction.

    Explanation
    ===========

    Given a derivation D on k(t) and p in k[t] where t is a nonlinear
    monomial over k, return q, r in k[t] such that p = Dq  + r, and
    deg(r) < deg_t(Dt).
    """
    ...

def laurent_series(a, d, F, n, DE) -> tuple[Any, Any, list[Any]] | Literal[0]:
    """
    Contribution of ``F`` to the full partial fraction decomposition of A/D.

    Explanation
    ===========

    Given a field K of characteristic 0 and ``A``,``D``,``F`` in K[x] with D monic,
    nonzero, coprime with A, and ``F`` the factor of multiplicity n in the square-
    free factorization of D, return the principal parts of the Laurent series of
    A/D at all the zeros of ``F``.
    """
    ...

def recognize_derivative(a, d, DE, z=...) -> bool:
    """
    Compute the squarefree factorization of the denominator of f
    and for each Di the polynomial H in K[x] (see Theorem 2.7.1), using the
    LaurentSeries algorithm. Write Di = GiEi where Gj = gcd(Hn, Di) and
    gcd(Ei,Hn) = 1. Since the residues of f at the roots of Gj are all 0, and
    the residue of f at a root alpha of Ei is Hi(a) != 0, f is the derivative of a
    rational function if and only if Ei = 1 for each i, which is equivalent to
    Di | H[-1] for each i.
    """
    ...

def recognize_log_derivative(a, d, DE, z=...) -> bool:
    """
    There exists a v in K(x)* such that f = dv/v
    where f a rational function if and only if f can be written as f = A/D
    where D is squarefree,deg(A) < deg(D), gcd(A, D) = 1,
    and all the roots of the Rothstein-Trager resultant are integers. In that case,
    any of the Rothstein-Trager, Lazard-Rioboo-Trager or Czichowski algorithm
    produces u in K(x) such that du/dx = uf.
    """
    ...

def residue_reduce(a, d, DE, z=..., invert=...) -> tuple[list[Any], Literal[True]] | tuple[list[Any], bool]:
    """
    Lazard-Rioboo-Rothstein-Trager resultant reduction.

    Explanation
    ===========

    Given a derivation ``D`` on k(t) and f in k(t) simple, return g
    elementary over k(t) and a Boolean b in {True, False} such that f -
    Dg in k[t] if b == True or f + h and f + h - Dg do not have an
    elementary integral over k(t) for any h in k<t> (reduced) if b ==
    False.

    Returns (G, b), where G is a tuple of tuples of the form (s_i, S_i),
    such that g = Add(*[RootSum(s_i, lambda z: z*log(S_i(z, t))) for
    S_i, s_i in G]). f - Dg is the remaining integral, which is elementary
    only if b == True, and hence the integral of f is elementary only if
    b == True.

    f - Dg is not calculated in this function because that would require
    explicitly calculating the RootSum.  Use residue_reduce_derivation().
    """
    ...

def residue_reduce_to_basic(H, DE, z) -> int:
    """
    Converts the tuple returned by residue_reduce() into a Basic expression.
    """
    ...

def residue_reduce_derivation(H, DE, z):
    """
    Computes the derivation of an expression returned by residue_reduce().

    In general, this is a rational function in t, so this returns an
    as_expr() result.
    """
    ...

def integrate_primitive_polynomial(p, DE) -> tuple[Any, Any, Literal[True]] | tuple[Any, Any, Literal[False]]:
    """
    Integration of primitive polynomials.

    Explanation
    ===========

    Given a primitive monomial t over k, and ``p`` in k[t], return q in k[t],
    r in k, and a bool b in {True, False} such that r = p - Dq is in k if b is
    True, or r = p - Dq does not have an elementary integral over k(t) if b is
    False.
    """
    ...

def integrate_primitive(a, d, DE, z=...) -> tuple[Any, Any | Equality | Relational | Ne | NonElementaryIntegral, Literal[False]] | tuple[Any, Any | Equality | Relational | Ne | NonElementaryIntegral, bool]:
    """
    Integration of primitive functions.

    Explanation
    ===========

    Given a primitive monomial t over k and f in k(t), return g elementary over
    k(t), i in k(t), and b in {True, False} such that i = f - Dg is in k if b
    is True or i = f - Dg does not have an elementary integral over k(t) if b
    is False.

    This function returns a Basic expression for the first argument.  If b is
    True, the second argument is Basic expression in k to recursively integrate.
    If b is False, the second argument is an unevaluated Integral, which has
    been proven to be nonelementary.
    """
    ...

def integrate_hyperexponential_polynomial(p, DE, z) -> tuple[Any, Any, Literal[True]] | tuple[Any, Any, bool]:
    """
    Integration of hyperexponential polynomials.

    Explanation
    ===========

    Given a hyperexponential monomial t over k and ``p`` in k[t, 1/t], return q in
    k[t, 1/t] and a bool b in {True, False} such that p - Dq in k if b is True,
    or p - Dq does not have an elementary integral over k(t) if b is False.
    """
    ...

def integrate_hyperexponential(a, d, DE, z=..., conds=...) -> tuple[Any, Any | Equality | Relational | Ne | NonElementaryIntegral, Literal[False]] | tuple[Any, Any | Equality | Relational | Ne | NonElementaryIntegral, bool]:
    """
    Integration of hyperexponential functions.

    Explanation
    ===========

    Given a hyperexponential monomial t over k and f in k(t), return g
    elementary over k(t), i in k(t), and a bool b in {True, False} such that
    i = f - Dg is in k if b is True or i = f - Dg does not have an elementary
    integral over k(t) if b is False.

    This function returns a Basic expression for the first argument.  If b is
    True, the second argument is Basic expression in k to recursively integrate.
    If b is False, the second argument is an unevaluated Integral, which has
    been proven to be nonelementary.
    """
    ...

def integrate_hypertangent_polynomial(p, DE) -> tuple[Any, Any]:
    """
    Integration of hypertangent polynomials.

    Explanation
    ===========

    Given a differential field k such that sqrt(-1) is not in k, a
    hypertangent monomial t over k, and p in k[t], return q in k[t] and
    c in k such that p - Dq - c*D(t**2 + 1)/(t**1 + 1) is in k and p -
    Dq does not have an elementary integral over k(t) if Dc != 0.
    """
    ...

def integrate_nonlinear_no_specials(a, d, DE, z=...) -> tuple[Any, Literal[False]] | tuple[Any, bool]:
    """
    Integration of nonlinear monomials with no specials.

    Explanation
    ===========

    Given a nonlinear monomial t over k such that Sirr ({p in k[t] | p is
    special, monic, and irreducible}) is empty, and f in k(t), returns g
    elementary over k(t) and a Boolean b in {True, False} such that f - Dg is
    in k if b == True, or f - Dg does not have an elementary integral over k(t)
    if b == False.

    This function is applicable to all nonlinear extensions, but in the case
    where it returns b == False, it will only have proven that the integral of
    f - Dg is nonelementary if Sirr is empty.

    This function returns a Basic expression.
    """
    ...

class NonElementaryIntegral(Integral):
    """
    Represents a nonelementary Integral.

    Explanation
    ===========

    If the result of integrate() is an instance of this class, it is
    guaranteed to be nonelementary.  Note that integrate() by default will try
    to find any closed-form solution, even in terms of special functions which
    may themselves not be elementary.  To make integrate() only give
    elementary solutions, or, in the cases where it can prove the integral to
    be nonelementary, instances of this class, use integrate(risch=True).
    In this case, integrate() may raise NotImplementedError if it cannot make
    such a determination.

    integrate() uses the deterministic Risch algorithm to integrate elementary
    functions or prove that they have no elementary integral.  In some cases,
    this algorithm can split an integral into an elementary and nonelementary
    part, so that the result of integrate will be the sum of an elementary
    expression and a NonElementaryIntegral.

    Examples
    ========

    >>> from sympy import integrate, exp, log, Integral
    >>> from sympy.abc import x

    >>> a = integrate(exp(-x**2), x, risch=True)
    >>> print(a)
    Integral(exp(-x**2), x)
    >>> type(a)
    <class 'sympy.integrals.risch.NonElementaryIntegral'>

    >>> expr = (2*log(x)**2 - log(x) - x**2)/(log(x)**3 - x**2*log(x))
    >>> b = integrate(expr, x, risch=True)
    >>> print(b)
    -log(-x + log(x))/2 + log(x + log(x))/2 + Integral(1/log(x), x)
    >>> type(b.atoms(Integral).pop())
    <class 'sympy.integrals.risch.NonElementaryIntegral'>

    """
    ...


def risch_integrate(f, x, extension=..., handle_first=..., separate_integral=..., rewrite_complex=..., conds=...) -> tuple[Any, NonElementaryIntegral] | tuple[Any, Literal[0]] | None:
    r"""
    The Risch Integration Algorithm.

    Explanation
    ===========

    Only transcendental functions are supported.  Currently, only exponentials
    and logarithms are supported, but support for trigonometric functions is
    forthcoming.

    If this function returns an unevaluated Integral in the result, it means
    that it has proven that integral to be nonelementary.  Any errors will
    result in raising NotImplementedError.  The unevaluated Integral will be
    an instance of NonElementaryIntegral, a subclass of Integral.

    handle_first may be either 'exp' or 'log'.  This changes the order in
    which the extension is built, and may result in a different (but
    equivalent) solution (for an example of this, see issue 5109).  It is also
    possible that the integral may be computed with one but not the other,
    because not all cases have been implemented yet.  It defaults to 'log' so
    that the outer extension is exponential when possible, because more of the
    exponential case has been implemented.

    If ``separate_integral`` is ``True``, the result is returned as a tuple (ans, i),
    where the integral is ans + i, ans is elementary, and i is either a
    NonElementaryIntegral or 0.  This useful if you want to try further
    integrating the NonElementaryIntegral part using other algorithms to
    possibly get a solution in terms of special functions.  It is False by
    default.

    Examples
    ========

    >>> from sympy.integrals.risch import risch_integrate
    >>> from sympy import exp, log, pprint
    >>> from sympy.abc import x

    First, we try integrating exp(-x**2). Except for a constant factor of
    2/sqrt(pi), this is the famous error function.

    >>> pprint(risch_integrate(exp(-x**2), x))
      /
     |
     |    2
     |  -x
     | e    dx
     |
    /

    The unevaluated Integral in the result means that risch_integrate() has
    proven that exp(-x**2) does not have an elementary anti-derivative.

    In many cases, risch_integrate() can split out the elementary
    anti-derivative part from the nonelementary anti-derivative part.
    For example,

    >>> pprint(risch_integrate((2*log(x)**2 - log(x) - x**2)/(log(x)**3 -
    ... x**2*log(x)), x))
                                             /
                                            |
      log(-x + log(x))   log(x + log(x))    |   1
    - ---------------- + --------------- +  | ------ dx
             2                  2           | log(x)
                                            |
                                           /

    This means that it has proven that the integral of 1/log(x) is
    nonelementary.  This function is also known as the logarithmic integral,
    and is often denoted as Li(x).

    risch_integrate() currently only accepts purely transcendental functions
    with exponentials and logarithms, though note that this can include
    nested exponentials and logarithms, as well as exponentials with bases
    other than E.

    >>> pprint(risch_integrate(exp(x)*exp(exp(x)), x))
     / x\
     \e /
    e
    >>> pprint(risch_integrate(exp(exp(x)), x))
      /
     |
     |  / x\
     |  \e /
     | e     dx
     |
    /

    >>> pprint(risch_integrate(x*x**x*log(x) + x**x + x*x**x, x))
       x
    x*x
    >>> pprint(risch_integrate(x**x, x))
      /
     |
     |  x
     | x  dx
     |
    /

    >>> pprint(risch_integrate(-1/(x*log(x)*log(log(x))**2), x))
         1
    -----------
    log(log(x))

    """
    ...

