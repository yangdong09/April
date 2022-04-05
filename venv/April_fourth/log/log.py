import logging
import os

logger = logging.getLogger('applog')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)


fileHandler = logging.FileHandler(filename=os.path.realpath(__file__)+"log.log")

formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      ' :%(levelname)s-[日志信息]: %(message)s')

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)


logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

