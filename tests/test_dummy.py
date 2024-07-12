import math
import pytest
import random

@pytest.mark.parametrize(
    "j",
    [j for j in range(1000)]
)
def test_dummy(j):
    l = random.randint(int(1e6), int(1e7))
    result1 = sum(i * i for i in range(int(l)))
    assert math.sqrt(897239852) != j