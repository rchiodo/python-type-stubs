from contextlib import contextmanager

"""Configuration utilities for polynomial manipulation algorithms. """
_default_config = ...
_current_config = ...
@contextmanager
def using(**kwargs) -> Generator[None, Any, None]:
    ...

def setup(key, value=...) -> None:
    """Assign a value to (or reset) a configuration item. """
    ...

def query(key):
    """Ask for a value of the given configuration item. """
    ...

def configure() -> None:
    """Initialized configuration of polys module. """
    ...

