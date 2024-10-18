import logging
#import logging.config

#logging.config.fileConfig('logging.ini')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H: %M: %S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#import Logger

#logger = logging.getLogger(__name__)

#Create handler
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('file.log')

#level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)

#formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)

#logger.addHandler(stream_h)
#logger.addHandler(file_h)

#logger.warning('this is a warning')
#logger.error('this is an error')


#For importing logging.config

logger = logging.getLogger('simpleExample')
logger.debug('this is a dubug message')

#This section of does not work. Can try dictConfig later on though to see if that still works. There should be an online python documentation on it.

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

import traceback

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error('The error is %s', traceback.format_exc())


from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over 2KB, and keep backup logs app. log.1, app. log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) #Give a file name, max amount of bytes that can be used until it rolls over to another log file, and backup counts
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')


from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over 2KB, and keep backup logs app. log.1, app. log.2, etc.
# s for seconds, m for minutes, h for hours, d for days, midnight, w0-6 (Monday to Sunday)
handler = TimedRotatingFileHandler('Timed_logging', when = 's', interval = 1, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Goodbye, world.')
    time.sleep(1)