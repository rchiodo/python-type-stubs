from sympy.plotting.backends.base_backend import Plot
from sympy.plotting.backends.matplotlibbackend.matplotlib import MatplotlibBackend
from sympy.plotting.backends.textbackend.text import TextBackend
from sympy.utilities.decorator import doctest_depends_on

@doctest_depends_on(modules=('matplotlib', ))
def plot_implicit(expr, x_var=..., y_var=..., adaptive=..., depth=..., n=..., line_color=..., show=..., **kwargs) -> MatplotlibBackend | TextBackend | Plot:
    ...

