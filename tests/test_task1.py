import pytest

from ..task1 import process_grades


@pytest.mark.parametrize(
    "records, expect",
    [
        (
            [
                "Иванов: 85",
                "Петров: 42",
                "Сидоров: abc",
                "Козлов: 90",
                ": 55",
                "Иванов: 70",
            ],
            {
                "valid_count": 4,
                "average": 71.8,
                "passed": ["Иванов", "Козлов"],
                "skipped": 2,
            },
        ),
        (
            ["Иван: 5", "Пв: 4", ": abc", "К: 0", "12: 55", "Иванов: 0"],
            {
                "valid_count": 3,
                "average": 3,
                "passed": [],
                "skipped": 3,
            },
        ),
    ],
)
def test_process_grades(records, expect):
    assert process_grades(records) == expect
