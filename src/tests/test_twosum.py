from src.solutions.twosum import Solution

solution = Solution()


def test_twoSum():
  nums = [2, 7, 11, 15]
  target = 9
  expect = [0, 1]
  acutal = solution.two_sum(nums, target)
  assert acutal == expect
