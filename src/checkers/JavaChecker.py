# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="sveta"
__date__ ="$Feb 8, 2011 1:41:46 PM$"

import ply
import ply.lex
import ply.yacc

import checkers
from checkers.AbstractChecker import AbstractChecker

class JavaChecker(AbstractStringChecker):
    tokens = (
        'LONGLITERAL',
        'INTLITERAL',
        'HEXLITERAL',
        'FLOATLITERAL',
        'DOUBLELITERAL',
        'CHARLITERAL',
        'STRINGLITERAL',
        'ONEROWCOMMENT',
        'MULTIROWCOMMENT',
        'ELLIPSIS',
        'EQEQ',
        'AMPAMP',
        'BARBAR',
        'PLUSPLUS',
        'SUBSUB',
        'PLUSEQ',
        'SUBEQ',
        'STAREQ',
        'SLASHEQ',
        'AMPEQ',
        'BAREQ',
        'CARETEQ',
        'PERCENTEQ',
        'BANGEQ'
    )

    
    reserved = {
        'abstract':'ABSTRACT',
        'assert':'ASSERT',
        'boolean':'BOOLEAN',
        'break':'BREAK',
        'byte':'BYTE',
        'catch':'CATCH',
        'char':'CHAR',
        'class':'CLASS',
        'const':'CONST',
        'continue':'CONTINUE',
        'default':'DEFAULT',
        'do':'DO',
        'double':'DOUBLE',
        'else':'ELSE',
        'enum':'ENUM',
        'extends':'EXTENDS',
        'false':'FALSE',
        'final':'FINAL',
        'finally':'FINALLY',
        'float':'FLOAT',
        'for':'FOR',
        'goto':'GOTO',
        'if':'IF',
        'implements':'IMPLEMENTS',
        'import':'IMPORT',
        'int':'INT',
        'interface':'INTERFACE',
        'long':'LONG',
        'native':'NATIVE',
        'new':'NEW',
        'null':'NULL',
        'package':'PACKAGE',
        'private':'PRIVATE',
        'protected':'PROTECTED',
        'public':'PUBLIC',
        'return':'RETURN',
        'short':'SHORT',
        'static':'STATIC',
        'strictfp':'STRICTFP',
        'super':'SUPER',
        'switch':'SWITCH',
        'synchronized':'SYNCHRONIZED',
        'this':'THIS',
        'throw':'THROW',
        'throws':'THROWS',
        'transient':'TRANSIENT',
        'try':'TRY',
        'true':'TRUE',
        'void':'VOID',
        'volatile':'VOLATILE',
        'while':'WHILE'
    }
    literals = ['(',')','{','}','[',']',';',':','.','=','!','~','?','+',
    '-','*','/','&','|','^','%','@','>','<']

    t_ELLIPSIS = r"\.\.\."
    t_EQEQ = r"=="
    t_AMPAMP = r"&&"
    t_BARBAR = r"\|\|"
    t_PLUSPLUS = r"\+\+"
    t_SUBSUB = r"--"
    t_PLUSEQ = r"\+="
    t_SUBEQ = r"-="
    t_STAREQ = r"\*="
    t_SLASHEQ = r"/="
    t_AMPEQ = r"&="
    t_BAREQ = r"\|="
    t_CARETEQ = r"\^="
    t_PERCENTEQ = r"%="
    t_BANGEQ = r"!="

    tokens = ['LONGLITERAL','INTLITERAL','HEXLITERAL','FLOATLITERAL','DOUBLELITERAL','CHARLITERAL','STRINGLITERAL','ONEROWCOMMENT',
    'MULTIROWCOMMENT','ELLIPSIS','EQEQ','AMPAMP','BARBAR','PLUSPLUS','SUBSUB','PLUSEQ','SUBEQ','STAREQ',
    'SLASHEQ','AMPEQ','BAREQ','CARETEQ','PERCENTEQ','BANGEQ'] + list(reserved.values())

    def t_LONGLITERAL(self,t):
        r"(\d)+(l|L)"
        return t

    def t_INTLITERAL(self,t):
        r"0|([1-9]\d*)"
        return t

    def t_HEXLITERAL(self,t):
        r"(0[0-7]+)|((0x|0X)(\d|[a-f]|[A-F])+)"
        return t

    def t_FLOATLITERAL(self,t):
        r"\d+\.\d*([eE][+\-]?\d+)([fF]?)"
        return t
    
    def t_DOUBLELITERAL(self,t):
        r"\d+\.\d*([eE][+\-]?\d+)([dD]?)"
        return t

    def t_CHARLITERAL(self,t):
        r"'\w'"
        return t
    
    def t_STRINGLITERAL(self,t):
        r"'([a-zA-Z0-9]|(\s)*)*'"
        return t
    
    def t_ONEROWCOMMENT(self,t):
        r"//.*"
        pass

    def t_MULTIROWCOMMENT(self,t):
        r"/\*.*\*/"
        pass

    def __init(self, config):
        AbstractStringChecker.__init__(self, config)

    def doStringCheck(self, stringSource):
        return []

if __name__ == "__main__":
    pass


