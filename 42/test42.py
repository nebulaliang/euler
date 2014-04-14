from problem42 import *
import unittest  
  
class AreaTestCase(unittest.TestCase):  
    # generate certain size of triangle numbers and test isTriangle function
    def testIsTriangle(self):
        bound = 10000
        triangle = [n*(n+1)/2 for n in xrange(1, bound)]
        for n in triangle:
            self.assertEqual(isTriangle(n), True)
        
        triangle = [1+n*(n+1)/2 for n in xrange(1, bound)]
        for n in triangle:
            self.assertEqual(isTriangle(n), False)
            
    # test the wordValue function        
    def testWordValue(self):
        self.assertEquals(wordValue('SKY'), 55)
        self.assertEquals(wordValue('A'), 1)
        self.assertEquals(wordValue('Z'), 26)
        self.assertEquals(wordValue('ABC'), 6)
        
if __name__ == "__main__":  
    unittest.main()  