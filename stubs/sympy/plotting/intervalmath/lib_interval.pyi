""" The module contains implemented functions for interval arithmetic."""
def Abs(x) -> interval:
    ...

def exp(x) -> interval:
    """evaluates the exponential of an interval"""
    ...

def log(x) -> interval:
    """evaluates the natural logarithm of an interval"""
    ...

def log10(x) -> interval:
    """evaluates the logarithm to the base 10 of an interval"""
    ...

def atan(x) -> interval:
    """evaluates the tan inverse of an interval"""
    ...

def sin(x) -> interval:
    """evaluates the sine of an interval"""
    ...

def cos(x) -> interval:
    """Evaluates the cos of an interval"""
    ...

def tan(x) -> interval | NotImplementedType:
    """Evaluates the tan of an interval"""
    ...

def sqrt(x) -> interval:
    """Evaluates the square root of an interval"""
    ...

def imin(*args) -> type[NotImplementedError] | interval:
    """Evaluates the minimum of a list of intervals"""
    ...

def imax(*args) -> type[NotImplementedError] | interval:
    """Evaluates the maximum of a list of intervals"""
    ...

def sinh(x) -> interval:
    """Evaluates the hyperbolic sine of an interval"""
    ...

def cosh(x) -> interval:
    """Evaluates the hyperbolic cos of an interval"""
    ...

def tanh(x) -> interval:
    """Evaluates the hyperbolic tan of an interval"""
    ...

def asin(x) -> interval | None:
    """Evaluates the inverse sine of an interval"""
    ...

def acos(x) -> interval | None:
    """Evaluates the inverse cos of an interval"""
    ...

def ceil(x) -> interval | type[NotImplementedError]:
    """Evaluates the ceiling of an interval"""
    ...

def floor(x) -> interval | type[NotImplementedError]:
    """Evaluates the floor of an interval"""
    ...

def acosh(x) -> interval | type[NotImplementedError]:
    """Evaluates the inverse hyperbolic cosine of an interval"""
    ...

def asinh(x) -> interval | type[NotImplementedError]:
    """Evaluates the inverse hyperbolic sine of an interval"""
    ...

def atanh(x) -> interval | type[NotImplementedError]:
    """Evaluates the inverse hyperbolic tangent of an interval"""
    ...

def And(*args) -> tuple[bool | None, bool | None]:
    """Defines the three valued ``And`` behaviour for a 2-tuple of
     three valued logic values"""
    ...

def Or(*args) -> tuple[bool | None, bool | None]:
    """Defines the three valued ``Or`` behaviour for a 2-tuple of
     three valued logic values"""
    ...

