import unittest
import page_goulash

class TestGoulash(unittest.TestCase):

    def test_dumplings(self):
        self.assertEqual(page_goulash.recipe().index(page_goulash.name), 30)

if __name__ == '__main__':
    unittest.main()
