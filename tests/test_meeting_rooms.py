import unittest
from solutions.meeting_rooms import Solution, Solution2, Solution3


class TestMeetingRooms(unittest.TestCase):
    def test_meeting_rooms(self):
        solution = Solution()
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertFalse(solution.can_attend_meetings(intervals))

        intervals = [[7, 10], [2, 4]]
        self.assertTrue(solution.can_attend_meetings(intervals))

    def test_meeting_rooms2(self):
        solution = Solution2()
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(2, solution.min_meeting_rooms(intervals))

        intervals = [[7, 10], [2, 4]]
        self.assertEqual(1, solution.min_meeting_rooms(intervals))

    def test_meeting_rooms3(self):
        solution = Solution3()
        n = 2
        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        self.assertEqual(0, solution.most_booked(n, meetings))

        n = 3
        meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        self.assertEqual(1, solution.most_booked(n, meetings))
