
__author__="proger"
__date__ ="$Jan 31, 2011 6:58:31 PM$"

#Python lex/yacc module
import ply.lex

# Abstract class for parsers for different types in config file.
# Each class that inherits this one
# should define tokens, regular expressions for these tokens,
# error function etc for analyser created in __init__
class AbstractParser:
    def __init__(self):
        # Creating lexical analyzer
        self.lexer = ply.lex.lex(module = self)

    # Parse stringToParse into object that this parser is able to parse
    def getValue(self, stringToParse):
        raise NotImplementedError('Abstract method')

