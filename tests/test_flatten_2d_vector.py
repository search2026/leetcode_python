import unittest
from solutions.flatten_2d_vector import Vector2D


class TestTwoSum(unittest.TestCase):
    def test_flatten_2d_vector(self):
        vector_2d = Vector2D([[1, 2], [3], [4]])
        vector_2d.next()
        vector_2d.next()
        vector_2d.next()
        self.assertTrue(vector_2d.hasNext())
        vector_2d.next()
        self.assertFalse(vector_2d.hasNext())
