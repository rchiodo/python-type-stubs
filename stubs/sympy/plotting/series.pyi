from sympy.printing.pycode import PythonCodePrinter

class IntervalMathPrinter(PythonCodePrinter):
    """A printer to be used inside `plot_implicit` when `adaptive=True`,
    in which case the interval arithmetic module is going to be used, which
    requires the following edits.
    """
    ...


class BaseSeries:
    """Base class for the data objects containing stuff to be plotted.

    Notes
    =====

    The backend should check if it supports the data series that is given.
    (e.g. TextBackend supports only LineOver1DRangeSeries).
    It is the backend responsibility to know how to use the class of
    data series that is given.

    Some data series classes are grouped (using a class attribute like is_2Dline)
    according to the api they present (based only on convention). The backend is
    not obliged to use that api (e.g. LineOver1DRangeSeries belongs to the
    is_2Dline group and presents the get_points method, but the
    TextBackend does not use the get_points method).

    BaseSeries
    """
    is_2Dline = ...
    is_3Dline = ...
    is_3Dsurface = ...
    is_contour = ...
    is_implicit = ...
    is_interactive = ...
    is_parametric = ...
    is_generic = ...
    is_vector = ...
    is_2Dvector = ...
    is_3Dvector = ...
    _N = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @property
    def expr(self) -> Tuple:
        """Return the expression (or expressions) of the series."""
        ...
    
    @expr.setter
    def expr(self, e) -> None:
        """Set the expression (or expressions) of the series."""
        ...
    
    @property
    def is_3D(self) -> bool:
        ...
    
    @property
    def is_line(self) -> bool:
        ...
    
    @property
    def line_color(self):
        ...
    
    @line_color.setter
    def line_color(self, val) -> None:
        ...
    
    @property
    def n(self) -> list[int]:
        """Returns a list [n1, n2, n3] of numbers of discratization points.
        """
        ...
    
    @n.setter
    def n(self, v) -> None:
        """Set the numbers of discretization points. ``v`` must be an int or
        a list.

        Let ``s`` be a series. Then:

        * to set the number of discretization points along the x direction (or
          first parameter): ``s.n = 10``
        * to set the number of discretization points along the x and y
          directions (or first and second parameters): ``s.n = [10, 15]``
        * to set the number of discretization points along the x, y and z
          directions: ``s.n = [10, 15, 20]``

        The following is highly unreccomended, because it prevents
        the execution of necessary code in order to keep updated data:
        ``s.n[1] = 15``
        """
        ...
    
    @property
    def params(self):
        """Get or set the current parameters dictionary.

        Parameters
        ==========

        p : dict

            * key: symbol associated to the parameter
            * val: the numeric value
        """
        ...
    
    @params.setter
    def params(self, p) -> None:
        ...
    
    @property
    def scales(self) -> list[Any]:
        ...
    
    @scales.setter
    def scales(self, v) -> None:
        ...
    
    @property
    def surface_color(self):
        ...
    
    @surface_color.setter
    def surface_color(self, val) -> None:
        ...
    
    @property
    def rendering_kw(self) -> dict[Any, Any]:
        ...
    
    @rendering_kw.setter
    def rendering_kw(self, kwargs) -> None:
        ...
    
    def eval_color_func(self, *args):
        """Evaluate the color function.

        Parameters
        ==========

        args : tuple
            Arguments to be passed to the coloring function. Can be coordinates
            or parameters or both.

        Notes
        =====

        The backend will request the data series to generate the numerical
        data. Depending on the data series, either the data series itself or
        the backend will eventually execute this function to generate the
        appropriate coloring value.
        """
        ...
    
    def get_data(self):
        """Compute and returns the numerical data.

        The number of parameters returned by this method depends on the
        specific instance. If ``s`` is the series, make sure to read
        ``help(s.get_data)`` to understand what it returns.
        """
        ...
    
    def get_label(self, use_latex=..., wrapper=...) -> str:
        """Return the label to be used to display the expression.

        Parameters
        ==========
        use_latex : bool
            If False, the string representation of the expression is returned.
            If True, the latex representation is returned.
        wrapper : str
            The backend might need the latex representation to be wrapped by
            some characters. Default to ``"$%s$"``.

        Returns
        =======
        label : str
        """
        ...
    
    @property
    def label(self) -> str:
        ...
    
    @label.setter
    def label(self, val) -> None:
        """Set the labels associated to this series."""
        ...
    
    @property
    def ranges(self) -> list[Any]:
        ...
    
    @ranges.setter
    def ranges(self, val) -> None:
        ...
    


class Line2DBaseSeries(BaseSeries):
    """A base class for 2D lines.

    - adding the label, steps and only_integers options
    - making is_2Dline true
    - defining get_segments and get_color_array
    """
    is_2Dline = ...
    _dim = ...
    _N = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def get_data(self) -> list[Any] | tuple[Any, Any, Any] | tuple[Any, Any] | tuple[Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any, Any] | tuple[Any, ...]:
        """Return coordinates for plotting the line.

        Returns
        =======

        x: np.ndarray
            x-coordinates

        y: np.ndarray
            y-coordinates

        z: np.ndarray (optional)
            z-coordinates in case of Parametric3DLineSeries,
            Parametric3DLineInteractiveSeries

        param : np.ndarray (optional)
            The parameter in case of Parametric2DLineSeries,
            Parametric3DLineSeries or AbsArgLineSeries (and their
            corresponding interactive series).
        """
        ...
    
    def get_segments(self):
        ...
    
    @property
    def var(self) -> None:
        ...
    
    @property
    def start(self) -> None:
        ...
    
    @property
    def end(self) -> None:
        ...
    
    @property
    def xscale(self):
        ...
    
    @xscale.setter
    def xscale(self, v) -> None:
        ...
    
    def get_color_array(self):
        ...
    


class List2DSeries(Line2DBaseSeries):
    """Representation for a line consisting of list of points."""
    def __init__(self, list_x, list_y, label=..., **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class LineOver1DRangeSeries(Line2DBaseSeries):
    """Representation for a line consisting of a SymPy expression over a range."""
    def __init__(self, expr, var_start_end, label=..., **kwargs) -> None:
        ...
    
    @property
    def nb_of_points(self) -> int:
        ...
    
    @nb_of_points.setter
    def nb_of_points(self, v) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_points(self) -> list[Any] | tuple[Any, Any]:
        """Return lists of coordinates for plotting. Depending on the
        ``adaptive`` option, this function will either use an adaptive algorithm
        or it will uniformly sample the expression over the provided range.

        This function is available for back-compatibility purposes. Consider
        using ``get_data()`` instead.

        Returns
        =======
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates
        """
        ...
    


class ParametricLineBaseSeries(Line2DBaseSeries):
    is_parametric = ...
    def get_label(self, use_latex=..., wrapper=...) -> str:
        ...
    
    def get_parameter_points(self):
        ...
    
    def get_points(self) -> list[Any]:
        """ Return lists of coordinates for plotting. Depending on the
        ``adaptive`` option, this function will either use an adaptive algorithm
        or it will uniformly sample the expression over the provided range.

        This function is available for back-compatibility purposes. Consider
        using ``get_data()`` instead.

        Returns
        =======
            x : list
                List of x-coordinates
            y : list
                List of y-coordinates
            z : list
                List of z-coordinates, only for 3D parametric line plot.
        """
        ...
    
    @property
    def nb_of_points(self) -> int:
        ...
    
    @nb_of_points.setter
    def nb_of_points(self, v) -> None:
        ...
    


class Parametric2DLineSeries(ParametricLineBaseSeries):
    """Representation for a line consisting of two parametric SymPy expressions
    over a range."""
    is_2Dline = ...
    def __init__(self, expr_x, expr_y, var_start_end, label=..., **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class Line3DBaseSeries(Line2DBaseSeries):
    """A base class for 3D lines.

    Most of the stuff is derived from Line2DBaseSeries."""
    is_2Dline = ...
    is_3Dline = ...
    _dim = ...
    def __init__(self) -> None:
        ...
    


class Parametric3DLineSeries(ParametricLineBaseSeries):
    """Representation for a 3D line consisting of three parametric SymPy
    expressions and a range."""
    is_2Dline = ...
    is_3Dline = ...
    def __init__(self, expr_x, expr_y, expr_z, var_start_end, label=..., **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_data(self) -> tuple[Any, Any, Any, Any]:
        ...
    


class SurfaceBaseSeries(BaseSeries):
    """A base class for 3D surfaces."""
    is_3Dsurface = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_color_array(self):
        ...
    


class SurfaceOver2DRangeSeries(SurfaceBaseSeries):
    """Representation for a 3D surface consisting of a SymPy expression and 2D
    range."""
    def __init__(self, expr, var_start_end_x, var_start_end_y, label=..., **kwargs) -> None:
        ...
    
    @property
    def var_x(self):
        ...
    
    @property
    def var_y(self):
        ...
    
    @property
    def start_x(self) -> float:
        ...
    
    @property
    def end_x(self) -> float:
        ...
    
    @property
    def start_y(self) -> float:
        ...
    
    @property
    def end_y(self) -> float:
        ...
    
    @property
    def nb_of_points_x(self) -> int:
        ...
    
    @nb_of_points_x.setter
    def nb_of_points_x(self, v) -> None:
        ...
    
    @property
    def nb_of_points_y(self) -> int:
        ...
    
    @nb_of_points_y.setter
    def nb_of_points_y(self, v) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_meshes(self) -> tuple[Any, Any] | tuple[Any, Any, Any] | tuple[Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any, Any] | tuple[Any, ...]:
        """Return the x,y,z coordinates for plotting the surface.
        This function is available for back-compatibility purposes. Consider
        using ``get_data()`` instead.
        """
        ...
    
    def get_data(self) -> tuple[Any, Any] | tuple[Any, Any, Any] | tuple[Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any, Any] | tuple[Any, ...]:
        """Return arrays of coordinates for plotting.

        Returns
        =======
        mesh_x : np.ndarray
            Discretized x-domain.
        mesh_y : np.ndarray
            Discretized y-domain.
        mesh_z : np.ndarray
            Results of the evaluation.
        """
        ...
    


class ParametricSurfaceSeries(SurfaceBaseSeries):
    """Representation for a 3D surface consisting of three parametric SymPy
    expressions and a range."""
    is_parametric = ...
    def __init__(self, expr_x, expr_y, expr_z, var_start_end_u, var_start_end_v, label=..., **kwargs) -> None:
        ...
    
    @property
    def var_u(self):
        ...
    
    @property
    def var_v(self):
        ...
    
    @property
    def start_u(self) -> float:
        ...
    
    @property
    def end_u(self) -> float:
        ...
    
    @property
    def start_v(self) -> float:
        ...
    
    @property
    def end_v(self) -> float:
        ...
    
    @property
    def nb_of_points_u(self) -> int:
        ...
    
    @nb_of_points_u.setter
    def nb_of_points_u(self, v) -> None:
        ...
    
    @property
    def nb_of_points_v(self) -> int:
        ...
    
    @nb_of_points_v.setter
    def nb_of_points_v(self, v) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_parameter_meshes(self) -> tuple[Any, ...] | tuple[()] | tuple[Any] | tuple[Any, Any] | tuple[Any, Any, Any]:
        ...
    
    def get_meshes(self) -> tuple[Any, ...] | tuple[Any, Any, Any]:
        """Return the x,y,z coordinates for plotting the surface.
        This function is available for back-compatibility purposes. Consider
        using ``get_data()`` instead.
        """
        ...
    
    def get_data(self) -> tuple[Any, Any] | tuple[Any, Any, Any] | tuple[Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any] | tuple[Any, Any, Any, Any, Any, Any] | tuple[Any, ...]:
        """Return arrays of coordinates for plotting.

        Returns
        =======
        x : np.ndarray [n2 x n1]
            x-coordinates.
        y : np.ndarray [n2 x n1]
            y-coordinates.
        z : np.ndarray [n2 x n1]
            z-coordinates.
        mesh_u : np.ndarray [n2 x n1]
            Discretized u range.
        mesh_v : np.ndarray [n2 x n1]
            Discretized v range.
        """
        ...
    


class ContourSeries(SurfaceOver2DRangeSeries):
    """Representation for a contour plot."""
    is_3Dsurface = ...
    is_contour = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class GenericDataSeries(BaseSeries):
    """Represents generic numerical data.

    Notes
    =====
    This class serves the purpose of back-compatibility with the "markers,
    annotations, fill, rectangles" keyword arguments that represent
    user-provided numerical data. In particular, it solves the problem of
    combining together two or more plot-objects with the ``extend`` or
    ``append`` methods: user-provided numerical data is also taken into
    consideration because it is stored in this series class.

    Also note that the current implementation is far from optimal, as each
    keyword argument is stored into an attribute in the ``Plot`` class, which
    requires a hard-coded if-statement in the ``MatplotlibBackend`` class.
    The implementation suggests that it is ok to add attributes and
    if-statements to provide more and more functionalities for user-provided
    numerical data (e.g. adding horizontal lines, or vertical lines, or bar
    plots, etc). However, in doing so one would reinvent the wheel: plotting
    libraries (like Matplotlib) already implements the necessary API.

    Instead of adding more keyword arguments and attributes, users interested
    in adding custom numerical data to a plot should retrieve the figure
    created by this plotting module. For example, this code:

    .. plot::
       :context: close-figs
       :include-source: True

       from sympy import Symbol, plot, cos
       x = Symbol("x")
       p = plot(cos(x), markers=[{"args": [[0, 1, 2], [0, 1, -1], "*"]}])

    Becomes:

    .. plot::
       :context: close-figs
       :include-source: True

       p = plot(cos(x), backend="matplotlib")
       fig, ax = p._backend.fig, p._backend.ax[0]
       ax.plot([0, 1, 2], [0, 1, -1], "*")
       fig

    Which is far better in terms of readibility. Also, it gives access to the
    full plotting library capabilities, without the need to reinvent the wheel.
    """
    is_generic = ...
    def __init__(self, tp, *args, **kwargs) -> None:
        ...
    
    def get_data(self) -> tuple[Any, ...]:
        ...
    


class ImplicitSeries(BaseSeries):
    """Representation for 2D Implicit plot."""
    is_implicit = ...
    use_cm = ...
    _N = ...
    def __init__(self, expr, var_start_end_x, var_start_end_y, label=..., **kwargs) -> None:
        ...
    
    @property
    def expr(self) -> BooleanFunction | Equality | Relational | Ne | GreaterThan | LessThan | None:
        ...
    
    @expr.setter
    def expr(self, expr) -> None:
        ...
    
    @property
    def line_color(self):
        ...
    
    @line_color.setter
    def line_color(self, v) -> None:
        ...
    
    color = ...
    def __str__(self) -> str:
        ...
    
    def get_data(self) -> tuple[list[Any], Literal['fill']] | tuple[Any, Any, Any, Literal['contour']] | tuple[Any, Any, Any, Literal['contourf']]:
        """Returns numerical data.

        Returns
        =======

        If the series is evaluated with the `adaptive=True` it returns:

        interval_list : list
            List of bounding rectangular intervals to be postprocessed and
            eventually used with Matplotlib's ``fill`` command.
        dummy : str
            A string containing ``"fill"``.

        Otherwise, it returns 2D numpy arrays to be used with Matplotlib's
        ``contour`` or ``contourf`` commands:

        x_array : np.ndarray
        y_array : np.ndarray
        z_array : np.ndarray
        plot_type : str
            A string specifying which plot command to use, ``"contour"``
            or ``"contourf"``.
        """
        ...
    
    def get_label(self, use_latex=..., wrapper=...) -> str:
        """Return the label to be used to display the expression.

        Parameters
        ==========
        use_latex : bool
            If False, the string representation of the expression is returned.
            If True, the latex representation is returned.
        wrapper : str
            The backend might need the latex representation to be wrapped by
            some characters. Default to ``"$%s$"``.

        Returns
        =======
        label : str
        """
        ...
    


def centers_of_segments(array):
    ...

def centers_of_faces(array):
    ...

def flat(x, y, z, eps=...):
    """Checks whether three points are almost collinear"""
    ...

