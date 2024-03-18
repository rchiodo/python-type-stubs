from typing import Any, Self
from sympy.liealgebras.cartan_type import Standard_Cartan

class TypeD(Standard_Cartan):
    def __new__(cls, n) -> Self:
        ...
    
    def dimension(self):
        """Dmension of the vector space V underlying the Lie algebra

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("D4")
        >>> c.dimension()
        4
        """
        ...
    
    def basic_root(self, i, j):
        """
        This is a method just to generate roots
        with a 1 iin the ith position and a -1
        in the jth position.

        """
        ...
    
    def simple_root(self, i):
        """
        Every lie algebra has a unique root system.
        Given a root system Q, there is a subset of the
        roots such that an element of Q is called a
        simple root if it cannot be written as the sum
        of two elements in Q.  If we let D denote the
        set of simple roots, then it is clear that every
        element of Q can be written as a linear combination
        of elements of D with all coefficients non-negative.

        In D_n, the first n-1 simple roots are the same as
        the roots in A_(n-1) (a 1 in the ith position, a -1
        in the (i+1)th position, and zeroes elsewhere).
        The nth simple root is the root in which there 1s in
        the nth and (n-1)th positions, and zeroes elsewhere.

        This method returns the ith simple root for the D series.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("D4")
        >>> c.simple_root(2)
        [0, 1, -1, 0]

        """
        ...
    
    def positive_roots(self) -> dict[Any, Any]:
        """
        This method generates all the positive roots of
        A_n.  This is half of all of the roots of D_n
        by multiplying all the positive roots by -1 we
        get the negative roots.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("A3")
        >>> c.positive_roots()
        {1: [1, -1, 0, 0], 2: [1, 0, -1, 0], 3: [1, 0, 0, -1], 4: [0, 1, -1, 0],
                5: [0, 1, 0, -1], 6: [0, 0, 1, -1]}
        """
        ...
    
    def roots(self):
        """
        Returns the total number of roots for D_n"
        """
        ...
    
    def cartan_matrix(self):
        """
        Returns the Cartan matrix for D_n.
        The Cartan matrix matrix for a Lie algebra is
        generated by assigning an ordering to the simple
        roots, (alpha[1], ...., alpha[l]).  Then the ijth
        entry of the Cartan matrix is (<alpha[i],alpha[j]>).

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType('D4')
        >>> c.cartan_matrix()
            Matrix([
            [ 2, -1,  0,  0],
            [-1,  2, -1, -1],
            [ 0, -1,  2,  0],
            [ 0, -1,  0,  2]])

        """
        ...
    
    def basis(self):
        """
        Returns the number of independent generators of D_n
        """
        ...
    
    def lie_algebra(self) -> str:
        """
        Returns the Lie algebra associated with D_n"
        """
        ...
    
    def dynkin_diagram(self):
        ...
    


