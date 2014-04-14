from problem14 import *
import unittest  
  
class AreaTestCase(unittest.TestCase):  
    # test numOfChain functon
    def testNumOfChain(self):
        self.assertEqual(numOfChain(1),1)
        self.assertEqual(numOfChain(2),2)
        self.assertEqual(numOfChain(4),3)
        self.assertEqual(numOfChain(8),4)
        self.assertEqual(numOfChain(16),5)
        self.assertEqual(numOfChain(5),6)
        self.assertEqual(numOfChain(10),7)
        self.assertEqual(numOfChain(20),8)
        self.assertEqual(numOfChain(40),9)
        self.assertEqual(numOfChain(13),10)
        
if __name__ == "__main__":  
    unittest.main()  