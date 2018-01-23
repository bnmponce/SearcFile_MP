import sys, os

class SeachFiles:
    """
    This class should contain all methods for search files
    """
    def search_files(self, file_name):
        self.file_name = file_name
        path = os.getcwd()
        total = 0

        for root, dirs, files in os.walk(path):
            for file in files:
                if (file_name in file.lower()):
                    print(os.path.join(root, file))
                    total += 1

seach = SeachFiles()
seach.search_files("test")