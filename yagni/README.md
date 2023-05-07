# YAGNI (You Aren’t Gonna Need It)

It is a principle of software development that advises against adding features or functionality to a program until it is actually needed. The basic idea is that developers should not try to anticipate every possible use case or feature that might be needed in the future, but instead should focus on the requirements of the current iteration of the software.
In essence, the YAGNI principle suggests that you should not write code for functionality that you do not currently need. This is because any additional code or features that are added to the software will increase its complexity, which can make it harder to understand, maintain, and debug. Additionally, any code that is not being used adds unnecessary overhead and can slow down the performance of the software.

<br>

## Bad Code
    import math


    class Calculator:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return self.num1 + self.num2

        def subtract(self):
            return self.num1 - self.num2

        def multiply(self):
            return self.num1 * self.num2

        def divide(self):
            return self.num1 / self.num2

        def modulo(self):
            return self.num1 % self.num2

        def power(self):
            return self.num1 ** self.num2

       # Currently not needed
        def square_root(self):
            return math.sqrt(self.num1)

       # Currently not needed
        def cube_root(self):
            return math.pow(self.num1, 1/3)

<br>

## Good Code
    class Calculator:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return self.num1 + self.num2

        def subtract(self):
            return self.num1 - self.num2

        def multiply(self):
            return self.num1 * self.num2

        def divide(self):
            return self.num1 / self.num2

        def modulo(self):
            return self.num1 % self.num2

        def power(self):
            return self.num1 ** self.num2
