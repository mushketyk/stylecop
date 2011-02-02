from config.parsers.AbstractParser import AbstractParser

__author__="proger"
__date__ ="$Feb 1, 2011 7:13:16 PM$"

from config.parsers.AbstractParser import AbstractParser

# Array parser for config. It handle attributes like:
#   value = ['c', 'cpp', 'java']
# Elements in array can be string with whitespace symbols like:
#   'long line'
# or whithout them like:
#   line
class ArrayParser(AbstractParser):
    # Literals for ply that can be used as single character literals
    literals = ['[', ',', ']']

    # Rule for array
    def p_array(self, p):
        """
            array : '[' elements ']'
        """
        return p

    # Rule for array elements
    def p_elements(self, p):
        """
            elements : element
                     | element ',' elements
                     | empty
        """
        element = p[1]
        # If array is empty element can be None
        if element != None:
            self.result.insert(0, p[1] )
        return p

    # Rule for array element
    def p_element(self, p):
        """
            element : WS_STRING
                    | NOWS_STRING
        """
        # At this place p[1] is a value that was returned by lexical analyzator
        # and contains element that can be added to result list
        p[0] = p[1]

    def __init__(self):
        AbstractParser.__init__(self)
        self.result = []

    def _parse(self, stringToParse):
        self.parser.parse(stringToParse)

        return self.result

