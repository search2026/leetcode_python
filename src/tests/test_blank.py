from src.solutions.blank import Solution

solution = Solution()


def test_method1():
  expect = 0
  acutal = solution.method()
  assert acutal == expect
