
from typing import Any, Literal


def get_class(lookup_view) -> Any | str:
    ...

def get_mod_func(callback) -> tuple[Any, Literal['']] | tuple[Any, Any]:
    ...

