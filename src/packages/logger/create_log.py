import logging
from os import getenv

ENV = getenv('PY_ENV', 'development')


def init(module):
    logger = logging.getLogger(module)

    if ENV == "development":
        logger.setLevel(logging.DEBUG)
    elif ENV == "test":
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - level: %(levelname)s - filename: %(filename)s - mod: %(module)s - func: %(funcName)s - line: %(lineno)d  - msg: %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
