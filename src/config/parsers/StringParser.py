# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 6:13:53 PM$"

# from ply.lex import LexError
from config.parsers.AbstractParser import AbstractParser


# Parser for string in config file. String can be either:
#   attribute = value
# or
#   attribute = 'long value'
class StringParser(AbstractParser):

    def p_string(self, p):
        """
            string : WS_STRING
                   | NOWS_STRING
        """
        self.result = p[1]

    def __init__(self):
        AbstractParser.__init__(self)

    def _parse(self, stringToParse):
        self.parser.parse(stringToParse)

        return self.result
