"""This module defines the constants
au - in cm
c  - the speed of light in cm/s
and the functions
distance_to_sun(format)
TitusBodeLaw(planet_number)"""

__name__ = "example1"

from math import *

au = 1.5e8*1e5
c = 3e10 # sec

def distance_to_sun(format):
    """Given a format (or unit) this returns thw
    mean distance of the sun in that unit"""
    if ( format == 'cm' ):
        return "%.3e" % au
    elif ( format == "km" ):
        return "%.3e" % (au/1e5)
    elif (format == "mi" ):
        return "%.3f" % (au/1e5/1.6)
    elif (format == "seconds" ):
        return au/c
    elif (format == "minutes" ):
        return au/c/60
    else:
        return "Unknown format"


def TitusBodeLaw(planet):
    """Given a planet number, starting with 1 for
    Mercury, it returns the orbital radius as
    calulated by the Titus-Bode Law"""
    if planet==1:
        n=0
    else:
        n = 3*pow(2,planet-2)
    return "%.1f" % ((n+4)/10.)

