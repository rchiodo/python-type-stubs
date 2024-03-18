from ctypes import Array, c_float, c_int
from typing import Any, Literal


def get_model_matrix(array_type=..., glGetMethod=...) -> Array[c_float]:
    """
    Returns the current modelview matrix.
    """
    ...

def get_projection_matrix(array_type=..., glGetMethod=...) -> Array[c_float]:
    """
    Returns the current modelview matrix.
    """
    ...

def get_viewport() -> Array[c_int]:
    """
    Returns the current viewport.
    """
    ...

def get_direction_vectors() -> tuple[tuple[Any, Any, Any], tuple[Any, Any, Any], tuple[Any, Any, Any]]:
    ...

def get_view_direction_vectors() -> tuple[tuple[Any, Any, Any], tuple[Any, Any, Any], tuple[Any, Any, Any]]:
    ...

def get_basis_vectors() -> tuple[tuple[Literal[1], Literal[0], Literal[0]], tuple[Literal[0], Literal[1], Literal[0]], tuple[Literal[0], Literal[0], Literal[1]]]:
    ...

def screen_to_model(x, y, z) -> tuple[float, float, float]:
    ...

def model_to_screen(x, y, z) -> tuple[float, float, float]:
    ...

def vec_subs(a, b) -> tuple[Any, ...]:
    ...

def billboard_matrix() -> None:
    """
    Removes rotational components of
    current matrix so that primitives
    are always drawn facing the viewer.

    |1|0|0|x|
    |0|1|0|x|
    |0|0|1|x| (x means left unchanged)
    |x|x|x|x|
    """
    ...

def create_bounds() -> list[list[Any]]:
    ...

def update_bounds(b, v) -> None:
    ...

def interpolate(a_min, a_max, a_ratio):
    ...

def rinterpolate(a_min, a_max, a_value):
    ...

def interpolate_color(color1, color2, ratio) -> tuple[Any, ...]:
    ...

def scale_value(v, v_min, v_len):
    ...

def scale_value_list(flist) -> list[Any]:
    ...

def strided_range(r_min, r_max, stride, max_steps=...) -> list[Any]:
    ...

def parse_option_string(s) -> dict[Any, Any] | None:
    ...

def dot_product(v1, v2) -> int:
    ...

def vec_sub(v1, v2) -> tuple[Any, ...]:
    ...

def vec_mag(v) -> Any:
    ...

