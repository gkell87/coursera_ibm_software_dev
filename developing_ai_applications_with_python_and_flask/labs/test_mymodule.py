# Import unittest with the module script and functions
import unittest
from module import square, double

# define a test case class for testing
class TestSquare(unittest.TestCase):

    # define test method for square function
    def test1(self):

        # check that calling square of 2 returns 4
        self.assertEqual(square(2), 4)

        # check that calling square of 3.0 returns 9.0
        self.assertEqual(square(3.0), 9.0)

        # check that scalling square of -3 does not return -9
        self.asserNotequal(square(-3), -9)

# define a test case for the double function
class TestDouble(unittest.TestCase):

    # define a test for the double function
    def test1(self):

        # check that calling a double of 2 gets 4
        self.assertEqual(double(2), 4)

        # check that calling a double of -3.1 returns -6.2
        self.assertEqual(double(-3.1), -6.2)

        # check if properly computes 0
        self.assertEqual(double(0), 0)

# run all test cases
unittest.main()





