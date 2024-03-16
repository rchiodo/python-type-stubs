from contextlib import contextmanager
from threading import local

class DotProdSimpState(local):
    def __init__(self) -> None:
        ...
    


_dotprodsimp_state = ...
@contextmanager
def dotprodsimp(x) -> Generator[None, Any, None]:
    ...

