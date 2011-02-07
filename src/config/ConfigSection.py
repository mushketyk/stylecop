from config.ConfigParsingException import ConfigParsingException

__author__="proger"
__date__ ="$Jan 31, 2011 5:01:16 PM$"


# Section of a config
# Can contain another sections or attributes
class ConfigSection:
    def __init__(self):
        self.sections = {}
        self.attributes = {}

    def getSectionNames(self):
        """ Get list of names of sections under this section """

        return [key for key in self.sections.keys()]

    def getSection(self, sectionName):
        """ Return section by it's name """

        if sectionName in self.sections.keys():
            return self.sections[sectionName]
        else:
            return None

    def addSection(self, sectionName, section):
        """ Add new sub-section """

        self.sections[sectionName] = section

    def delSection(self, sectionName):
        """ Delete section by section name """
        del self.sections[sectionName]

    def getAttributeNames(self):
        """ Get list of names of attributes in the section """

        return [key for key in self.attributes.keys()]

    def getAttribute(self, attributeName):
        """ Return attribute if exist """

        if attributeName in self.attributes.keys():
            return self.attributes[attributeName]
        else:
            return None

    def _getCheckedAttribute(self, attributeName, attributeType):
        """ Return attribute with attributeName if it exists and it's
            type is attributeType"""

        attribute = self.getAttribute(attributeName)
        if isinstance(attribute, attributeType):
            return attribute
        else:
            raise ConfigParsingException(attributeName + " was requested as " +
                                         str(attributeType) + " but it was read from config file as " +
                                         str(type(attribute)))

    def getDictionary(self, dictionaryName):
        """ return attribute if it's dictionary """
        return self._getCheckedAttribute(dictionaryName, dict)

    def getTuple(self, tupleName):
        """ return attribute if it is tuple """
        return self._getCheckedAttribute(tupleName, tuple)
    
    def getString(self, attributeName):
        """ return attribute if it is string """
        return self._getCheckedAttribute(attributeName, str)
    
    def getStringFromList(self, attributeName, validList):
        """ return attribute if it is sting and it's value in validList """

        stringVal = self.getString(attributeName)
        if stringVal in validList:
            return stringVal
        else:
            raise ConfigParsingException(attributeName + "value: " + stringVal +
                                         "not in the valid list " + str(validList))

    def addAttribute(self, attributeName, attributeValue):
        self.attributes[attributeName] = attributeValue

    def delAttribute(self, attributeName):
        """ Delete attribute by name """
        del self.attributes[attributeName]

    def __str__(self):
        res = '{'
        for key in self.attributes.keys():
            res += key + ':' + str(self.attributes[key]) + ','

        for key in self.sections.keys():
            res += key + ':' + str(self.sections[key])

        return res + '}'


