import logging

from termcolor import colored

# Level name constants and converters.
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_level_to_name = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}
_name_to_level = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}

_level_to_color = {
    CRITICAL: 'red',
    ERROR: 'red',
    WARNING: 'yellow',
    INFO: 'cyan',
    DEBUG: 'green',
    NOTSET: 'white',
}

class BasicFormatter(logging.Formatter):
    """
    """
    default_format = '[%(levelname)-.1s %(name)s %(asctime)s] %(message)s'

    def __init__(self, fmt=default_format, datefmt=None, style='%'):
        super(BasicFormatter, self).__init__(fmt=fmt, datefmt=datefmt, style=style)


class ColoredFormatter(logging.Formatter):
    """
    Formatter class for `ColoredLogger`.
    """
    # default_format = '[%(levelname)-.1s %(name)s %(asctime)s] %(message)s'
    default_format = '[%(asctime)s %(name)s] [%(levelname)s] %(message)s'

    def __init__(self, fmt=default_format, datefmt=None, style='%'):
        super(ColoredFormatter, self).__init__(fmt=fmt, datefmt=datefmt, style=style)

    def _is_colored(self, message):
        return message.startswith('\x1b[')

    def formatMessage(self, record):
        record.message = colored(record.message, 'white') if not self._is_colored(record.message) else record.message
        return colored(self._style.format(record), _level_to_color[record.levelno])
