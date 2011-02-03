# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

from config.ConfigParser import ConfigParser
from config.ConfigSection import ConfigSection

class  ConfigReaderTest(unittest.TestCase):
    def setUp(self):
        self.parser = ConfigParser(1)
    
    def _assertEqualSections(self, section1, section2):
        attributeNames1 = section1.getAttributeNames()
        attributeNames2 = section2.getAttributeNames()

        self.assertEqual(attributeNames1, attributeNames2, "")

        for attribute in attributeNames1:
            self.assertEqual(section1.getAttribute(attribute), section2.getAttribute(attribute), "")

        sectionNames1 = section1.getSectionNames()
        sectionNames2 = section2.getSectionNames()

        self.assertEqual(sectionNames1, sectionNames2, "")

        for section in sectionNames1:
            self._assertEqualSections(section1.getSection(section), section2.getSection(section))

    def test_configParser(self):
        configString = """
            attr1 = 'long value';
            attr2 = [value1, value2];
            [section1] {
                [section11] {
                    attr111 = ['el1', 'el2', 'el3'];
                }
                attr11 = 'val val';
            }

            [section2] {
                attr21 = val;
                
            }

            dict1 = {val1 : 'long val', 'val val' : value};
        """
        result = self.parser.parseConfig(configString)

        section11 = ConfigSection()
        section11.addAttribute('attr111', ['el1', 'el2', 'el3'])

        section1 = ConfigSection()
        section1.addAttribute('attr11', 'val val')
        section1.addSection('section11', section11)

        section2 = ConfigSection()
        section2.addAttribute('attr21', 'val')

        topSection = ConfigSection()
        topSection.addSection('section1', section1)
        topSection.addSection('section2', section2)

        topSection.addAttribute('attr1', 'long value')
        topSection.addAttribute('attr2', ['value1', 'value2'])
        topSection.addAttribute('dict1', {'val1' : 'long val', 'val val' : 'value'})

        expected = topSection

        self._assertEqualSections(result, expected)

if __name__ == '__main__':
    unittest.main()

