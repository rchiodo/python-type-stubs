from sympy.utilities.decorator import doctest_depends_on

@doctest_depends_on(modules=('pyglet', ))
class PygletPlot:
    @doctest_depends_on(modules=('pyglet', ))
    def __init__(self, *fargs, **win_args) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def saveimage(self, outfile=..., format=..., size=...) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def __getitem__(self, i):
        ...
    
    def __setitem__(self, i, args) -> None:
        ...
    
    def __delitem__(self, i) -> None:
        ...
    
    def firstavailableindex(self) -> int:
        ...
    
    def append(self, *args) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self):
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
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
    


