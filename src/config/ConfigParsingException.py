# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 1, 2011 6:12:37 PM$"

class ConfigParsingException(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return repr(self.val)

if __name__ == "__main__":
    pass
