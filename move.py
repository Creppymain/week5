class Animal:
    def move(self):
        pass

class Vehicle:
    def move(self):
        pass

# Animal classes
class Dog(Animal):
    def move(self):
        print("Running on four legs 🐕")

class Fish(Animal):
    def move(self):
        print("Swimming gracefully 🐟")

class Bird(Animal):
    def move(self):
        print("Flying through the air 🦅")

# Vehicle classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the street 🚲")

class Airplane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ⛵")

# Function that works with any movable object
def make_it_move(movable_object):
    movable_object.move()

# Create instances
animals = [Dog(), Fish(), Bird()]
vehicles = [Car(), Bicycle(), Airplane(), Boat()]

# Demonstrate polymorphism
print("Animals moving:")
for animal in animals:
    make_it_move(animal)

print("\nVehicles moving:")
for vehicle in vehicles:
    make_it_move(vehicle)