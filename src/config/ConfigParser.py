__author__ = "proger"
__date__ = "$Jan 31, 2011 5:27:47 PM$"

import ply
import ply.lex
import ply.yacc

from config.ConfigSection import ConfigSection
from config.ConfigParsingException import ConfigParsingException

# Read ply documentation if you are going to read next
# because I don't think you'll understand following code

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
    literals = ['[', ',', ']', '{', '}', '=', ';', ':']

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
        self.rootSection = self._configElementsToSection(p[1])
        

    def p_configElements(self, p):
        """
            configElements : configElement
                           | configElement configElements
                           | empty
        """
                

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
        
        if len(p) > 2:
            attributeValue = p[3]
            attributeName = p[1]
            p[0] = [ [attributeValue, attributeName] ]
        else:
            p[0] = [ p[1] ]
        

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
        
        section = self._configElementsToSection(p[5])
        sectionName = p[2]
        p[0] = [section, sectionName]
        
    def p_sectionName(self, p):
        """
            sectionName : NOWS_STRING
        """
        
        p[0] = p[1]
        
    def p_attributeValue(self, p):
        """
            attributeValue : stringValue
                           | arrayValue
                           | dictionary
        """
        
        p[0] = p[1]
        
    # string value rule
    def p_stringValue(self, p):
        """
            stringValue : WS_STRING
                        | NOWS_STRING
        """
        
        p[0] = p[1]
        

    # attribute name rule
    def p_attributeName(self, p):
        """
            attributeName : NOWS_STRING
        """
        
        p[0] = p[1]
        
    # Rule for array
    def p_arrayValue(self, p):
        """
            arrayValue : '[' arrayElements ']'
        """
        
        p[0] = tuple(p[2])
        
    # Rule for array elements
    def p_arrayElements(self, p):
        """
            arrayElements : arrayElement
                          | arrayElement ',' arrayElements
                          | empty
        """
        
        if len(p) > 2:
            p[0] =  p[1] + p[3]
        elif p[1]:
            p[0] = p[1]
        else:
            p[0] = []

    # Rule for array element
    def p_arrayElement(self, p):
        """
            arrayElement : WS_STRING
                         | NOWS_STRING
        """
        # At this place p[1] is a value that was returned by lexical analyzator
        # and contains element that can be added to result list

        p[0] = [p[1]]


    # dictionary rule
    def p_dictionary(self, p):
        """
            dictionary : '{' dictElements '}'
        """
        p[0] = p[2]

    # dictionary elements rule
    def p_dictElements(self, p):
        """
            dictElements : dictElement
                         | dictElement ',' dictElements
                         | empty
        """
        # if dictElements is empty
        if not p[1]:
            p[0] = {}
            return

        # dictElements isn't empty so first element in rule is dictElement
        # and it is list [key, value] of new dictionary element
        dictElement = p[1]
        dictKey = dictElement[0]
        dictValue = dictElement[1]
        # if there a lot dictionary elements...
        if len(p) > 2:
            dictElements = p[3]
            # ... add new element to dictionary
            dictElements[dictKey] = dictValue
            # ... return dictionary
            p[0] = dictElements
        else:
            # one last element - create dictionary with it's key, value
            p[0] = {dictKey : dictValue}
        
    # dictionary element rule
    def p_dictElement(self, p):
        """
            dictElement : dictKey ':' dictValue
        """
        dictKey = p[1]
        dictValue = p[3]

        p[0] = [dictKey, dictValue]

    # dictionary key
    def p_dictKey(self, p):
        """
            dictKey : NOWS_STRING
                    | WS_STRING
        """
        p[0] = p[1]

    # dictionary value
    def p_dictValue(self, p):
        """
            dictValue : NOWS_STRING
                      | WS_STRING
        """
        p[0] = p[1]

    # Rule for empty token
    def p_empty(self, p):
        'empty :'
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
        self.parser.parse(configString)

        return self.rootSection

