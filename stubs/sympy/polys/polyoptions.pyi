from sympy.utilities import public

"""Options manager for :class:`~.Poly` and public API functions. """
__all__ = ["Options"]
class Option:
    """Base class for all kinds of options. """
    option: str | None = ...
    is_Flag = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    after: list[str] = ...
    before: list[str] = ...
    @classmethod
    def default(cls) -> None:
        ...
    
    @classmethod
    def preprocess(cls, option) -> None:
        ...
    
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Flag(Option):
    """Base class for all kinds of flags. """
    is_Flag = ...


class BooleanOption(Option):
    """An option that must have a boolean value or equivalent assigned. """
    @classmethod
    def preprocess(cls, value) -> bool:
        ...
    


class OptionType(type):
    """Base type for all options that does registers options. """
    def __init__(cls, *args, **kwargs) -> None:
        ...
    


@public
class Options(dict):
    """
    Options manager for polynomial manipulation module.

    Examples
    ========

    >>> from sympy.polys.polyoptions import Options
    >>> from sympy.polys.polyoptions import build_options

    >>> from sympy.abc import x, y, z

    >>> Options((x, y, z), {'domain': 'ZZ'})
    {'auto': False, 'domain': ZZ, 'gens': (x, y, z)}

    >>> build_options((x, y, z), {'domain': 'ZZ'})
    {'auto': False, 'domain': ZZ, 'gens': (x, y, z)}

    **Options**

    * Expand --- boolean option
    * Gens --- option
    * Wrt --- option
    * Sort --- option
    * Order --- option
    * Field --- boolean option
    * Greedy --- boolean option
    * Domain --- option
    * Split --- boolean option
    * Gaussian --- boolean option
    * Extension --- option
    * Modulus --- option
    * Symmetric --- boolean option
    * Strict --- boolean option

    **Flags**

    * Auto --- boolean flag
    * Frac --- boolean flag
    * Formal --- boolean flag
    * Polys --- boolean flag
    * Include --- boolean flag
    * All --- boolean flag
    * Gen --- flag
    * Series --- boolean flag

    """
    __order__ = ...
    __options__: dict[str, type[Option]] = ...
    def __init__(self, gens, args, flags=..., strict=...) -> None:
        ...
    
    def clone(self, updates=...) -> Self:
        """Clone ``self`` and update specified options. """
        ...
    
    def __setattr__(self, attr, value) -> None:
        ...
    
    @property
    def args(self) -> dict[Any, Any]:
        ...
    
    @property
    def options(self) -> dict[Any, Any]:
        ...
    
    @property
    def flags(self) -> dict[Any, Any]:
        ...
    


class Expand(BooleanOption, metaclass=OptionType):
    """``expand`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    @classmethod
    def default(cls) -> Literal[True]:
        ...
    


class Gens(Option, metaclass=OptionType):
    """``gens`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    @classmethod
    def default(cls) -> tuple[()]:
        ...
    
    @classmethod
    def preprocess(cls, gens) -> tuple[Basic, ...]:
        ...
    


class Wrt(Option, metaclass=OptionType):
    """``wrt`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    _re_split = ...
    @classmethod
    def preprocess(cls, wrt) -> list[str] | list[Any] | list[str | Any]:
        ...
    


class Sort(Option, metaclass=OptionType):
    """``sort`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    @classmethod
    def default(cls) -> list[Any]:
        ...
    
    @classmethod
    def preprocess(cls, sort) -> list[str]:
        ...
    


class Order(Option, metaclass=OptionType):
    """``order`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes: list[str] = ...
    @classmethod
    def default(cls) -> LexOrder:
        ...
    
    @classmethod
    def preprocess(cls, order) -> Callable[..., Any] | LexOrder:
        ...
    


class Field(BooleanOption, metaclass=OptionType):
    """``field`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...


class Greedy(BooleanOption, metaclass=OptionType):
    """``greedy`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...


class Composite(BooleanOption, metaclass=OptionType):
    """``composite`` option to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> None:
        ...
    
    requires: list[str] = ...
    excludes = ...


class Domain(Option, metaclass=OptionType):
    """``domain`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...
    after = ...
    _re_realfield = ...
    _re_complexfield = ...
    _re_finitefield = ...
    _re_polynomial = ...
    _re_fraction = ...
    _re_algebraic = ...
    @classmethod
    def preprocess(cls, domain) -> Any | GaussianIntegerRing | GaussianRationalField:
        ...
    
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Split(BooleanOption, metaclass=OptionType):
    """``split`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Gaussian(BooleanOption, metaclass=OptionType):
    """``gaussian`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Extension(Option, metaclass=OptionType):
    """``extension`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...
    @classmethod
    def preprocess(cls, extension) -> bool | set[Any] | None:
        ...
    
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Modulus(Option, metaclass=OptionType):
    """``modulus`` option to polynomial manipulation functions. """
    option = ...
    requires: list[str] = ...
    excludes = ...
    @classmethod
    def preprocess(cls, modulus) -> int:
        ...
    
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Symmetric(BooleanOption, metaclass=OptionType):
    """``symmetric`` option to polynomial manipulation functions. """
    option = ...
    requires = ...
    excludes = ...


class Strict(BooleanOption, metaclass=OptionType):
    """``strict`` option to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[True]:
        ...
    


class Auto(BooleanOption, Flag, metaclass=OptionType):
    """``auto`` flag to polynomial manipulation functions. """
    option = ...
    after = ...
    @classmethod
    def default(cls) -> Literal[True]:
        ...
    
    @classmethod
    def postprocess(cls, options) -> None:
        ...
    


class Frac(BooleanOption, Flag, metaclass=OptionType):
    """``auto`` option to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[False]:
        ...
    


class Formal(BooleanOption, Flag, metaclass=OptionType):
    """``formal`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[False]:
        ...
    


class Polys(BooleanOption, Flag, metaclass=OptionType):
    """``polys`` flag to polynomial manipulation functions. """
    option = ...


class Include(BooleanOption, Flag, metaclass=OptionType):
    """``include`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[False]:
        ...
    


class All(BooleanOption, Flag, metaclass=OptionType):
    """``all`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[False]:
        ...
    


class Gen(Flag, metaclass=OptionType):
    """``gen`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[0]:
        ...
    
    @classmethod
    def preprocess(cls, gen) -> Basic | int:
        ...
    


class Series(BooleanOption, Flag, metaclass=OptionType):
    """``series`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Literal[False]:
        ...
    


class Symbols(Flag, metaclass=OptionType):
    """``symbols`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def default(cls) -> Generator[Symbol, Any, NoReturn]:
        ...
    
    @classmethod
    def preprocess(cls, symbols):
        ...
    


class Method(Flag, metaclass=OptionType):
    """``method`` flag to polynomial manipulation functions. """
    option = ...
    @classmethod
    def preprocess(cls, method) -> str:
        ...
    


def build_options(gens, args=...) -> Any:
    """Construct options from keyword arguments or ... options. """
    ...

def allowed_flags(args, flags) -> None:
    """
    Allow specified flags to be used in the given context.

    Examples
    ========

    >>> from sympy.polys.polyoptions import allowed_flags
    >>> from sympy.polys.domains import ZZ

    >>> allowed_flags({'domain': ZZ}, [])

    >>> allowed_flags({'domain': ZZ, 'frac': True}, [])
    Traceback (most recent call last):
    ...
    FlagError: 'frac' flag is not allowed in this context

    >>> allowed_flags({'domain': ZZ, 'frac': True}, ['frac'])

    """
    ...

def set_defaults(options, **defaults) -> dict[Any, Any]:
    """Update options with default values. """
    ...

