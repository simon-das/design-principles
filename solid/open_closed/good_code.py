class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"


class AnimalSoundMaker:
    def __init__(self, animals):
        self.animals = animals

    def make_sounds(self):
        for animal in self.animals:
            print(animal.make_sound() + " I am a " + animal.species)


animals = [
    Dog("Buddy", "Golden Retriever"),
    Cat("Whiskers", "Siamese"),
    Cow("Bessie", "Holstein")
]

animal_sound_maker = AnimalSoundMaker(animals)
animal_sound_maker.make_sounds()
