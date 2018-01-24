class ValidateInput(object):

    """
    ValidateInput class and methods
    This class contains methods which are helpful to validation of the inputs
    to search_files project.
    """

    def validate_file_name(self, validate_name):

        """
        Validate_file_name method is development to validate the name of any file.

        :param self:
        :param validate_name: This attribute is the name of file or folder to validate It will be a string
        :return: This method returns a boolean. True will be return if the name is a valid name for a file,
        if not it should be returned false
        """

        self.validate_name = str(validate_name)
        validate_name.strip(' ')

        if (len(validate_name)> 0) and (len(validate_name)<= 240):
            if self.check_no_allowed_characters(validate_name)== False:
                return True
            else:
                return False
        else:
            return False

    def check_no_allowed_characters(self, file_name):

        """
        check_no_allowed_characters method is implemented to verify that some specific
        characters are into the string that is sent to this method.
        :param file_name: It is a string to verifi it is contains some specific characters
        :return: boolean, True should be returned when at least one of specific characters are in the string.
        """
        
        no_allowed_characters = ':/\?*|<>'
        response = False
        counter = 0
        while counter < len(no_allowed_characters):
            if no_allowed_characters[counter] in file_name:
                response = True
            counter = counter + 1
        return response




validate = ValidateInput()
print(validate.validate_file_name('test4 tes6  &^(test()= &^(test()= &^(test()='))
