from sympy.polys.domains.domain import Domain
from sympy.utilities import public

@public
class CharacteristicZero(Domain):
    has_CharacteristicZero = ...
    def characteristic(self) -> Literal[0]:
        ...
    


