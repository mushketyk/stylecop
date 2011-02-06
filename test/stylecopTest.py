# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import stylecop

class  StylecopTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Stylecop()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testSpitArgv(self):
        argv = ["stylecop", "--repo", "svn", ".", "param1", "param2"]
        expected = (["stylecop", "--repo", "svn"], ["param1", "param2"])

        result = splitArgv(argv)
        self.assertEqual(expected, result, "msg")
        

if __name__ == '__main__':
    unittest.main()

