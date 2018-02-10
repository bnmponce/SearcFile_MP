import unittest
import os
from _datetime import datetime
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

    def test_set_and_get_file_folder_name_for_file_name(self):
        self.file.set_file_folder_name(self.file_name)
        name_get = self.file.get_file_folder_name()
        self.assertEqual(self.file_name, name_get)

    def test_set_and_get_file_folder_name_for_folder_name(self):
        self.file.set_file_folder_name("test_search")
        get_name = self.file.get_file_folder_name()
        self.assertEqual("test_search", get_name)

    def test_set_and_get_path_for_a_file(self):
        self.file.set_path(self.file_path)
        path_get = self.file.get_path()
        self.assertEqual(self.file_path, path_get)

    def test_set_and_get_path_for_a_folder(self):
        self.file.set_path(self.path)
        get_path = self.file.get_path()
        self.assertEqual(self.path, get_path)

    def test_set_and_get_file_size(self):
        self.file.set_size(1048576)
        size_get = self.file.get_size()
        self.assertEqual(1, size_get)

    def test_set_and_get_is_file_for_file(self):
        self.file.set_is_file(os.path.isfile(self.file_path))
        self.assertTrue(self.file.get_is_file())

    def test_set_and_get_is_file_for_folder(self):
        self.file.set_is_file(os.path.isdir(self.path))
        self.assertTrue(self.file.get_is_file())

    def test_set_is_file_for_non_existing_paths(self):
        self.file.set_is_file(os.path.isdir('C:\\NonExist'))
        self.assertFalse(self.file.get_is_file())

    def test_set_and_get_extension_for_files(self):
        self.file.set_extension('.txt')
        extension = os.path.splitext(self.file_path)
        self.assertEqual(extension[1], self.file.get_extension())

    def test_set_and_get_extension_for_folder(self):
        self.file.set_extension('')
        extension = os.path.split(self.path)
        self.assertEqual(extension[1], self.file.get_extension())

    def test_set_and_get_file_date_created(self):
        self.file.set_date_created(datetime.now().timestamp())
        today_date = datetime.strftime(datetime.now(), '%m%d%Y')
        self.assertEqual(today_date, self.file.get_date_created())

    def test_set_and_get_file_date_modified(self):
        self.file.set_date_modified(datetime.now().timestamp())
        today_date = datetime.strftime(datetime.now(), '%m%d%Y')
        self.assertEqual(today_date, self.file.get_date_modified())

    def test_set_and_get_file_date_last_access(self):
        self.file.set_date_last_access(datetime.now().timestamp())
        today_date = datetime.strftime(datetime.now(), '%m%d%Y')
        self.assertEqual(today_date, self.file.get_date_last_access())

    def test_set_and_get_file_owner(self):
        self.file.set_owner('Administrator')
        owner = self.file.get_owner()
        self.assertEqual('Administrator', owner)

    def test_convert_date_tool(self):
        date = self.file.convert_date(datetime.now().timestamp())
        date2 = datetime.strftime(datetime.now(), '%m%d%Y')
        self.assertEqual(date, date2)


if __name__ == '__main__':
    unittest.main()