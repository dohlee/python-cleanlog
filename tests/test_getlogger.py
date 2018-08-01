import cleanlog

logger = cleanlog.ColoredLogger('test_getlogger')


def test_getlogger():
    logger2 = cleanlog.getLogger('test_getlogger')
    logger2.setLevel(cleanlog.DEBUG)
    logger2.debug('TEST')
