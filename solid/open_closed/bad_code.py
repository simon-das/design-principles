class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"


def make_animal_sound(animal):
    if isinstance(animal, Dog):
        return animal.make_sound() + " I am a " + animal.species
    elif isinstance(animal, Cat):
        return animal.make_sound() + " I am a " + animal.species
    elif isinstance(animal, Cow):
        return animal.make_sound() + " I am a " + animal.species


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")
cow = Cow("Bessie", "Holstein")

print(make_animal_sound(dog))
print(make_animal_sound(cat))
print(make_animal_sound(cow))
