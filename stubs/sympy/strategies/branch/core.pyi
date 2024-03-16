""" Generic SymPy-Independent Strategies """
def identity(x) -> Generator[Any, Any, None]:
    ...

def exhaust(brule) -> Callable[..., Generator[Any, Any, None]]:
    """ Apply a branching rule repeatedly until it has no effect """
    ...

def onaction(brule, fn) -> Callable[..., Generator[Any, Any, None]]:
    ...

def debug(brule, file=...) -> Callable[..., Generator[Any, Any, None]]:
    """ Print the input and output expressions at each rule application """
    ...

def multiplex(*brules) -> Callable[..., Generator[Any, Any, None]]:
    """ Multiplex many branching rules into one """
    ...

def condition(cond, brule) -> Callable[..., Generator[Any, Any, None]]:
    """ Only apply branching rule if condition is true """
    ...

def sfilter(pred, brule) -> Callable[..., Generator[Any, Any, None]]:
    """ Yield only those results which satisfy the predicate """
    ...

def notempty(brule) -> Callable[..., Generator[Any, Any, None]]:
    ...

def do_one(*brules) -> Callable[..., Generator[Any, Any, None]]:
    """ Execute one of the branching rules """
    ...

def chain(*brules) -> Callable[..., Generator[Any, Any, None]]:
    """
    Compose a sequence of brules so that they apply to the expr sequentially
    """
    ...

def yieldify(rl) -> Callable[..., Generator[Any, Any, None]]:
    """ Turn a rule into a branching rule """
    ...

