class ColorGradient:
    colors = ...
    intervals = ...
    def __init__(self, *args) -> None:
        ...
    
    def copy(self) -> ColorGradient:
        ...
    
    def __call__(self, r, g, b) -> tuple[Any, Any, Any]:
        ...
    


default_color_schemes = ...
class ColorScheme:
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __call__(self, x, y, z, u, v) -> None:
        ...
    
    def apply_to_curve(self, verts, u_set, set_len=..., inc_pos=...) -> list[Any]:
        """
        Apply this color scheme to a
        set of vertices over a single
        independent variable u.
        """
        ...
    
    def apply_to_surface(self, verts, u_set, v_set, set_len=..., inc_pos=...) -> list[Any]:
        """
        Apply this color scheme to a
        set of vertices over two
        independent variables u and v.
        """
        ...
    
    def str_base(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    


