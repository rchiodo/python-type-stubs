
__all__ = ["lex", "grlex", "grevlex", "ilex", "igrlex", "igrevlex"]
from typing import Any, Callable


class MonomialOrder:
    alias: str | None = ...
    is_global: bool | None = ...
    is_default = ...
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, monomial):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class LexOrder(MonomialOrder):
    alias = ...
    is_global = ...
    is_default = ...
    def __call__(self, monomial):
        ...
    


class GradedLexOrder(MonomialOrder):
    alias = ...
    is_global = ...
    def __call__(self, monomial) -> tuple[int, Any]:
        ...
    


class ReversedGradedLexOrder(MonomialOrder):
    alias = ...
    is_global = ...
    def __call__(self, monomial) -> tuple[int, tuple[Any, ...]]:
        ...
    


class ProductOrder(MonomialOrder):
    def __init__(self, *args) -> None:
        ...
    
    def __call__(self, monomial) -> tuple[Any, ...]:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @property
    def is_global(self) -> bool | None:
        ...
    


class InverseOrder(MonomialOrder):
    def __init__(self, O) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, monomial) -> tuple[Any, ...]:
        ...
    
    @property
    def is_global(self) -> bool | None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


lex = ...
grlex = ...
grevlex = ...
ilex = ...
igrlex = ...
igrevlex = ...
_monomial_key = ...
def monomial_key(order=..., gens=...) -> Callable[..., Any] | LexOrder:
    ...

class _ItemGetter:
    def __init__(self, seq) -> None:
        ...
    
    def __call__(self, m) -> tuple[Any, ...]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


def build_product_order(arg, gens) -> ProductOrder:
    ...

