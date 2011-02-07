# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

import config
from config.ConfigSection import ConfigSection

class  ConfigSectionTest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigSection()
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testGetSection(self):
        sectionName = "section"
        self.config.addSection(sectionName, ConfigSection())

        self.assertNotEqual(self.config.getSection(sectionName),
                            None,
                            "Added section should exist")

    def testGetNonExistingSection(self):
        nonExistingSection ="IDontExist"
        
        self.assertEqual(self.config.getSection(nonExistingSection),
                         None, 
                         "config.getSection on non existing section should return None")

    def testDelSection(self):
        sectionName = "sectionName"

        self.config.addSection(sectionName, ConfigSection())
        self.assertNotEqual(self.config.getSection(sectionName),
                            None,
                            "Added section should exist")

        self.config.delSection(sectionName)

        self.assertEqual(self.config.getSection(sectionName),
                         None,
                         "config.getSection on deleted section should return None")

    def testGetAttribute(self):
        attributeName = "attributeName"
        attributeValue = "1234"
        self.config.addAttribute(attributeName, attributeValue)

        self.assertEqual(self.config.getAttribute(attributeName),
                         attributeValue,
                         "self.config.getAttribute returned wrong value of attribute")

    def testGetNonExistingAttribute(self):
        nonExistingAttribute = "nonExistingAttribute"

        self.assertEqual(self.config.getAttribute(nonExistingAttribute),
                         None,
                         "Non existing attribute should be equals None")

    def testDelAttribute(self):
        attributeName = "sectionName"
        attributeValue = "4321"

        self.config.addAttribute(attributeName, attributeValue)
        self.assertEqual(self.config.getAttribute(attributeName),
                            attributeValue,
                            "Added attributes should exist")

        self.config.delAttribute(attributeName)

        self.assertEqual(self.config.getAttribute(attributeName),
                         None,
                         "config.getAttribute on deleted attributes should return None")

if __name__ == '__main__':
    unittest.main()

