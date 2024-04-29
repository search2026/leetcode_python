import unittest
from solutions.course_schedule import Solution, Solution2, Solution3, Solution4


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule(self):
        solution = Solution()
        num_courses = 2
        prerequisites = [[1, 0]]
        self.assertTrue(solution.can_finish(num_courses, prerequisites))

        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(solution.can_finish(num_courses, prerequisites))

    def test_course_schedule2(self):
        solution = Solution2()
        num_courses = 2
        prerequisites = [[1, 0]]
        expect = [0, 1]
        actual = solution.find_order(num_courses, prerequisites)
        self.assertEqual(expect, actual)

        num_courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        # expect = [0, 2, 1, 3]
        expect = [0, 1, 2, 3]
        actual = solution.find_order(num_courses, prerequisites)
        self.assertEqual(expect, actual)

        num_courses = 1
        prerequisites = []
        expect = [0]
        actual = solution.find_order(num_courses, prerequisites)
        self.assertEqual(expect, actual)

    def test_course_schedule3(self):
        solution = Solution3()
        courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        expect = 3
        actual = solution.schedule_course(courses)
        self.assertEqual(expect, actual)

        courses = [[1, 2]]
        expect = 1
        actual = solution.schedule_course(courses)
        self.assertEqual(expect, actual)

        courses = [[3, 2], [4, 3]]
        expect = 0
        actual = solution.schedule_course(courses)
        self.assertEqual(expect, actual)

    def test_course_schedule4(self):
        solution = Solution4()
        num_courses = 2
        prerequisites = [[1, 0]]
        queries = [[0, 1], [1, 0]]
        expect = [False, True]
        actual = solution.check_if_prerequisite(num_courses, prerequisites, queries)
        self.assertEqual(expect, actual)

        num_courses = 2
        prerequisites = []
        queries = [[1, 0], [0, 1]]
        expect = [False, False]
        actual = solution.check_if_prerequisite(num_courses, prerequisites, queries)
        self.assertEqual(expect, actual)

        num_courses = 3
        prerequisites = [[1, 2], [1, 0], [2, 0]]
        queries = [[1, 0], [1, 2]]
        expect = [True, True]
        actual = solution.check_if_prerequisite(num_courses, prerequisites, queries)
        self.assertEqual(expect, actual)
