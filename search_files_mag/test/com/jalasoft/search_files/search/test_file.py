import unittest
from src.com.jalasoft.search_files.search.search_all_files import *

class Test_file(unittest.TestCase):

    def setUp(self):
        self.file = File()
        self.path = "C:\\test_search\\"
        self.file_name = "test.txt"
        self.file_path = os.path.join(self.path, self.file_name)
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        file = open(self.file_path, 'a')
        file.close()

    def test_set_file_folder_name_for_file_name(self):
        self.file.set_file_folder_name(self.file_name)
        name_get = self.file.get_file_folder_name()
        self.assertEqual(self.file_name, name_get)

    def test_set_file_folder_name_for_folder_name(self):
        self.file.set_file_folder_name("test_search")
        get_name = self.file.get_file_folder_name()
        self.assertEqual("test_search", get_name)

    def test_set_path_for_a_file(self):
        self.file.set_path(self.file_path)
        path_get = self.file.get_path()
        self.assertEqual(self.file_path, path_get)

    def test_set_path_for_a_folder(self):
        self.file.set_path(self.path)
        get_path = self.file.get_path()
        self.assertEqual(self.path, get_path)


if __name__ == '__main__':
    unittest.main()