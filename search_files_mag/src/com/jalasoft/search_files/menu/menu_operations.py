from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.menu.menu_options import *
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.utils.validate_input import *
from prettytable import PrettyTable

class MenuOperations(object):
    """
    MenuOperations class and methods
    This class contains all methods required to handle the arguments's parameter operation for the Menu
    """

    def __init__(self):
        """
        This is the constructor to initialize new objects required to handle the parameters operations
        :param self:
        """
        logger.info ('Constructor initialized...')
        self.menu = Menu()
        self.valid_input = ValidateInput()
        self.print_menu = PrintMenu()
        self.search = SearchFiles()
        self.table = PrettyTable()

    valid_input = ValidateInput()

    def name_operation(self, name):
        """
        This name_operation method handles the "name" parameter from Menu
        :param name: This attribute is the name of the file or folder
        :return: This method returns a boolean. True if this is a valid name, otherwise it will return false.
        """
        logger.info ('Enter to name_operation method')
        validator = self.valid_input.is_valid_name(name)
        if validator:
            self.menu.set_name(name)
            logger.info ('Filter by name completed')
            return True
        else:
            print("Please, enter a valid name, the following characters are not valid: :/\?*|<> ")
            exit()

    def path_operation(self, path):
        """
        This path_operation method handles the "path" parameter from Menu
        :param path: This attribute is the path where the search will be performed
        :return: This method returns a boolean. True if this is a valid path, otherwise it will return false.
        """
        logger.info ('Enter to path_operation method')
        validator = self.valid_input.is_valid_path(path)
        if validator:
            self.menu.set_path(path)
            logger.info ('Filter by path completed')
            return True
        else:
            print("The path you enter does not exist. Please enter a valid path")
            exit()

    def type_operation(self, type):
        """
        This type_operation method handles the "type" parameter from Menu
        :param type: This attribute is the type of element to search: file or folder
        :return: This method returns a boolean. True if is given a valid type (1=file, 2=folder or 3=both). Otherwise
        it will return false.
        """
        logger.info ('Enter to type_operation method')
        validator = self.valid_input.is_valid_type(type)
        if validator:
            self.menu.set_type_search(type)
            logger.info ('Filter by type file/folder completed')
            return True
        else:
            print("Please, enter a valid type: 1=file, 2=folder, 3=both")
            exit()

    def case_sensitive_operation(self, case_sensitive):
        """
        This case_sensitive_operation method handles the "case_sensitive" parameter from Menu
        :param case_sensitive: This attribute determine if the search by "name" should be considered as case sensitive or not
        :return: This method returns a boolean. True if is given a valid value (c=case sensitive or n=non case sensitive).
        Otherwise it will return false.
        """
        logger.info ('Enter to case_sensitive_operation method')
        validator = self.valid_input.is_valid_flag_of_sensitivecase(case_sensitive)
        if validator:
            self.menu.set_case_sensitive(case_sensitive)
            logger.info ('Filter by case sensitive completed')
            return True
        else:
            print("Please enter a valid parameter: c=case sensitive or n=non case sensitive")
            exit()

    def extension_filter(self, extension, results):
        """
        This extension_filter method handles the "extension" parameter from Menu
        :param extension: This attribute determine the "extension"
        :param results: This contains the previous result in order to filter by extension
        :return: This method return a list of objects filtered by the extension given.
        """
        logger.info ('Enter to extension_filter method')
        return self.search.filter_by_extension(extension, results)
        logger.info ('Filter by extension completed')

    def size_filter(self, size, operator, results):
        """
        This size_filter method handles the "size" and "operator" parameters from Menu
        :param size: It is a float and this attribute define the size of elements to search
        :param operator: They are string and can be (l=less than, g=greater than, e=equal)
        :param results: This contains the previous result in order to filter by size and operator given
        :return: This method returns a list of objects filtered by size and operator
        """
        logger.info ('Enter to size_filter method')
        validator = self.valid_input.is_valid_size(size)
        if validator:
            valid_operator = self.valid_input.is_valid_operators(operator)
            if valid_operator:
                logger.info ('Filter by size completed')
                if operator == 'l':
                    return self.search.filter_by_size('l', float(size), results)
                if operator == 'g':
                    return self.search.filter_by_size('g', float(size), results)
                if operator == 'e':
                    return self.search.filter_by_size('e', float(size), results)
            else:
                print("Please enter a valid operator: l = less than, g= greater than or e = equal")
                exit()
        else:
            print("please enter a valid number as size, negative numbers or characters are not allowed")
            exit()

    def date_filter(self, date, opdate, controldate, results):
        """
        This date_filter method handles the "date", "operator date" and "control date" parameter from Menu. All 3 need to be specified
        :param date: It determines the date to perform a search. needs to follow the MM/DD/YYYY format. It is an optional parameter.
        :param opdate: It is an string and can be (l=less than, g=greater than, e=equal)
        :param controldate: It is an string and can be (c=created date, m=modified date, a=accessed date)
        :param results:  This contains the previous result in order to filter by date, operator date and control date given
        :return: This method return a list of objects filtered by: date_created, date_modified and date_las_access
        """
        logger.info ('Enter to date_filter method')
        if date and opdate and controldate:
            validator = self.valid_input.is_valid_date(date)
            if validator:
                validator = self.valid_input.is_valid_operators(opdate)
                if validator:
                    validator = self.valid_input.is_valid_controldate(controldate)
                    if validator:
                        if controldate == 'c':
                            logger.info ('Filter by date created completed')
                            return self.search.filter_by_date_created(results, date, opdate)
                        elif controldate == 'm':
                            logger.info ('Filter by date modified completed')
                            return self.search.filter_by_date_modified(results, date, opdate)
                        elif controldate == 'a':
                            logger.info ('Filter by date created last access')
                            return self.search.filter_by_date_last_access(results, date, opdate)
                        else:
                            print("invalid control date entered")
                    else:
                        print("Please, enter a valid control date parameter: c, m or a")
                        exit()
                else:
                    print("Please enter a valid operator date: l = less than, g= greater than or e = equal")
                    exit()
            else:
                print("Please enter a valid date in the following format 'MM-DD-YYYY' un numeral format")
                exit()
        else:
            print("You must to enter three parameters to search by date: -d, -op, -cd")
            exit()

    def owner_filter(self, owner, results):
        """
        This owner_filter method handles the "owner" parameter from Menu.
        :param owner: It is a string and is the owner of element being searched.
        :param results: This contains the previous result in order to filter by owner
        :return: This method return a list of objects filtered by owner
        """
        logger.info ('Enter to owner_filter method')
        validator = True
        if validator:
            return self.search.filter_by_owner(results, owner)
            logger.info ('Filter by owner completed')
        else:
            print("please enter a owner")
            exit()

    def content_filter(self, content, results):
        """
        This content_filter method handles the "content" parameter from Menu.
        :param content: It is the content to search on a file
        :param results: This contains the previous result in order to filter string given as content. Work only for txt files
        :return: This method return a list of objects filtered by content
        """
        logger.info ('Enter to content_filter method')
        validator = True
        if validator:
            return self.search.content_searcher(results, content)
            logger.info ('Filter by content completed')
        else:
            print("Please enter the content you are looking for")
            exit()

    def name_find_filter(self, namefind, name, results):
        """
        This name_find_filter method handles the "namefind" and "name" parameters from Menu.
        :param namefind: It is a string and can be only 'e' to determine the exact name match
        :param name: It is a string and is the name of element to be searched.
        :param results: This contains the previous result in order to filter by exactly match
        :return: This method return a list of objects filtered by exact match of name given
        """
        logger.info ('Enter to name_find_filter method')
        validator = self.valid_input.is_valid_operator_to_exact_search(namefind)
        if validator:
            if namefind == 'e':
                return self.search.search_exactly_equal(results, name)
                logger.info ('Filter by exact name match completed')
        else:
            print("please enter a valid value 'e' for the argument nf")
            exit()

    def print_results(self, results):
        """
        This print_results method handles the "results" obtained from search/filter to be print as table.
        :param results: This contains the list of objects obtained by search and filters
        :return: It returns a table of elements as result of search.
        """
        logger.info ('Enter to print_results method')
        self.table.field_names = ["Path", "Type", "Size", "Owner", "Created Date", "Modified Date", "Accessed Date"]
        self.table.align["Path"] = "l"
        self.table.align["Type"] = "r"
        self.table.align["Size"] = "r"
        self.table.align["Owner"] = "r"
        self.table.align["Create Date"] = "r"
        self.table.align["Modified Date"] = "r"
        self.table.align["Accessed Date"] = "r"

        for item in results:
            if item.get_is_file():
                return_type = 'File'
            else:
                return_type = 'Folder'

            self.table.add_row([item.get_path(),
                                return_type,
                                item.get_size(),
                                item.get_owner(),
                                item.get_date_created(),
                                item.get_date_modified(),
                                item.get_date_last_access()])

        print(self.table)
        logger.info ('Searched completed and printed results in table. Exiting from print_result method')
