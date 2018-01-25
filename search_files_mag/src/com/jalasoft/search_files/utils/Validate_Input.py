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

        self.name = str(name)
        name.strip()

        if (len(name) > 0) and (len(name) <= 240):
            if self.has_wilcards(name) == False:
                if self.is_sent_name_only_with_spaces(name) == False:
                    if self.is_name_begins_with_space(name) == False:
                        if self.is_name_ends_with_space(name) == False:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

        else:
            return False

    def has_wilcards(self, name):

        """
        has_wilcards method is implemented to verify that some specific
        characters are into the string that is sent to this method.
        :param name: It is a string to verify it is contains some specific characters
        :return: boolean, True should be returned when at least one of specific characters are in the string.
        """
        no_allowed_characters = ':/\?*|<>'
        response = False
        counter = 0
        while counter < len(no_allowed_characters):
            if no_allowed_characters[counter] in name:
                response = True
            counter = counter + 1
        return response

    def is_sent_name_only_with_spaces(self, name):
        """
        is_sent_name_only_with_spaces this method verify if name contains only spaces
        :param name: It is a string to verify it contains only spaces
        :return: this attribute returns True if the string sent is only spaces the otherwise it will return false
        """
        response = True
        counter = 0
        while counter < len(name):
            if name[counter] != ' ':
                response = False
            counter = counter + 1
        return response

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
        
        path = path
        return os.path.isdir(path)


validate = ValidateInput()
print(validate.is_valid_name('Payroll'))