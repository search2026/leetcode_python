import unittest
from solutions.jump_game import Solution, Solution2


class TestJumpGame(unittest.TestCase):
    def test_can_jump1(self):
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        expect = True
        actual = solution.canJump(nums)
        assert actual == expect

        nums = [3, 2, 1, 0, 4]
        expect = False
        actual = solution.canJump(nums)
        assert actual == expect

    def test_can_jump2(self):
        solution = Solution2()
        nums = [2, 3, 1, 1, 4]
        expect = True
        actual = solution.canJump(nums)
        assert actual == expect

        nums = [3, 2, 1, 0, 4]
        expect = False
        actual = solution.canJump(nums)
        assert actual == expect
