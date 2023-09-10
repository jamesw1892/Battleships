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
