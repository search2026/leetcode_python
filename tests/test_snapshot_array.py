import unittest
from solutions.snapshot_array import SnapshotArray


class TestSnapshotArray(unittest.TestCase):
    def test_snapshot_array(self):
        snapshot = SnapshotArray(3)
        snapshot.set(0, 5)
        snapshot.snap()
        snapshot.set(0, 6)
        self.assertEqual(snapshot.get(0, 0), 5)
