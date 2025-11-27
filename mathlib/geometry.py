"""
Geometry module for geometric calculations.
"""
import math
from typing import Union


class Geometry:
    """A class for performing geometric calculations."""

    @staticmethod
    def circle_area(radius: Union[int, float]) -> float:
        """Calculate the area of a circle.

        Args:
            radius: The radius of the circle

        Returns:
            The area of the circle

        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

    @staticmethod
    def circle_circumference(radius: Union[int, float]) -> float:
        """Calculate the circumference of a circle.

        Args:
            radius: The radius of the circle

        Returns:
            The circumference of the circle

        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * math.pi * radius

    @staticmethod
    def rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a rectangle.

        Args:
            length: The length of the rectangle
            width: The width of the rectangle

        Returns:
            The area of the rectangle

        Raises:
            ValueError: If length or width is negative
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return length * width

    @staticmethod
    def rectangle_perimeter(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the perimeter of a rectangle.

        Args:
            length: The length of the rectangle
            width: The width of the rectangle

        Returns:
            The perimeter of the rectangle

        Raises:
            ValueError: If length or width is negative
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return 2 * (length + width)

    @staticmethod
    def triangle_area(base: Union[int, float], height: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a triangle.

        Args:
            base: The base of the triangle
            height: The height of the triangle

        Returns:
            The area of the triangle

        Raises:
            ValueError: If base or height is negative
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height

    @staticmethod
    def pythagorean_theorem(a: Union[int, float], b: Union[int, float]) -> float:
        """Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

        Args:
            a: Length of first side
            b: Length of second side

        Returns:
            Length of the hypotenuse

        Raises:
            ValueError: If a or b is negative
        """
        if a < 0 or b < 0:
            raise ValueError("Side lengths cannot be negative")
        return math.sqrt(a ** 2 + b ** 2)

    @staticmethod
    def sphere_volume(radius: Union[int, float]) -> float:
        """Calculate the volume of a sphere.

        Args:
            radius: The radius of the sphere

        Returns:
            The volume of the sphere

        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return (4 / 3) * math.pi * radius ** 3

    @staticmethod
    def sphere_surface_area(radius: Union[int, float]) -> float:
        """Calculate the surface area of a sphere.

        Args:
            radius: The radius of the sphere

        Returns:
            The surface area of the sphere

        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 4 * math.pi * radius ** 2

    @staticmethod
    def cylinder_volume(radius: Union[int, float], height: Union[int, float]) -> float:
        """Calculate the volume of a cylinder.

        Args:
            radius: The radius of the cylinder base
            height: The height of the cylinder

        Returns:
            The volume of the cylinder

        Raises:
            ValueError: If radius or height is negative
        """
        if radius < 0 or height < 0:
            raise ValueError("Radius and height cannot be negative")
        return math.pi * radius ** 2 * height

    @staticmethod
    def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate the Euclidean distance between two points in 2D space.

        Args:
            x1: X coordinate of first point
            y1: Y coordinate of first point
            x2: X coordinate of second point
            y2: Y coordinate of second point

        Returns:
            The distance between the two points
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
