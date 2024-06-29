import pytest
from problem_13_romanToInt import Solution


@pytest.mark.parametrize(
    "given, want",
    (
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("DCXXI", 621),
        ("MCMXCVI", 1996),
    ),
)
def test_romanToInt(given: str, want: int) -> None:
    solution = Solution()
    got = solution.romanToInt(given)
    assert got == want
