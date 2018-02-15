import os
import unicodedata
from src.com.jalasoft.search_files.utils.logging import logger

class ValidateInput(object):
    """
    ValidateInput class and methods
    This class contains methods which are helpful to validation of the inputs
    to search_files project.
    """

    def is_valid_name(self, name):
        """
        is_valid_name method is development to validate the name of any file.

        :param self:
        :param name: This attribute is the name of file or folder to validate It will be a string
        :return: This method returns a boolean. True will be return if the name is a valid name for a file,
        if not it should be returned false
        """
        logger.info('Enter to is_valid_name method')
        result = False
        if name is not None:
            if (len(name) > 0) and (len(name) <= 240):
                if self._has_wilcards(name) == False and self._is_sent_name_only_with_spaces(name) == False and \
                        self._is_name_begins_with_space(name) == False and self._is_name_ends_with_space(name) == False:
                    result = True

        logger.info("Exiting from is_valid_name method")
        return result

    def _has_wilcards(self, name):

        """
        has_wilcards method is implemented to verify that some specific
        characters are into the string that is sent to this method.
        :param name: It is a string to verify it is contains some specific characters
        :return: boolean, True should be returned when at least one of specific characters are in the string.
        """
        logger.info("Enter to has_wildards method")
        no_allowed_characters = ':/\?*|<>'
        result = False
        counter = 0
        while counter < len(no_allowed_characters):
            if no_allowed_characters[counter] in name:
                result = True
            counter = counter + 1
        logger.info("Exiting from has_wilcards method")
        return result

    def _is_sent_name_only_with_spaces(self, name):
        """
        is_sent_name_only_with_spaces this method verify if name contains only spaces
        :param name: It is a string to verify it contains only spaces
        :return: this attribute returns True if the string sent is only spaces the otherwise it will return false
        """
        logger.info("Enter to is_sent_name_only_with_spaces method")
        result = True
        counter = 0
        while counter < len(name):
            if name[counter] != ' ':
                result = False
            counter = counter + 1
        logger.info("Exiting from is_sent_name_only_with_spaces method")
        return result

    def _is_name_begins_with_space(self, name):
        """
        This method verify if name begins with a space
        :param name: It is a string
        :return: It returns True if name begins in space otherwise returns false
        """
        logger.info("Enter to is_name_begins_with_space method")
        result = False
        if name[0] == ' ':
            result = True
        logger.info("Exiting from is_name_begins_with_space method")
        return result

    def _is_name_ends_with_space(self, name):
        """
        This method verify if name ends with a space
        :param name: It is a string
        :return: It returns True if name ends in space otherwise returns false
        """
        logger.info("Enter to is_name_ends_with_space method")
        last_character = name[(len(name)-1)]
        result = False
        if last_character == ' ':
            result = True
        logger.info("Exiting from is_name_ends_with_space method")
        return result

    def is_valid_path(self, path):
        """
        This method is helpful to validate the path
        :param path: it is a string
        :return: it returns Tru when the path is a valid path otherwise it returns false
        """
        logger.info("Enter to is_valid_path method")
        path = path

        logger.info("Exiting from is_valid_path method")
        return os.path.isdir(path)


    def is_valid_type(self, value):
        """
        This method is to validate the type field
        :param value: String
        :return: This method return true if value is in (1, 2, 3) in otherwise is false
        """
        logger.info("Enter to is_valid_type method")
        result = False

        if value in ('1', '2', '3'):
            result = True
        logger.info("Exiting from is_valid_type method")
        return result

    def is_valid_flag_of_sensitivecase(self, value):
        """
        This method is to validate if the value insert by user is valid flag.
        :param value: String
        :return: This method returns true if value is 'c' or 'n' in otherwise it returns false.
        """
        logger.info("Enter to is_valid_flag_of_sensitivecase method")
        result = False
        if value in ('c', 'n'):
            result = True

        logger.info("Exiting from is_valid_flag_of_sensitivecase method")
        return result


    def is_valid_operator_to_exact_search(self, value):
        """
        this method is to validate if the operator insert by user is valid operator
        :param value: string
        :return: This method returns True id the value is 'e' in otherwise ti returns false.
        """

        logger.info("Enter to is_valid_operator_to_exact_search method")
        result = False
        if value == 'e':
            result = True
        logger.info("Exiting from is_valid_operator_to_exact_search method")
        return result

    def is_valid_size(self, value):
        """
        This method is to verify if the size is a valid size
        :param value: it is a number
        :return: It should be return true if the the value is a positive number
        """
        logger.info('Enter to is_valid_size method')
        result = False
        if value is not None:

            try:
                size = float(value)
                if size >= 0:
                    result = True
                return result
            except ValueError:
                pass
            try:
                size = unicodedata.numeric(value)
                if size >= 0:
                    result = True
                return result
            except(TypeError, ValueError):
                pass
        logger.info('Exiting from is_valid_size method')
        return result

    def is_size_meets_condition(self, file, value_to_compare, operator):
        """
        This method is created to compare the size of the file that was found with the size conditional entered by user
        :param file: It is a tuple that contaiuns the file name and file size
        :param value_to_compare: It is the size that is entered by user
        :param operator: It is a character that is insert by user as condition
        :return: It returns true is the file size meets the conditions otherwise it returns false.
        """
        logger.info('Enter to is_size_meets_condition method')
        result = False
        if file is not None:
            size = file[1]
            if self.is_valid_size(size) and self.is_valid_size(value_to_compare) and operator in ('l', 'g', 'e'):
                value = float(value_to_compare)
                if operator == str('l'):
                    if size < value:
                        result = True
                if operator == str('g'):
                    if size > value:
                        result = True
                if operator == str('e'):
                    if size == value:
                        result = True
        logger.info('Exiting from is_size_meets_condition method')
        return result


    def is_file_extension_same_extension_entered_by_user(self, path, extension):
        """
        This method is created to compare the extension of the file that was found
        with the extension that was insert by user
        :param path: it is the path of the file that is found
        :param extension: it is the extension that is inserted by user
        :return: It returns true inf extension of the file that is found is the same of extension insert by user
        """
        logger.info('Enter to is_file_extension_same_extension_entered_by_user method')
        result = False
        if path is not None and extension is not None:

            file = os.path.splitext(path)
            exten = file[1]

            if extension == exten:
                result = True
        logger.info('Exiting from is_file_extension_same_extension_entered_by_user method')
        return result


    def is_valid_date(self, input_date):
        """
        This method is implemented to validate if the date insert by user is a valid date.
        :param input_date: It is a string and is the date insert by user
        :return: It returns True if the date insert by user is valid date in otherwise it returns false
        """
        logger.info('Enter to is_valid_date method')
        result = False
        if input_date is not '' and input_date is not None:
            if input_date[2] == '-' and input_date[5] == '-':
                date = input_date.split('-')
                year_len = len(date[2])
                try:
                    month = int(date[0])
                    day = int(date[1])
                    year = int(date[2])
                    logger.info('Begins the date validation')
                    if year >= 0 and year <= 9999 and year_len == 4:

                        if month >= 1 and month <= 12:

                            if month == 2:
                                if day >= 1 and day <= 28:
                                    result = True
                            else:
                                if day >= 1 and day <= 31:
                                    result = True
                    return result
                except ValueError:
                    pass
        logger.info('Exiting from is_valid_date method')
        return result


    def is_date_meets_condition(self, result_date, input_date, operator):
        """
        This method is implemented to verify that the date of the file that is found in the response
        meets the condition of the date that is insert by user.
        :param result_date: It is a string that is the data of the file that is found in the response
        :param input_date: It is a  string that is the date that is insert by user
        :param operator: it is the conditional
        :return: It returns true if the dated of the file meets the condition in otherwise it returns false
        """
        logger.info('Enter is_date_meets_condition method')
        result = False
        if self.is_valid_date(result_date) and self.is_valid_date(input_date) and operator in ('l', 'g', 'e'):
            input_date = input_date.split('-')
            result_date = result_date.split('-')
            date = input_date[2]
            if len(input_date[0]) < 2:
                date = date + '0'+ input_date[0]
            else:
                date = date + input_date[0]

            if len(input_date[1]) < 2:
                date = date + '0' + input_date[1]
            else:
                date = date + input_date[1]

            res_date = result_date[2]
            if len(result_date[0]) < 2:
                res_date = res_date + '0' + result_date[0]

            else:
                res_date = res_date + result_date[0]

            if len(result_date[1]) < 2:
                res_date = res_date + '0' + result_date[1]
            else:
                res_date = res_date + result_date[1]

            logger.info('date was convert to int' + date +'Date Insert by user' + res_date + 'date of the file')

            date = int(date)
            res_date = int(res_date)

            logger.info('Begins the date validation')
            if operator == str('l'):
                if res_date <= date:
                    result = True

            if operator == str('g'):
                if res_date > date:
                    result = True

            if operator == str('e'):
                if res_date == date:
                    result = True
        logger.info('Exiting from is_date_meets_condition method')
        return result

    def is_valid_controldate(self, value):
        """
        This method verify that control date is a valid operator
        :param value: string
        :return: It returns true if operator enter by user is in (c, m, a) in otherwise ti returns false
        """
        logger.info('Enter to is_valid_controldate method')
        result = False
        if value in ('c','m', 'a'):
            result = True
        logger.info('Exiting from is_valid_controldate method')
        return result

    def is_valid_operators(self, value):
        """
        this method is to verify that value enter var user is a valid operator day
        :param value: string
        :return: It returns true if value insert by user is in (l, g, e) in otherwise ti returns false
        """
        logger.info('Enter to is_valid_operators method')
        result = False
        if value in ('l', 'g', 'e'):
            result = True
        logger.info('Exiting from is_valid_operators method')
        return result