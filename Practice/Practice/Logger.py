import logging
logger = logging.getLogger(__name__)
logger.propagate = False #Does not lock anything to the base logger.
logger.info('hello from logger')