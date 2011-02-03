# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

from config.parsers.ArrayParser import ArrayParser
from config.ConfigParsingException import ConfigParsingException

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

    def testEmptyArray(self):
        input = "[]"
        result = self.parser.parse(input)
        expected = []

        self.assertEqual(result, expected, "")

    def testWrongString(self):
        input = "[3, 4, 'asdf 123 ]"
        parser = self.parser
        self.assertRaises(ConfigParsingException, parser.parse, input)

    def testWrongArray(self):
        input = "[3, 4"
        parser = self.parser
        self.assertRaises(ConfigParsingException, parser.parse, input)

if __name__ == '__main__':
    unittest.main()

