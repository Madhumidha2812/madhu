import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


radii_list = [10, 501, 22, 37, 100, 999, 87, 351]


for radius in radii_list:
    circle = Circle(radius)
    circle_area = circle.area()
    circle_perimeter = circle.perimeter()
    print(f"Radius: {radius}, Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")
