# cleanlog

Python package for nice colored logs.

## Installation

```shell
pip install cleanlog
```

## At a glance

```python
# log.py
import cleanlog

logger = cleanlog.ColoredLogger('mylogger')
# Note that since cleanlog just wraps built-in logging module,
# this is equivalent to logger.setLevel(logging.DEBUG).
logger.setLevel(cleanlog.DEBUG)

logger.critical('A critical message.')
logger.error('An error message.')
logger.warning('A warning message.')
logger.info('An info message.')
logger.debug('A debug message.')
```

![log.py](https://cdn.rawgit.com/dohlee/python-cleanlog/develop/img/glance.svg)

### TODO

- [x] Implement cleanlog.BasicLogger.
