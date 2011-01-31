from xml.dom import NotFoundErr
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 5:01:16 PM$"


# Section of a config
# Can contain another sections or attributes
class ConfigSection:
    def __init__(self):
        self.sections = {}
        self.attributes = {}

    def getSections(self):
        return [key for key in self.sections.keys()]

    def addSection(self, sectionName, section):
        self.sections[sectionName] = section

    def delSection(self, sectionName):
        del self.sections[sectionName]

    def _getAttribute(self, parsingFunction, attributeName):
        attribute = self.attributes[attributeName]
        if attribute.getValue() == None:
            attributeString = attribute.getString()
            attribute.value = parsingFunction(attributeString)
            
        return attribute.value


    def getAttributeArray(self, arrayName):
        pass

    def getAttributeDictionary(self, dictName):
        pass

    def getAttributeString(self, attributeName, posibleNames):
        value = _getAttribute(self, _stringParser, attributeName)

        if value in posibleNames:
            return value
        else:
            raise ValueError(value + " isn't permited for the attribute " + attributeName)

    def addAttribute(self, attributeName, attribute):
        self.attributes[attributeName] = attribute

    def delAtribute(self, attributeName):
        del self.attributes[attributeName]

    # TODO use StringParser class here
    def _stringParser(stringToParse):
        return stringToParse

    def _arrayParser(stringToParse):
        raise NotImplementedError('_arrayParser is not implemented')

    def _dictParser(stringTOParse):
        raise NotImplementedError('_dictParser is not implemented')

if __name__ == "__main__":
    print "Hello World"
