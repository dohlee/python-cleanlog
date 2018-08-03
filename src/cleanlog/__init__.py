__version__ = '0.1.3'

import logging
import cleanlog.formatter as cf

# Integer representation of level names.
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def ColoredLogger(name=None, *args, **kwargs):
    """
    """
    logger = logging.getLogger(name)
    if not len(logger.handlers):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(cf.ColoredFormatter())
        logger.addHandler(stream_handler)

    return logger


# Wrap logging.getLogger just for convenience.
getLogger = logging.getLogger
