import configparser
import definition

class Menu:
    config_file = definition.ROOT_DIR + "\\config\\settings.ini"
    def read_settings(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
    # def __init__(self):
    #     print("nu")
    # method to read the settings.ini file
        return config

    # method to get the name from settings.ini file
    def get_name(self):
        config = self.read_settings()
        name = config['CONFIG']['name']
        #print(name)
        return name

    # get_name()

    # method to get the path from settings.ini file
    def get_path(self):
        config = self.read_settings()
        path = config['CONFIG']['path']
        #print(path)
        return path

    # get_path()

    # method to get the path from settings.ini file
    def get_type_search(self):
        config = self.read_settings()
        type_search = config['CONFIG']['type_search']
        return type_search
        

    # method to overwrite name on settings.ini file
    def set_name(self, name):
        config = self.read_settings()
        config['CONFIG']['name'] = name
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        self.get_name()
        # set_name()

        # method to overwrite name on settings.ini file

    def set_path(self, path):
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


