import numpy as np

def L2(v, *args):
    """Compute the weighted L2 norm.

    INPUTS
    =======
    v: a list of floats
    args: a list of arguments, arg[0] is a list of weights (floats)

    RETURNS
    ========
    s: weighted L2 norm of the input v

    NOTES
    =====
    PRE:
        - both v and arg[0] must be lists of floats
        - v and arg[0] are of the same length
    POST:
        - v and other arguments are not changed by this function
        - raises Value Error when length of lists of weights do not match length of target list
        - returns a float

    EXAMPLES
    =========
    >>> L2([1.0, 2.0], [2.0, 3.0])
    6.324555320336759
    """

    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)
