from sympy.polys.domains.domainelement import DomainElement
from sympy.utilities import public
from mpmath.ctx_mp_python import PythonMPContext, _mpc, _mpf

"""Real and complex elements. """
@public
class RealElement(_mpf, DomainElement):
    """An element of a real domain. """
    __slots__ = ...
    _mpf_ = ...
    def parent(self):
        ...
    


@public
class ComplexElement(_mpc, DomainElement):
    """An element of a complex domain. """
    __slots__ = ...
    _mpc_ = ...
    def parent(self):
        ...
    


new = ...
@public
class MPContext(PythonMPContext):
    def __init__(ctx, prec=..., dps=..., tol=..., real=...) -> None:
        ...
    
    def make_tol(ctx) -> mpf:
        ...
    
    def to_rational(ctx, s, limit=...) -> tuple[int, Any | Literal[1]] | tuple[Any, Any]:
        ...
    
    def almosteq(ctx, s, t, rel_eps=..., abs_eps=...) -> Literal[True]:
        ...
    


