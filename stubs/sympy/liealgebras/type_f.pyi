from typing import Any, Literal, Self
from sympy.core.numbers import Integer, Rational
from sympy.liealgebras.cartan_type import Standard_Cartan
from sympy.matrices import Matrix

class TypeF(Standard_Cartan):
    def __new__(cls, n) -> Self:
        ...
    
    def dimension(self) -> Literal[4]:
        """Dimension of the vector space V underlying the Lie algebra

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("F4")
        >>> c.dimension()
        4
        """
        ...
    
    def basic_root(self, i, j):
        """Generate roots with 1 in ith position and -1 in jth position

        """
        ...
    
    def simple_root(self, i) -> list[int] | list[Rational | Any | Integer] | None:
        """The ith simple root of F_4

        Every lie algebra has a unique root system.
        Given a root system Q, there is a subset of the
        roots such that an element of Q is called a
        simple root if it cannot be written as the sum
        of two elements in Q.  If we let D denote the
        set of simple roots, then it is clear that every
        element of Q can be written as a linear combination
        of elements of D with all coefficients non-negative.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("F4")
        >>> c.simple_root(3)
        [0, 0, 0, 1]

        """
        ...
    
    def positive_roots(self) -> dict[Any, Any]:
        """Generate all the positive roots of A_n

        This is half of all of the roots of F_4; by multiplying all the
        positive roots by -1 we get the negative roots.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("A3")
        >>> c.positive_roots()
        {1: [1, -1, 0, 0], 2: [1, 0, -1, 0], 3: [1, 0, 0, -1], 4: [0, 1, -1, 0],
                5: [0, 1, 0, -1], 6: [0, 0, 1, -1]}

        """
        ...
    
    def roots(self) -> Literal[48]:
        """
        Returns the total number of roots for F_4
        """
        ...
    
    def cartan_matrix(self) -> Matrix:
        """The Cartan matrix for F_4

        The Cartan matrix matrix for a Lie algebra is
        generated by assigning an ordering to the simple
        roots, (alpha[1], ...., alpha[l]).  Then the ijth
        entry of the Cartan matrix is (<alpha[i],alpha[j]>).

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType('A4')
        >>> c.cartan_matrix()
        Matrix([
        [ 2, -1,  0,  0],
        [-1,  2, -1,  0],
        [ 0, -1,  2, -1],
        [ 0,  0, -1,  2]])
        """
        ...
    
    def basis(self) -> Literal[52]:
        """
        Returns the number of independent generators of F_4
        """
        ...
    
    def dynkin_diagram(self) -> str:
        ...
    


