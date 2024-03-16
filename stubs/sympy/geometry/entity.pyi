from typing import Any, Self
from sympy.core.basic import Basic
from sympy.core.evalf import EvalfMixin
from sympy.multipledispatch import dispatch
from sympy.sets import Set
from sympy.sets.sets import FiniteSet, Union

"""The definition of the base geometrical entity with attributes common to
all derived geometrical entities.

Contains
========

GeometryEntity
GeometricSet

Notes
=====

A GeometryEntity is any object that has special geometric properties.
A GeometrySet is a superclass of any GeometryEntity that can also
be viewed as a sympy.sets.Set.  In particular, points are the only
GeometryEntity not considered a Set.

Rn is a GeometrySet representing n-dimensional Euclidean space. R2 and
R3 are currently the only ambient spaces implemented.

"""
ordering_of_classes = ...
T = ...
class GeometryEntity(Basic, EvalfMixin):
    """The base class for all geometrical entities.

    This class does not represent any particular geometric entity, it only
    provides the implementation of some methods common to all subclasses.

    """
    __slots__: tuple[str, ...] = ...
    def __cmp__(self, other) -> int:
        """Comparison of two GeometryEntities."""
        ...
    
    def __contains__(self, other):
        """Subclasses should implement this method for anything more complex than equality."""
        ...
    
    def __getnewargs__(self) -> tuple[Basic, ...]:
        """Returns a tuple that will be passed to __new__ on unpickling."""
        ...
    
    def __ne__(self, o) -> bool:
        """Test inequality of two geometrical entities."""
        ...
    
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def __radd__(self, a):
        """Implementation of reverse add method."""
        ...
    
    def __rtruediv__(self, a):
        """Implementation of reverse division method."""
        ...
    
    def __repr__(self) -> str:
        """String representation of a GeometryEntity that can be evaluated
        by sympy."""
        ...
    
    def __rmul__(self, a):
        """Implementation of reverse multiplication method."""
        ...
    
    def __rsub__(self, a):
        """Implementation of reverse subtraction method."""
        ...
    
    def __str__(self) -> str:
        """String representation of a GeometryEntity."""
        ...
    
    @property
    def ambient_dimension(self):
        """What is the dimension of the space that the object is contained in?"""
        ...
    
    @property
    def bounds(self):
        """Return a tuple (xmin, ymin, xmax, ymax) representing the bounding
        rectangle for the geometric figure.

        """
        ...
    
    def encloses(self, o) -> bool:
        """
        Return True if o is inside (not on or outside) the boundaries of self.

        The object will be decomposed into Points and individual Entities need
        only define an encloses_point method for their class.

        See Also
        ========

        sympy.geometry.ellipse.Ellipse.encloses_point
        sympy.geometry.polygon.Polygon.encloses_point

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t  = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t2 = Polygon(*RegularPolygon(Point(0, 0), 2, 3).vertices)
        >>> t2.encloses(t)
        True
        >>> t.encloses(t2)
        False

        """
        ...
    
    def equals(self, o):
        ...
    
    def intersection(self, o):
        """
        Returns a list of all of the intersections of self with o.

        Notes
        =====

        An entity is not required to implement this method.

        If two different types of entities can intersect, the item with
        higher index in ordering_of_classes should implement
        intersections with anything having a lower index.

        See Also
        ========

        sympy.geometry.util.intersection

        """
        ...
    
    def is_similar(self, other):
        """Is this geometrical entity similar to another geometrical entity?

        Two entities are similar if a uniform scaling (enlarging or
        shrinking) of one of the entities will allow one to obtain the other.

        Notes
        =====

        This method is not intended to be used directly but rather
        through the `are_similar` function found in util.py.
        An entity is not required to implement this method.
        If two different types of entities can be similar, it is only
        required that one of them be able to determine this.

        See Also
        ========

        scale

        """
        ...
    
    def reflect(self, line) -> Self:
        """
        Reflects an object across a line.

        Parameters
        ==========

        line: Line

        Examples
        ========

        >>> from sympy import pi, sqrt, Line, RegularPolygon
        >>> l = Line((0, pi), slope=sqrt(2))
        >>> pent = RegularPolygon((1, 2), 1, 5)
        >>> rpent = pent.reflect(l)
        >>> rpent
        RegularPolygon(Point2D(-2*sqrt(2)*pi/3 - 1/3 + 4*sqrt(2)/3, 2/3 + 2*sqrt(2)/3 + 2*pi/3), -1, 5, -atan(2*sqrt(2)) + 3*pi/5)

        >>> from sympy import pi, Line, Circle, Point
        >>> l = Line((0, pi), slope=1)
        >>> circ = Circle(Point(0, 0), 5)
        >>> rcirc = circ.reflect(l)
        >>> rcirc
        Circle(Point2D(-pi, pi), -5)

        """
        ...
    
    def rotate(self, angle, pt=...) -> Self:
        """Rotate ``angle`` radians counterclockwise about Point ``pt``.

        The default pt is the origin, Point(0, 0)

        See Also
        ========

        scale, translate

        Examples
        ========

        >>> from sympy import Point, RegularPolygon, Polygon, pi
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t # vertex on x axis
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.rotate(pi/2) # vertex on y axis now
        Triangle(Point2D(0, 1), Point2D(-sqrt(3)/2, -1/2), Point2D(sqrt(3)/2, -1/2))

        """
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Self:
        """Scale the object by multiplying the x,y-coordinates by x and y.

        If pt is given, the scaling is done relative to that point; the
        object is shifted by -pt, scaled, and shifted by pt.

        See Also
        ========

        rotate, translate

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.scale(2)
        Triangle(Point2D(2, 0), Point2D(-1, sqrt(3)/2), Point2D(-1, -sqrt(3)/2))
        >>> t.scale(2, 2)
        Triangle(Point2D(2, 0), Point2D(-1, sqrt(3)), Point2D(-1, -sqrt(3)))

        """
        ...
    
    def translate(self, x=..., y=...) -> Self:
        """Shift the object by adding to the x,y-coordinates the values x and y.

        See Also
        ========

        rotate, scale

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.translate(2)
        Triangle(Point2D(3, 0), Point2D(3/2, sqrt(3)/2), Point2D(3/2, -sqrt(3)/2))
        >>> t.translate(2, 2)
        Triangle(Point2D(3, 2), Point2D(3/2, sqrt(3)/2 + 2), Point2D(3/2, 2 - sqrt(3)/2))

        """
        ...
    
    def parameter_value(self, other, t) -> dict[Any, Any]:
        """Return the parameter corresponding to the given point.
        Evaluating an arbitrary point of the entity at this parameter
        value will return the given point.

        Examples
        ========

        >>> from sympy import Line, Point
        >>> from sympy.abc import t
        >>> a = Point(0, 0)
        >>> b = Point(2, 2)
        >>> Line(a, b).parameter_value((1, 1), t)
        {t: 1/2}
        >>> Line(a, b).arbitrary_point(t).subs(_)
        Point2D(1, 1)
        """
        ...
    


class GeometrySet(GeometryEntity, Set):
    """Parent class of all GeometryEntity that are also Sets
    (compatible with sympy.sets)
    """
    __slots__ = ...


@dispatch(GeometrySet, Set)
def union_sets(self, o) -> FiniteSet | Union | None:
    """ Returns the union of self and o
    for use with sympy.sets.Set, if possible. """
    ...

@dispatch(GeometrySet, Set)
def intersection_sets(self, o) -> FiniteSet | Union | None:
    """ Returns a sympy.sets.Set of intersection objects,
    if possible. """
    ...

def translate(x, y):
    """Return the matrix to translate a 2-D point by x and y."""
    ...

def scale(x, y, pt=...):
    """Return the matrix to multiply a 2-D point's coordinates by x and y.

    If pt is given, the scaling is done relative to that point."""
    ...

def rotate(th):
    """Return the matrix to rotate a 2-D point about the origin by ``angle``.

    The angle is measured in radians. To Point a point about a point other
    then the origin, translate the Point, do the rotation, and
    translate it back:

    >>> from sympy.geometry.entity import rotate, translate
    >>> from sympy import Point, pi
    >>> rot_about_11 = translate(-1, -1)*rotate(pi/2)*translate(1, 1)
    >>> Point(1, 1).transform(rot_about_11)
    Point2D(1, 1)
    >>> Point(0, 0).transform(rot_about_11)
    Point2D(2, 0)
    """
    ...

