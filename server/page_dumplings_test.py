import unittest
import page_dumplings

class TestDumplings(unittest.TestCase):

    def test_dumplings(self):
        self.assertEqual(page_dumplings.recipe().index(page_dumplings.name), 715)

if __name__ == '__main__':
    unittest.main()
