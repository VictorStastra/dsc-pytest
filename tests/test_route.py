import pytest

from src.logic import Route, Stop

NAMES = ['stop1', 'stop2', 'stop3', 'stop4', 'stop5']

list_of_stops = [Stop(name=name, x=i, y=i) for i, name in 
                 enumerate(NAMES)]

print(list_of_stops)

# Create a test which tests the correct initialization of a
# Route object, can we do this immidiately with a fixture?
route = Route(id=1, stops=list_of_stops)

# Create a test which adds a Stop object to a Route object

# Create a test which removes a Stop object from a Route object
# What happens if we try to remove a Stop object which is not in
# the Route object?
# What happens if .....?

