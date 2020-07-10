from oop1 import Vehicle

# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # todo
    def drive(self):
        return 'vroooom'

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# todo
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)
    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

#todo
for v in vehicles:
    print(v.drive())


#ref 15 classes and 11 args