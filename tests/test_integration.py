"""Integration tests demonstrating interactions between different modules."""
import pytest
import math
from mathlib.calculator import Calculator
from mathlib.statistics import Statistics
from mathlib.geometry import Geometry


class TestMathLibIntegration:
    """Integration tests for the math library modules."""

    @pytest.fixture
    def calc(self):
        """Fixture to provide a Calculator instance."""
        return Calculator()

    @pytest.fixture
    def stats(self):
        """Fixture to provide a Statistics instance."""
        return Statistics()

    @pytest.fixture
    def geom(self):
        """Fixture to provide a Geometry instance."""
        return Geometry()

    @pytest.mark.integration
    def test_calculate_circle_statistics(self, geom, stats):
        """Test calculating statistics on multiple circle areas."""
        radii = [1, 2, 3, 4, 5]
        areas = [geom.circle_area(r) for r in radii]

        # Calculate statistics on the areas
        mean_area = stats.mean(areas)
        median_area = stats.median(areas)

        # Verify results
        expected_mean = sum(math.pi * r**2 for r in radii) / len(radii)
        assert mean_area == pytest.approx(expected_mean)
        assert median_area == pytest.approx(geom.circle_area(3))

    @pytest.mark.integration
    def test_rectangle_dimensions_with_calculator(self, calc, geom):
        """Test calculating rectangle properties using calculator operations."""
        # Calculate dimensions using calculator
        length = calc.add(5, 3)  # 8
        width = calc.multiply(2, 2)  # 4

        # Use geometry module to calculate area and perimeter
        area = geom.rectangle_area(length, width)
        perimeter = geom.rectangle_perimeter(length, width)

        assert area == 32
        assert perimeter == 24

    @pytest.mark.integration
    def test_statistical_analysis_of_calculated_values(self, calc, stats):
        """Test performing statistical analysis on calculated values."""
        # Generate a series of calculated values
        base_value = 10
        values = []
        for i in range(1, 6):
            result = calc.multiply(base_value, i)
            values.append(result)

        # Perform statistical analysis
        mean = stats.mean(values)
        median = stats.median(values)
        range_val = stats.range_value(values)

        assert mean == 30.0
        assert median == 30
        assert range_val == 40

    @pytest.mark.integration
    def test_pythagorean_with_calculations(self, calc, geom):
        """Test Pythagorean theorem with calculated side lengths."""
        # Calculate side lengths
        side_a = calc.add(2, 1)  # 3
        side_b = calc.power(2, 2)  # 4

        # Calculate hypotenuse
        hypotenuse = geom.pythagorean_theorem(side_a, side_b)

        assert hypotenuse == pytest.approx(5)

    @pytest.mark.integration
    def test_sphere_calculations_with_statistics(self, calc, geom, stats):
        """Test calculating sphere properties and analyzing them statistically."""
        # Calculate radii using calculator
        radii = [calc.add(i, 1) for i in range(5)]  # [1, 2, 3, 4, 5]

        # Calculate volumes
        volumes = [geom.sphere_volume(r) for r in radii]

        # Calculate surface areas
        surface_areas = [geom.sphere_surface_area(r) for r in radii]

        # Perform statistical analysis
        mean_volume = stats.mean(volumes)
        mean_surface_area = stats.mean(surface_areas)

        # Verify calculations
        expected_mean_volume = sum(
            (4/3) * math.pi * r**3 for r in radii) / len(radii)
        expected_mean_surface = sum(
            4 * math.pi * r**2 for r in radii) / len(radii)

        assert mean_volume == pytest.approx(expected_mean_volume)
        assert mean_surface_area == pytest.approx(expected_mean_surface)

    @pytest.mark.integration
    def test_complex_calculation_pipeline(self, calc, stats, geom):
        """Test a complex pipeline using all modules."""
        # Step 1: Calculate some initial values
        base = calc.power(2, 3)  # 8
        multiplier = calc.add(2, 3)  # 5

        # Step 2: Generate a dataset
        dataset = [calc.multiply(base, i) for i in range(1, multiplier + 1)]
        # dataset = [8, 16, 24, 32, 40]

        # Step 3: Calculate statistics
        mean_val = stats.mean(dataset)
        std_dev = stats.standard_deviation(dataset)

        # Step 4: Use mean as radius for geometry calculation
        circle_area = geom.circle_area(mean_val)

        # Step 5: Verify all calculations
        assert mean_val == 24.0
        assert std_dev == pytest.approx(12.649, rel=1e-2)
        assert circle_area == pytest.approx(math.pi * 24**2)

    @pytest.mark.integration
    def test_distance_calculation_with_stats(self, calc, geom, stats):
        """Test calculating distances and analyzing them statistically."""
        # Define points using calculator
        points = [
            (0, 0),
            (calc.add(2, 1), calc.add(3, 1)),  # (3, 4)
            (calc.multiply(2, 3), calc.multiply(2, 4)),  # (6, 8)
        ]

        # Calculate distances from origin
        distances = [geom.distance_between_points(
            0, 0, x, y) for x, y in points]

        # Analyze distances
        mean_distance = stats.mean(distances)
        max_distance = max(distances)

        assert distances[0] == 0
        assert distances[1] == pytest.approx(5)
        assert distances[2] == pytest.approx(10)
        assert mean_distance == pytest.approx(5)
        assert max_distance == pytest.approx(10)

    @pytest.mark.integration
    def test_factorial_and_statistics(self, calc, stats):
        """Test calculating factorials and performing statistical analysis."""
        # Calculate factorials for numbers 1-5
        numbers = list(range(1, 6))
        factorials = [calc.factorial(n) for n in numbers]
        # factorials = [1, 2, 6, 24, 120]

        # Calculate statistics
        median_factorial = stats.median(factorials)
        range_factorial = stats.range_value(factorials)

        assert median_factorial == 6
        assert range_factorial == 119

    @pytest.mark.integration
    def test_geometric_mean_approximation(self, calc, stats, geom):
        """Test approximating geometric mean using available tools."""
        # Calculate areas of squares with different side lengths
        side_lengths = [2, 4, 8]
        areas = [geom.rectangle_area(s, s) for s in side_lengths]
        # areas = [4, 16, 64]

        # Calculate arithmetic mean
        arithmetic_mean = stats.mean(areas)

        # Calculate geometric mean using calculator
        # Geometric mean = (4 * 16 * 64)^(1/3)
        product = calc.multiply(calc.multiply(4, 16), 64)
        geometric_mean_cubed = product
        geometric_mean = calc.power(geometric_mean_cubed, 1/3)

        assert arithmetic_mean == pytest.approx(28)
        assert geometric_mean == pytest.approx(16)
        assert geometric_mean < arithmetic_mean

    @pytest.mark.integration
    @pytest.mark.slow
    def test_large_dataset_processing(self, calc, stats, geom):
        """Test processing a large dataset using all modules."""
        # Generate a large dataset
        size = 1000
        dataset = [calc.add(i, calc.multiply(i, 0.5)) for i in range(size)]

        # Calculate comprehensive statistics
        mean_val = stats.mean(dataset)
        median_val = stats.median(dataset)
        std_dev = stats.standard_deviation(dataset)
        percentile_90 = stats.percentile(dataset, 90)

        # Use statistics to create geometric shapes
        circle_area = geom.circle_area(mean_val)
        sphere_volume = geom.sphere_volume(median_val)

        # Verify calculations make sense
        assert mean_val > 0
        assert median_val > 0
        assert std_dev > 0
        assert percentile_90 > median_val
        assert circle_area > 0
        assert sphere_volume > 0

    @pytest.mark.integration
    def test_error_propagation(self, calc, geom):
        """Test that errors propagate correctly across modules."""
        # Test divide by zero in calculator
        with pytest.raises(ValueError):
            result = calc.divide(10, 0)

        # Test negative radius in geometry
        with pytest.raises(ValueError):
            area = geom.circle_area(-5)

        # Test that valid calculations still work after errors
        valid_result = calc.add(5, 3)
        valid_area = geom.circle_area(2)

        assert valid_result == 8
        assert valid_area == pytest.approx(4 * math.pi)

    @pytest.mark.integration
    def test_chained_operations(self, calc, stats, geom):
        """Test chaining operations across all modules."""
        # Create a chain: calculation -> statistics -> geometry -> calculation

        # Step 1: Create base values
        values = [calc.power(i, 2) for i in range(1, 6)]
        # values = [1, 4, 9, 16, 25]

        # Step 2: Calculate mean
        mean_squared = stats.mean(values)
        # mean_squared = 11

        # Step 3: Use mean as circle radius
        area = geom.circle_area(mean_squared)

        # Step 4: Calculate square root of area and compare
        sqrt_area = calc.square_root(area)

        # Verify chain
        assert mean_squared == 11.0
        assert area == pytest.approx(math.pi * 121)
        assert sqrt_area == pytest.approx(math.sqrt(math.pi * 121))
