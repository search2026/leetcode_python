import unittest
from solutions.find_median_from_data_stream import MedianFinder


class TestFindMedianFromDataStream(unittest.TestCase):
    def test_find_median_from_data_stream(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        expect = 1.5
        actual = median_finder.findMedian()
        self.assertEqual(expect, actual)

        median_finder.addNum(3)
        expect = 2
        actual = median_finder.findMedian()
        self.assertEqual(expect, actual)
