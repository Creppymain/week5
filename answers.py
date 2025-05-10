# class with inheritance to demonstrate OOP concepts

class Superhero:
    """Base class representing a superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness):
        # Encapsulation: Using _protected and __private attributes
        self.name = name  # Public attribute
        self._secret_identity = secret_identity  # Protected attribute
        self.__powers = powers  # Private attribute (name mangling)
        self.weakness = weakness  # Public attribute
        
    # Public method to access private powers
    def show_powers(self):
        return f"{self.name}'s powers: {self.__powers}"
    
    # Protected method (convention)
    def _reveal_secret(self):
        return f"My real identity is {self._secret_identity}"
    
    def fight(self):
        return f"{self.name} is fighting villains!"
    
    def __str__(self):
        return f"Superhero: {self.name} | Weakness: {self.weakness}"


class Avenger(Superhero):
    """Child class inheriting from Superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness, movies_appeared):
        super().__init__(name, secret_identity, powers, weakness)
        self.movies_appeared = movies_appeared  # New attribute
        
    # Method overriding (polymorphism)
    def fight(self):
        return f"{self.name} is fighting with Avengers teamwork!"
    
    # New method specific to Avengers
    def assemble(self):
        return f"{self.name} is assembling the Avengers!"
    
    def __str__(self):
        return super().__str__() + f" | MCU Movies: {self.movies_appeared}"


# Demonstration
if __name__ == "__main__":
    print("=== Superhero Class Demo ===")
    
    # Create a basic superhero
    superman = Superhero("Superman", "Clark Kent", 
                        ["Flight", "Super strength", "Heat vision"], 
                        "Kryptonite")
    print(superman)
    print(superman.show_powers())
    print(superman.fight())
    # print(superman.__powers)  # Would cause AttributeError (encapsulation)
    
    # Create an Avenger (inherited class)
    iron_man = Avenger("Iron Man", "Tony Stark",
                      ["Tech genius", "Powered armor", "AI assistance"],
                      "Electromagnets", 10)
    print("\n" + str(iron_man))
    print(iron_man.show_powers())  # Inherited method
    print(iron_man.fight())  # Overridden method
    print(iron_man.assemble())  # New method






# Python Polymorphism with Animal and Vehicle Movements


class Animal:
    def move(self):
        pass

class Vehicle:
    def move(self):
        pass

# Animal classes
class Dog(Animal):
    def move(self):
        print("Running on four legs ")

class Fish(Animal):
    def move(self):
        print("Swimming gracefully ")

class Bird(Animal):
    def move(self):
        print("Flying through the air ")

# Vehicle classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the street ")

class Airplane(Vehicle):
    def move(self):
        print("Flying through the sky ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")

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
