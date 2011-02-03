# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="sveta"
__date__ ="$Feb 3, 2011 10:44:33 AM$"

from config.parsers.AbstractParser import AbstractParser

# Dictionary parser for config. It handles attributes like:
#attr: { key_1 = 'value1', key_2 = 'value2', key_n = 'valuen'}

class DictionaryParser(AbstractParser):
    literals=['{','=',',','}']

    def p_dictionary(self,p):
        """
            dictionary : '{' pairs '}'
        """
        return p

    def p_pairs(self,p):
        """
            pairs: pair
                 | pair ',' pairs
                 | empty
        """
        pair = p[1]

        if pair != None:
            self.result.insert(0,p[1])
        return p

    def p_pair(self,p):
        """
            pair: key '=' value
        """
        return p

    def p_key(self,p):
        """
            key: NOWS_STRING
        """
        p[0]=p[1]

    def p_value(self,p):
        """
            value: WS_STRING
                 | NOWS_STRING
        """
        p[0]=p[1]
        
    def __init__(self):
        AbstractParser.__init__(self)
        self.result = []

    def _parse(self, stringToParse):
        self.parser.parse(stringToParse)

        return self.result