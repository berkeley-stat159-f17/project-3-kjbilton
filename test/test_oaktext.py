import sys
sys.path.append("scripts")

from oaktext import get_coords

def test_get_coords():
    # Make an address to parse coordinates from
    addr = '123 Fake street, (100, 40)'
    coords = get_coords(addr)

    # Make sure that we get a tuple, as specified in the function
    assert isinstance(coords, tuple)

    # Ensure we get the right coordinates out
    assert coords == (100, 40)
