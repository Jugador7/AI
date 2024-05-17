import unittest

from mymodule import square, double, add

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4) #test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0) #test when 3.0 is given as input the output is 9.0.
        self.assertEqual(square(-3), 9) #test when -3 is given as input the output is -9.

class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) #test when 2 is given as input the output is 4. 
        self.assertEqual(double(-3.1), -6.2) #test when -3.1 is given as input the output is -6.2. 
        self.assertEqual(double(0), 0) #test when 0 is given as input the output is 0.

class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2,4), 6) #test when 2 and 4 are given as input the output is 6.
        self.assertEqual(add(0,0), 0) #test when -5.0 and 5.0 are given as input the output is 0.0. 
        self.assertEqual(add(2.3,3.6), 5.9) #test when -9 and -5 are given as input the output is -14.  
        self.assertEqual(add("hello ","world"), "hello world") #test when "hello " and "world" are given as input the output is "hello world".
        self.assertEqual(add(2.300,4.300), 6.6) #test when 2.3000 and 4.300 are given as input the output is 6.6.
        self.assertNotEqual(add(-2,-2), 0) #test when -2 and -2 are given as input the output is not 0.   

unittest.main()