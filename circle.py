radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)

areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

for i, radius in enumerate(radius_list):
    print(f"Circle {i + 1}:")
    print(f"Radius: {radius}")
    print(f"Area: {areas[i]}")
    print(f"Circumference: {circumferences[i]}")
    print()
