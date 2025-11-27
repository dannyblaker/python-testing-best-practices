# Example: Using the MathLib in Practice

from mathlib.calculator import Calculator
from mathlib.statistics import Statistics
from mathlib.geometry import Geometry


def main():
    """Demonstrate the usage of the math library."""

    # Initialize modules
    calc = Calculator()
    stats = Statistics()
    geom = Geometry()

    print("=" * 50)
    print("MathLib Demo - Mathematics Library")
    print("=" * 50)

    # Calculator examples
    print("\n📊 Calculator Operations:")
    print(f"  Addition: 15 + 7 = {calc.add(15, 7)}")
    print(f"  Multiplication: 12 × 8 = {calc.multiply(12, 8)}")
    print(f"  Power: 2^10 = {calc.power(2, 10)}")
    print(f"  Square root of 144 = {calc.square_root(144)}")
    print(f"  Factorial of 6 = {calc.factorial(6)}")

    # Statistics examples
    print("\n📈 Statistical Analysis:")
    data = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40]
    print(f"  Dataset: {data}")
    print(f"  Mean: {stats.mean(data):.2f}")
    print(f"  Median: {stats.median(data)}")
    print(f"  Standard Deviation: {stats.standard_deviation(data):.2f}")
    print(f"  Range: {stats.range_value(data)}")
    print(f"  75th Percentile: {stats.percentile(data, 75):.2f}")

    # Geometry examples
    print("\n📐 Geometric Calculations:")
    radius = 5
    print(f"  Circle (radius={radius}):")
    print(f"    Area: {geom.circle_area(radius):.2f}")
    print(f"    Circumference: {geom.circle_circumference(radius):.2f}")

    length, width = 10, 6
    print(f"  Rectangle ({length}×{width}):")
    print(f"    Area: {geom.rectangle_area(length, width)}")
    print(f"    Perimeter: {geom.rectangle_perimeter(length, width)}")

    a, b = 3, 4
    print(f"  Right Triangle (sides {a} and {b}):")
    print(f"    Hypotenuse: {geom.pythagorean_theorem(a, b)}")

    # Integration example
    print("\n🔗 Integrated Example:")
    print("  Calculating statistics on circle areas...")
    radii = [1, 2, 3, 4, 5]
    areas = [geom.circle_area(r) for r in radii]
    mean_area = stats.mean(areas)
    print(f"  Radii: {radii}")
    print(f"  Mean area: {mean_area:.2f}")

    print("\n" + "=" * 50)
    print("Demo complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
