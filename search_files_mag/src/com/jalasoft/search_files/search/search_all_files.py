import sys, os

class SeachFiles:
    """
    This class should contain all methods for search files
    """
    def search_files(self, file_name):
        """
        This method search all files that contains the name sent as parameter
        :param file_name:
        :return: LIST of all the files that matches with the name sent
        """
        self.file_name = file_name
        path = os.getcwd()
        for root, folders, files in os.walk(path):
            all_files = []
            for file in files:
                if file_name in file.lower():
                    all_files.append(os.path.join(root, file))
            return all_files

    def search_folders(self, folder_name):
        """
        This method search all folders that contains the name sent as parameter
        :param folder_name:
        :return: LIST of all the folders that matches with the name sent
        """
        self.folder_name = folder_name
        path = os.getcwd()
        for root, folders, files in os.walk(path):
            all_folders = []
            for folder in folders:
                if folder_name in folder.lower():
                    all_folders.append(os.path.join(root, folder))
            return all_folders

    def search_by_name(self, name):
        """
        This method search by name all the files and folders that matches with the name sent as parameter
        :param name: file or folder name
        :return: list of files and folder with that matches with the name entered
        """
        self.name = name
        path = os.getcwd()
        for root, folders, files in os.walk(path):
            result = []
            for file in files:
                if name in file.lower():
                    result.append(os.path.join(root, file))

            for folder in folders:
                if name in folder.lower():
                    result.append(os.path.join(root, folder))

            return result

    def list_results(self, name):
        """
        List all results that were returned with the search_by_name method
        :param name: file or folder name
        :return: all the results
        """
        self.name = name
        results = self.search_by_name(name)
        for files in results:
            print(files)


files = SeachFiles()
files.list_results("test")