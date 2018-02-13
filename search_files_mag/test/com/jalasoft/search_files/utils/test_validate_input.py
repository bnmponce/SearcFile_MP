import unittest
from src.com.jalasoft.search_files.utils.validate_input import *

class Test_Validat_Input(unittest.TestCase):


    # Unittest for is_valid_name
    def test_name_validate_space_at_beging(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_name('   Test_name_test')
        self.assertFalse(valid)

    def test_name_validate_specific_wilcards(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_name('T*est_name_test')
        self.assertFalse(valid)

    def test_validate_name_allow_spaces_in_the_name(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_name('Test name test')
        self.assertTrue(valid)

    #Unittest for is_valid_type
    def test_character_is_validated_in_is_valid_type_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_type('Te')
        self.assertFalse(valid)

    def test_wilcard_is_validate_in_is_valid_type_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_type('*')
        self.assertFalse(valid)

    def test_empty_is_validate_in_is_valid_type(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_type('')
        self.assertFalse(valid)

    # Unitest for is_valid_flag_of_sensitivecase method
    def test_wilcard_is_validate_is_valid_flag_of_sensitivecase_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase('$')
        self.assertFalse(valid)

    def test_empty_is_validate_is_valid_flag_of_sensitivecase_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase('')
        self.assertFalse(valid)

    def test_space_is_validate_is_valid_flag_of_sensitivecase_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase('_')
        self.assertFalse(valid)

    # Unitest for is_valid_operator_to_exact_search method
    def test_wilcard_is_validate_is_valid_operator_to_exact_search(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase('%')
        self.assertFalse(valid)

    def test_empty_is_validate_is_valid_operator_to_exact_search(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase('')
        self.assertFalse(valid)

    def test_space_is_validate_is_valid_operator_to_exact_search(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_flag_of_sensitivecase(' ')
        self.assertFalse(valid)

    # Unittest for is_valid_size method
    def test_negative_number_is_validate_is_valid_size(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_size(-2)
        self.assertFalse(valid)

    def test_decimal_is_validate_is_valid_size(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_size(2.2)
        self.assertTrue(valid)

    def test_letter_is_validate_is_valid_size(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_size('test')
        self.assertFalse(valid)

    # Unittest for is_size_meets_conditions method
    def test_size_is_greater_than_conditions_is_size_meets_condition(self):
        valid_input = ValidateInput()
        valid = valid_input.is_size_meets_condition((0,5.5), '0.5', 'g')
        self.assertTrue(valid)

    def test_empty_value_is_validate_is_size_meets_condition_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_size_meets_condition((0, 5.5), '', '')
        self.assertFalse(valid)

    def test_wildcard_value_is_validate_is_size_meets_condition_method(self):
        valid_input = ValidateInput()
        valid = valid_input.is_size_meets_condition((0, 5.5), '%', '_')
        self.assertFalse(valid)

    #Unittest for is_valiz_path method
    #Unittest for is_file_extension_same_extension_enter_by_user method
    def test_extension_of_file_is_different_to_extension_enter_by_user(self):
        valid_input = ValidateInput()
        valid = valid_input.is_file_extension_same_extension_entered_by_user('D:\Fundacion\test.docx', '.txt')
        self.assertFalse(valid)

    def test_file_does_not_have_extension(self):
        valid_input = ValidateInput()
        valid = valid_input.is_file_extension_same_extension_entered_by_user('D:\Fundacion\test', '.txt')
        self.assertFalse(valid)

    #Unittest is_valid_date method
    def test_invalid_year_is_validate_in_is_valid_date(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_date('12-31-018')
        self.assertFalse(valid)

    def test_wilcard_is_validate_in_date(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_date('12-*--018')
        self.assertFalse(valid)

    def test_letter_is_validate_in_date(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_date('mm-31-aaaa')
        self.assertFalse(valid)

    def test_empty_is_validate_in_is_validate_in_date(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_date('')
        self.assertFalse(valid)

    #Unittest is_date_meets_condition method
    def test_date_of_file_do_not_meet_the_codintion(self):
        valid_input = ValidateInput()
        valid = valid_input.is_date_meets_condition('05-31-2017', '06-31-2017', 'g')
        self.assertFalse(valid)

    def test_wildcard_is_validate_in_is_size_meets_condition_nethod(self):
        valid_input = ValidateInput()
        valid = valid_input.is_date_meets_condition('05-3*-2017', '06-31-2017', '&')
        self.assertFalse(valid)

    def test_empty_is_validate_in_is_size_meets_condition_nethod(self):
        valid_input = ValidateInput()
        valid = valid_input.is_date_meets_condition('', '', '')
        self.assertFalse(valid)

    #Unit test is_valid_controldate method
    def test_wildcard_is_validated_in_is_valid_controldate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_controldate('*')
        self.assertFalse(valid)


    def test_empty_is_validated_in_is_valid_controldate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_controldate('')
        self.assertFalse(valid)


    def test_space_is_validated_in_is_valid_controldate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_controldate(' ')
        self.assertFalse(valid)

    #Unittest is_valid_opdate method
    def test_wildcard_is_validated_in_is_valid_opdate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_opdate('*')
        self.assertFalse(valid)


    def test_empty_is_validated_in_is_valid_opdate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_opdate('')
        self.assertFalse(valid)


    def test_space_is_validated_in_is_valid_opdate(self):
        valid_input = ValidateInput()
        valid = valid_input.is_valid_opdate(' ')
        self.assertFalse(valid)



test = Test_Validat_Input()
print(test.test_name_validate_space_at_beging())