import pytest
from src.logic import distance_between_points


@pytest.mark.distance
def test_distance_between_points():
    assert distance_between_points((0, 0), (1, 1)) == 1.4142135623730951
    

# Think of what tests you want to write for this simple function.
# What can we expect as input and output? Should input be 
# validated/checked? What happens if the input is not valid?
# What happens if the input is valid but the output is not valid?
# Do we want to test for multiple inputs and outputs?
# What happens if point 2 is the same as point 1? What if point 2 lies
# "lower" on x and y axis than point 1? How is this function used 
# in our application? -- What should we enforce?
