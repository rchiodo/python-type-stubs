from sympy.plotting.pygletplot.plot_object import PlotObject

class PlotMode(PlotObject):
    """
    Grandparent class for plotting
    modes. Serves as interface for
    registration, lookup, and init
    of modes.

    To create a new plot mode,
    inherit from PlotModeBase
    or one of its children, such
    as PlotSurface or PlotCurve.
    """
    intervals = ...
    aliases = ...
    is_default = ...
    def draw(self):
        ...
    
    _mode_alias_list = ...
    _mode_map = ...
    _mode_default_map = ...
    def __new__(cls, *args, **kwargs) -> PlotMode:
        """
        This is the function which interprets
        arguments given to Plot.__init__ and
        Plot.__setattr__. Returns an initialized
        instance of the appropriate child class.
        """
        ...
    
    _was_initialized = ...


def var_count_error(is_independent, is_plotting) -> str:
    """
    Used to format an error message which differs
    slightly in 4 places.
    """
    ...

