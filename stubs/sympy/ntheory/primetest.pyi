"""
Primality testing

"""
MERSENNE_PRIME_EXPONENTS = ...
def is_fermat_pseudoprime(n, a) -> bool:
    r"""Returns True if ``n`` is prime or is an odd composite integer that
    is coprime to ``a`` and satisfy the modular arithmetic congruence relation:

    .. math ::
        a^{n-1} \equiv 1 \pmod{n}

    (where mod refers to the modulo operation).

    Parameters
    ==========

    n : Integer
        ``n`` is a positive integer.
    a : Integer
        ``a`` is a positive integer.
        ``a`` and ``n`` should be relatively prime.

    Returns
    =======

    bool : If ``n`` is prime, it always returns ``True``.
           The composite number that returns ``True`` is called an Fermat pseudoprime.

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_fermat_pseudoprime
    >>> from sympy.ntheory.factor_ import isprime
    >>> for n in range(1, 1000):
    ...     if is_fermat_pseudoprime(n, 2) and not isprime(n):
    ...         print(n)
    341
    561
    645

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fermat_pseudoprime
    """
    ...

def is_euler_pseudoprime(n, a) -> bool:
    r"""Returns True if ``n`` is prime or is an odd composite integer that
    is coprime to ``a`` and satisfy the modular arithmetic congruence relation:

    .. math ::
        a^{(n-1)/2} \equiv \pm 1 \pmod{n}

    (where mod refers to the modulo operation).

    Parameters
    ==========

    n : Integer
        ``n`` is a positive integer.
    a : Integer
        ``a`` is a positive integer.
        ``a`` and ``n`` should be relatively prime.

    Returns
    =======

    bool : If ``n`` is prime, it always returns ``True``.
           The composite number that returns ``True`` is called an Euler pseudoprime.

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_euler_pseudoprime
    >>> from sympy.ntheory.factor_ import isprime
    >>> for n in range(1, 1000):
    ...     if is_euler_pseudoprime(n, 2) and not isprime(n):
    ...         print(n)
    341
    561

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler_pseudoprime
    """
    ...

def is_euler_jacobi_pseudoprime(n, a) -> bool:
    r"""Returns True if ``n`` is prime or is an odd composite integer that
    is coprime to ``a`` and satisfy the modular arithmetic congruence relation:

    .. math ::
        a^{(n-1)/2} \equiv \left(\frac{a}{n}\right) \pmod{n}

    (where mod refers to the modulo operation).

    Parameters
    ==========

    n : Integer
        ``n`` is a positive integer.
    a : Integer
        ``a`` is a positive integer.
        ``a`` and ``n`` should be relatively prime.

    Returns
    =======

    bool : If ``n`` is prime, it always returns ``True``.
           The composite number that returns ``True`` is called an Euler-Jacobi pseudoprime.

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_euler_jacobi_pseudoprime
    >>> from sympy.ntheory.factor_ import isprime
    >>> for n in range(1, 1000):
    ...     if is_euler_jacobi_pseudoprime(n, 2) and not isprime(n):
    ...         print(n)
    561

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler%E2%80%93Jacobi_pseudoprime
    """
    ...

def is_square(n, prep=...) -> bool:
    """Return True if n == a * a for some integer a, else False.
    If n is suspected of *not* being a square then this is a
    quick method of confirming that it is not.

    Examples
    ========

    >>> from sympy.ntheory.primetest import is_square
    >>> is_square(25)
    True
    >>> is_square(2)
    False

    References
    ==========

    .. [1]  https://mersenneforum.org/showpost.php?p=110896

    See Also
    ========
    sympy.core.intfunc.isqrt
    """
    ...

def mr(n, bases) -> bool:
    """Perform a Miller-Rabin strong pseudoprime test on n using a
    given list of bases/witnesses.

    References
    ==========

    .. [1] Richard Crandall & Carl Pomerance (2005), "Prime Numbers:
           A Computational Perspective", Springer, 2nd edition, 135-138

    A list of thresholds and the bases they require are here:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants

    Examples
    ========

    >>> from sympy.ntheory.primetest import mr
    >>> mr(1373651, [2, 3])
    False
    >>> mr(479001599, [31, 73])
    True

    """
    ...

def is_lucas_prp(n) -> bool:
    """Standard Lucas compositeness test with Selfridge parameters.  Returns
    False if n is definitely composite, and True if n is a Lucas probable
    prime.

    This is typically used in combination with the Miller-Rabin test.

    References
    ==========
    .. [1] Robert Baillie, Samuel S. Wagstaff, Lucas Pseudoprimes,
           Math. Comp. Vol 35, Number 152 (1980), pp. 1391-1417,
           https://doi.org/10.1090%2FS0025-5718-1980-0583518-6
           http://mpqs.free.fr/LucasPseudoprimes.pdf
    .. [2] OEIS A217120: Lucas Pseudoprimes
           https://oeis.org/A217120
    .. [3] https://en.wikipedia.org/wiki/Lucas_pseudoprime

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_lucas_prp
    >>> for i in range(10000):
    ...     if is_lucas_prp(i) and not isprime(i):
    ...         print(i)
    323
    377
    1159
    1829
    3827
    5459
    5777
    9071
    9179
    """
    ...

def is_strong_lucas_prp(n) -> bool:
    """Strong Lucas compositeness test with Selfridge parameters.  Returns
    False if n is definitely composite, and True if n is a strong Lucas
    probable prime.

    This is often used in combination with the Miller-Rabin test, and
    in particular, when combined with M-R base 2 creates the strong BPSW test.

    References
    ==========
    .. [1] Robert Baillie, Samuel S. Wagstaff, Lucas Pseudoprimes,
           Math. Comp. Vol 35, Number 152 (1980), pp. 1391-1417,
           https://doi.org/10.1090%2FS0025-5718-1980-0583518-6
           http://mpqs.free.fr/LucasPseudoprimes.pdf
    .. [2] OEIS A217255: Strong Lucas Pseudoprimes
           https://oeis.org/A217255
    .. [3] https://en.wikipedia.org/wiki/Lucas_pseudoprime
    .. [4] https://en.wikipedia.org/wiki/Baillie-PSW_primality_test

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_strong_lucas_prp
    >>> for i in range(20000):
    ...     if is_strong_lucas_prp(i) and not isprime(i):
    ...        print(i)
    5459
    5777
    10877
    16109
    18971
    """
    ...

def is_extra_strong_lucas_prp(n) -> bool:
    """Extra Strong Lucas compositeness test.  Returns False if n is
    definitely composite, and True if n is an "extra strong" Lucas probable
    prime.

    The parameters are selected using P = 3, Q = 1, then incrementing P until
    (D|n) == -1.  The test itself is as defined in [1]_, from the
    Mo and Jones preprint.  The parameter selection and test are the same as
    used in OEIS A217719, Perl's Math::Prime::Util, and the Lucas pseudoprime
    page on Wikipedia.

    It is 20-50% faster than the strong test.

    Because of the different parameters selected, there is no relationship
    between the strong Lucas pseudoprimes and extra strong Lucas pseudoprimes.
    In particular, one is not a subset of the other.

    References
    ==========
    .. [1] Jon Grantham, Frobenius Pseudoprimes,
           Math. Comp. Vol 70, Number 234 (2001), pp. 873-891,
           https://doi.org/10.1090%2FS0025-5718-00-01197-2
    .. [2] OEIS A217719: Extra Strong Lucas Pseudoprimes
           https://oeis.org/A217719
    .. [3] https://en.wikipedia.org/wiki/Lucas_pseudoprime

    Examples
    ========

    >>> from sympy.ntheory.primetest import isprime, is_extra_strong_lucas_prp
    >>> for i in range(20000):
    ...     if is_extra_strong_lucas_prp(i) and not isprime(i):
    ...        print(i)
    989
    3239
    5777
    10877
    """
    ...

def proth_test(n) -> bool | None:
    r""" Test if the Proth number `n = k2^m + 1` is prime. where k is a positive odd number and `2^m > k`.

    Parameters
    ==========

    n : Integer
        ``n`` is Proth number

    Returns
    =======

    bool : If ``True``, then ``n`` is the Proth prime

    Raises
    ======

    ValueError
        If ``n`` is not Proth number.

    Examples
    ========

    >>> from sympy.ntheory.primetest import proth_test
    >>> proth_test(41)
    True
    >>> proth_test(57)
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Proth_prime

    """
    ...

def is_mersenne_prime(n) -> bool:
    """Returns True if  ``n`` is a Mersenne prime, else False.

    A Mersenne prime is a prime number having the form `2^i - 1`.

    Examples
    ========

    >>> from sympy.ntheory.factor_ import is_mersenne_prime
    >>> is_mersenne_prime(6)
    False
    >>> is_mersenne_prime(127)
    True

    References
    ==========

    .. [1] https://mathworld.wolfram.com/MersennePrime.html

    """
    ...

def isprime(n) -> bool:
    """
    Test if n is a prime number (True) or not (False). For n < 2^64 the
    answer is definitive; larger n values have a small probability of actually
    being pseudoprimes.

    Negative numbers (e.g. -2) are not considered prime.

    The first step is looking for trivial factors, which if found enables
    a quick return.  Next, if the sieve is large enough, use bisection search
    on the sieve.  For small numbers, a set of deterministic Miller-Rabin
    tests are performed with bases that are known to have no counterexamples
    in their range.  Finally if the number is larger than 2^64, a strong
    BPSW test is performed.  While this is a probable prime test and we
    believe counterexamples exist, there are no known counterexamples.

    Examples
    ========

    >>> from sympy.ntheory import isprime
    >>> isprime(13)
    True
    >>> isprime(13.0)  # limited precision
    False
    >>> isprime(15)
    False

    Notes
    =====

    This routine is intended only for integer input, not numerical
    expressions which may represent numbers. Floats are also
    rejected as input because they represent numbers of limited
    precision. While it is tempting to permit 7.0 to represent an
    integer there are errors that may "pass silently" if this is
    allowed:

    >>> from sympy import Float, S
    >>> int(1e3) == 1e3 == 10**3
    True
    >>> int(1e23) == 1e23
    True
    >>> int(1e23) == 10**23
    False

    >>> near_int = 1 + S(1)/10**19
    >>> near_int == int(near_int)
    False
    >>> n = Float(near_int, 10)  # truncated by precision
    >>> n % 1 == 0
    True
    >>> n = Float(near_int, 20)
    >>> n % 1 == 0
    False

    See Also
    ========

    sympy.ntheory.generate.primerange : Generates all primes in a given range
    sympy.functions.combinatorial.numbers.primepi : Return the number of primes less than or equal to n
    sympy.ntheory.generate.prime : Return the nth prime

    References
    ==========
    .. [1] https://en.wikipedia.org/wiki/Strong_pseudoprime
    .. [2] Robert Baillie, Samuel S. Wagstaff, Lucas Pseudoprimes,
           Math. Comp. Vol 35, Number 152 (1980), pp. 1391-1417,
           https://doi.org/10.1090%2FS0025-5718-1980-0583518-6
           http://mpqs.free.fr/LucasPseudoprimes.pdf
    .. [3] https://en.wikipedia.org/wiki/Baillie-PSW_primality_test
    """
    ...

def is_gaussian_prime(num) -> bool:
    r"""Test if num is a Gaussian prime number.

    References
    ==========

    .. [1] https://oeis.org/wiki/Gaussian_primes
    """
    ...

