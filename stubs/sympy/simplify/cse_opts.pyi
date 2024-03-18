""" Optimizations of the expression tree representation for better CSE
opportunities.
"""
from sympy.core.basic import Basic


def sub_pre(e) -> Basic:
    """ Replace y - x with -(x - y) if -1 can be extracted from y - x.
    """
    ...

def sub_post(e):
    """ Replace 1*-1*x with -x.
    """
    ...

