import logging

from cleanlog.formatter import ColoredFormatter


def test_colored_formatter():
    logger = logging.getLogger('colored_formatter_test')
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ColoredFormatter())
    logger.addHandler(stream_handler)

    logger.error('Hello, world!')
    logger.fatal('Hello, world!')
    logger.info('Hello, world!')
    logger.debug('Hello, world!')
