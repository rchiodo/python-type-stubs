from sympy.polys.domains.domain import Domain
from sympy.utilities import public

@public
class CompositeDomain(Domain):
    is_Composite = ...
    def inject(self, *symbols) -> Self:
        ...
    
    def drop(self, *symbols) -> Self:
        ...
    
    def set_domain(self, domain) -> Self:
        ...
    
    @property
    def is_Exact(self):
        ...
    
    def get_exact(self) -> Self:
        ...
    
    @property
    def has_CharacteristicZero(self):
        ...
    
    def characteristic(self):
        ...
    


