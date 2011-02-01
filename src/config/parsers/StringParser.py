# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 6:13:53 PM$"

# from ply.lex import LexError
from config.parsers.AbstractParser import AbstractParser
from config.ConfigParsingException import ConfigParsingException

# TODO Add unit tests
class StringParser(AbstractParser):
    tokens = (
        'WS_STRING',  # String with whitespaces like param = 'text value'
        'NOWS_STRING' # String with no whitespaces like param = value
    )

    def t_WS_STRING(self, t):
        r"'((\S)|(\s))*'"
        t.value = t.value.strip("'")
        return t

    def t_NOWS_STRING(self, t):
        r"[^ \t\n\r\f\v']+"
        return t

    def t_error(self, t):
        # TODO Use logger instead of print
        errorMessage = "Error parsing string " + str(self.stringToParse)
        print(errorMessage)
        raise ConfigParsingException(errorMessage)

    def __init__(self):
        AbstractParser.__init__(self)

    def parse(self, stringToParse):
        self.stringToParse = stringToParse
        trimed = stringToParse.strip()

        self.lexer.input(trimed)
        token = self.lexer.next()
        return token.value



if __name__ == "__main__":
    import sys
    sp = StringParser()
    val = sp.parse("'asa bcd   ")
    print(val)
