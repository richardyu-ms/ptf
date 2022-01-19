from ptf.base_tests import BaseTest
"""
This class is the test data for test group_mode_test.py
"""

class FrameworkTest(BaseTest):
    def setUp(self) -> None:
        print("FrameworkTest::setUp")
        
    def tearDown(self) -> None:
        print("FrameworkTest::setUp")
    
    def runTest(self):
        self.aTest()
        #self.bTest()
        self.cTest()
        
    def aTest(self):
        print("FrameworkTest::aTest")
        
    def bTest(self):
        print("FrameworkTest::bTest")
    
    def cTest(self):
        print("FrameworkTest::cTest")



class FrameworkTest2(BaseTest):
    def setUp(self) -> None:
        print("FrameworkTest2::setUp")
        
    def tearDown(self) -> None:
        print("FrameworkTest2::setUp")
    
    def runTest(self):
        self.aTest()
        #self.bTest()
        self.cTest()
        
    def aTest(self):
        print("FrameworkTest2::aTest")
        
    def bTest(self):
        print("FrameworkTest2::bTest")
    
    def cTest(self):
        print("FrameworkTest2::cTest")
