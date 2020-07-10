# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass
#top level basic grandpartents 

class FlightVehicle(Vehicle):
    pass
#takes parents diff from grandpartents

class Airplane(FlightVehicle):
    pass
#takes parents diff from grandpartents child

class Starship(FlightVehicle):
    pass
#takes parents diff from grandpartents child

class GroundVehicle(Vehicle):
    pass
#takes parents 

class Car(GroundVehicle):
    pass
#last level siblings

class Motorcycle(GroundVehicle):
    pass
#last level siblings

#wrote down on paper because the chart was confusing