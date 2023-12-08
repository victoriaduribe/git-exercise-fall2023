import unittest 
from triangle_def import Triangle # import class definition to be used for unit test 

# define test
class TestAreaofRectangle(unittest.TestCase): # test area of triangle
    def runTest(self):
        triangle = Triangle(4, 10) # give inputs for imported class definition (base, height) of triangle
        self.assertEqual(triangle.get_area(), 20, "incorrect area") # define test value and error message if fails
 
# run test
unittest.main() 