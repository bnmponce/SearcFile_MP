import configparser
import definition

class Menu:
    """
    Menu class and methods
    This class contains all get and set methods required to read/overwrite the setting.ini file
    in such way obtain the parameter to search file/folders
    """

    config_file = definition.ROOT_DIR + "\\config\\settings.ini"

    def read_settings(self):
        """
        This read_setting method allows to read the list of parsed file names (settings.ini)
        :param self:
        :return: This method return the configurations from setting.ini
        """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config

    def get_name(self):
        """
        This get_name method retrieves the name parameter from settings.ini
        :param self:
        :return: It returns the name configured in settings.ini
        """
        config = self.read_settings()
        name = config['CONFIG']['name']
        return name

    def get_path(self):
        """
        This get_path method retrieves the path parameter from settings.ini
        :param self:
        :return: It returns the path configured in settings.ini
        """
        config = self.read_settings()
        path = config['CONFIG']['path']
        return path

    def get_type_search(self):
        """
        This get_type_search method retrieves the type of search parameter from settings.ini
        :param self:
        :return: It returns the search type configured in settings.ini which can be  1 = file, 2 = folder, 3 = both
        """
        config = self.read_settings()
        type_search = config['CONFIG']['type_search']
        return type_search

    def get_size(self):
        """
        This get_size method retrieves the size parameter from settings.ini
        :param self:
        :return: It returns the size configured in settings.ini
        """
        config = self.read_settings()
        size = config['CONFIG']['size']
        return size

    def get_extension(self):
        """
        This get_extension method retrieves the file extension parameter from settings.ini
        :param self:
        :return: It returns the file extension configured in settings.ini
        """
        config = self.read_settings()
        extension = config['CONFIG']['extension']
        return extension

    # def get_operator(self):
    #     config = self.read_settings()
    #     operator = config['CONFIG']['operator']
    #     return operator

    def get_date(self):
        """
        This get_date method retrieves the date from settings.ini
        :param self:
        :return: It returns the size configured in settings.ini
        """
        config = self.read_settings()
        date = config['CONFIG']['date']
        return date

    def set_name(self, name):
        """
        This set_name method overwrite the name parameter in settings.ini
        :param self:
        :param name: It receive a valid file name which should meet file name rules
        """
        config = self.read_settings()
        config['CONFIG']['name'] = name
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_name()

    def set_path(self, path):
        """
        This set_name method overwrite the name parameter in settings.ini
        :param self:
        :param name: It receive a valid file name which should meet file name rules
        """
        config = self.read_settings()
        config['CONFIG']['path'] = path
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_path()
        # set_name()

    def set_type_search(self, type_search):
        config = self.read_settings()
        config['CONFIG']['type_search'] = type_search
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_type_search()
        # set_name()

    def set_size(self, size):
        config = self.read_settings()
        config['CONFIG']['size'] = size
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_size()

    def set_extension(self, extension):
        config = self.read_settings()
        config['CONFIG']['extension'] = extension
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_extension()

    # def set_operator(self, operator):
    #     config = self.read_settings()
    #     config['CONFIG']['operator'] = operator
    #     with open(self.config_file, 'w') as configfile:
    #         config.write(configfile)
    #     self.get_operator()

    def set_date(self, date):
        config = self.read_settings()
        config['CONFIG']['date'] = date
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_date()