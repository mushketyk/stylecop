# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Jan 31, 2011 5:05:04 PM$"

# Single attribute in config.
# This class contains two fields:
#    configString - string that was read in config after the '=' sign
#    value - parsed value.
class ConfigAttribute:
    def __init__(self, configString = "", value = None):
        self.configString = configString
        self.value = value

    def getConfigString(self):
        return self.configString

    def setConfigString(self, configString):
        self.configString = configString

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

if __name__ == "__main__":
    print "Hello World"
