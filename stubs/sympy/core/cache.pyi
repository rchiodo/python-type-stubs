from typing import Callable

""" Caching facility for SymPy """
class _cache(list):
    """ List of cached functions """
    def print_cache(self) -> None:
        """print cache info"""
        ...
    
    def clear_cache(self) -> None:
        """clear cache content"""
        ...
    


CACHE = ...
print_cache = ...
clear_cache = ...
USE_CACHE = ...
scs = ...
if scs.lower() == 'none':
    SYMPY_CACHE_SIZE = ...
else:
    SYMPY_CACHE_SIZE = ...
if USE_CACHE == 'no':
    cacheit = ...
else:
    cacheit = ...
def cached_property(func) -> property:
    '''Decorator to cache property method'''
    ...

def lazy_function(module: str, name: str) -> Callable:
    """Create a lazy proxy for a function in a module.

    The module containing the function is not imported until the function is used.

    """
    class LazyFunctionMeta(type):
        ...
    
    
    class LazyFunction(metaclass=LazyFunctionMeta):
        ...
    
    

