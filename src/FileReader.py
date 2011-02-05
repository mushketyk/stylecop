# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="proger"
__date__ ="$Feb 5, 2011 6:39:35 PM$"

BUF_SIZE = 4096

# Because ply can't read file and takes only string to parse
# We need to read file to a single string before parseing a file
def readFile(fileName):
    file = None
    try:
        file = open(fileName, "rb", BUF_SIZE)
        result = file.read()
        
        return result
    except IOError as ex:
        raise ex
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    pass
