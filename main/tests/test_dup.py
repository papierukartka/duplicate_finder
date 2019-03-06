import unittest
import dup
from tests.mocks import DataMock
class TestDup(unittest.TestCase):
    def setUp(self):
        self.rootdir = "../rootdir"
        self.maxDiff = None

    def test_walk_recursively(self):
        self.assertEqual(dup.walk_recursively(self.rootdir), DataMock.walk_recursively(self))

    def test_rm_duplicates(self):
        self.assertEqual(dup.rm_duplicates(self.rootdir), DataMock.rm_duplicates(self))