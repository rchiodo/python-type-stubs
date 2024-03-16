from sympy.external.gmpy import GROUND_TYPES
from sympy.polys.matrices._dfm import DFM

"""
sympy.polys.matrices.dfm

Provides the :class:`DFM` class if ``GROUND_TYPES=flint'``. Otherwise, ``DFM``
is a placeholder class that raises NotImplementedError when instantiated.
"""
if GROUND_TYPES == "flint":
    ...
else:
    class DFM_dummy:
        """
        Placeholder class for DFM when python-flint is not installed.
        """
        def __init__(*args, **kwargs) -> None:
            ...
        
    
    
    DFM = ...
