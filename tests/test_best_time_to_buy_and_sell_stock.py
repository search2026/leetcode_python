import unittest
from solutions.best_time_to_buy_and_sell_stock import Solution, Solution2, Solution3
from solutions.best_time_to_buy_and_sell_stock import Solution4, Solution5, Solution6


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        solution = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        expect = 5
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [7, 6, 4, 3, 1]
        expect = 0
        actual = solution.max_profit(prices)
        assert actual == expect

    def test_best_time_to_buy_and_sell_stock_2(self):
        solution = Solution2()
        prices = [7, 1, 5, 3, 6, 4]
        expect = 7
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [1, 2, 3, 4, 5]
        expect = 4
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [7, 6, 4, 3, 1]
        expect = 0
        actual = solution.max_profit(prices)
        assert actual == expect

    def test_best_time_to_buy_and_sell_stock_3(self):
        solution = Solution3()
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expect = 6
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [1, 2, 3, 4, 5]
        expect = 4
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [7, 6, 4, 3, 1]
        expect = 0
        actual = solution.max_profit(prices)
        assert actual == expect

    def test_best_time_to_buy_and_sell_stock_4(self):
        solution = Solution4()
        k = 2
        prices = [2, 4, 1]
        expect = 2
        actual = solution.max_profit(k, prices)
        assert actual == expect

        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        expect = 7
        actual = solution.max_profit(k, prices)
        assert actual == expect

    def test_best_time_to_buy_and_sell_stock_5(self):
        solution = Solution5()
        prices = [1, 2, 3, 0, 2]
        expect = 3
        actual = solution.max_profit(prices)
        assert actual == expect

        prices = [1]
        expect = 0
        actual = solution.max_profit(prices)
        assert actual == expect

    def test_best_time_to_buy_and_sell_stock_6(self):
        solution = Solution6()
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        expect = 8
        actual = solution.max_profit(prices, fee)
        assert actual == expect

        prices = [1, 3, 7, 5, 10, 3]
        fee = 3
        expect = 6
        actual = solution.max_profit(prices, fee)
        assert actual == expect
