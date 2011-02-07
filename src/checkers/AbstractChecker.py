# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 5, 2011 7:32:29 PM$"

# Base class for checker
class AbstractChecker():
    def __init__(self, config):
        self.config = config

    def getConfig(self):
        return self.config

    # Method that checks source file style. Sources file is a single string
    # with \n symbol at the end of each line because ply can read only
    # string as it input
    # Method should return list of strings of style violations
    # and throw ParsingExeption error if checker fails to parse a file
    def check(self, sourceString):
        raise NotImplementedError('AbstractChecker.check is an abstract method')

if __name__ == "__main__":
    pass
