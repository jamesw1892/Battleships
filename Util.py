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
