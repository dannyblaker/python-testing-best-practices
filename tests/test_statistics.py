"""Unit tests for the Statistics module."""
import pytest
import math
from mathlib.statistics import Statistics


class TestStatistics:
    """Test suite for Statistics class."""

    @pytest.fixture
    def stats(self):
        """Fixture to provide a Statistics instance."""
        return Statistics()

    # Test mean
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 3, 4, 5], 3.0),
        ([10], 10.0),
        ([1, 1, 1, 1], 1.0),
        ([-1, 0, 1], 0.0),
        ([1.5, 2.5, 3.5], 2.5),
        ([100, 200, 300], 200.0),
    ])
    def test_mean(self, stats, numbers, expected):
        """Test mean calculation with various inputs."""
        assert stats.mean(numbers) == pytest.approx(expected)

    @pytest.mark.unit
    def test_mean_empty_list(self, stats):
        """Test that mean of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate mean of empty list"):
            stats.mean([])

    # Test median
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 2.5),
        ([5, 1, 3, 2, 4], 3),
        ([10], 10),
        ([1, 1, 2, 2], 1.5),
        ([1.5, 2.5, 3.5], 2.5),
    ])
    def test_median(self, stats, numbers, expected):
        """Test median calculation with various inputs."""
        assert stats.median(numbers) == pytest.approx(expected)

    @pytest.mark.unit
    def test_median_empty_list(self, stats):
        """Test that median of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate median of empty list"):
            stats.median([])

    # Test mode
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 2, 3, 3, 3, 4], [3]),
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
        ([5], [5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 1, 1, 2, 3], [1]),
    ])
    def test_mode(self, stats, numbers, expected):
        """Test mode calculation with various inputs."""
        assert stats.mode(numbers) == expected

    @pytest.mark.unit
    def test_mode_empty_list(self, stats):
        """Test that mode of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate mode of empty list"):
            stats.mode([])

    # Test variance
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,sample,expected", [
        ([1, 2, 3, 4, 5], True, 2.5),
        ([1, 2, 3, 4, 5], False, 2.0),
        ([2, 4, 6, 8], True, 20/3),
        ([10, 10, 10], True, 0.0),
        ([1, 5], True, 8.0),
    ])
    def test_variance(self, stats, numbers, sample, expected):
        """Test variance calculation with various inputs."""
        assert stats.variance(numbers, sample) == pytest.approx(expected)

    @pytest.mark.unit
    def test_variance_empty_list(self, stats):
        """Test that variance of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate variance of empty list"):
            stats.variance([])

    @pytest.mark.unit
    def test_variance_single_element_sample(self, stats):
        """Test that sample variance with single element raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate sample variance with only one data point"):
            stats.variance([5], sample=True)

    @pytest.mark.unit
    def test_variance_single_element_population(self, stats):
        """Test that population variance with single element returns 0."""
        assert stats.variance([5], sample=False) == 0.0

    # Test standard deviation
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,sample,expected", [
        ([1, 2, 3, 4, 5], True, math.sqrt(2.5)),
        ([1, 2, 3, 4, 5], False, math.sqrt(2.0)),
        ([10, 10, 10], True, 0.0),
        ([2, 4, 6, 8], False, math.sqrt(5.0)),
    ])
    def test_standard_deviation(self, stats, numbers, sample, expected):
        """Test standard deviation calculation with various inputs."""
        assert stats.standard_deviation(
            numbers, sample) == pytest.approx(expected)

    # Test range
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,expected", [
        ([1, 2, 3, 4, 5], 4),
        ([10], 0),
        ([1, 100], 99),
        ([-5, 5], 10),
        ([1.5, 2.5, 3.5], 2.0),
    ])
    def test_range_value(self, stats, numbers, expected):
        """Test range calculation with various inputs."""
        assert stats.range_value(numbers) == pytest.approx(expected)

    @pytest.mark.unit
    def test_range_empty_list(self, stats):
        """Test that range of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate range of empty list"):
            stats.range_value([])

    # Test percentile
    @pytest.mark.unit
    @pytest.mark.parametrize("numbers,p,expected", [
        ([1, 2, 3, 4, 5], 0, 1),
        ([1, 2, 3, 4, 5], 50, 3),
        ([1, 2, 3, 4, 5], 100, 5),
        ([1, 2, 3, 4, 5], 25, 2),
        ([1, 2, 3, 4, 5], 75, 4),
        ([10, 20, 30, 40, 50], 50, 30),
    ])
    def test_percentile(self, stats, numbers, p, expected):
        """Test percentile calculation with various inputs."""
        assert stats.percentile(numbers, p) == pytest.approx(expected)

    @pytest.mark.unit
    def test_percentile_empty_list(self, stats):
        """Test that percentile of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate percentile of empty list"):
            stats.percentile([], 50)

    @pytest.mark.unit
    @pytest.mark.parametrize("p", [-1, 101, 150])
    def test_percentile_invalid_p(self, stats, p):
        """Test that invalid percentile values raise ValueError."""
        with pytest.raises(ValueError, match="Percentile must be between 0 and 100"):
            stats.percentile([1, 2, 3], p)

    # Test with mixed positive and negative numbers
    @pytest.mark.unit
    def test_statistics_with_mixed_numbers(self, stats):
        """Test statistical functions with mixed positive and negative numbers."""
        numbers = [-10, -5, 0, 5, 10]
        assert stats.mean(numbers) == 0.0
        assert stats.median(numbers) == 0
        assert stats.range_value(numbers) == 20

    # Test with floating point numbers
    @pytest.mark.unit
    def test_statistics_with_floats(self, stats):
        """Test statistical functions with floating point numbers."""
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
        assert stats.mean(numbers) == pytest.approx(3.3)
        assert stats.variance(
            numbers, sample=False) == pytest.approx(2.42, rel=1e-2)
