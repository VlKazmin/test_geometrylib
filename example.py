from geometrylib.circle import Circle
from geometrylib.triangle import Triangle

circle = Circle(radius=12)
print("Площадь круга:", circle.area()) 
print("Площадь круга (с округлением):", circle.area(decimal=2))

print()

triangle = Triangle(a=3, b=5, c=5)
print("Площадь треугольника:", triangle.area())
print("Площадь треугольника (с округлением):",triangle.area(decimal=2))
print("Треугольник прямоугольный:", triangle.is_right_angled())
