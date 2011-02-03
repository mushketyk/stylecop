__author__ = "proger"
__date__ = "$Jan 31, 2011 5:27:47 PM$"

import ply
import ply.lex
import ply.yacc

from config.ConfigSection import ConfigSection
from config.ConfigParsingException import ConfigParsingException

# Class that read config file
# Config file looks like:
#    globalAtribute = 'hello user';
#    globalArr = [1, 2, 'long value'];
#
#    [section] {
#        localDictionary = { a : 'long val', 'long key' : 'key' };
#        [underneath] {
#           array = [1, 2, 3, 4];
#        }
#    }
class ConfigParser:
    # !!!!!!!!!!!!!!!!!!!!!!!!!!
    #  Lexical analyzer
    # !!!!!!!!!!!!!!!!!!!!!!!!!!

    tokens = (
              'WS_STRING', # String with whitespaces like param = 'text value'
              'NOWS_STRING', # String with no whitespaces like param = value
              'NEWLINE'
              )


    # Symbols that will be skiped by lexical analyzator
    t_ignore = " \t\n"

    # Literals for ply that can be used as single character literals
    literals = ['[', ',', ']', '{', '}', '=', ';']

    def t_WS_STRING(self, t):
        r"'([a-zA-Z0-9]|(\s))*'"
        print('t_WS_STRING ' + str(t))
        t.value = t.value.strip("'")
        return t

    def t_NOWS_STRING(self, t):
        r"[a-zA-Z0-9]+"
        print('t_NOWS_STRING ' + str(t))
        return t

    # t_NEWLINE = '\n'

    # Error handler for lex
    def t_error(self, t):
        # TODO Use logger instead of print
        token = t.value if t else ""
        errorMessage = "Lex error during parsing string " + token
        print(errorMessage)
        raise ConfigParsingException(errorMessage)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!
    #  Syntax analyzer
    # !!!!!!!!!!!!!!!!!!!!!!!!!!
   

    def p_config(self, p):
        """
            config : configElements
        """
        print('p_config ' + str(p))
        self.rootSection = self._configElementsToSection(p[1])
        print(str(self.rootSection))

    def p_configElements(self, p):
        """
            configElements : configElement
                           | configElement configElements
                           | empty
        """
        print('p_configElements ' + str(p))
        

        if len(p) > 2:
            configElements = p[2]
            p[0] = p[1] + p[2]
        elif p[1]:
            p[0] = p[1]
        else:
            p[0] = []

    def p_configElement(self,p):
        """
            configElement : attributeName '=' attributeValue ';'
                          | section
        """
        print('p_configElement ' + str(p))
        if len(p) > 2:
            attributeValue = p[3]
            attributeName = p[1]
            p[0] = [ [attributeValue, attributeName] ]
        else:
            p[0] = [ p[1] ]
        print(str(p[0]))

    def _configElementsToSection(self, configElements):
        section = ConfigSection()
        for element in configElements:
            if isinstance(element[0], ConfigSection):
                section.addSection(element[1], element[0])
            else:
                section.addAttribute(element[1], element[0])

        return section

    def p_section(self, p):
        """
            section : '[' sectionName ']' '{' configElements '}'
        """
        print('p_section ' + str(p))

        section = self._configElementsToSection(p[5])
        sectionName = p[2]
        p[0] = [section, sectionName]
        print('[' + str(section) + ', ' + sectionName + ']')

    def p_sectionName(self, p):
        """
            sectionName : NOWS_STRING
        """
        print('p_sectionName ' + str(p))
        p[0] = p[1]
        print(p[0])

    def p_attributeValue(self, p):
        """
            attributeValue : stringValue
                           | arrayValue
        """
        print('p_attributeValue ' + str(p))
        p[0] = p[1]
        print(p[0])

    def p_stringValue(self, p):
        """
            stringValue : WS_STRING
                        | NOWS_STRING
        """
        print('p_stringValue ' + str(p))
        p[0] = p[1]
        print(p[0])

    def p_attributeName(self, p):
        """
            attributeName : NOWS_STRING
        """
        print('p_attributeName ' + str(p))
        p[0] = p[1]
        print(p[0])

    # Rule for array
    def p_arrayValue(self, p):
        """
            arrayValue : '[' arrayElements ']'
        """
        print('p_arrayValue ' + str(p))
        p[0] = p[2]
        print(p[0])

    # Rule for array elements
    def p_arrayElements(self, p):
        """
            arrayElements : arrayElement
                          | arrayElement ',' arrayElements
                          | empty
        """
        print('p_arrayElements ' + str(p))
        if len(p) > 2:
            p[0] =  p[1] + p[3]
        elif p[1]:
            p[0] = p[1]
        else:
            p[0] = []
        print(p[0])

    # Rule for array element
    def p_arrayElement(self, p):
        """
            arrayElement : WS_STRING
                         | NOWS_STRING
        """
        # At this place p[1] is a value that was returned by lexical analyzator
        # and contains element that can be added to result list
        print('p_arrayElement ' + str(p))
        p[0] = [p[1]]
        print(p[0])

    # Rule for empty token
    def p_empty(self, p):
        'empty :'
        print('p_empty ' + str(p))
        pass

    # Error handler for yacc
    def p_error(self, p):
        # TODO Use logger instead of print
        value = p.value if p else ""
        errorMessage = "Yacc error during parsing string " + value
        print(errorMessage)
        raise ConfigParsingException(errorMessage)

    def __init__(self, toDebug = 0):
         # Creating lexical analyzer
        self.lexer = ply.lex.lex(module=self, debug = toDebug)
        # Create yacc
        self.parser = ply.yacc.yacc(module=self)

        


    # Return ConfigSection that contains all section of config file
    def parseConfig(self, configString):
       # self.sectionsStack = [ConfigSection()]
        #self.rootSection = SectionConfig()
        self.parser.parse(configString)

        return self.rootSection
        # return sectionsStack[0]

if __name__ == "__main__":
    pass
