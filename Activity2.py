# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves...")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water...")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
