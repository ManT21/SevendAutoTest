import configparser


def read_baseurl_config():
    #读取配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    baseurl = config.get('HTTP', 'baseurl')
    return baseurl


def read_interface_config(interfacename):
    #读取配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    baseurl = read_baseurl_config()
    interface = baseurl+config.get('INTERFACE', interfacename)
    return interface


def read_password_config(mobile):
    #读取配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    password = config.get('PASSWORD', mobile)
    return password

