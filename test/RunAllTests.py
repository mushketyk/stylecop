# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys

import unittest
import config
from configTest.ConfigReaderTest import ConfigReaderTest
from configTest.ConfigSectionTest import ConfigSectionTest
from checkersTest.CheckersFactoryTest import CheckersFactoryTest

def runAllSuits(*suits):
    for suit in suits:
        testResult = unittest.TestResult()
        suit.run(testResult)

        print(testResult)
        if len(testResult.errors) != 0:
            print("Number of errors: " + str(len(testResult.errors)))
            for error in testResult.errors:
                print(error)
        else:
            print("No errors")

        if len(testResult.failures) != 0:
            print("Number of failures: " + str(len(testResult.failures)))
            for failure in testResult.failures:
                print(failure)
        else:
            print("No failures")

def loadSuit(klass):
    return unittest.TestLoader().loadTestsFromTestCase(klass)

if __name__ == "__main__":

        configSectionTestSuit = loadSuit(ConfigSectionTest)
        configRederTestSuit = loadSuit(ConfigReaderTest)
        configCheckersFactorySuit = loadSuit(CheckersFactoryTest)

        runAllSuits(configSectionTestSuit,
                    configRederTestSuit,
                    configCheckersFactorySuit)


