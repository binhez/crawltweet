import configparser

def config_sql():
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    server = config['SQL_CONNECTION']['SERVER']
    gvi_database = config['SQL_CONNECTION']['DATABASE']
    username = config['SQL_CONNECTION']['USERNAME']
    password = config['SQL_CONNECTION']['PASSWORD']
    driver = config['SQL_CONNECTION']['DRIVER']

    return server, gvi_database, username, password, driver
