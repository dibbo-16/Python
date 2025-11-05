# Polymorphism means one name, many forms – the same function or operator can behave differently depending on the object or data type.

# Method Overriding (same method name in parent and child class).

# Same function name works differently for different objects.

class Bird:
    def make_sound(self):
        print("Birds make sounds")

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp Chirp")

class Crow(Bird):
    def make_sound(self):
        print("Caw Caw")

# Usage
birds = [Sparrow(), Crow(), Bird()]
for b in birds:
    b.make_sound()   # Polymorphism in action

    
# Same method name make_sound() behaves differently depending on the object type.    