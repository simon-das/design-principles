# OCP (Open-Closed Principle)

The Open-Closed Principle states that an entity (class, module, function, etc.) should be open for extension and closed for modification.

The Open-Closed Principle is a programming principle that suggests that once you have written some code, you should avoid changing it as much as possible. Instead, you should design your code in a way that allows you to add new features or functionality without having to change the existing code. This makes your code more flexible and easier to maintain over time.

<br>

## Bad Code
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
    
<br>

## Good Code
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
