
__author__="proger"
__date__ ="$Jan 31, 2011 6:58:31 PM$"

#Python lex/yacc module
import ply.lex
import ply.yacc
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

    # Symbols that will be skiped by lexical analyzator
    t_ignore = " \t"

    def t_WS_STRING(self, t):
        r"'([a-zA-Z0-9]|(\s))*'"
        t.value = t.value.strip("'")
        return t

    def t_NOWS_STRING(self, t):
        r"[a-zA-Z0-9]+"
        return t

    # Error handler for lex
    def t_error(self, t):
        # TODO Use logger instead of print
        token = t.value if t else ""
        errorMessage = "Lex error during parsing string " + str(self.stringToParse) + token
        print(errorMessage)
        raise ConfigParsingException(errorMessage)

    # Rule for empty token
    def p_empty(self, p):
        'empty :'
        pass

    # Error handler for yacc
    def p_error(self, p):
        # TODO Use logger instead of print
        value = p.value if p else ""
        errorMessage = "Yacc error during parsing string " + str(self.stringToParse) + " at " + value
        print(errorMessage)
        raise ConfigParsingException(errorMessage)

    def __init__(self):
        # Creating lexical analyzer
        self.lexer = ply.lex.lex(module=self)
        # Create yacc
        self.parser = ply.yacc.yacc(module=self)

    # Parse stringToParse into object that this parser is able to parse
    def parse(self, stringToParse):
        self.stringToParse = stringToParse
        trimed = stringToParse.strip()

        return self._parse(trimed)

    def _parse(self, stringToParse):
        raise NotImplementedError('Abstract method')

