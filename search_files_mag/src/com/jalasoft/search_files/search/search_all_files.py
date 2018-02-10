import os
from datetime import *
import win32security
import mmap
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.utils.logging import logger


class SearchFiles:
    """
    This class should contain all methods for search files
    """
    def set_file_values(self, root, file):
        """
        This method set all the file values needed to this project it was implemented to don't duplicate code
        :param root: the file root path
        :param file: the file name
        :return: A file object with all the values entered
        """
        file_object = File()
        file_and_path = os.path.join(root, file)
        file_object.set_file_folder_name(file)
        file_object.set_path(file_and_path)
        file_object.set_size(os.path.getsize(file_and_path))
        file_object.set_is_file(True)
        file_object.set_extension(self.extract_extension(file_and_path))
        file_object.set_date_created(os.path.getctime(file_and_path))
        file_object.set_date_modified(os.path.getmtime(file_and_path))
        file_object.set_date_last_access(os.path.getatime(file_and_path))
        file_object.set_owner(self.get_owner(file_and_path))
        return file_object


    def set_folder_values(self, root, folder):
        """
        This method set all the folder values needed to this project
        :param root: Folder root path
        :param folder: folder name
        :return: Return a file object
        """
        file_object = File()
        folder_and_path = os.path.join(root, folder)
        file_object.set_file_folder_name(folder)
        file_object.set_path(folder_and_path)
        file_object.set_size(self.calculate_folder_size(folder_and_path))
        file_object.set_is_file(False)
        file_object.set_extension(None)
        file_object.set_date_created(os.path.getctime(folder_and_path))
        file_object.set_date_modified(os.path.getmtime(folder_and_path))
        file_object.set_date_last_access(os.path.getatime(folder_and_path))
        file_object.set_owner(self.get_owner(folder_and_path))
        return file_object

    def file_all_results(self, path, name, type_search, case_sensitive):
        """
        This method set all the values needed to handle files
        :param name: file/folder name
        :param type_search: This method receive a type_search if the type is
        1 it search just files, 2 it search just folders and 3 for both files and folders
        :return:
        """
        logger.info("file_all_results: Enter")
        self.name = name
        results = []
        self.path = path
        logger.info("file_all_results: Load files and/or directories")
        for root, folders, files in os.walk(path):
            if type_search == 1 or type_search == 3:
                for file in files:
                    if case_sensitive == 'c':
                        if name in file:
                            file_object = self.set_file_values(root, file)
                            results.append(file_object)
                    else:
                        if name.lower() in file.lower():
                            file_object = self.set_file_values(root, file)
                            results.append(file_object)

            if type_search == 2 or type_search == 3:
                for folder in folders:
                    if case_sensitive == 'c':
                        if name in folder:
                            file_object = self.set_folder_values(root, folder)
                            results.append(file_object)
                    else:
                        if name.lower() in folder.lower():
                            file_object = self.set_folder_values(root, folder)
                            results.append(file_object)

        logger.info("file_all_results: Exit")
        return results

    def filter_by_extension(self, extension, results):
        """
        Given the search result and the extension that need to be filtered this method return a filtered result that show just
        the files with the extension received
        :param extension: extension to show
        :param results: previous search result that need to be filtered
        :return: The file path for all the files that have the extension received as parameter
        """
        filter_result = []
        for result in results:
            if extension in str(result.get_extension()):
                filter_result.append(result.get_path())
        return filter_result

    def filter_by_size(self, operator, size_to_filter, results):
        """
        This method filter the result received according the operators, size_to_filter and results for equal to size to filter
        of the result also received as parameter
        :param operator: Allowed values are 'l' for less than, 'g' for greater than and 'e'
        :param size_to_filter: the size_to_filter
        :param results: It's the result of the previous search
        :return: A list that meets with the criteria to be filtered
        """
        filter_result = []
        for result in results:
            if operator == 'e':
                if result.get_size() == size_to_filter:
                    path_and_size = (result.get_path(), result.get_size())
                    filter_result.append(path_and_size)

            if operator == 'l':
                if result.get_size() < size_to_filter:
                    path_and_size = (result.get_path(), result.get_size())
                    filter_result.append(path_and_size)

            if operator == 'g':
                if result.get_size() > size_to_filter:
                    path_and_size = (result.get_path(), result.get_size())
                    filter_result.append(path_and_size)

        return filter_result

    def filter_by_date_created(self, results, date, operator):
        """
        This method filter the result get from a previous search and create a new result just with the objects that meets the date_created criteria
        :param results: This is the result of a previous search
        :param date: Date that need to be filtered it need a operator
        :param operator: The valid operators are 'e' for equal, 'l' for less and 'g' for greater
        :return: A new result with the file or folder path and the date created
        """
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            date_created = self.convert_string_to_date(result.get_date_created())
            path = result.get_path()
            if operator == 'e':
                if date_created == date_get:
                    path_date_created = (path, datetime.strftime(date_created, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
            if operator == 'l':
                if date_created < date_get:
                    path_date_created = (path, datetime.strftime(date_created, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
            if operator == 'g':
                if date_created > date_get:
                    path_date_created = (path, datetime.strftime(date_created, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
        return result_filtered

    def filter_by_date_modified(self, results, date, operator):
        """
        This method filter the result get from a previous search and create a new result just with the objects that meets the date_modified criteria
        :param results: This is the result of a previous search
        :param date: Date that need to be filtered it need a operator
        :param operator: The valid operators are 'e' for equal, 'l' for less and 'g' for greater
        :return: A new result with the file or folder path and the date modified
        """
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            date_modified = self.convert_string_to_date(result.get_date_modified())
            path = result.get_path()
            if operator == 'e':
                if date_modified == date_get:
                    path_date_modified = (path, datetime.strftime(date_modified, '%m-%d-%Y'))
                    result_filtered.append(path_date_modified)
            if operator == 'l':
                if date_modified < date_get:
                    path_date_modified = (path, datetime.strftime(date_modified, '%m-%d-%Y'))
                    result_filtered.append(path_date_modified)
            if operator == 'g':
                if date_modified > date_get:
                    path_date_modified = (path, datetime.strftime(date_modified, '%m-%d-%Y'))
                    result_filtered.append(path_date_modified)
        return result_filtered

    def filter_by_date_last_access(self, results, date, operator):
        """
        This method filter the result get from a previous search and create a new result just with the objects that meets the last accessed date criteria
        :param results: This is the result of a previous search
        :param date: Date that need to be filtered it need a operator
        :param operator: The valid operators are 'e' for equal, 'l' for less and 'g' for greater
        :return: A new result with the file or folder path and the last accessed date
        """
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            path = result.get_path()
            date_last_access = self.convert_string_to_date(result.get_date_last_access())
            if operator == 'e':
                if date_last_access == date_get:
                    path_date_created = (path, datetime.strftime(date_last_access, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
            if operator == 'l':
                if date_last_access < date_get:
                    path_date_created = (path, datetime.strftime(date_last_access, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
            if operator == 'g':
                if date_last_access > date_get:
                    path_date_created = (path, datetime.strftime(date_last_access, '%m-%d-%Y'))
                    result_filtered.append(path_date_created)
        return result_filtered

    def filter_by_owner(self, results, owner):
        """
        This method filter a previous search with owner criteria it returns a new result just with the files and folders that meet the owner criteria
        :param results: These are results of a previous search that need to be filtered to meet the owner criteria
        :param owner: This is the owner that need to be filtered
        :return: A new result just with the folders and paths that belong to owner entered as parameter
        """
        results_filtered = []
        for result in results:
            if owner == result.get_owner():
                path_and_owner = (result.get_path(), result.get_owner())
                results_filtered.append(path_and_owner)
        return results_filtered

    def calculate_folder_size(self, path):
        """
        Given a folder name this method calculate the total size
        :param path: Folder path
        :return: folder size in bytes
        """
        folder_size = 0
        for root, folders, files in os.walk(path):
            for file in files:
                folder_size = folder_size + os.path.getsize(os.path.join(root, file))
        return folder_size

    def extract_extension(self, path):
        """
        This method extract the extension from the path received as parameter
        :param path: file path
        :return: for a file path it return extension and return None if it's a folder path
        """
        path_splitted = os.path.splitext(path)
        extension = path_splitted[1]
        return extension

    def format_date_parameter(self, date):
        """
        This method takes the arg send from menu and convert on another string that is used to filter by date methods
        :param date: String date e.g. '02-09-2018'
        :return: String date without additional characters e.g. '02092018'
        """
        date_on_string = date.replace('-', '')
        return date_on_string

    def convert_string_to_date(self, date_string):
        """
        This method convert a date in string e.g. '02092018' on a date on datetime 02 09 2018
        :param date_string: Receives a string date '02092018'
        :return: A datetime date 02 09 2018
        """
        date = datetime.strptime(date_string, '%m%d%Y')
        return date

    def get_owner(self, file_folder_path):
        """
        This method receive a file or folder path and return the owner name
        :param file_folder_path: File or folder path
        :return: The owner name for the path received
        """
        file_and_folder = win32security.GetFileSecurity(file_folder_path, win32security.OWNER_SECURITY_INFORMATION)
        username = win32security.LookupAccountSid(None, file_and_folder.GetSecurityDescriptorOwner())
        return username[0]

    def content_seacher(self, results, text):
        """
        This method search and string on a received file path and return the list of files that contain the text received
        :param results: A previous search result
        :param text: Text that need to be searched on the files
        :return: A list of paths for the files that contains the text entered
        """
        results_filtered = []
        for result in results:
            allowed_to_search = {'.doc', '.docx', '.xls', '.txt'}
            extension = result.get_extension()
            if extension in allowed_to_search:
                if extension == '.txt':
                    with open(result.get_path()) as in_file:
                        text_on_file = mmap.mmap(in_file.fileno(), 0, access=mmap.ACCESS_READ)
                        if text_on_file.find(text.encode()) != -1:
                            results_filtered.append(result.get_path())
        return results_filtered

    def search_exactly_equal(self, results, name):
        """
        This method search for a file or folder name with a name that match exactly with the name entered from command line
        :param results: A previous search result
        :param name: the name that should match exactly with the folder o file name
        :return: a list of files and folders filtered
        """
        results_filtered = []
        for result in results:
            if result.get_file_folder_name() == name:
                results_filtered.append(result.get_path())
        return results_filtered

search = SearchFiles()
result = search.file_all_results('D:\\', 'test', 3, 'c')
print(search.search_exactly_equal(result, 'test.docx'))