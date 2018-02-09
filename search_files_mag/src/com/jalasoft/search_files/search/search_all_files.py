import os
from datetime import *
from src.com.jalasoft.search_files.search.file import File


class SearchFiles:
    """
    This class should contain all methods for search files
    """
    def file_all_results(self, path, name, type_search):
        """
        This method set all the values needed to handle files
        :param name: file/folder name
        :param type_search: This method receive a type_search if the type is
        1 it search just files, 2 it search just folders and 3 for both files and folders
        :return:
        """
        self.name = name
        results = []
        self.path = path
        for root, folders, files in os.walk(path):
            if type_search == 1 or type_search == 3:
                for file in files:
                    if name in file.lower():
                        file_object = File()
                        file_and_path = os.path.join(root, file)
                        file_object.set_path(file_and_path)
                        file_object.set_size(os.path.getsize(file_and_path))
                        file_object.set_is_file(True)
                        file_object.set_extension(self.extract_extension(file_and_path))
                        file_object.set_date_created(os.path.getctime(file_and_path))
                        file_object.set_date_modified(os.path.getmtime(file_and_path))
                        file_object.set_date_last_access(os.path.getatime(file_and_path))
                        results.append(file_object)

            if type_search == 2 or type_search == 3:
                for folder in folders:
                    if name in folder.lower():
                        file_object = File()
                        folder_and_path = os.path.join(root, folder)
                        file_object.set_path(folder_and_path)
                        file_object.set_size(self.calculate_folder_size(folder_and_path))
                        file_object.set_is_file(False)
                        file_object.set_extension(None)
                        file_object.set_date_created(os.path.getctime(folder_and_path))
                        file_object.set_date_modified(os.path.getmtime(folder_and_path))
                        file_object.set_date_last_access(os.path.getatime(folder_and_path))
                        results.append(file_object)
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
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            date_created = self.convert_string_to_date(result.get_date_created())
            if operator == 'e':
                if date_created == date_get:
                    path = result.get_path()
                    date_c = result.get_date_created()
                    path_date_created = (path, date_c)
                    result_filtered.append(path_date_created)
            if operator == 'l':
                if date_created < date_get:
                    path = result.get_path()
                    date_c = result.get_date_created()
                    path_date_created = (path, date_c)
                    result_filtered.append(path_date_created)
            if operator == 'g':
                if date_created > date_get:
                    path = result.get_path()
                    date_c = result.get_date_created()
                    path_date_created = (path, date_c)
                    result_filtered.append(path_date_created)
        return result_filtered

    def filter_by_date_modified(self, results, date, operator):
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            date_modified = self.convert_string_to_date(result.get_date_modified())
            if operator == 'e':
                if date_modified == date_get:
                    path = result.get_path()
                    date_m = result.get_date_modified()
                    path_date_modified = (path, date_m)
                    result_filtered.append(path_date_modified)
            if operator == 'l':
                if date_modified < date_get:
                    path = result.get_path()
                    date_m = result.get_date_modified()
                    path_date_modified = (path, date_m)
                    result_filtered.append(path_date_modified)
            if operator == 'g':
                if date_modified > date_get:
                    path = result.get_path()
                    date_m = result.get_date_modified()
                    path_date_modified = (path, date_m)
                    result_filtered.append(path_date_modified)
        return result_filtered

    def filter_by_date_last_access(self, results, date, operator):
        result_filtered = []
        date_get = self.convert_string_to_date(self.format_date_parameter(date))
        for result in results:
            date_last_access = self.convert_string_to_date(result.get_date_last_access())
            if operator == 'e':
                if date_last_access == date_get:
                    path = result.get_path()
                    date_l_a = result.get_date_last_access()
                    path_date_created = (path, date_l_a)
                    result_filtered.append(path_date_created)
            if operator == 'l':
                if date_last_access < date_get:
                    path = result.get_path()
                    date_l_a = result.get_date_last_access()
                    path_date_created = (path, date_l_a)
                    result_filtered.append(path_date_created)
            if operator == 'g':
                if date_last_access > date_get:
                    path = result.get_path()
                    date_l_a = result.get_date_last_access()
                    path_date_created = (path, date_l_a)
                    result_filtered.append(path_date_created)
        return result_filtered

    def print_search_by_date(self, result):
        new_result = []
        for res in result:
            print(res)
            # date = time.strftime("%m-%d-%Y", res[1])
            # new_result.append(res[0], date)
        # return new_result

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
        date_on_string = date.replace('-', '')
        return date_on_string

    def convert_string_to_date(self, date_string):
        date = datetime.strptime(date_string, '%m%d%Y')
        return date



# search = SearchFiles()
# result = search.file_all_results('D:\\', 'test', 3)
# t = search.filter_by_date_modified(result, '01-01-2017', 'g')
# for i in t:
#     print(i)

# search = SearchFiles()
# result = search.file_all_results('D:\\', 'test', 3)
# for i in result:
#     print(type(i.get_date_modified()))
#     print(i.get_date_modified())

# print(type(search.convert_date('07-31-2013')))