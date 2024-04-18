from src.solutions.romantointeger import Solution

solution = Solution()


def test_romantointeger():
    s = 'III'
    expect = 3
    actual = solution.roman_to_int(s)
    assert actual == expect

    s = 'LVIII'
    expect = 58
    actual = solution.roman_to_int(s)
    assert actual == expect

    s = 'MCMXCIV'
    expect = 1994
    actual = solution.roman_to_int(s)
    assert actual == expect
