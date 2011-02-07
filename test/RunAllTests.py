# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys

sys.path.append('/home/proger/Documents/Programming/Python/StyleCop/test/config')
print(sys.path)

import unittest
import config
from configTest.ConfigReaderTest import ConfigReaderTest
from configTest.ConfigSectionTest import ConfigSectionTest

def runAllSuits(*suits):
    for suit in suits:
        testResult = unittest.TestResult()
        suit.run(testResult)

        print(testResult)

def loadSuit(klass):
    return unittest.TestLoader().loadTestsFromTestCase(klass)

if __name__ == "__main__":

        configSectionTestSuit = loadSuit(ConfigSectionTest)
        configRederTestSuit = loadSuit(ConfigReaderTest)

        runAllSuits(configSectionTestSuit,
                    configRederTestSuit)


