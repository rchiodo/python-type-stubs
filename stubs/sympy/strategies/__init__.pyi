from sympy.strategies import branch, rl, traverse
from sympy.strategies.rl import distribute, flatten, glom, rebuild, rm_id, sort, unpack
from sympy.strategies.util import new
from sympy.strategies.core import chain, condition, debug, do_one, exhaust, minimize, null_safe, tryit
from sympy.strategies.tools import canon, typed

""" Rewrite Rules

DISCLAIMER: This module is experimental. The interface is subject to change.

A rule is a function that transforms one expression into another

    Rule :: Expr -> Expr

A strategy is a function that says how a rule should be applied to a syntax
tree. In general strategies take rules and produce a new rule

    Strategy :: [Rules], Other-stuff -> Rule

This allows developers to separate a mathematical transformation from the
algorithmic details of applying that transformation. The goal is to separate
the work of mathematical programming from algorithmic programming.

Submodules

strategies.rl         - some fundamental rules
strategies.core       - generic non-SymPy specific strategies
strategies.traverse   - strategies that traverse a SymPy tree
strategies.tools      - some conglomerate strategies that do depend on SymPy
"""
__all__ = ['rl', 'traverse', 'rm_id', 'unpack', 'flatten', 'sort', 'glom', 'distribute', 'rebuild', 'new', 'condition', 'debug', 'chain', 'null_safe', 'do_one', 'exhaust', 'minimize', 'tryit', 'canon', 'typed', 'branch']
