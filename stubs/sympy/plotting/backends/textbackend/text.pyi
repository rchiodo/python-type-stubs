import sympy.plotting.backends.base_backend as base_backend

class TextBackend(base_backend.Plot):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    


