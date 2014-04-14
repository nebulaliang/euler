from problem55 import *
import unittest  
  
class AreaTestCase(unittest.TestCase):  
    # test reverseInt functon
    def testReverseInt(self):
        self.assertEqual(reverseInt(123),321)
        self.assertEqual(reverseInt(120),21)
        self.assertEqual(reverseInt(121),121)
        
    # test isPalindromic
    def testIsPalindromic(self):
        self.assertEqual(isPalindromic(121),True)
        self.assertEqual(isPalindromic(12121),True)
        self.assertEqual(isPalindromic(123),False)
        self.assertEqual(isPalindromic(10),False)
        
    # test isLychrel function
    def testIsLychrel(self):
        self.assertEqual(isLychrel(10677,50),True)
        self.assertEqual(isLychrel(10677,53),False)
        self.assertEqual(isLychrel(196,50),True)
        self.assertEqual(isLychrel(47,2),False)
        self.assertEqual(isLychrel(349,3),False)
        self.assertEqual(isLychrel(349,2),True)
        
if __name__ == "__main__":  
    unittest.main()  