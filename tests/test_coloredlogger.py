import cleanlog


def show_output(logger):
    logger.critical('critical')
    logger.error('error')
    logger.warning('warning')
    logger.info('info')
    logger.debug('debug')


def test_coloredlogger_with_no_name():
    logger = cleanlog.ColoredLogger()  # Its name should be 'root'.
    show_output(logger)


def test_coloredlogger_with_name():
    logger = cleanlog.ColoredLogger('TEST')
    show_output(logger)


def test_coloredlogger_set_level_debug():
    logger = cleanlog.ColoredLogger('TEST')
    logger.setLevel(cleanlog.DEBUG)
    show_output(logger)


def test_coloredlogger_set_level_info():
    logger = cleanlog.ColoredLogger('TEST')
    logger.setLevel(cleanlog.INFO)
    show_output(logger)


def test_coloredlogger_set_level_warning():
    logger = cleanlog.ColoredLogger('TEST')
    logger.setLevel(cleanlog.WARN)
    show_output(logger)


def test_coloredlogger_set_level_error():
    logger = cleanlog.ColoredLogger('TEST')
    logger.setLevel(cleanlog.ERROR)
    show_output(logger)


def test_coloredlogger_set_level_critical():
    logger = cleanlog.ColoredLogger('TEST')
    logger.setLevel(cleanlog.CRITICAL)
    show_output(logger)


if __name__ == '__main__':
    # test_coloredlogger_with_no_name()
    # test_coloredlogger_with_name()
    # test_coloredlogger_set_level_debug()
    # test_coloredlogger_set_level_info()
    # test_coloredlogger_set_level_warning()
    # test_coloredlogger_set_level_error()
    test_coloredlogger_set_level_critical()
