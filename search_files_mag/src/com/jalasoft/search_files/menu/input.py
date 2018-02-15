import configparser
import definition
from src.com.jalasoft.search_files.utils.logging import logger

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
        logger.info('Enter to read_settings method')
        config = configparser.ConfigParser()
        config.read(self.config_file)
        logger.info('Exit from read_settings method')
        return config

    def get_name(self):
        """
        This get_name method retrieves the name parameter from settings.ini
        :param self:
        :return: It returns the name configured in settings.ini
        """
        logger.info('Enter to get_name method')
        config = self.read_settings()
        name = config['CONFIG']['name']
        logger.info('Exit from get_name method')
        return name

    def get_path(self):
        """
        This get_path method retrieves the path parameter from settings.ini
        :param self:
        :return: It returns the path configured in settings.ini
        """
        logger.info('Enter to get_path method')
        config = self.read_settings()
        path = config['CONFIG']['path']
        logger.info('Exit from get_path method')
        return path

    def get_type_search(self):
        """
        This get_type_search method retrieves the type of search parameter from settings.ini
        :param self:
        :return: It returns the search type configured in settings.ini which can be  1 = file, 2 = folder, 3 = both
        """
        logger.info('Enter to get_type_search method')
        config = self.read_settings()
        type_search = config['CONFIG']['type_search']
        logger.info('Exit from get_type_search method')
        return type_search

    def get_case_sensitive(self):
        """
        This get_case_sensitive method retrieves the case sensitive parameter from settings.ini
        :param self:
        :return: It returns the parameter to determine if search will be case sensitive or not. By default is non case
        sensitive 'n'
        """
        logger.info('Enter to get_case_sensitive method')
        config = self.read_settings()
        case_sensitive = config['CONFIG']['case_sensitive']
        logger.info('Exit from get_case_sensitive method')
        return case_sensitive

    def set_name(self, name):
        """
        This set_name method overwrite the name parameter in settings.ini
        :param self:
        :param name: It receives a valid file name which should meet file name rules
        """
        logger.info('Enter to set_name method')
        config = self.read_settings()
        config['CONFIG']['name'] = name
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        logger.info('Overwritten name in setting.ini file. Exiting from set_name method')

    def set_path(self, path):
        """
        This set_name method overwrite the path parameter in settings.ini
        :param self:
        :param path: It receives a valid path that exist in the system
        """
        logger.info('Enter to set_path method')
        config = self.read_settings()
        config['CONFIG']['path'] = path
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        logger.info('Overwritten path in setting.ini file. Exiting from set_path method')

    def set_type_search(self, type_search):
        """
        This set_name method overwrite the type search parameter in settings.ini
        :param self:
        :param type_search: It receives a valid type among 1, 2, 3 values
        """
        logger.info('Enter to set_type_search method')
        config = self.read_settings()
        config['CONFIG']['type_search'] = type_search
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        logger.info('Overwritten type search in setting.ini file. Exiting from set_type_search method')

    def set_case_sensitive(self, case_sensitive):
        """
        This set_name method overwrite the name parameter in settings.ini
        :param self:
        :param case_sensitive: It receives a valid parameter to determine if search will be case sensitive or not
        """
        logger.info('Enter to set_case_sensitive method')
        config = self.read_settings()
        config['CONFIG']['case_sensitive'] = case_sensitive
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        logger.info('Overwritten case sensitive parameter in setting.ini file. Exiting from set_case_sensitive method')
