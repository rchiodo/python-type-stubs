from sympy.external.gmpy import GROUND_TYPES
from sympy.polys.matrices._dfm import DFM

if GROUND_TYPES == "flint":
    ...
else:
    class DFM_dummy:
        def __init__(*args, **kwargs) -> None:
            ...
        
    
    
    DFM = ...
