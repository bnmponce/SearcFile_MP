import unittest
from src.com.jalasoft.search_files.menu.input import *


class TestInput(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.name = "test1"
        self.path = "E:/"
        self.file_type = "3"
        self.case_sensitive = "n"

    def test_set_and_get_name(self):
        self.menu.set_name(self.name)
        test_name = self.menu.get_name()
        self.assertEqual(self.name, test_name)

    def test_set_and_get_path(self):
        self.menu.set_path(self.path)
        test_path = self.menu.get_path()
        self.assertEqual(self.path, test_path)

    def test_set_and_get_type_search(self):
        self.menu.set_type_search(self.file_type)
        test_file_type = self.menu.get_type_search()
        self.assertEqual(self.file_type, test_file_type)

    def test_set_and_get_case_sensitive(self):
        self.menu.set_case_sensitive(self.case_sensitive)
        test_case_sensitive = self.menu.get_case_sensitive()
        self.assertEqual(self.case_sensitive, test_case_sensitive)


if __name__ == '__main__':
    unittest.main()
