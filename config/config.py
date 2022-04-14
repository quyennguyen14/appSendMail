from configparser import ConfigParser

class config():
    def str2bool(self, v):
        if v.lower() in ("true", "1"):
            return True
        elif v.lower() in ("false", "0"):
            return None
        else:
            return v.lower()

    def config_mssql_db(self, filename='config/config.ini', section='mssql'):
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        data = parser[section]
        return data

    def emailConfig(self, filename='config/config.ini', section='emailconfig'):
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        data = parser[section]
        return data
