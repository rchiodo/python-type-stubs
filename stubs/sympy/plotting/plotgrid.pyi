class PlotGrid:
    """This class helps to plot subplots from already created SymPy plots
    in a single figure.

    Examples
    ========

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> from sympy import symbols
        >>> from sympy.plotting import plot, plot3d, PlotGrid
        >>> x, y = symbols('x, y')
        >>> p1 = plot(x, x**2, x**3, (x, -5, 5))
        >>> p2 = plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
        >>> p3 = plot(x**3, (x, -5, 5))
        >>> p4 = plot3d(x*y, (x, -5, 5), (y, -5, 5))

    Plotting vertically in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 1, p1, p2)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)

    Plotting horizontally in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(1, 3, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    Plotting in a grid form:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 2, p1, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[3]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    """
    def __init__(self, nrows, ncolumns, *args, show=..., size=..., **kwargs) -> None:
        """
        Parameters
        ==========

        nrows :
            The number of rows that should be in the grid of the
            required subplot.
        ncolumns :
            The number of columns that should be in the grid
            of the required subplot.

        nrows and ncolumns together define the required grid.

        Arguments
        =========

        A list of predefined plot objects entered in a row-wise sequence
        i.e. plot objects which are to be in the top row of the required
        grid are written first, then the second row objects and so on

        Keyword arguments
        =================

        show : Boolean
            The default value is set to ``True``. Set show to ``False`` and
            the function will not display the subplot. The returned instance
            of the ``PlotGrid`` class can then be used to save or display the
            plot by calling the ``save()`` and ``show()`` methods
            respectively.
        size : (float, float), optional
            A tuple in the form (width, height) in inches to specify the size of
            the overall figure. The default value is set to ``None``, meaning
            the size will be set by the default backend.
        """
        ...
    
    @property
    def fig(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


