from main import calculate_statistics
import pytest

def test_calculate_statistics():
    numbers = [1, 2, 3, 4, 5]
    mean, std_dev = calculate_statistics(numbers)
    assert mean == 3.0
    assert std_dev == pytest.approx(1.414, abs=0.01)
