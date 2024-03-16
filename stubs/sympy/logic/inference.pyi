"""Inference in propositional logic"""
def literal_symbol(literal) -> bool:
    """
    The symbol in this literal (without the negation).

    Examples
    ========

    >>> from sympy.abc import A
    >>> from sympy.logic.inference import literal_symbol
    >>> literal_symbol(A)
    A
    >>> literal_symbol(~A)
    A

    """
    ...

def satisfiable(expr, algorithm=..., all_models=..., minimal=..., use_lra_theory=...) -> dict[Any, Any] | Generator[bool, None, None] | Generator[Any | Literal[False], Any, None] | Generator[dict[Any, Any] | Literal[False], Any, None] | Generator[dict[Any, Any] | Literal[False], Any, NoReturn] | bool | None:
    """
    Check satisfiability of a propositional sentence.
    Returns a model when it succeeds.
    Returns {true: true} for trivially true expressions.

    On setting all_models to True, if given expr is satisfiable then
    returns a generator of models. However, if expr is unsatisfiable
    then returns a generator containing the single element False.

    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.inference import satisfiable
    >>> satisfiable(A & ~B)
    {A: True, B: False}
    >>> satisfiable(A & ~A)
    False
    >>> satisfiable(True)
    {True: True}
    >>> next(satisfiable(A & ~A, all_models=True))
    False
    >>> models = satisfiable((A >> B) & B, all_models=True)
    >>> next(models)
    {A: False, B: True}
    >>> next(models)
    {A: True, B: True}
    >>> def use_models(models):
    ...     for model in models:
    ...         if model:
    ...             # Do something with the model.
    ...             print(model)
    ...         else:
    ...             # Given expr is unsatisfiable.
    ...             print("UNSAT")
    >>> use_models(satisfiable(A >> ~A, all_models=True))
    {A: False}
    >>> use_models(satisfiable(A ^ A, all_models=True))
    UNSAT

    """
    ...

def valid(expr) -> bool:
    """
    Check validity of a propositional sentence.
    A valid propositional sentence is True under every assignment.

    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.inference import valid
    >>> valid(A | ~A)
    True
    >>> valid(A | B)
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Validity

    """
    ...

def pl_true(expr, model=..., deep=...) -> bool | None:
    """
    Returns whether the given assignment is a model or not.

    If the assignment does not specify the value for every proposition,
    this may return None to indicate 'not obvious'.

    Parameters
    ==========

    model : dict, optional, default: {}
        Mapping of symbols to boolean values to indicate assignment.
    deep: boolean, optional, default: False
        Gives the value of the expression under partial assignments
        correctly. May still return None to indicate 'not obvious'.


    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.inference import pl_true
    >>> pl_true( A & B, {A: True, B: True})
    True
    >>> pl_true(A & B, {A: False})
    False
    >>> pl_true(A & B, {A: True})
    >>> pl_true(A & B, {A: True}, deep=True)
    >>> pl_true(A >> (B >> A))
    >>> pl_true(A >> (B >> A), deep=True)
    True
    >>> pl_true(A & ~A)
    >>> pl_true(A & ~A, deep=True)
    False
    >>> pl_true(A & B & (~A | ~B), {A: True})
    >>> pl_true(A & B & (~A | ~B), {A: True}, deep=True)
    False

    """
    ...

def entails(expr, formula_set=...) -> bool:
    """
    Check whether the given expr_set entail an expr.
    If formula_set is empty then it returns the validity of expr.

    Examples
    ========

    >>> from sympy.abc import A, B, C
    >>> from sympy.logic.inference import entails
    >>> entails(A, [A >> B, B >> C])
    False
    >>> entails(C, [A >> B, B >> C, A])
    True
    >>> entails(A >> B)
    False
    >>> entails(A >> (B >> A))
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logical_consequence

    """
    ...

class KB:
    """Base class for all knowledge bases"""
    def __init__(self, sentence=...) -> None:
        ...
    
    def tell(self, sentence):
        ...
    
    def ask(self, query):
        ...
    
    def retract(self, sentence):
        ...
    
    @property
    def clauses(self) -> list[Any]:
        ...
    


class PropKB(KB):
    """A KB for Propositional Logic.  Inefficient, with no indexing."""
    def tell(self, sentence) -> None:
        """Add the sentence's clauses to the KB

        Examples
        ========

        >>> from sympy.logic.inference import PropKB
        >>> from sympy.abc import x, y
        >>> l = PropKB()
        >>> l.clauses
        []

        >>> l.tell(x | y)
        >>> l.clauses
        [x | y]

        >>> l.tell(y)
        >>> l.clauses
        [y, x | y]

        """
        ...
    
    def ask(self, query) -> bool:
        """Checks if the query is true given the set of clauses.

        Examples
        ========

        >>> from sympy.logic.inference import PropKB
        >>> from sympy.abc import x, y
        >>> l = PropKB()
        >>> l.tell(x & ~y)
        >>> l.ask(x)
        True
        >>> l.ask(y)
        False

        """
        ...
    
    def retract(self, sentence) -> None:
        """Remove the sentence's clauses from the KB

        Examples
        ========

        >>> from sympy.logic.inference import PropKB
        >>> from sympy.abc import x, y
        >>> l = PropKB()
        >>> l.clauses
        []

        >>> l.tell(x | y)
        >>> l.clauses
        [x | y]

        >>> l.retract(x | y)
        >>> l.clauses
        []

        """
        ...
    


