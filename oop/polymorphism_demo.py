# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        """Base method that should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the length and width of the rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the radius of the circle."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * self.radius ** 2
