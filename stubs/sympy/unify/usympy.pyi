""" SymPy interface to Unification engine

See sympy.unify for module level docstring
See sympy.unify.core for algorithmic docstring """
basic_new_legal = ...
eval_false_legal = ...
illegal = ...
def sympy_associative(op) -> bool:
    ...

def sympy_commutative(op) -> bool:
    ...

def is_associative(x) -> bool:
    ...

def is_commutative(x) -> bool | None:
    ...

def mk_matchtype(typ) -> Callable[..., bool]:
    ...

def deconstruct(s, variables=...) -> Variable | CondVariable | Basic | Compound:
    """ Turn a SymPy object into a Compound """
    ...

def construct(t) -> Any:
    """ Turn a Compound into a SymPy object """
    ...

def rebuild(s) -> Any | Basic:
    """ Rebuild a SymPy expression.

    This removes harm caused by Expr-Rules interactions.
    """
    ...

def unify(x, y, s=..., variables=..., **kwargs) -> Generator[dict[Any, Any], Any, None]:
    """ Structural unification of two expressions/patterns.

    Examples
    ========

    >>> from sympy.unify.usympy import unify
    >>> from sympy import Basic, S
    >>> from sympy.abc import x, y, z, p, q

    >>> next(unify(Basic(S(1), S(2)), Basic(S(1), x), variables=[x]))
    {x: 2}

    >>> expr = 2*x + y + z
    >>> pattern = 2*p + q
    >>> next(unify(expr, pattern, {}, variables=(p, q)))
    {p: x, q: y + z}

    Unification supports commutative and associative matching

    >>> expr = x + y + z
    >>> pattern = p + q
    >>> len(list(unify(expr, pattern, {}, variables=(p, q))))
    12

    Symbols not indicated to be variables are treated as literal,
    else they are wild-like and match anything in a sub-expression.

    >>> expr = x*y*z + 3
    >>> pattern = x*y + 3
    >>> next(unify(expr, pattern, {}, variables=[x, y]))
    {x: y, y: x*z}

    The x and y of the pattern above were in a Mul and matched factors
    in the Mul of expr. Here, a single symbol matches an entire term:

    >>> expr = x*y + 3
    >>> pattern = p + 3
    >>> next(unify(expr, pattern, {}, variables=[p]))
    {p: x*y}

    """
    ...

