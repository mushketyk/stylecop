
__author__="proger"
__date__ ="$Jan 31, 2011 5:01:16 PM$"


# Section of a config
# Can contain another sections or attributes
class ConfigSection:
    def __init__(self):
        self.sections = {}
        self.attributes = {}

    def getSectionNames(self):
        return [key for key in self.sections.keys()]

    def getSection(self, sectionName):
        if sectionName in self.sections.keys():
            return self.sections[sectionName]
        else:
            return None

    def addSection(self, sectionName, section):
        self.sections[sectionName] = section

    def delSection(self, sectionName):
        del self.sections[sectionName]

    def getAttributeNames(self):
        return [key for key in self.attributes.keys()]

    def getAttribute(self, attributeName):
        if attributeName in self.attributes.keys():
            return self.attributes[attributeName]
        else:
            return None

    def getDictionary(self, dictionaryName):
        pass

    def getArray(self, arrayName):
        pass
    
    def getString(self, attributeName):
        pass
    
    def getStringFromList(self, attributeName, validList):
        pass

    def addAttribute(self, attributeName, attributeValue):
        self.attributes[attributeName] = attributeValue

    def delAttribute(self, attributeName):
        del self.attributes[attributeName]

    def __str__(self):
        res = '{'
        for key in self.attributes.keys():
            res += key + ':' + str(self.attributes[key]) + ','

        for key in self.sections.keys():
            res += key + ':' + str(self.sections[key])

        return res + '}'


