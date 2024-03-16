from sympy.utilities.decorator import doctest_depends_on

@doctest_depends_on(modules=('pyglet', ))
class PygletPlot:
    """
    Plot Examples
    =============

    See examples/advanced/pyglet_plotting.py for many more examples.

    >>> from sympy.plotting.pygletplot import PygletPlot as Plot
    >>> from sympy.abc import x, y, z

    >>> Plot(x*y**3-y*x**3)
    [0]: -x**3*y + x*y**3, 'mode=cartesian'

    >>> p = Plot()
    >>> p[1] = x*y
    >>> p[1].color = z, (0.4,0.4,0.9), (0.9,0.4,0.4)

    >>> p = Plot()
    >>> p[1] =  x**2+y**2
    >>> p[2] = -x**2-y**2


    Variable Intervals
    ==================

    The basic format is [var, min, max, steps], but the
    syntax is flexible and arguments left out are taken
    from the defaults for the current coordinate mode:

    >>> Plot(x**2) # implies [x,-5,5,100]
    [0]: x**2, 'mode=cartesian'
    >>> Plot(x**2, [], []) # [x,-1,1,40], [y,-1,1,40]
    [0]: x**2, 'mode=cartesian'
    >>> Plot(x**2-y**2, [100], [100]) # [x,-1,1,100], [y,-1,1,100]
    [0]: x**2 - y**2, 'mode=cartesian'
    >>> Plot(x**2, [x,-13,13,100])
    [0]: x**2, 'mode=cartesian'
    >>> Plot(x**2, [-13,13]) # [x,-13,13,100]
    [0]: x**2, 'mode=cartesian'
    >>> Plot(x**2, [x,-13,13]) # [x,-13,13,10]
    [0]: x**2, 'mode=cartesian'
    >>> Plot(1*x, [], [x], mode='cylindrical')
    ... # [unbound_theta,0,2*Pi,40], [x,-1,1,20]
    [0]: x, 'mode=cartesian'


    Coordinate Modes
    ================

    Plot supports several curvilinear coordinate modes, and
    they independent for each plotted function. You can specify
    a coordinate mode explicitly with the 'mode' named argument,
    but it can be automatically determined for Cartesian or
    parametric plots, and therefore must only be specified for
    polar, cylindrical, and spherical modes.

    Specifically, Plot(function arguments) and Plot[n] =
    (function arguments) will interpret your arguments as a
    Cartesian plot if you provide one function and a parametric
    plot if you provide two or three functions. Similarly, the
    arguments will be interpreted as a curve if one variable is
    used, and a surface if two are used.

    Supported mode names by number of variables:

    1: parametric, cartesian, polar
    2: parametric, cartesian, cylindrical = polar, spherical

    >>> Plot(1, mode='spherical')


    Calculator-like Interface
    =========================

    >>> p = Plot(visible=False)
    >>> f = x**2
    >>> p[1] = f
    >>> p[2] = f.diff(x)
    >>> p[3] = f.diff(x).diff(x)
    >>> p
    [1]: x**2, 'mode=cartesian'
    [2]: 2*x, 'mode=cartesian'
    [3]: 2, 'mode=cartesian'
    >>> p.show()
    >>> p.clear()
    >>> p
    <blank plot>
    >>> p[1] =  x**2+y**2
    >>> p[1].style = 'solid'
    >>> p[2] = -x**2-y**2
    >>> p[2].style = 'wireframe'
    >>> p[1].color = z, (0.4,0.4,0.9), (0.9,0.4,0.4)
    >>> p[1].style = 'both'
    >>> p[2].style = 'both'
    >>> p.close()


    Plot Window Keyboard Controls
    =============================

    Screen Rotation:
        X,Y axis      Arrow Keys, A,S,D,W, Numpad 4,6,8,2
        Z axis        Q,E, Numpad 7,9

    Model Rotation:
        Z axis        Z,C, Numpad 1,3

    Zoom:             R,F, PgUp,PgDn, Numpad +,-

    Reset Camera:     X, Numpad 5

    Camera Presets:
        XY            F1
        XZ            F2
        YZ            F3
        Perspective   F4

    Sensitivity Modifier: SHIFT

    Axes Toggle:
        Visible       F5
        Colors        F6

    Close Window:     ESCAPE

    =============================

    """
    @doctest_depends_on(modules=('pyglet', ))
    def __init__(self, *fargs, **win_args) -> None:
        """
        Positional Arguments
        ====================

        Any given positional arguments are used to
        initialize a plot function at index 1. In
        other words...

        >>> from sympy.plotting.pygletplot import PygletPlot as Plot
        >>> from sympy.abc import x
        >>> p = Plot(x**2, visible=False)

        ...is equivalent to...

        >>> p = Plot(visible=False)
        >>> p[1] = x**2

        Note that in earlier versions of the plotting
        module, you were able to specify multiple
        functions in the initializer. This functionality
        has been dropped in favor of better automatic
        plot plot_mode detection.


        Named Arguments
        ===============

        axes
            An option string of the form
            "key1=value1; key2 = value2" which
            can use the following options:

            style = ordinate
                none OR frame OR box OR ordinate

            stride = 0.25
                val OR (val_x, val_y, val_z)

            overlay = True (draw on top of plot)
                True OR False

            colored = False (False uses Black,
                             True uses colors
                             R,G,B = X,Y,Z)
                True OR False

            label_axes = False (display axis names
                                at endpoints)
                True OR False

        visible = True (show immediately
            True OR False


        The following named arguments are passed as
        arguments to window initialization:

        antialiasing = True
            True OR False

        ortho = False
            True OR False

        invert_mouse_zoom = False
            True OR False

        """
        ...
    
    def show(self) -> None:
        """
        Creates and displays a plot window, or activates it
        (gives it focus) if it has already been created.
        """
        ...
    
    def close(self) -> None:
        """
        Closes the plot window.
        """
        ...
    
    def saveimage(self, outfile=..., format=..., size=...) -> None:
        """
        Saves a screen capture of the plot window to an
        image file.

        If outfile is given, it can either be a path
        or a file object. Otherwise a png image will
        be saved to the current working directory.
        If the format is omitted, it is determined from
        the filename extension.
        """
        ...
    
    def clear(self) -> None:
        """
        Clears the function list of this plot.
        """
        ...
    
    def __getitem__(self, i):
        """
        Returns the function at position i in the
        function list.
        """
        ...
    
    def __setitem__(self, i, args) -> None:
        """
        Parses and adds a PlotMode to the function
        list.
        """
        ...
    
    def __delitem__(self, i) -> None:
        """
        Removes the function in the function list at
        position i.
        """
        ...
    
    def firstavailableindex(self) -> int:
        """
        Returns the first unused index in the function list.
        """
        ...
    
    def append(self, *args) -> None:
        """
        Parses and adds a PlotMode to the function
        list at the first available index.
        """
        ...
    
    def __len__(self) -> int:
        """
        Returns the number of functions in the function list.
        """
        ...
    
    def __iter__(self):
        """
        Allows iteration of the function list.
        """
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        """
        Returns a string containing a new-line separated
        list of the functions in the function list.
        """
        ...
    
    def adjust_all_bounds(self) -> None:
        ...
    
    def wait_for_calculations(self) -> None:
        ...
    


class ScreenShot:
    def __init__(self, plot) -> None:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def save(self, outfile=..., format=..., size=...) -> None:
        ...
    


