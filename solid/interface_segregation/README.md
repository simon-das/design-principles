# Interface Segregation Principle

The Interface Segregation Principle is a programming concept that states that a client should only be required to use the methods that it needs from an interface. It means that an interface should be designed in such a way that it is specific to the needs of the client, and the client should not be required to implement or depend on any methods that it doesn't need or use. In other words, the interface should be broken down into smaller, more specialized interfaces, rather than having a single large interface that contains methods for many different purposes.

<br>

## Bad Code
    from abc import ABC, abstractmethod


    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass


    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)


    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * (self.radius ** 2)

        # Forced to implement perimeter method
        def perimeter(self):
            return 2 * 3.14 * self.radius

<br>

## Good Code
    from abc import ABC, abstractmethod


    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass


    class Polygon(ABC):
        @abstractmethod
        def perimeter(self):
            pass


    class Rectangle(Shape, Polygon):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)


    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * (self.radius ** 2)
