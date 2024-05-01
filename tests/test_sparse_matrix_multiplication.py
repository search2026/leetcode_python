import unittest
from solutions.sparse_matrix_multiplication import Solution


class TestSparseMatrixMultiplication(unittest.TestCase):
    def test_sparse_matrix_multiplication(self):
        solution = Solution()
        mat1 = [[1, 0, 0], [-1, 0, 3]]
        mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
        expect = [[7, 0, 0], [-7, 0, 3]]
        actual = solution.multiply(mat1, mat2)
        self.assertCountEqual(actual, expect)

        mat1 = [[0]]
        mat2 = [[0]]
        expect = [[0]]
        actual = solution.multiply(mat1, mat2)
        self.assertCountEqual(actual, expect)
