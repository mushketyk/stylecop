#!/usr/bin/python3

from argparse import ArgumentParser
import repos
import FileReader

# argv that was pass to script includes arguments that was passed by VCS
# to hook and user specified parameters. This functions split argv into two
# list: with script name and parameters specified by user and VCS parameters
def splitArgv(argv):
    
    dotPos = argv.index(".")
    print(dotPos)
    return argv[0 : dotPos], argv[dotPos + 1 : len(argv)]


def main():
    """ Main fucntion for style checking """
    try:
        userParams, repoParams = splitArgv(sys.argv)
        parser = ArgumentParser(description = "StyleCop parameters")

        parser.add_argument("--repo", dest="repo", action="store",
                            help="Repository that use this script in hook")
        parser.add_argument("--stage", dest="stage", action="store",
                            help="Stage of work with VCS")
        parser.add_argument("--config", dest="config", action="store",
                            help="StyleCop config file")


        args = parser.parse_args(userParams)

        configParser = ConfigParser()
        configString = FileReader.readFile(args.config)
        config = configParser.parse(configString)

        factory = repos.ReposFactory()
        repository = factory.getRepository(args.repo, args.stage, config)
        changedFiles = repository.getChangedFiles(repoParams)

        checkersFactory = CheckersFactory(config)

        errors = 0

        for file in changedFiles:
            ext = getFileExtension(file)
            checker = checkersFactory.getChecker(ext)
            sourceString = FileReader.readFile(file)

            errors += checker.check()

        if errors > 0:
            sys.stderr.write("Total number of style errors: " + errors)
            sys.stderr.write("Update failed")

        # If there were no errors we permit this update
        return errors

    except ValueError as er:
        pass
    except Exception as ex:
        pass
    


if __name__ == '__main__':
    #main()
    print(splitArgv(["stylecop", "--repo", "svn", ".", "param1", "param2"]))