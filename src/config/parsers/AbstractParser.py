
__author__="proger"
__date__ ="$Jan 31, 2011 6:58:31 PM$"

#Python lex/yacc module
import ply.lex
from config.ConfigParsingException import ConfigParsingException

# Abstract class for parsers for different types in config file.
# Each class that inherits this one
# should define tokens, regular expressions for these tokens,
# error function etc for analyser created in __init__
class AbstractParser:
    tokens = (
              'WS_STRING', # String with whitespaces like param = 'text value'
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
        # Creating lexical analyzer
        self.lexer = ply.lex.lex(module=self)

    # Parse stringToParse into object that this parser is able to parse
    def parse(self, stringToParse):
        raise NotImplementedError('Abstract method')

