import sympy.plotting.backends.base_backend as base_backend

class MatplotlibBackend(base_backend.Plot):
    def __init__(self, *series, **kwargs) -> None:
        ...
    
    @staticmethod
    def get_segments(x, y, z=...):
        ...
    
    def process_series(self) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def close(self) -> None:
        ...
    


