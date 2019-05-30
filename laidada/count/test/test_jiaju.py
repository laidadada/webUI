import unittest


class TestUnitTestDemo02(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "5"
    @classmethod
    def tearDownClass(cls):
        print "6"
    def setUp(self):
        print "3"
    def tearDown(self):
        print "4"
    def test_print01(self):
        print "1"
    def test_print02(self):
        print "2"

if __name__ == '__main__':
    unittest.main()
