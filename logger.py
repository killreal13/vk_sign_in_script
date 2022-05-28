import logging


logging.basicConfig(filename='logs.txt', filemode='w')
info_logger = logging.getLogger('info_logger')
logger_handler = logging.FileHandler('logs.txt')
logger_handler.setLevel(logging.INFO)
info_logger.addHandler(logger_handler)