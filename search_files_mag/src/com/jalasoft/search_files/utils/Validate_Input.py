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
            if self.has_no_allowed_characters(name) == False:
                if self.is_only_spaces(name) == False:
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False

    def has_no_allowed_characters(self, name):

        """
        has_no_allowed_characters method is implemented to verify that some specific
        characters are into the string that is sent to this method.
        :param file_name: It is a string to verifi it is contains some specific characters
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

    def is_only_spaces(self, name):
        response = True
        counter = 0
        while counter < len(name):
            if name[counter] != ' ':
                response = False
            counter = counter + 1
        return response


validate = ValidateInput()
print(validate.is_valid_name('   m   '))