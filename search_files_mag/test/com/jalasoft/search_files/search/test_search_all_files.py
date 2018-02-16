import unittest
from datetime import datetime
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.search.file import *


class TestSearchAllFiles(unittest.TestCase):


    def setUp(self):
        self.search = SearchFiles()
        self.username = 'Ariel Zurita'
        self.today_date = datetime.strftime(datetime.now(), '%m%d%Y')
        self.path = "C:\\test_search\\"
        self.path2 = "C:\\test_search\\test"
        self.file_name = "test.txt"
        self.file_name2 = "ARIEL.txt"
        self.file_path = os.path.join(self.path, self.file_name)
        self.file_path2 = os.path.join(self.path, self.file_name2)
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            os.makedirs(self.path2)
        file = open(self.file_path, 'a')
        file2 = open(self.file_path2, 'a')
        file.close()
        file2.close()

    def test_set_file_values(self):
        file_set = File()
        for root, folders, files in os.walk(self.path):
            for file in files:
                file_set = self.search.set_file_values(root, file)
        self.assertIsNotNone(file_set)
        self.assertEqual(file_set.get_file_folder_name(), self.file_name)
        self.assertEqual(file_set.get_path(), self.file_path)
        self.assertEqual(file_set.get_size(), 0.0)
        self.assertTrue(file_set.get_is_file())
        self.assertEqual(file_set.get_extension(), '.txt')
        self.assertEqual(file_set.get_date_created(), self.today_date)
        self.assertEqual(file_set.get_date_modified(), self.today_date)
        self.assertEqual(file_set.get_date_last_access(), self.today_date)
        self.assertIsNotNone(file_set.get_owner())

    def test_set_folder_values(self):
        folder_set = File()
        for root, folders, files in os.walk(self.path):
            for folder in folders:
                folder_set = self.search.set_folder_values(root, folder)
        self.assertIsNotNone(folder_set)
        self.assertEqual(folder_set.get_file_folder_name(), 'test')
        self.assertEqual(folder_set.get_path(), self.path2)
        self.assertEqual(folder_set.get_size(), 0.0)
        self.assertFalse(folder_set.get_is_file())
        self.assertIsNone(folder_set.get_extension())
        self.assertEqual(folder_set.get_date_created(), self.today_date)
        self.assertEqual(folder_set.get_date_modified(), self.today_date)
        self.assertEqual(folder_set.get_date_last_access(), self.today_date)
        self.assertIsNotNone(folder_set.get_owner())

    def test_search_all_resutls_for_a_file(self):
        results = self.search.file_all_results(self.path, 'test', 1)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEqual(results[0].get_file_folder_name(), 'test.txt')
        self.assertEqual(results[0].get_path(), self.file_path)
        self.assertEqual(results[0].get_size(), 0.0)
        self.assertTrue(results[0].get_is_file())
        self.assertEqual(results[0].get_extension(), '.txt')
        self.assertEqual(results[0].get_date_created(), self.today_date)
        self.assertEqual(results[0].get_date_modified(), self.today_date)
        self.assertEqual(results[0].get_date_last_access(), self.today_date)
        self.assertIsNotNone(results[0].get_owner())

    def test_search_all_resutls_for_a_folder(self):
        results = self.search.file_all_results(self.path, 'test', 2)
        self.assertIsNotNone(results)
        self.assertEqual(results[0].get_file_folder_name(), 'test')
        self.assertEqual(results[0].get_path(), self.path2)
        self.assertEqual(results[0].get_size(), 0.0)
        self.assertFalse(results[0].get_is_file())
        self.assertIsNone(results[0].get_extension())
        self.assertEqual(results[0].get_date_created(), self.today_date)
        self.assertEqual(results[0].get_date_modified(), self.today_date)
        self.assertEqual(results[0].get_date_last_access(), self.today_date)
        self.assertIsNotNone(results[0].get_owner())

    def test_search_results_for_files_and_folders(self):
        results = self.search.file_all_results(self.path, 'test', 3)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get_file_folder_name(), 'test.txt')
        self.assertEqual(results[0].get_path(), self.file_path)
        self.assertEqual(results[0].get_size(), 0.0)
        self.assertTrue(results[0].get_is_file())
        self.assertEqual(results[0].get_extension(), '.txt')
        self.assertEqual(results[0].get_date_created(), self.today_date)
        self.assertEqual(results[0].get_date_modified(), self.today_date)
        self.assertEqual(results[0].get_date_last_access(), self.today_date)
        self.assertIsNotNone(results[0].get_owner())
        self.assertEqual(results[1].get_file_folder_name(), 'test')
        self.assertEqual(results[1].get_path(), self.path2)
        self.assertEqual(results[1].get_size(), 0.0)
        self.assertFalse(results[1].get_is_file())
        self.assertIsNone(results[1].get_extension())
        self.assertEqual(results[1].get_date_created(), self.today_date)
        self.assertEqual(results[1].get_date_modified(), self.today_date)
        self.assertEqual(results[1].get_date_last_access(), self.today_date)
        self.assertIsNotNone(results[1].get_owner())

    def test_filter_by_extension(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_extension('txt', result1)
        self.assertIsNotNone(result2)
        self.assertEqual(result2[0].get_extension(), '.txt')

    def test_filter_by_size_with_operator_equal(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_size('e', 0.0, result1)
        self.assertIsNotNone(result2)
        self.assertEqual(result2[0].get_size(), 0.0)
        self.assertEqual(result2[1].get_size(), 0.0)

    def test_filter_by_size_with_operator_less(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_size('l', 0.0, result1)
        self.assertIsNotNone(result2)

    def test_filter_by_size_with_operator_greater(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_size('g', 0.0, result1)
        self.assertIsNotNone(result2)

    def test_filter_by_date_created_with_operator_equal(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_created(result1, self.today_date, 'e')
        self.assertIsNotNone(result2)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0].get_date_created(), self.today_date)
        self.assertEqual(result2[1].get_date_created(), self.today_date)

    def test_filter_by_date_created_with_operator_less(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_created(result1, self.today_date, 'l')
        self.assertIsNotNone(result2)

    def test_filter_by_date_created_with_operator_greater(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_created(result1, self.today_date, 'g')
        self.assertIsNotNone(result2)

    def test_filter_by_date_modified_with_operator_equal(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_modified(result1, self.today_date, 'e')
        self.assertIsNotNone(result2)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0].get_date_modified(), self.today_date)
        self.assertEqual(result2[1].get_date_modified(), self.today_date)

    def test_filter_by_date_modified_with_operator_less(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_modified(result1, self.today_date, 'l')
        self.assertIsNotNone(result2)

    def test_filter_by_date_modified_with_operator_greater(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_modified(result1, self.today_date, 'g')
        self.assertIsNotNone(result2)

    def test_filter_by_date_last_access_with_operator_equal(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_last_access(result1, self.today_date, 'e')
        self.assertIsNotNone(result2)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0].get_date_last_access(), self.today_date)
        self.assertEqual(result2[1].get_date_last_access(), self.today_date)

    def test_filter_by_date_last_access_with_operator_less(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_last_access(result1, self.today_date, 'l')
        self.assertIsNotNone(result2)

    def test_filter_by_date_last_access_with_operator_greater(self):
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_date_last_access(result1, self.today_date, 'g')
        self.assertIsNotNone(result2)

    def test_filter_by_owner(self):
        """
        This unittest will fail each time that it's used in other machines please change username 'PC' with a valid username
        for your machine
        """
        result1 = self.search.file_all_results(self.path, 'test', 3)
        result2 = self.search.filter_by_owner(result1, self.username)
        self.assertIsNotNone(result2)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0].get_owner(), self.username)
        self.assertEqual(result2[1].get_owner(), self.username)

    def test_calculate_folder_size(self):
        result = self.search.calculate_folder_size(self.path)
        self.assertEqual(result, 0.0)

    def test_extract_extension(self):
        result = self.search.extract_extension(self.file_path)
        self.assertEqual(result, '.txt')

    def test_format_date_parameter(self):
        result = self.search.format_date_parameter('02-11-2018')
        self.assertEqual(result, '02112018')

    def test_convert_string_to_date(self):
        result = self.search.convert_string_to_date('02112018')
        self.assertEqual(result, datetime(2018, 2, 11, 0, 0))

    def test_get_owner(self):
        """
        This unittest will fail each time that it's used in other machines please change username 'PC' with a valid username
        for your machine
        """
        result = self.search.get_owner(self.file_path)
        self.assertEqual(result, self.username)

    def test_search_exactly_equal(self):
        result1 = self.search.file_all_results(self.path, 'ARIEL', 3)
        result2 = self.search.search_exactly_equal(result1, 'ARIEL')
        self.assertIsNotNone(result2)
        self.assertEqual(result2[0].get_file_folder_name(), 'ARIEL.txt')

if __name__ == '__main__':
    unittest.main()
