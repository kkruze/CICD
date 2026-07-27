import unittest

from hello import say_hello

class Testhello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World")
