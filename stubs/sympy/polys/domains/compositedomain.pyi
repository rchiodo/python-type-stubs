from sympy.polys.domains.domain import Domain
from sympy.utilities import public

"""Implementation of :class:`CompositeDomain` class. """
@public
class CompositeDomain(Domain):
    """Base class for composite domains, e.g. ZZ[x], ZZ(X). """
    is_Composite = ...
    def inject(self, *symbols) -> Self:
        """Inject generators into this domain.  """
        ...
    
    def drop(self, *symbols) -> Self:
        """Drop generators from this domain. """
        ...
    
    def set_domain(self, domain) -> Self:
        """Set the ground domain of this domain. """
        ...
    
    @property
    def is_Exact(self):
        """Returns ``True`` if this domain is exact. """
        ...
    
    def get_exact(self) -> Self:
        """Returns an exact version of this domain. """
        ...
    
    @property
    def has_CharacteristicZero(self):
        ...
    
    def characteristic(self):
        ...
    


