import configparser
import argparse


class Menu:
    # def __init__(self):
    #     print("nu")
    # method to read the settings.ini file
    def read_settings(self):
        config = configparser.ConfigParser()
        config.read('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini')
        # print(config['CONFIG']['name'])
        return config

    # method to get the name from settings.ini file
    def get_name(self):
        config = self.read_settings()
        name = config['CONFIG']['name']
        #print(name)
        return name

    # get_name()

    # method to get the path from settings.ini file
    def get_path(self):
        config = self.read_settings()
        path = config['CONFIG']['path']
        #print(path)
        return path

    # get_path()

    # method to get the path from settings.ini file
    def get_type_search(self):
        config = self.read_settings()
        type_search = config['CONFIG']['type_search']
        #print(type_search)
        return type_search
        # get_path()

    # method to overwrite name on settings.ini file
    def set_name(self, name):
        config = self.read_settings()
        config['CONFIG']['name'] = name
        with open('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini', 'w') as configfile:
            config.write(configfile)
        self.get_name()
        # set_name()

        # method to overwrite name on settings.ini file

    def set_path(self, path):
        config = self.read_settings()
        config['CONFIG']['path'] = path
        with open('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini',
                  'w') as configfile:
            config.write(configfile)
        self.get_path()
        # set_name()

    def set_type_search(self, type_search):
        config = self.read_settings()
        config['CONFIG']['type_search'] = type_search
        with open('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini',
                  'w') as configfile:
            config.write(configfile)
        self.get_type_search()
        # set_name()

menu = Menu()

parser = argparse.ArgumentParser(
        description='DEV FUNDAMENTALS II - SEARCH FILES AND FOLDERS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
parser.add_argument(
    '-s',
    dest='search',
    action='store_true',
    help='perform search with criteria given.',
)
parser.add_argument(
    '--name',
    '-n',
    default=menu.get_name(),
    help='Configure the name of the file or folder to search.',
)
parser.add_argument(
    '--path',
    '-p',
    default=menu.get_path(),
    help='Configure the path in order to search a file or folder.',
)
parser.add_argument(
    '--type',
    '-t',
    default=menu.get_type_search(),
    help='Configure the type of search file or folder to search.',
)

args = parser.parse_args()

if args.search:
    # print("call name validator")
    print(args.name)
    if args.name:
        validator = True #Add method to validate name
        if validator:
            menu.set_name(args.name)
        else:
            print("validation error message")
            exit()
    if args.path:
        validator = True #Add method to validate path
        if validator:
            menu.set_path(args.path)
        else:
            print("validation error message")
            exit()
    if args.type:
        validator = True #Add method to validate file type
        if validator:
            menu.set_type_search(args.type)
        else:
            print("validation error message type")
            exit()
    # Add method to search
    print("Searching.....")
else:
    print("You need to introduce the -s argument to search your files/folders")

