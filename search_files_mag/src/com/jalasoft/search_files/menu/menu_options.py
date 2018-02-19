import argparse
from src.com.jalasoft.search_files.menu.input import *
from src.com.jalasoft.search_files.utils.logging import logger


class PrintMenu(object):
    """
    Print Menu class and method
    This class contains the method that will define the arguments required in our menu based on
    command-line parsing module.
    """
    def print_menu(self):
        """
        This method contains the options/arguments available in the command-line menu by using the
        add_argument() method.
        args contains the data from the options specified by using the parse_args() method.
        :param self:
        :return: The arguments
        """
        logger.info('Enter to print_menu method to determine arguments available')
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
            help='Enter the operator to search by specific size:'
                 ' -l: to search files less than the size specified'
                 ' -g: to search the files greater than the size specified'
                 ' -e: to search the exact match size ',
        )
        parser.add_argument(
            '--extension',
            '-ext',
            help='Configure the file extension to search. It will search all file types by default if none is given',
        )
        parser.add_argument(
            '--date',
            '-d',
            help='Configure the date to search a file',
        )
        parser.add_argument(
            '--opdate',
            '-od',
            help='Enter the date operator to search by specific date:'
                 '  l: to search files less than the date specified'
                 '  g: to search the files greater than the date specified'
                 '  e: to search the exact match date ',
        )
        parser.add_argument(
            '--controldate',
            '-cd',
            help='Enter the operator to search by control date: created, modified and acceded'
                 '  c: to search files created in the specified date'
                 '  m: to search files modified in the specified date'
                 '  a: to search files acceded in the specified date ',
        )
        parser.add_argument(
            '--casesensitive',
            '-cs',
            default='n',
            help='Enter the argument -cs to specify if your search by name will be case sensitive or not'
                 'By default it will be case sensitive, other wise use the values:'
                 '  y: you confirm as yes, you want to search by case sensitive name'
                 '  n: you confirm as no, you do not want to search by case sensitive name'
        )
        parser.add_argument(
            '--owner',
            '-ow',
            help='Enter the owner name to filter the search by owner.',
        )
        parser.add_argument(
            '--content',
            '-c',
            help='Enter the operator -c and the content you want to search. It is only supported .txt for the moment'
                 'It will search all matches with the text introduced. If you want to search an specific text, use:'
                 '  -f argument followed by e to search the exact match'
        )
        parser.add_argument(
            '--namefind',
            '-nf',
            help='Enter the argument find / -f to specify if you want to search by an specific name/text'
                 'By default the searches are finding all matches that contains the text introduced. Otherwise use:'
                 '  e: if you want to find an exact name/text'
        )
        parser.add_argument(
            '--contentfind',
            '-cf',
            help='Enter the argument find / -f to specify if you want to search by an specific name/text'
                 'By default the searches are finding all matches that contains the text introduced. Otherwise use:'
                 '  e: if you want to find an exact name/text'
        )
        parser.add_argument(
            '-r',
            dest='reset',
            action='store_true',
            help='perform a reset of default values of search all in the path C:.'
                 'path: C:'
                 'name: " "'
                 'Type: 3 = both files and folder'
                 'Case Sensitive: n=nonCase sensitive',
        )

        args = parser.parse_args()
        logger.info('Arguments defined. Exit from print_menu method')
        return args
