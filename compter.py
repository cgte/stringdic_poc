"""
compute some distance between two strings
"""

from collections import Counter
from math import exp


def dist(string1, string2):
    """
    >>> dist('abcd', 'abcd')
    0
    >>> dist('abcd', 'abc')
    1
    """
    if string1 == string2:
        return 0
    count1 = Counter(string1)
    count2 = Counter(string2)

    keys = set(count1.keys())
    keys.update(count2.keys())
    dist = sum(abs(count1.get(letter, 0) - count2.get(letter, 0)) for letter in keys)
    return dist


def expprox(string1, string2):
    """
    Returns a nornamised distance between two strings

    >>> expprox('abcd', 'abcd')
    0.0
    >>> expprox('qwertyuiop', 'aasdfghjkl;') > 0.99
    True

    """
    return 1 - exp(-dist(string1, string2) ** 2)


def distfrom(string1):
    """ Tooling for comparing many string to a given one

    >>> from_abc = distfrom('abc')
    >>> from_abc('abc')
    0.0
    >>> sorted(['bcd', 'abc'], key=from_abc)
    ['abc', 'bcd']
    """

    def wrapped(string2):
        return expprox(string1, string2)

    return wrapped
