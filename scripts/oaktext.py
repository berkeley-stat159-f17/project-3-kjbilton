import re
import numpy as np

def get_coords(addr):
    coords = re.findall('[\d.]+, [\-\d.]+', addr)

    # Return a missing value if there aren't any coordinates
    if not coords:
        return np.nan

    # Return a tuple otherwise
    coords = coords[0].split(',')
    return (float(coords[0]), float(coords[1]))
