import re
import numpy as np

def get_coords(addr):
    """Extract the latitude and longitude from a string containing these values

    Parameters
    ----------
    addr : str
        String containing latitude and longitude, separated by a comma

    Returns
    -------
    coords : tuple
        Tuple (latitude, longitude)

    Example
    -------
    >>> get_coords('123 Fake St., Berkeley, CA (-123.456, 78.9)')
    >>> (-123.456, 78.9)
    """
    coords = re.findall('[\-\d.]+, [\-\d.]+', addr)

    # Return a missing value if there aren't any coordinates
    if not coords:
        return np.nan

    # Return a tuple otherwise
    coords = coords[0].split(',')
    return (float(coords[0]), float(coords[1]))
