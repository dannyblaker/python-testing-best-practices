"""
Statistics module for statistical calculations.
"""
import math
from typing import List, Union


class Statistics:
    """A class for performing statistical calculations."""

    @staticmethod
    def mean(numbers: List[Union[int, float]]) -> float:
        """Calculate the arithmetic mean of a list of numbers.

        Args:
            numbers: List of numbers

        Returns:
            The mean value

        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the median of a list of numbers.

        Args:
            numbers: List of numbers

        Returns:
            The median value

        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")

        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)

        if n % 2 == 0:
            return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        else:
            return sorted_numbers[n // 2]

    @staticmethod
    def mode(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
        """Calculate the mode(s) of a list of numbers.

        Args:
            numbers: List of numbers

        Returns:
            List of mode values (can be multiple if there's a tie)

        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")

        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1

        max_frequency = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq ==
                 max_frequency]

        return sorted(modes)

    @staticmethod
    def variance(numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate the variance of a list of numbers.

        Args:
            numbers: List of numbers
            sample: If True, calculate sample variance (n-1), otherwise population variance (n)

        Returns:
            The variance

        Raises:
            ValueError: If the list is empty or has only one element for sample variance
        """
        if not numbers:
            raise ValueError("Cannot calculate variance of empty list")
        if sample and len(numbers) == 1:
            raise ValueError(
                "Cannot calculate sample variance with only one data point")

        mean_value = Statistics.mean(numbers)
        squared_diffs = [(x - mean_value) ** 2 for x in numbers]
        divisor = len(numbers) - 1 if sample else len(numbers)

        return sum(squared_diffs) / divisor

    @staticmethod
    def standard_deviation(numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate the standard deviation of a list of numbers.

        Args:
            numbers: List of numbers
            sample: If True, calculate sample std dev, otherwise population std dev

        Returns:
            The standard deviation

        Raises:
            ValueError: If the list is empty or has only one element for sample std dev
        """
        return math.sqrt(Statistics.variance(numbers, sample))

    @staticmethod
    def range_value(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the range (max - min) of a list of numbers.

        Args:
            numbers: List of numbers

        Returns:
            The range value

        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate range of empty list")
        return max(numbers) - min(numbers)

    @staticmethod
    def percentile(numbers: List[Union[int, float]], p: float) -> float:
        """Calculate the p-th percentile of a list of numbers.

        Args:
            numbers: List of numbers
            p: Percentile value (0-100)

        Returns:
            The percentile value

        Raises:
            ValueError: If the list is empty or p is not between 0 and 100
        """
        if not numbers:
            raise ValueError("Cannot calculate percentile of empty list")
        if not 0 <= p <= 100:
            raise ValueError("Percentile must be between 0 and 100")

        sorted_numbers = sorted(numbers)
        k = (len(sorted_numbers) - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return sorted_numbers[int(k)]

        d0 = sorted_numbers[int(f)] * (c - k)
        d1 = sorted_numbers[int(c)] * (k - f)
        return d0 + d1
