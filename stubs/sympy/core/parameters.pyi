from contextlib import contextmanager
from threading import local
from typing import Any, Generator

class _global_parameters(local):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __setattr__(self, name, value) -> None:
        ...
    


global_parameters = ...
class evaluate:
    def __init__(self, x) -> None:
        ...
    
    def __enter__(self) -> None:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...
    


@contextmanager
def distribute(x) -> Generator[None, Any, None]:
    ...

