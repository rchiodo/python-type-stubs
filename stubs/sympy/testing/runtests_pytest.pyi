import functools
import pathlib
from typing import List, Optional, Tuple

"""Backwards compatible functions for running tests from SymPy using pytest.

SymPy historically had its own testing framework that aimed to:
- be compatible with pytest;
- operate similarly (or identically) to pytest;
- not require any external dependencies;
- have all the functionality in one file only;
- have no magic, just import the test file and execute the test functions; and
- be portable.

To reduce the maintence burden of developing an independent testing framework
and to leverage the benefits of existing Python testing infrastructure, SymPy
now uses pytest (and various of its plugins) to run the test suite.

To maintain backwards compatibility with the legacy testing interface of SymPy,
which implemented functions that allowed users to run the tests on their
installed version of SymPy, the functions in this module are implemented to
match the existing API while thinly wrapping pytest.

These two key functions are `test` and `doctest`.

"""
TESTPATHS_DEFAULT = ...
BLACKLIST_DEFAULT = ...
class PytestPluginManager:
    """Module names for pytest plugins used by SymPy."""
    PYTEST: str = ...
    RANDOMLY: str = ...
    SPLIT: str = ...
    TIMEOUT: str = ...
    XDIST: str = ...
    @functools.cached_property
    def has_pytest(self) -> bool:
        ...
    
    @functools.cached_property
    def has_randomly(self) -> bool:
        ...
    
    @functools.cached_property
    def has_split(self) -> bool:
        ...
    
    @functools.cached_property
    def has_timeout(self) -> bool:
        ...
    
    @functools.cached_property
    def has_xdist(self) -> bool:
        ...
    


split_pattern = ...
@functools.lru_cache
def sympy_dir() -> pathlib.Path:
    """Returns the root SymPy directory."""
    ...

def update_args_with_rootdir(args: List[str]) -> List[str]:
    """Adds `--rootdir` and path to the args `list` passed to `pytest.main`.

    This is required to ensure that pytest is able to find the SymPy tests in
    instances where it gets confused determining the root directory, e.g. when
    running with Pyodide (e.g. `bin/test_pyodide.mjs`).

    """
    ...

def update_args_with_paths(paths: List[str], keywords: Optional[Tuple[str]], args: List[str]) -> List[str]:
    """Appends valid paths and flags to the args `list` passed to `pytest.main`.

    The are three different types of "path" that a user may pass to the `paths`
    positional arguments, all of which need to be handled slightly differently:

    1. Nothing is passed
        The paths to the `testpaths` defined in `pytest.ini` need to be appended
        to the arguments list.
    2. Full, valid paths are passed
        These paths need to be validated but can then be directly appended to
        the arguments list.
    3. Partial paths are passed.
        The `testpaths` defined in `pytest.ini` need to be recursed and any
        matches be appended to the arguments list.

    """
    ...

def make_absolute_path(partial_path: str) -> str:
    """Convert a partial path to an absolute path.

    A path such a `sympy/core` might be needed. However, absolute paths should
    be used in the arguments to pytest in all cases as it avoids errors that
    arise from nonexistent paths.

    This function assumes that partial_paths will be passed in such that they
    begin with the explicit `sympy` directory, i.e. `sympy/...`.

    """
    ...

def test(*paths, subprocess=..., rerun=..., **kwargs) -> bool | None:
    """Interface to run tests via pytest compatible with SymPy's test runner.

    Explanation
    ===========

    Note that a `pytest.ExitCode`, which is an `enum`, is returned. This is
    different to the legacy SymPy test runner which would return a `bool`. If
    all tests sucessfully pass the `pytest.ExitCode.OK` with value `0` is
    returned, whereas the legacy SymPy test runner would return `True`. In any
    other scenario, a non-zero `enum` value is returned, whereas the legacy
    SymPy test runner would return `False`. Users need to, therefore, be careful
    if treating the pytest exit codes as booleans because
    `bool(pytest.ExitCode.OK)` evaluates to `False`, the opposite of legacy
    behaviour.

    Examples
    ========

    >>> import sympy  # doctest: +SKIP

    Run one file:

    >>> sympy.test('sympy/core/tests/test_basic.py')  # doctest: +SKIP
    >>> sympy.test('_basic')  # doctest: +SKIP

    Run all tests in sympy/functions/ and some particular file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...            "sympy/functions")  # doctest: +SKIP

    Run all tests in sympy/core and sympy/utilities:

    >>> sympy.test("/core", "/util")  # doctest: +SKIP

    Run specific test from a file:

    >>> sympy.test("sympy/core/tests/test_basic.py",
    ...            kw="test_equality")  # doctest: +SKIP

    Run specific test from any file:

    >>> sympy.test(kw="subs")  # doctest: +SKIP

    Run the tests using the legacy SymPy runner:

    >>> sympy.test(use_sympy_runner=True)  # doctest: +SKIP

    Note that this option is slated for deprecation in the near future and is
    only currently provided to ensure users have an alternative option while the
    pytest-based runner receives real-world testing.

    Parameters
    ==========
    paths : first n positional arguments of strings
        Paths, both partial and absolute, describing which subset(s) of the test
        suite are to be run.
    subprocess : bool, default is True
        Legacy option, is currently ignored.
    rerun : int, default is 0
        Legacy option, is ignored.
    use_sympy_runner : bool or None, default is None
        Temporary option to invoke the legacy SymPy test runner instead of
        `pytest.main`. Will be removed in the near future.
    verbose : bool, default is False
        Sets the verbosity of the pytest output. Using `True` will add the
        `--verbose` option to the pytest call.
    tb : str, 'auto', 'long', 'short', 'line', 'native', or 'no'
        Sets the traceback print mode of pytest using the `--tb` option.
    kw : str
        Only run tests which match the given substring expression. An expression
        is a Python evaluatable expression where all names are substring-matched
        against test names and their parent classes. Example: -k 'test_method or
        test_other' matches all test functions and classes whose name contains
        'test_method' or 'test_other', while -k 'not test_method' matches those
        that don't contain 'test_method' in their names. -k 'not test_method and
        not test_other' will eliminate the matches. Additionally keywords are
        matched to classes and functions containing extra names in their
        'extra_keyword_matches' set, as well as functions which have names
        assigned directly to them. The matching is case-insensitive.
    pdb : bool, default is False
        Start the interactive Python debugger on errors or `KeyboardInterrupt`.
    colors : bool, default is True
        Color terminal output.
    force_colors : bool, default is False
        Legacy option, is ignored.
    sort : bool, default is True
        Run the tests in sorted order. pytest uses a sorted test order by
        default. Requires pytest-randomly.
    seed : int
        Seed to use for random number generation. Requires pytest-randomly.
    timeout : int, default is 0
        Timeout in seconds before dumping the stacks. 0 means no timeout.
        Requires pytest-timeout.
    fail_on_timeout : bool, default is False
        Legacy option, is currently ignored.
    slow : bool, default is False
        Run the subset of tests marked as `slow`.
    enhance_asserts : bool, default is False
        Legacy option, is currently ignored.
    split : string in form `<SPLIT>/<GROUPS>` or None, default is None
        Used to split the tests up. As an example, if `split='2/3' is used then
        only the middle third of tests are run. Requires pytest-split.
    time_balance : bool, default is True
        Legacy option, is currently ignored.
    blacklist : iterable of test paths as strings, default is BLACKLIST_DEFAULT
        Blacklisted test paths are ignored using the `--ignore` option. Paths
        may be partial or absolute. If partial then they are matched against
        all paths in the pytest tests path.
    parallel : bool, default is False
        Parallelize the test running using pytest-xdist. If `True` then pytest
        will automatically detect the number of CPU cores available and use them
        all. Requires pytest-xdist.
    store_durations : bool, False
        Store test durations into the file `.test_durations`. The is used by
        `pytest-split` to help determine more even splits when more than one
        test group is being used. Requires pytest-split.

    """
    ...

def doctest():
    """Interface to run doctests via pytest compatible with SymPy's test runner.
    """
    ...

