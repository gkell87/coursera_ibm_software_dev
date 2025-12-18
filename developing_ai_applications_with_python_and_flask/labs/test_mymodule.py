# Import unittest with the module script and functions
import unittest
from mymodule import square, double, add

# define a test case class for testing
class TestSquare(unittest.TestCase):

    # define test method for square function
    def test1(self):

        # check that calling square of 2 returns 4
        self.assertEqual(square(2), 4)

        # check that calling square of 3.0 returns 9.0
        self.assertEqual(square(3.0), 9.0)

        # check that scalling square of -3 does not return -9
        self.assertNotEqual(square(-3), -9)

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

# define a test case for the add function
class TestAdd(unittest.TestCase):

    # define a test for the add function
    def test1(self):

        # check that calling a add of 2 and 4 gets 6
        self.assertEqual(add(2, 4), 6)

        # check that calling a add of 0 and 0 gets 0
        self.assertEqual(add(0, 0), 0)

        # check if calling a add of 2.3 and 3.6 gets 5.9
        self.assertEqual(add(2.3, 3.6), 5.9)

        # check if calling a add of Hello and World gets Hello World
        self.assertEqual(add('Hello ', 'World'), 'Hello World')

        # check if calling a add of -2 and -2 does not get 0
        self.assertNotEqual(add(-2, -2), 0)

# run all test cases
unittest.main()





