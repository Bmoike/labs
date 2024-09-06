import math


# class that creates the calculations for a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return round(2 * self.radius, 2)

    def calculate_circumference(self):
        return round(2 * math.pi * self.radius, 2)

    def calculate_area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius

    def __str__(self):
        return (
            f"Radius: {self.radius}, Diameter: {self.calculate_diameter()}, Circumference: {self.calculate_circumference()}"
            f", Area: {self.calculate_area()}")


# validations
def Validator():
    while True:
        try:
            user_input = round(float(input("Please enter a radius with a decimal: ")), 2)
            return user_input
        except ValueError:
            print("Please input a type float as directed.")


# breaks the loop for growing the circle
def end_loop():
    while True:
        loop_break = input("Grow circle?(y/n): ").lower()
        if loop_break == 'y':
            return False
        elif loop_break == 'n':
            return True
        else:
            print("Please enter (y/n) only.")


# gets the calculations for the circle
def get_circle(circle):
    while True:
        circle.calculate_diameter()
        circle.calculate_circumference()
        circle.calculate_area()
        circle.get_radius()
        print(circle)
        if not end_loop():
            circle.grow()
        else:
            print("Goodbye!")
            break


# main
user_radius = Validator()
c1 = Circle(user_radius)
get_circle(c1)
