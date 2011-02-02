# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

from config.parsers.ArrayParser import ArrayParser

class  ArrayParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = ArrayParser()
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testArrayWithElements(self):
        input = "[ 1 , 2 , 'abc abc' ]"
        result = self.parser.parse(input)
        expected = ["1", "2", "abc abc"]

        self.assertEqual(result, expected, "")

if __name__ == '__main__':
    unittest.main()

