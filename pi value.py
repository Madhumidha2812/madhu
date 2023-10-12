class Circle:
    def __init__(self, radius):
        self.__pi = 3.141  
        self.radius = radius

    def calculate_area(self):
        return self.__pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * self.__pi * self.radius


circle = Circle(5)
print(f"Area: {circle.calculate_area()}")
print(f"Circumference: {circle.calculate_circumference()}")
