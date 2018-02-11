import unittest
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.search.file import *
class TestSearchAllFiles(unittest.TestCase):

    def setUp(self):
        self.search = SearchFiles()
        self.path = "C:\\test_search\\"
        self.file_name = "test.txt"
        self.file_path = os.path.join(self.path, self.file_name)
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        file = open(self.file_path, 'a')
        file.close()

    def test_set_file_values(self):
        file_set = File()
        for root, folders, files in os.walk(self.path):
            for file in files:
                file_set = self.search.set_file_values(root, file)
        self.assertIsNotNone(file_set)

    if __name__ == '__main__':
        unittest.main()