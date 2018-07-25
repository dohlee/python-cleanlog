# cleanlog

Python package for nice colored logs.

## Installation

```shell
pip install cleanlog
```

## At a glance

```python
# cleanlog.py
import cleanlog
import logging

logger = cleanlog.ColoredLogger('mylogger')

logger.critical('A critical message.')
logger.error('An error message.')
logger.warning('A warning message.')
logger.info('An info message.')
logger.debug('A debug message.')
```

[TODO] Make SVG animation here.

### TODO

- [ ] Implement cleanlog.BasicLogger.

