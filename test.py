# import from other module 
from geometry.Point import Point
from geometry.Cylinder import Cylinder
from geometry.Line import Line

source = Point(x=1,y=1)
destination = Point(x=5,y=5)
line = Line(source=source, destination=destination)
print(f"Line distance = {line.distance()}")
print(f"Line slope = {line.slope()}")

cylinder = Cylinder(
    r=10,
    h= 5
)
print(f"Cylinder surface area = {cylinder.surface_area()}")
print(f"Cylinder volume = {cylinder.volume()}")

 