def rescale(l,a,b):
    """Rescales the elements of list l with new_l=a+b*l.
    Examples:
    A simple shift would be done with a=shift, b=1.
    A multiplication of all elements with a=0, b=scale
    To convert an observed frequency to a Doppler velocity,
    v = c - (c/f0)*f
    where f0 is the frequency in the Local Standard of Rest."""
    result = []
    for i in range(0,len(l)):
        result.append(a + b*l[i])
    return result
