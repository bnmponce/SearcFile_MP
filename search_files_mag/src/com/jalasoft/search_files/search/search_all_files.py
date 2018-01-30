import sys, os
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
                        results.append(file_object)
        return results

    def calculate_folder_size(self, path):
        folder_size = 0
        for root, folders, files in os.walk(path):
            for file in files:
                folder_size = folder_size + os.path.getsize(os.path.join(root, file))
        return folder_size

    def extract_extension(self, path):
        path_splitted = os.path.splitext(path)
        extension = path_splitted[1]
        return extension

# search = SearchFiles()
# result = search.file_all_results('D:\\', 'test', 3)
# for i in result:
#     print(i.get_path())