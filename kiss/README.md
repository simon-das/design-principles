# KISS (Keep It Simple, Stupid)



KISS (Keep It Simple, Stupid) is a principle in software engineering that encourages keeping things simple and straightforward. It emphasizes that software systems should be designed in a simple and concise manner to make them easy to understand, modify, and maintain. The KISS principle states that the simplest solution is often the best solution.

In other words, when designing a software system, developers should strive to keep the design as simple as possible, and avoid making it more complex than necessary. This can help to reduce the risk of bugs and errors, and make it easier to maintain and update the system over time.

For example, instead of writing complex code to solve a simple problem, a developer might choose to use a built-in library or function that provides a simpler and more straightforward solution. Similarly, when designing user interfaces, designers might choose to use simple, intuitive layouts and controls that are easy to understand and use.

The KISS principle is often used in conjunction with other software design principles, such as the SOLID principles and the YAGNI (You Aren't Gonna Need It) principle, to create software systems that are robust, scalable, and maintainable.

<br>

## Bad Code
    def calculate_average(list_of_numbers):
        total_sum = 0

        for num in list_of_numbers:
            total_sum += num

        average = total_sum / len(list_of_numbers)

        return average
    
<br>
    
## Good Code
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)
    
