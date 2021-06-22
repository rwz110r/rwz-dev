import logging
def log():
    logging.basicConfig(level=logging.INFO,format='%(name)s-%(asctime)s-%(levelname)s-%(message)s')
    logger = logging.getLogger('REAPI')
    return logger
logger = log()
