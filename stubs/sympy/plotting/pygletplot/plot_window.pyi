from sympy.plotting.pygletplot.managed_window import ManagedWindow

class PlotWindow(ManagedWindow):
    def __init__(self, plot, antialiasing=..., ortho=..., invert_mouse_zoom=..., linewidth=..., caption=..., **kwargs) -> None:
        """
        Named Arguments
        ===============

        antialiasing = True
            True OR False
        ortho = False
            True OR False
        invert_mouse_zoom = False
            True OR False
        """
        ...
    
    def setup(self) -> None:
        ...
    
    def on_resize(self, w, h) -> None:
        ...
    
    def update(self, dt) -> None:
        ...
    
    def draw(self) -> None:
        ...
    
    def update_caption(self, calc_verts_pos, calc_verts_len, calc_cverts_pos, calc_cverts_len) -> None:
        ...
    


