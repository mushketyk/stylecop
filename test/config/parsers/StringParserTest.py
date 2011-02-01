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
        self.assertEquals(self.parser.parse('   abcd   '), 'abcd', '')

    def testNoWS(self):
        self.assertEquals(self.parser.parse("  ' ab  cd ' "), ' ab  cd ', '')

    def testErrorString(self):
        self.assertRaises(ConfigParsingException, self.parser.parse, "  'asdf ads " )
       

if __name__ == '__main__':
    unittest.main()


