import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common data','base_url')

    @staticmethod
    def getUsername():
        return config.get('common data','Username')

    @staticmethod
    def getPassword():
        return config.get('common data','Password')
