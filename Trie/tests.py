import unittest

from trie import Trie

class MyTest(unittest.TestCase):
    def test_trie(self):
        tr = Trie()
        words = ["Hello World", "Chinmaya", "Strange", "Things", "Will"]
        for x in words:
            tr.insert(x)

        self.assertTrue(tr.search("Hello World"))
        self.assertFalse(tr.search("Hii"))
        self.assertTrue(tr.search("Chinmaya"))
        self.assertTrue("Will")

if __name__ == '__main__':
    unittest.main()

