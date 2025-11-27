"""Unit tests for the Geometry module."""
import pytest
import math
from mathlib.geometry import Geometry


class TestGeometry:
    """Test suite for Geometry class."""

    @pytest.fixture
    def geom(self):
        """Fixture to provide a Geometry instance."""
        return Geometry()

    # Test circle area
    @pytest.mark.unit
    @pytest.mark.parametrize("radius,expected", [
        (1, math.pi),
        (2, 4 * math.pi),
        (0, 0),
        (5, 25 * math.pi),
        (0.5, 0.25 * math.pi),
    ])
    def test_circle_area(self, geom, radius, expected):
        """Test circle area calculation with various radii."""
        assert geom.circle_area(radius) == pytest.approx(expected)

    @pytest.mark.unit
    def test_circle_area_negative_radius(self, geom):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            geom.circle_area(-1)

    # Test circle circumference
    @pytest.mark.unit
    @pytest.mark.parametrize("radius,expected", [
        (1, 2 * math.pi),
        (2, 4 * math.pi),
        (0, 0),
        (5, 10 * math.pi),
        (0.5, math.pi),
    ])
    def test_circle_circumference(self, geom, radius, expected):
        """Test circle circumference calculation with various radii."""
        assert geom.circle_circumference(radius) == pytest.approx(expected)

    @pytest.mark.unit
    def test_circle_circumference_negative_radius(self, geom):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            geom.circle_circumference(-1)

    # Test rectangle area
    @pytest.mark.unit
    @pytest.mark.parametrize("length,width,expected", [
        (2, 3, 6),
        (5, 5, 25),
        (1, 1, 1),
        (0, 5, 0),
        (2.5, 4, 10),
    ])
    def test_rectangle_area(self, geom, length, width, expected):
        """Test rectangle area calculation with various dimensions."""
        assert geom.rectangle_area(length, width) == pytest.approx(expected)

    @pytest.mark.unit
    @pytest.mark.parametrize("length,width", [
        (-1, 5),
        (5, -1),
        (-1, -1),
    ])
    def test_rectangle_area_negative_dimensions(self, geom, length, width):
        """Test that negative dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            geom.rectangle_area(length, width)

    # Test rectangle perimeter
    @pytest.mark.unit
    @pytest.mark.parametrize("length,width,expected", [
        (2, 3, 10),
        (5, 5, 20),
        (1, 1, 4),
        (0, 5, 10),
        (2.5, 4, 13),
    ])
    def test_rectangle_perimeter(self, geom, length, width, expected):
        """Test rectangle perimeter calculation with various dimensions."""
        assert geom.rectangle_perimeter(
            length, width) == pytest.approx(expected)

    @pytest.mark.unit
    @pytest.mark.parametrize("length,width", [
        (-1, 5),
        (5, -1),
    ])
    def test_rectangle_perimeter_negative_dimensions(self, geom, length, width):
        """Test that negative dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            geom.rectangle_perimeter(length, width)

    # Test triangle area
    @pytest.mark.unit
    @pytest.mark.parametrize("base,height,expected", [
        (4, 3, 6),
        (10, 5, 25),
        (0, 5, 0),
        (5, 0, 0),
        (2.5, 4, 5),
    ])
    def test_triangle_area(self, geom, base, height, expected):
        """Test triangle area calculation with various dimensions."""
        assert geom.triangle_area(base, height) == pytest.approx(expected)

    @pytest.mark.unit
    @pytest.mark.parametrize("base,height", [
        (-1, 5),
        (5, -1),
    ])
    def test_triangle_area_negative_dimensions(self, geom, base, height):
        """Test that negative dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Base and height cannot be negative"):
            geom.triangle_area(base, height)

    # Test Pythagorean theorem
    @pytest.mark.unit
    @pytest.mark.parametrize("a,b,expected", [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (1, 1, math.sqrt(2)),
        (0, 5, 5),
    ])
    def test_pythagorean_theorem(self, geom, a, b, expected):
        """Test Pythagorean theorem with various inputs."""
        assert geom.pythagorean_theorem(a, b) == pytest.approx(expected)

    @pytest.mark.unit
    @pytest.mark.parametrize("a,b", [
        (-1, 5),
        (5, -1),
    ])
    def test_pythagorean_theorem_negative_sides(self, geom, a, b):
        """Test that negative side lengths raise ValueError."""
        with pytest.raises(ValueError, match="Side lengths cannot be negative"):
            geom.pythagorean_theorem(a, b)

    # Test sphere volume
    @pytest.mark.unit
    @pytest.mark.parametrize("radius,expected", [
        (1, (4/3) * math.pi),
        (2, (4/3) * math.pi * 8),
        (0, 0),
        (3, 36 * math.pi),
    ])
    def test_sphere_volume(self, geom, radius, expected):
        """Test sphere volume calculation with various radii."""
        assert geom.sphere_volume(radius) == pytest.approx(expected)

    @pytest.mark.unit
    def test_sphere_volume_negative_radius(self, geom):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            geom.sphere_volume(-1)

    # Test sphere surface area
    @pytest.mark.unit
    @pytest.mark.parametrize("radius,expected", [
        (1, 4 * math.pi),
        (2, 16 * math.pi),
        (0, 0),
        (3, 36 * math.pi),
    ])
    def test_sphere_surface_area(self, geom, radius, expected):
        """Test sphere surface area calculation with various radii."""
        assert geom.sphere_surface_area(radius) == pytest.approx(expected)

    @pytest.mark.unit
    def test_sphere_surface_area_negative_radius(self, geom):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            geom.sphere_surface_area(-1)

    # Test cylinder volume
    @pytest.mark.unit
    @pytest.mark.parametrize("radius,height,expected", [
        (1, 1, math.pi),
        (2, 3, 12 * math.pi),
        (0, 5, 0),
        (5, 0, 0),
        (3, 4, 36 * math.pi),
    ])
    def test_cylinder_volume(self, geom, radius, height, expected):
        """Test cylinder volume calculation with various dimensions."""
        assert geom.cylinder_volume(radius, height) == pytest.approx(expected)

    @pytest.mark.unit
    @pytest.mark.parametrize("radius,height", [
        (-1, 5),
        (5, -1),
    ])
    def test_cylinder_volume_negative_dimensions(self, geom, radius, height):
        """Test that negative dimensions raise ValueError."""
        with pytest.raises(ValueError, match="Radius and height cannot be negative"):
            geom.cylinder_volume(radius, height)

    # Test distance between points
    @pytest.mark.unit
    @pytest.mark.parametrize("x1,y1,x2,y2,expected", [
        (0, 0, 3, 4, 5),
        (0, 0, 0, 0, 0),
        (1, 1, 4, 5, 5),
        (-1, -1, 2, 3, 5),
        (0, 0, 1, 1, math.sqrt(2)),
    ])
    def test_distance_between_points(self, geom, x1, y1, x2, y2, expected):
        """Test distance calculation between two points."""
        assert geom.distance_between_points(
            x1, y1, x2, y2) == pytest.approx(expected)

    # Edge cases
    @pytest.mark.unit
    def test_geometry_with_large_numbers(self, geom):
        """Test geometric calculations with large numbers."""
        large = 1000
        assert geom.rectangle_area(large, large) == large * large
        assert geom.circle_area(large) == pytest.approx(math.pi * large ** 2)

    @pytest.mark.unit
    def test_geometry_with_small_numbers(self, geom):
        """Test geometric calculations with very small numbers."""
        small = 0.001
        assert geom.rectangle_area(
            small, small) == pytest.approx(small * small)
        assert geom.circle_area(small) == pytest.approx(math.pi * small ** 2)
