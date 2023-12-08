import unittest
from triangle_def import Triangle

# define test
class TestAreaofRectangle(unittest.TestCase):
    def runTest(self):
        triangle = Triangle(4, 10)
        self.assertEqual(triangle.get_area(), 25, "incorrect area")
 
# run test
unittest.main()