# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 6:13:53 PM$"

# from ply.lex import LexError
from config.parsers.AbstractParser import AbstractParser


# TODO Add unit tests
class StringParser(AbstractParser):
   

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
