# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 10, 2011 1:32:38 PM$"

from checkers.AbstractChecker import AbstractChecker
import FileReader

class AbstractStringChecker(AbstractChecker):
    """
        This class is a base class for all classes that use ply as an instrument
        for checker creation. Cause ply can read input only from a string but not from
        a file this class read file to string and call doStringCheck that should
        be implemented by inherited checkers.
    """

    def __init__(self, config):
        AbstractChecker.__init__(self, config)

    def check(self, sourceFile):
        sourceString = FileReader.readFile(args.config)
        return self.doStringCheck(sourceString)

    def doStringCheck(self, sourceString):
        """
            Method with the same requirments as AbstractChecker.check has, except it
            receives a string instead of a file.
        """
        raise NotImplementedError('AbstractStringChecker is an abstract class')


