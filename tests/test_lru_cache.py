import unittest
from solutions.lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.put(3, 3)
        self.assertEqual(lru_cache.get(2), -1)
        lru_cache.put(4, 4)
        self.assertEqual(lru_cache.get(3), 3)
        self.assertEqual(lru_cache.get(4), 4)
        self.assertEqual(lru_cache.get(1), -1)

