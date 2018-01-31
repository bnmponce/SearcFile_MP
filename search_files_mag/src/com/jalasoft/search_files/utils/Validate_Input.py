import os
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
        if value in (1, 2, 3):
            return True
        else:
            return False

    def is_number(self, value):
        """
        This method verify that the value sent is o not a number
        :param value: It can be a int or string
        :return: It returns True when the value is int, float, complex number otherwise it returns False
        """
        if type(value) in (int, float, complex):
            return True
        else:
            return False

    def is_valid_size(self, value):
        """
        This method is to verify if the size is a valid size
        :param value: it is a number
        :return: It should be return true if the the value is a positive number
        """
        result= False
        if self.is_number(value):
            if value >= 0:
                result = True
        return result

    def is_size_meets_condition(self, file_size, value_to_compare, operator):
        """
        This method is implemented to verify that size meets the condition to search, this method receive 3 attributes
        the size of file or folder, the value to compare the size and the operator
        :param file_size: int
        :param value_to_compare: int
        :param oper: > < =
        :return: it returns true when the size meets the condition that is sent by the operator in otherwise it returns false
        """
        result = False
        if operator == str('<'):
            if file_size < value_to_compare:
                result = True
        if operator == str('>'):
            if file_size > value_to_compare:
                result = True
        if operator == str('='):
            if file_size == value_to_compare:
                result = True
        return result


    def is_valid_extention(self, path):
        """
        This method is created to verify that the extexntion of a file is a valid extension
        :param path: The path of the file is sent as a string
        :return: it return true if the extension of the file is in the list of the extensions that are set in the method
        """
        file = os.path.splitext(path)
        extension = file[1]
        valid_extension = ['.py', '.txt', 'jpg', '.png']
        if extension in valid_extension:
            return True
        else:
            return False






