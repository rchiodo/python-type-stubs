"""Symbolic primitives + unicode/ASCII abstraction for pretty.py"""
from typing import Any, LiteralString


unicode_warnings = ...
def U(name) -> str | None:
    """
    Get a unicode character by name or, None if not found.

    This exists because older versions of Python use older unicode databases.
    """
    ...

__all__ = ['greek_unicode', 'sub', 'sup', 'xsym', 'vobj', 'hobj', 'pretty_symbol', 'annotated', 'center_pad', 'center']
_use_unicode = ...
def pretty_use_unicode(flag=...) -> bool:
    """Set whether pretty-printer should use unicode by default"""
    ...

def pretty_try_use_unicode() -> None:
    """See if unicode output is available and leverage it if possible"""
    ...

def xstr(*args) -> str:
    ...

g = ...
G = ...
greek_letters = ...
greek_unicode = ...
b = ...
B = ...
bold_unicode = ...
gb = ...
GB = ...
greek_bold_letters = ...
greek_bold_unicode = ...
digit_2txt = ...
symb_2txt = ...
LSUB = ...
GSUB = ...
DSUB = ...
SSUB = ...
LSUP = ...
DSUP = ...
SSUP = ...
sub = ...
sup = ...
modifier_dict = ...
HUP = ...
CUP = ...
MID = ...
EXT = ...
HLO = ...
CLO = ...
TOP = ...
BOT = ...
_xobj_unicode = ...
_xobj_ascii = ...
def xobj(symb, length):
    """Construct spatial object of given length.

    return: [] of equal-length strings
    """
    ...

def vobj(symb, height) -> str:
    """Construct vertical object of a given height

       see: xobj
    """
    ...

def hobj(symb, width) -> str:
    """Construct horizontal object of a given width

       see: xobj
    """
    ...

root = ...
VF = ...
frac = ...
_xsym = ...
def xsym(sym):
    """get symbology for a 'character'"""
    ...

atoms_table = ...
def pretty_atom(atom_name, default=..., printer=...) -> str | None:
    """return pretty representation of an atom"""
    ...

def pretty_symbol(symb_name, bold_name=...) -> str | None:
    """return pretty representation of a symbol"""
    ...

def annotated(letter):
    """
    Return a stylised drawing of the letter ``letter``, together with
    information on how to put annotations (super- and subscripts to the
    left and to the right) on it.

    See pretty.py functions _print_meijerg, _print_hyper on how to use this
    information.
    """
    ...

_remove_combining = ...
def is_combining(sym) -> bool:
    """Check whether symbol is a unicode modifier. """
    ...

def center_accent(string, accent):
    """
    Returns a string with accent inserted on the middle character. Useful to
    put combining accents on symbol names, including multi-character names.

    Parameters
    ==========

    string : string
        The string to place the accent in.
    accent : string
        The combining accent to insert

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Combining_character
    .. [2] https://en.wikipedia.org/wiki/Combining_Diacritical_Marks

    """
    ...

def line_width(line) -> int:
    """Unicode combining symbols (modifiers) are not ever displayed as
    separate symbols and thus should not be counted
    """
    ...

def is_subscriptable_in_unicode(subscript) -> bool:
    """
    Checks whether a string is subscriptable in unicode or not.

    Parameters
    ==========

    subscript: the string which needs to be checked

    Examples
    ========

    >>> from sympy.printing.pretty.pretty_symbology import is_subscriptable_in_unicode
    >>> is_subscriptable_in_unicode('abc')
    False
    >>> is_subscriptable_in_unicode('123')
    True

    """
    ...

def center_pad(wstring, wtarget, fillchar=...) -> tuple[Any, Any]:
    """
    Return the padding strings necessary to center a string of
    wstring characters wide in a wtarget wide space.

    The line_width wstring should always be less or equal to wtarget
    or else a ValueError will be raised.
    """
    ...

def center(string, width, fillchar=...) -> LiteralString:
    """Return a centered string of length determined by `line_width`
    that uses `fillchar` for padding.
    """
    ...

