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
            dest='search',
            action='store_true',
            help='perform search with criteria given.',
        )
        parser.add_argument(
            '--name',
            '-n',
            default=menu_options.get_name(),
            help='Configure the name of the file or folder to search.',
        )
        parser.add_argument(
            '--path',
            '-p',
            default=menu_options.get_path(),
            help='Configure the path in order to search a file or folder.',
        )
        parser.add_argument(
            '--type',
            '-t',
            default=menu_options.get_type_search(),
            help='Configure the type of search file or folder to search.',
        )
        parser.add_argument(
            '--size',
            '-z',
            help='Configure the file size (Mb) to search. If you specify only the size, it will search by default'
                 ' the files size less than the size specified. Otherwise use the following operators: -l, -g or -e'
        )
        parser.add_argument(
            '--operator',
            '-o',
            default='l',
            help='enter the operator to search by specific size:'
                 ' -l: to search files less than the size specified'
                 ' -g: to search the files greater than the size specified'
                 ' -e: to search the exact match size ',
        )
        parser.add_argument(
            '--extension',
            '-ex',
            help='Configure the file extension to search. It will search all file types by default if none is given',
        )
        parser.add_argument(
            '--date',
            '-d',
            help='Configure the date to search a file',
        )

        args = parser.parse_args()
        return args
