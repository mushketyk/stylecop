# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
from config.parsers.StringParser import StringParser
from config.ConfigParsingException import ConfigParsingException

class  StringParserTest(unittest.TestCase):   

    def setUp(self):
        self.parser = StringParser()    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testWS(self):
        string = '   abcd   '
        expected = 'abcd'
        result = self.parser.parse(string)
        self.assertEquals(result, expected, '')

    def testNoWS(self):
        string = "  ' ab  cd ' "
        expected = ' ab  cd '
        result = self.parser.parse(string)
        self.assertEquals(result, expected, '')

    def testErrorString(self):
        self.assertRaises(ConfigParsingException, self.parser.parse, "  'asdf ads " )
       

if __name__ == '__main__':
    unittest.main()


