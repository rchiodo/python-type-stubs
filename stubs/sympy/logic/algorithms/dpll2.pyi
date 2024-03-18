
from typing import Any, Generator, Literal


def dpll_satisfiable(expr, all_models=..., use_lra_theory=...) -> Generator[bool, None, None] | Generator[Any | Literal[False], Any, None] | dict[Any, Any] | Literal[False]:
    ...

class SATSolver:
    def __init__(self, clauses, variables, var_settings, symbols=..., heuristic=..., clause_learning=..., INTERVAL=..., lra_theory=...) -> None:
        ...
    


class Level:
    def __init__(self, decision, flipped=...) -> None:
        ...
    


