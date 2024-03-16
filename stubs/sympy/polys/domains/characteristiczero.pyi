from sympy.polys.domains.domain import Domain
from sympy.utilities import public

"""Implementation of :class:`CharacteristicZero` class. """
@public
class CharacteristicZero(Domain):
    """Domain that has infinite number of elements. """
    has_CharacteristicZero = ...
    def characteristic(self) -> Literal[0]:
        """Return the characteristic of this domain. """
        ...
    


