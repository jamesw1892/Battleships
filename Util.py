#!/usr/bin/python

"""
Utility functions.
"""

def padCentreFunc(length: int):
    """
    Return a function that will pad the input as a string to a length of at
    least 'length', centred.
    """

    def padCentre(to_pad) -> str:
        out = str(to_pad)
        while len(out) < length - 1:
            out = f" {out} "
        if len(out) < length:
            out += " "
        return out

    return padCentre

def padCentre(to_pad, length: int):
    """
    Return 'to_pad' as a string of length at least 'length', centred.
    """
    return padCentreFunc(length)(to_pad)

def intToUnsigned1Byte(num: int) -> str:
    """
    Return 'num' as a 1-byte (length 8) binary string, padded at the beginning
    with 0s if necessary. If it is not between 0 and 255 inclusive then an
    AssertionError is thrown.
    """
    assert 0 <= num <= 255, "Can only represent integers between 0 and 255"
    bin_str = bin(num)[2:]
    return "0" * (8 - len(bin_str)) + bin_str

def make2D(list_1d, length_inner_list: int) -> list[list]:
    """
    Return a 2D list from the input 1D iterable of given inner length. The
    elements from the given iterable will be used to fill lists of the given
    length repeatedly until all elements are used and return a list of those
    lists. Raises TypeError if first input is not an iterable and if second
    input is not an integer. Raises ValueError if second input is zero or
    negative.
    """
    if length_inner_list <= 0:
        raise ValueError("Inner list length cannot be zero or negative")

    return [list(list_1d[start_index:start_index + length_inner_list])
            for start_index in range(0, len(list_1d), length_inner_list)]
