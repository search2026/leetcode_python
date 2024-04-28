import unittest
from solutions.cheapest_flights_within_k_stops import Solution


class TestTwoSum(unittest.TestCase):
    def test_cheapest_flights_within_k_stops(self):
        solution = Solution()
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1
        expect = 700
        actual = solution.find_cheapest_price(n, flights, src, dst, k)
        self.assertEqual(expect, actual)

        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        expect = 200
        actual = solution.find_cheapest_price(n, flights, src, dst, k)
        self.assertEqual(expect, actual)

        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        expect = 500
        actual = solution.find_cheapest_price(n, flights, src, dst, k)
        self.assertEqual(expect, actual)
