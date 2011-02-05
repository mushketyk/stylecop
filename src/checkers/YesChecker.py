# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 5, 2011 7:41:14 PM$"

import checkers
from checkers.AbstractChecker import AbstractChecker

# Checker that pass every file. Used if file that is necessary to check
# has unknown extension
class YesChecker(AbstractChecker):
    def __init(self, config):
        AbstractChecker.__init__(self, config)

    def check(self, stringSource):
        return 0

if __name__ == "__main__":
    pass
