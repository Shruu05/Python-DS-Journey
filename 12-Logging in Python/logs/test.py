import logger
import logging
def add(a,b):
    logging.debug('Add is taking place')
    return a + b

logging.debug('The add func is called')
add(10,15)