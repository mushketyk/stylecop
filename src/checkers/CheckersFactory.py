from checkers.YesChecker import YesChecker
from checkers.ParsingExeption import ParsingException
# To change this template, choose Tools | Templates
# and open the template in the editor.



__author__="proger"
__date__ ="$Feb 10, 2011 1:43:08 PM$"

class CheckersFactory:
    def __init__(self, extensionDictionary):
        self.extDict = extensionDictionary
        self.checkersCache = {}

    def getChecker(self, fileExtension, config):
        if fileExtension not in self.extDict.keys():
            return YesChecker(config)

        checkerName = self.extDict[fileExtension]
        if checkerName not in self.checkersCache.keys():
            checkerClass = self._loadChecker(checkerName)
            self.checkersCache[checkerName] = checkerClass(config)

        return self.checkersCache[checkerName]


    def _loadChecker(self, checkerName):
        """
            Method that loads checker. checkerName should be in a folowing form:
            <packages>.module.class, where packages aren't obligatory
            Fore example:
                mail.mime.audio.MIMEAudio
        """
        try:
            import sys
            print(sys.path)
            nameElements = checkerName.split(".")
            name = nameElements[0]

            module = __import__(name)

            for element in nameElements[1:-1]:
                name = ".".join([name, element])
                __import__(name)
                module = getattr(module, element)
            
            className = nameElements[-1]
            checkerClass = getattr(module, className)

            return checkerClass
        except Exception as ex:
            print(ex)
            # TODO Write to logger what happened here (exceptionType, errorText)
            raise ParsingException('parsing error occured')


if __name__ == "__main__":
    import sys
    sys.path.append('/home/proger/Documents/Programming/Python/StyleCop/test')
    print(sys.path)
    str = ' checkersTest\n'
    print(str.encode())
    res = __import__(str)
    print(res)
#    # Example that shows how to load class MIMEAudio in email.mime.audio module
#    packet = __import__("email")
#    __import__("email.mime")
#    packet = getattr(packet, "mime")
#    __import__("email.mime.audio")
#    module = getattr(packet, "audio")
#
#
#    Class = getattr(module, "MIMEAudio")
#    print(Class)
