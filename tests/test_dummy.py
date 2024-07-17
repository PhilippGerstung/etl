import math
import random

import pytest


@pytest.mark.parametrize("j", list(range(1000)))
def test_dummy(j):
    random_int: int = random.randint(int(1e6), int(1e7))
    sum(i * i for i in range(int(random_int)))
    assert math.sqrt(897239852) != j
