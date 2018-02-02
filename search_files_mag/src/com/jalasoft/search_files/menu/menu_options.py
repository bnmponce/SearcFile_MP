import argparse

from src.com.jalasoft.search_files.menu.input import *

class PrintMenu(object):

    def print_menu(self):
        menu_options = Menu()
        parser = argparse.ArgumentParser(
            description = 'DEV FUNDAMENTALS II - SEARCH FILES AND FOLDERS.',
            formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        )
        parser.add_argument(
            '-s',
            dest = 'search',
            action = 'store_true',
            help = 'perform search with criteria given.',
        )
        parser.add_argument(
            '--name',
            '-n',
            default = menu_options.get_name(),
            help = 'Configure the name of the file or folder to search.',
        )
        parser.add_argument(
            '--path',
            '-p',
            default = menu_options.get_path(),
            help='Configure the path in order to search a file or folder.',
        )
        parser.add_argument(
            '--type',
            '-t',
            default = menu_options.get_type_search(),
            help='Configure the type of search file or folder to search.',
        )
        args = parser.parse_args()
        return args
