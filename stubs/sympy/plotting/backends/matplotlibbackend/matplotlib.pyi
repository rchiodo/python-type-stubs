import sympy.plotting.backends.base_backend as base_backend

class MatplotlibBackend(base_backend.Plot):
    """ This class implements the functionalities to use Matplotlib with SymPy
    plotting functions.
    """
    def __init__(self, *series, **kwargs) -> None:
        ...
    
    @staticmethod
    def get_segments(x, y, z=...):
        """ Convert two list of coordinates to a list of segments to be used
        with Matplotlib's :external:class:`~matplotlib.collections.LineCollection`.

        Parameters
        ==========
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates

            z : list
                List of z-coordinates for a 3D line.
        """
        ...
    
    def process_series(self) -> None:
        """
        Iterates over every ``Plot`` object and further calls
        _process_series()
        """
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def close(self) -> None:
        ...
    


