#Build a geometry calculator to compute area of circle, rectangle, and triangle using a module. php-iqrj-dew

import math

def area_circle(radius):
    if radius < 0:
        raise ValueError("radius cannot be  negative")
    return math.pi*(radius*radius)   #formula of radius Area = PI * Radius * Radius 

def area_rectangle(lenght, width):
    if lenght < 0 or width < 0:
        raise ValueError("lenght and width cannot be negative")
    return lenght * width            #formula of rectangle = lenght * width

def area_triangle(base , height):
    if base < 0 or height < 0:
        raise ValueError("base and height cannot be negative")
    return 0.5 * base * height


circle = area_circle(10.5)
print(f"area of circle {circle}") 
rectangle = area_rectangle(8,5)
print(f"area of rectangle {rectangle}") 
triangle = area_triangle(2,5)
print(f"area of triangle {triangle}")










