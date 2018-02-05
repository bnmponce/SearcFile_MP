import os
import unicodedata
import time
import parser


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
        result = False

        if (len(name) > 0) and (len(name) <= 240):
            if self.has_wilcards(name) == False:
                if self.is_sent_name_only_with_spaces(name) == False:
                    if self.is_name_begins_with_space(name) == False:
                        if self.is_name_ends_with_space(name) == False:
                            result = True
                        else:
                            result = False
                    else:
                        result = False
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return result

    def has_wilcards(self, name):

        """
        has_wilcards method is implemented to verify that some specific
        characters are into the string that is sent to this method.
        :param name: It is a string to verify it is contains some specific characters
        :return: boolean, True should be returned when at least one of specific characters are in the string.
        """
        no_allowed_characters = ':/\?*|<>'
        result = False
        counter = 0
        while counter < len(no_allowed_characters):
            if no_allowed_characters[counter] in name:
                result = True
            counter = counter + 1
        return result

    def is_sent_name_only_with_spaces(self, name):
        """
        is_sent_name_only_with_spaces this method verify if name contains only spaces
        :param name: It is a string to verify it contains only spaces
        :return: this attribute returns True if the string sent is only spaces the otherwise it will return false
        """
        result = True
        counter = 0
        while counter < len(name):
            if name[counter] != ' ':
                result = False
            counter = counter + 1
        return result

    def is_name_begins_with_space(self, name):
        """
        This method verify if name begins with a space
        :param name: It is a string
        :return: It returns True if name begins in space otherwise returns false
        """
        if name[0]== ' ':
            return True
        else:
            return False

    def is_name_ends_with_space(self, name):
        """
        This method verify if name ends with a space
        :param name: It is a string
        :return: It returns True if name ends in space otherwise returns false
        """
        last_character = name[(len(name)-1)]
        if last_character == ' ':
            return True
        else:
            return False

    def is_valid_path(self, path):
        """
        This method is helpful to validate the path
        :param path: it is a string
        :return: it returns Tru when the path is a valid path otherwise it returns false
        """
        path = path
        return os.path.isdir(path)

    def is_valid_type(self, value):
        """
        This method is to validate the type field
        :param value: Int
        :return: This methos return tru if value is in (1, 2, 3) in otherwise is false
        """
        if value in ('1', '2', '3'):
            return True
        else:
            return False

    def is_type_a_file(self, value):
        """
        This methos is created to verify that type inset by user is a type for file
        :param value: int
        :return:
        """
        result = False
        if value == '1':
            result = True
        return result

    def is_type_a_folder(self, value):
        result = False
        if value == '2':
            result = True
        return result

    def is_type_both_file_folder(self, value):

        result = False
        if value == '3':
            result = True
        return result


    def is_valid_size(self, value):
        """
        This method is to verify if the size is a valid size
        :param value: it is a number
        :return: It should be return true if the the value is a positive number
        """
        result = False
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
        return result

    def is_size_meets_condition(self, file, value_to_compare, operator):
        """
        This method is created to compare the size of the file that was found with the size conditional entered by user
        :param file: It is a tuple that contaiuns the file name and file size
        :param value_to_compare: It is the size that is entered by user
        :param operator: It is a character that is insert by user as condition
        :return: It returns true is the file size meets the conditions otherwise it returns false.
        """
        result = False
        size = file[1]
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
        return result


    def is_valid_extention(self, path, extension):
        """
        This method is created to compare the extension of the file that was found
        with the extension that was insert by user
        :param path: it is the path of the file that is found
        :param extension: it is the extansion that is inserted by user
        :return: It retruns true inf extension of the file that is found is the same of extension insert by user
        """
        file = os.path.splitext(path)
        exten = file[1]
        if extension == exten:
            return True
        else:
            return False

    def is_valid_date(self, input_date):
        date = input_date.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        result = False
        if year >= 0 and year <= 9999:

            if month >= 1 and month <= 12:

                if month == 2:
                    if day >=1 and day <=28:

                        result = True
                else:
                    if day >= 1 and day <= 31:

                        result = True
        return result


    def is_date_meets_condition(self, result_date, input_date, operator):
        input_date = input_date.split('-')
        date = int(input_date[0] + input_date[1] + input_date[2])
        result_date= result_date.split('-')
        res_date = int(result_date[0] + result_date[1]+ result_date[2])
        print(type(res_date), res_date)
        print(type(date), date)

        result = False

        if operator == str('l'):
            if res_date <= date:
                result = True

        if operator == str('g'):
            if res_date > date:
                result = True

        if operator == str('e'):
            if res_date == date:
                result = True

        return result

    def is_date_between(self,result_date, minor_date, major_date):
        minor_date = minor_date.split('-')
        mi_date = int(minor_date[0]+ minor_date[1]+minor_date[2])
        major_date = major_date.split('-')
        ma_date = int(major_date[0] + major_date[1] + major_date[2])
        result_date = result_date.split('-')
        res_date = int(result_date [0] + result_date[1] + result_date[2])
        result = False

        if (res_date >= mi_date) and (res_date <= ma_date):
            result = True

        return result

