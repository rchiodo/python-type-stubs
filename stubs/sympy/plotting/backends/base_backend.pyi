from typing import Self


_show = ...
def unset_show() -> None:
    ...

class Plot:
    def __init__(self, *args, title=..., xlabel=..., ylabel=..., zlabel=..., aspect_ratio=..., xlim=..., ylim=..., axis_center=..., axis=..., xscale=..., yscale=..., legend=..., autoscale=..., margin=..., annotations=..., markers=..., rectangles=..., fill=..., backend=..., size=..., **kwargs) -> None:
        ...
    
    @property
    def backend(self) -> type[Self]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __getitem__(self, index):
        ...
    
    def __setitem__(self, index, *args) -> None:
        ...
    
    def __delitem__(self, index) -> None:
        ...
    
    def append(self, arg) -> None:
        ...
    
    def extend(self, arg) -> None:
        ...
    
    def show(self):
        ...
    
    def save(self, path):
        ...
    
    def close(self):
        ...
    
    @property
    def markers(self) -> None:
        ...
    
    @markers.setter
    def markers(self, v) -> None:
        ...
    
    @property
    def annotations(self) -> None:
        ...
    
    @annotations.setter
    def annotations(self, v) -> None:
        ...
    
    @property
    def rectangles(self) -> None:
        ...
    
    @rectangles.setter
    def rectangles(self, v) -> None:
        ...
    
    @property
    def fill(self) -> None:
        ...
    
    @fill.setter
    def fill(self, v) -> None:
        ...
    


