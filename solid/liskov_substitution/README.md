# Liskov Substitution Principle

The Liskov Substitution Principle is a programming concept that states that an object of a parent class should be replaceable with an object of its child class without causing any problems or unexpected behavior in the program. In other words, any subclass should be able to be used in place of its parent class without breaking the code.

<br>

## Bad Code
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            self.height = height

        def area(self):
            return self.width * self.height


    class Square(Rectangle):
        def __init__(self, size):
            self.width = size
            self.height = size
            
<br>

## Good Code
    class Shape:
        def area(self):
            pass


    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height


    class Square(Shape):
        def __init__(self, size):
            self.size = size

        def area(self):
            return self.size ** 2
