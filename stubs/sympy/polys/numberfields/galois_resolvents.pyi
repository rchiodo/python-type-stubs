r"""
Galois resolvents

Each of the functions in ``sympy.polys.numberfields.galoisgroups`` that
computes Galois groups for a particular degree $n$ uses resolvents. Given the
polynomial $T$ whose Galois group is to be computed, a resolvent is a
polynomial $R$ whose roots are defined as functions of the roots of $T$.

One way to compute the coefficients of $R$ is by approximating the roots of $T$
to sufficient precision. This module defines a :py:class:`~.Resolvent` class
that handles this job, determining the necessary precision, and computing $R$.

In some cases, the coefficients of $R$ are symmetric in the roots of $T$,
meaning they are equal to fixed functions of the coefficients of $T$. Therefore
another approach is to compute these functions once and for all, and record
them in a lookup table. This module defines code that can compute such tables.
The tables for polynomials $T$ of degrees 4 through 6, produced by this code,
are recorded in the resolvent_lookup.py module.

"""
class GaloisGroupException(Exception):
    ...


class ResolventException(GaloisGroupException):
    ...


class Resolvent:
    r"""
    If $G$ is a subgroup of the symmetric group $S_n$,
    $F$ a multivariate polynomial in $\mathbb{Z}[X_1, \ldots, X_n]$,
    $H$ the stabilizer of $F$ in $G$ (i.e. the permutations $\sigma$ such that
    $F(X_{\sigma(1)}, \ldots, X_{\sigma(n)}) = F(X_1, \ldots, X_n)$), and $s$
    a set of left coset representatives of $H$ in $G$, then the resolvent
    polynomial $R(Y)$ is the product over $\sigma \in s$ of
    $Y - F(X_{\sigma(1)}, \ldots, X_{\sigma(n)})$.

    For example, consider the resolvent for the form
    $$F = X_0 X_2 + X_1 X_3$$
    and the group $G = S_4$. In this case, the stabilizer $H$ is the dihedral
    group $D4 = < (0123), (02) >$, and a set of representatives of $G/H$ is
    $\{I, (01), (03)\}$. The resolvent can be constructed as follows:

    >>> from sympy.combinatorics.permutations import Permutation
    >>> from sympy.core.symbol import symbols
    >>> from sympy.polys.numberfields.galoisgroups import Resolvent
    >>> X = symbols('X0 X1 X2 X3')
    >>> F = X[0]*X[2] + X[1]*X[3]
    >>> s = [Permutation([0, 1, 2, 3]), Permutation([1, 0, 2, 3]),
    ... Permutation([3, 1, 2, 0])]
    >>> R = Resolvent(F, X, s)

    This resolvent has three roots, which are the conjugates of ``F`` under the
    three permutations in ``s``:

    >>> R.root_lambdas[0](*X)
    X0*X2 + X1*X3
    >>> R.root_lambdas[1](*X)
    X0*X3 + X1*X2
    >>> R.root_lambdas[2](*X)
    X0*X1 + X2*X3

    Resolvents are useful for computing Galois groups. Given a polynomial $T$
    of degree $n$, we will use a resolvent $R$ where $Gal(T) \leq G \leq S_n$.
    We will then want to substitute the roots of $T$ for the variables $X_i$
    in $R$, and study things like the discriminant of $R$, and the way $R$
    factors over $\mathbb{Q}$.

    From the symmetry in $R$'s construction, and since $Gal(T) \leq G$, we know
    from Galois theory that the coefficients of $R$ must lie in $\mathbb{Z}$.
    This allows us to compute the coefficients of $R$ by approximating the
    roots of $T$ to sufficient precision, plugging these values in for the
    variables $X_i$ in the coefficient expressions of $R$, and then simply
    rounding to the nearest integer.

    In order to determine a sufficient precision for the roots of $T$, this
    ``Resolvent`` class imposes certain requirements on the form ``F``. It
    could be possible to design a different ``Resolvent`` class, that made
    different precision estimates, and different assumptions about ``F``.

    ``F`` must be homogeneous, and all terms must have unit coefficient.
    Furthermore, if $r$ is the number of terms in ``F``, and $t$ the total
    degree, and if $m$ is the number of conjugates of ``F``, i.e. the number
    of permutations in ``s``, then we require that $m < r 2^t$. Again, it is
    not impossible to work with forms ``F`` that violate these assumptions, but
    this ``Resolvent`` class requires them.

    Since determining the integer coefficients of the resolvent for a given
    polynomial $T$ is one of the main problems this class solves, we take some
    time to explain the precision bounds it uses.

    The general problem is:
    Given a multivariate polynomial $P \in \mathbb{Z}[X_1, \ldots, X_n]$, and a
    bound $M \in \mathbb{R}_+$, compute an $\varepsilon > 0$ such that for any
    complex numbers $a_1, \ldots, a_n$ with $|a_i| < M$, if the $a_i$ are
    approximated to within an accuracy of $\varepsilon$ by $b_i$, that is,
    $|a_i - b_i| < \varepsilon$ for $i = 1, \ldots, n$, then
    $|P(a_1, \ldots, a_n) - P(b_1, \ldots, b_n)| < 1/2$. In other words, if it
    is known that $P(a_1, \ldots, a_n) = c$ for some $c \in \mathbb{Z}$, then
    $P(b_1, \ldots, b_n)$ can be rounded to the nearest integer in order to
    determine $c$.

    To derive our error bound, consider the monomial $xyz$. Defining
    $d_i = b_i - a_i$, our error is
    $|(a_1 + d_1)(a_2 + d_2)(a_3 + d_3) - a_1 a_2 a_3|$, which is bounded
    above by $|(M + \varepsilon)^3 - M^3|$. Passing to a general monomial of
    total degree $t$, this expression is bounded by
    $M^{t-1}\varepsilon(t + 2^t\varepsilon/M)$ provided $\varepsilon < M$,
    and by $(t+1)M^{t-1}\varepsilon$ provided $\varepsilon < M/2^t$.
    But since our goal is to make the error less than $1/2$, we will choose
    $\varepsilon < 1/(2(t+1)M^{t-1})$, which implies the condition that
    $\varepsilon < M/2^t$, as long as $M \geq 2$.

    Passing from the general monomial to the general polynomial is easy, by
    scaling and summing error bounds.

    In our specific case, we are given a homogeneous polynomial $F$ of
    $r$ terms and total degree $t$, all of whose coefficients are $\pm 1$. We
    are given the $m$ permutations that make the conjugates of $F$, and
    we want to bound the error in the coefficients of the monic polynomial
    $R(Y)$ having $F$ and its conjugates as roots (i.e. the resolvent).

    For $j$ from $1$ to $m$, the coefficient of $Y^{m-j}$ in $R(Y)$ is the
    $j$th elementary symmetric polynomial in the conjugates of $F$. This sums
    the products of these conjugates, taken $j$ at a time, in all possible
    combinations. There are $\binom{m}{j}$ such combinations, and each product
    of $j$ conjugates of $F$ expands to a sum of $r^j$ terms, each of unit
    coefficient, and total degree $jt$. An error bound for the $j$th coeff of
    $R$ is therefore
    $$\binom{m}{j} r^j (jt + 1) M^{jt - 1} \varepsilon$$
    When our goal is to evaluate all the coefficients of $R$, we will want to
    use the maximum of these error bounds. It is clear that this bound is
    strictly increasing for $j$ up to the ceiling of $m/2$. After that point,
    the first factor $\binom{m}{j}$ begins to decrease, while the others
    continue to increase. However, the binomial coefficient never falls by more
    than a factor of $1/m$ at a time, so our assumptions that $M \geq 2$ and
    $m < r 2^t$ are enough to tell us that the constant coefficient of $R$,
    i.e. that where $j = m$, has the largest error bound. Therefore we can use
    $$r^m (mt + 1) M^{mt - 1} \varepsilon$$
    as our error bound for all the coefficients.

    Note that this bound is also (more than) adequate to determine whether any
    of the roots of $R$ is an integer. Each of these roots is a single
    conjugate of $F$, which contains less error than the trace, i.e. the
    coefficient of $Y^{m - 1}$. By rounding the roots of $R$ to the nearest
    integers, we therefore get all the candidates for integer roots of $R$. By
    plugging these candidates into $R$, we can check whether any of them
    actually is a root.

    Note: We take the definition of resolvent from Cohen, but the error bound
    is ours.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.
       (Def 6.3.2)

    """
    def __init__(self, F, X, s) -> None:
        r"""
        Parameters
        ==========

        F : :py:class:`~.Expr`
            polynomial in the symbols in *X*
        X : list of :py:class:`~.Symbol`
        s : list of :py:class:`~.Permutation`
            representing the cosets of the stabilizer of *F* in
            some subgroup $G$ of $S_n$, where $n$ is the length of *X*.
        """
        ...
    
    def get_prec(self, M, target=...) -> int | Any:
        r"""
        For a given upper bound *M* on the magnitude of the complex numbers to
        be plugged in for this resolvent's symbols, compute a sufficient
        precision for evaluating those complex numbers, such that the
        coefficients, or the integer roots, of the resolvent can be determined.

        Parameters
        ==========

        M : real number
            Upper bound on magnitude of the complex numbers to be plugged in.

        target : str, 'coeffs' or 'roots', default='coeffs'
            Name the task for which a sufficient precision is desired.
            This is either determining the coefficients of the resolvent
            ('coeffs') or determining its possible integer roots ('roots').
            The latter may require significantly lower precision.

        Returns
        =======

        int $m$
            such that $2^{-m}$ is a sufficient upper bound on the
            error in approximating the complex numbers to be plugged in.

        """
        ...
    
    def approximate_roots_of_poly(self, T, target=...) -> list[Any]:
        """
        Approximate the roots of a given polynomial *T* to sufficient precision
        in order to evaluate this resolvent's coefficients, or determine
        whether the resolvent has an integer root.

        Parameters
        ==========

        T : :py:class:`~.Poly`

        target : str, 'coeffs' or 'roots', default='coeffs'
            Set the approximation precision to be sufficient for the desired
            task, which is either determining the coefficients of the resolvent
            ('coeffs') or determining its possible integer roots ('roots').
            The latter may require significantly lower precision.

        Returns
        =======

        list of elements of :ref:`CC`

        """
        ...
    
    @staticmethod
    def round_mpf(a) -> int | Any:
        ...
    
    def round_roots_to_integers_for_poly(self, T) -> dict[int, int | Any]:
        """
        For a given polynomial *T*, round the roots of this resolvent to the
        nearest integers.

        Explanation
        ===========

        None of the integers returned by this method is guaranteed to be a
        root of the resolvent; however, if the resolvent has any integer roots
        (for the given polynomial *T*), then they must be among these.

        If the coefficients of the resolvent are also desired, then this method
        should not be used. Instead, use the ``eval_for_poly`` method. This
        method may be significantly faster than ``eval_for_poly``.

        Parameters
        ==========

        T : :py:class:`~.Poly`

        Returns
        =======

        dict
            Keys are the indices of those permutations in ``self.s`` such that
            the corresponding root did round to a rational integer.

            Values are :ref:`ZZ`.


        """
        ...
    
    def eval_for_poly(self, T, find_integer_root=...) -> tuple[list[Any], int | Any | None, int | None]:
        r"""
        Compute the integer values of the coefficients of this resolvent, when
        plugging in the roots of a given polynomial.

        Parameters
        ==========

        T : :py:class:`~.Poly`

        find_integer_root : ``bool``, default ``False``
            If ``True``, then also determine whether the resolvent has an
            integer root, and return the first one found, along with its
            index, i.e. the index of the permutation ``self.s[i]`` it
            corresponds to.

        Returns
        =======

        Tuple ``(R, a, i)``

            ``R`` is this resolvent as a dense univariate polynomial over
            :ref:`ZZ`, i.e. a list of :ref:`ZZ`.

            If *find_integer_root* was ``True``, then ``a`` and ``i`` are the
            first integer root found, and its index, if one exists.
            Otherwise ``a`` and ``i`` are both ``None``.

        """
        ...
    


def wrap(text, width=...) -> LiteralString | Literal['']:
    """Line wrap a polynomial expression. """
    ...

def s_vars(n) -> Any:
    """Form the symbols s1, s2, ..., sn to stand for elem. symm. polys. """
    ...

def sparse_symmetrize_resolvent_coeffs(F, X, s, verbose=...) -> tuple[list[Any], list[Any]]:
    """
    Compute the coefficients of a resolvent as functions of the coefficients of
    the associated polynomial.

    F must be a sparse polynomial.
    """
    ...

def define_resolvents() -> dict[tuple[Literal[4], Literal[0]] | tuple[Literal[4], Literal[1]] | tuple[Literal[5], Literal[1]] | tuple[Literal[6], Literal[1]] | tuple[Literal[6], Literal[2]], Any]:
    """Define all the resolvents for polys T of degree 4 through 6. """
    ...

def generate_lambda_lookup(verbose=..., trial_run=...) -> str:
    """
    Generate the whole lookup table of coeff lambdas, for all resolvents.
    """
    ...

def get_resolvent_by_lookup(T, number) -> list[Any]:
    """
    Use the lookup table, to return a resolvent (as dup) for a given
    polynomial *T*.

    Parameters
    ==========

    T : Poly
        The polynomial whose resolvent is needed

    number : int
        For some degrees, there are multiple resolvents.
        Use this to indicate which one you want.

    Returns
    =======

    dup

    """
    ...

if __name__ == "__main__":
    verbose = ...
    trial_run = ...
    table = ...
