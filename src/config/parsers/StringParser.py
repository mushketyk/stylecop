# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 6:13:53 PM$"

from ply.lex import LexError
from AbstractParser import AbstractParser

# TODO Add unit tests
class StringParser(AbstractParser):
    tokens = (
        'WS_STRING',  # String with whitespaces like param = 'text value'
        'NOWS_STRING' # String with no whitespaces like param = value
    )

    def t_WS_STRING(self, t):
        r"'((\S)|(\s))*'"
        t.value = t.value.strip("'").strip()
        return t

    def t_NOWS_STRING(self, t):
        r"(\S)+"
        return t

    def t_error(self, t):
        # TODO Use logger instead of print
        errorMessage = "Error parsing string " + str(self.stringToParse)
        print(errorMessage)
        raise ValueError(errorMessage)

    def __init__(self):
        AbstractParser.__init__(self)

    def getValue(self, stringToParse):
        self.stringToParse = stringToParse
        trimed = stringToParse.strip()

        self.lexer.input(trimed)
        return self.lexer.next()


if __name__ == "__main__":
    import sys
    sp = StringParser()
    val = sp.getValue("'asa bcd'   ")
    print(val)
