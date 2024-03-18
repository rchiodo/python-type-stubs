
from types import NotImplementedType
from typing import Any, Tuple
from sympy.plotting.backends.base_backend import Plot
from sympy.plotting.backends.matplotlibbackend.matplotlib import MatplotlibBackend
from sympy.plotting.backends.textbackend.text import TextBackend


def plot_factory(*args, **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

plot_backends = ...
def plot(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def plot_parametric(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def plot3d_parametric_line(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def plot3d(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def plot3d_parametric_surface(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def plot_contour(*args, show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

def check_arguments(args, expr_len, nb_of_free_symbols) -> list[Any] | list[Tuple | NotImplementedType] | None:
    ...

