import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def info(fn):

    def wrapper(*args, **kwargs):
        logger.info("Entering {:s}...".format(fn.__name__))
        logger.info('Input Value: %s %s', fn.__name__, args)
        result = fn(*args, **kwargs)
        logger.info('Output Value: %s', result)
        logger.info("Finished {:s}.".format(fn.__name__))
        return result

    return wrapper
