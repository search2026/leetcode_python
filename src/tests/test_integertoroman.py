from src.solutions.integertoroman import Solution

solution = Solution()

def test_integertoroman():
    num = 3
    expect = 'III'
    actual = solution.int_to_roman(num)
    assert actual == expect

    num = 58
    expect = 'LVIII'
    actual = solution.int_to_roman(num)
    assert actual == expect

    num = 1994
    expect = 'MCMXCIV'
    actual = solution.int_to_roman(num)
    assert actual == expect
