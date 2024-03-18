from typing import Any, Callable, Generator

from sympy.core.numbers import Integer
from sympy.core.symbol import Symbol


class PlotInterval:
    """
    """
    def require_all_args(f) -> Callable[..., Any]:
        ...
    
    def __init__(self, *args) -> None:
        ...
    
    def get_v(self) -> Symbol | None:
        ...
    
    def set_v(self, v) -> None:
        ...
    
    def get_v_min(self) -> None:
        ...
    
    def set_v_min(self, v_min) -> None:
        ...
    
    def get_v_max(self) -> None:
        ...
    
    def set_v_max(self, v_max) -> None:
        ...
    
    def get_v_steps(self) -> Integer | None:
        ...
    
    def set_v_steps(self, v_steps) -> None:
        ...
    
    @require_all_args
    def get_v_len(self) -> Any:
        ...
    
    v = ...
    v_min = ...
    v_max = ...
    v_steps = ...
    v_len = ...
    def fill_from(self, b) -> None:
        ...
    
    @staticmethod
    def try_parse(*args) -> PlotInterval | None:
        """
        Returns a PlotInterval if args can be interpreted
        as such, otherwise None.
        """
        ...
    
    def __repr__(self) -> str:
        """
        A string representing the interval in class constructor form.
        """
        ...
    
    def __str__(self) -> str:
        """
        A string representing the interval in list form.
        """
        ...
    
    @require_all_args
    def assert_complete(self) -> None:
        ...
    
    @require_all_args
    def vrange(self) -> Generator[Any, Any, None]:
        """
        Yields v_steps+1 SymPy numbers ranging from
        v_min to v_max.
        """
        ...
    
    @require_all_args
    def vrange2(self) -> Generator[tuple[Any, Any], Any, None]:
        """
        Yields v_steps pairs of SymPy numbers ranging from
        (v_min, v_min + step) to (v_max - step, v_max).
        """
        ...
    
    def frange(self) -> Generator[float, Any, None]:
        ...
    


