# tests/test_mymodule.py

import unittest
from mylibrary.mymodule import hello_world

class TestMyModule(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()
