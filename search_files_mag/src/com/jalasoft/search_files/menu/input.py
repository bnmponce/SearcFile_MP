import configparser

def read_settings():
    config = configparser.ConfigParser()
    config.read('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini')
    #print(config['CONFIG']['name'])
    return config

def get_name():
    config = read_settings()
    name = config['CONFIG']['name']
    print(name)
    return name
get_name()

def get_path():
    config = read_settings()
    path = config['CONFIG']['path']
    print(path)
    return path
get_path()

def set_name():
    config = read_settings()
    config['CONFIG']['name'] = 'test2'
    with open('E:\\2018\\DevFundamentals2\\SearchFileProject\\search_files_mag\\config\\settings.ini', 'w') as configfile:
        config.write(configfile)
    get_name()
set_name()