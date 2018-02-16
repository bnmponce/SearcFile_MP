import unittest
from src.com.jalasoft.search_files.menu.menu_operations import *
from src.com.jalasoft.search_files.search.file import *

class Test_Menu_Operations(unittest.TestCase):
    def setUp(self):
        self.menu_operations = MenuOperations()
        self.name = "test1234"
        self.path = "D:\\"
        self.type = "1"
        self.case_sensitive = "n"
        self.results = []
        self.file = File()
        self.file.path = "D:\\downloads\gokk-104.mp4"
        self.file.name = "gokk-104.mp4"
        self.file.owner = "Gladys"
        self.file.size = 10
        self.file.extension = "mp4"
        self.file.date_accessed = "01012018"
        self.file.date_created = "01012018"
        self.file.date_modified = "01012018"
        self.results.append(self.file)
        self.folder = File()
        self.folder.path = "D:\\downloads\gokk"
        self.folder.name = "gokk"
        self.folder.owner = "Admin"
        self.folder.extension = ""
        self.folder.size = 200
        self.folder.date_accessed = "01012017"
        self.folder.date_created = "01012017"
        self.folder.date_modified = "01012017"
        self.results.append(self.folder)

    def test_name_operation(self):
        state = self.menu_operations.name_operation(self.name)
        self.assertTrue(state)

    def test_path_operation(self):
        state = self.menu_operations.path_operation(self.path)
        self.assertTrue(state)

    def test_type_operation(self):
        state = self.menu_operations.type_operation(self.type)
        self.assertTrue(state)

    def test_case_sensitive_operation(self):
        state = self.menu_operations.case_sensitive_operation(self.case_sensitive)
        self.assertTrue(state)

    def test_extension_operation(self):
        result = self.menu_operations.extension_filter("mp4", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_extension(), "mp4")

    def test_size_lower_operation(self):
        result = self.menu_operations.size_filter(100, "l", self.results)
        self.assertEqual(len(result), 1)
        size = result[0].get_size() < 100
        self.assertTrue(size)

    def test_size_equal_operation(self):
        result = self.menu_operations.size_filter(10, "e", self.results)
        self.assertEqual(len(result), 1)
        size = result[0].get_size() == 10
        self.assertTrue(size)

    def test_size_equal_operation(self):
        result = self.menu_operations.size_filter(50, "g", self.results)
        self.assertEqual(len(result), 1)
        size = result[0].get_size() > 50
        self.assertTrue(size)

    def test_owner_operation(self):
        result = self.menu_operations.owner_filter("Gladys", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_owner(), "Gladys")

    def test_name_find_operation(self):
        result = self.menu_operations.name_find_filter("e", "gokk-104", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_file_folder_name(), "gokk-104.mp4")

    def test_date_created_equal_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "e", "c", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_created(), "01012018")

    def test_date_created_lower_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "l", "c", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_created(), "01012017")

    def test_date_created_greater_operation(self):
        result = self.menu_operations.date_filter("01-01-2017", "g", "c", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_created(), "01012018")

    def test_date_modified_equal_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "e", "m", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_modified(), "01012018")

    def test_date_modified_lower_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "l", "m", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_modified(), "01012017")

    def test_date_modified_greater_operation(self):
        result = self.menu_operations.date_filter("01-01-2017", "g", "m", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_modified(), "01012018")

    def test_date_accessed_equal_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "e", "a", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_last_access(), "01012018")

    def test_date_accessed_lower_operation(self):
        result = self.menu_operations.date_filter("01-01-2018", "l", "a", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_last_access(), "01012017")

    def test_date_accessed_greater_operation(self):
        result = self.menu_operations.date_filter("01-01-2017", "g", "a", self.results)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_date_last_access(), "01012018")

if __name__ == '__main__':
    unittest.main()