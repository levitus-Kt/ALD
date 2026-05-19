import pytest

from ..task2 import longest_increasing_streak


@pytest.mark.parametrize(
    "nums, expect",
    [
        (
            [1, 2, 3],
            {"length": 3, "streak": [1, 2, 3]},
        ),
        (
            [1, 3, 2, 5, 8, 4, 7],
            {"length": 3, "streak": [2, 5, 8]},
        ),
        (
            [],
            {"length": 0, "streak": []},
        ),
        (
            [3],
            {"length": 0, "streak": []},
        ),
        (
            [8, 7, 4, 2],
            {"length": 0, "streak": []},
        ),
    ],
)
def test_process_grades(nums, expect):
    assert longest_increasing_streak(nums) == expect
