from funcScript import *
from nonfunctScript import *

import unittest


class MyTest(unittest.TestCase):
    def testHelloFunction(self):
        self.assertEqual(hello("travis"), "Hello travis")
    def testGoodbyeFunction(self):
        self.assertEqual(goodbye("travis"), "Goodbye travis")
