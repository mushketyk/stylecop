# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

import checkersTest
import checkersTest.forCheckerFactoryTest
import checkersTest.forCheckerFactoryTest.somePackage
import checkersTest.forCheckerFactoryTest.somePackage.someModule
from checkersTest.forCheckerFactoryTest.somePackage.someModule import SomeClass

import checkers
import checkers.CheckersFactory
from checkers.CheckersFactory import CheckersFactory

import config
import config.ConfigSection
from config.ConfigSection import ConfigSection

import checkers
import checkers.YesChecker
from checkers.YesChecker import YesChecker

class  CheckersFactoryTest(unittest.TestCase):
    def setUp(self):
        self.extDict = {'c' : 'checkersTest.forCheckerFactoryTest.somePackage.someModule.SomeClass'}
        self.factory = CheckersFactory(self.extDict)

    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testGetChecker(self):
        config = ConfigSection()
        
        instance = self.factory.getChecker('c', config)
        
        self.assertTrue(isinstance(instance, SomeClass), "")

    def testGetYesChecker(self):
        config = ConfigSection()

        instance = self.factory.getChecker('java', config)

        self.assertTrue(isinstance(instance, YesChecker), "")

if __name__ == '__main__':
    unittest.main()
   

