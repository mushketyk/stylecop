# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 5, 2011 7:44:18 PM$"

class ParsingException(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return repr(self.val)


