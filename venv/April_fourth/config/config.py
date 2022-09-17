import configparser
import os
from April_fourth.log.log import logger


class Config:
    __filepath = os.path.join \
        (os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'config.ini')

    # def __init__(self):
    #     self.__configData = self.__get_num()


    def get_num(self):
        config = configparser.ConfigParser()
        config.read(Config.__filepath)
        token = config.get('Headers','Authorization')

        return token

