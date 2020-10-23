import logging

logging.basicConfig(level=0,filename='python-log.log', filemode='w', format='%(levelname)s - %(message)s')

logging.debug('Attempted to divide by zero')
logging.warning('User left field blank in the form')
logging.error("Couldn't find specified file")

# > DEBUG - Attempted to divide by zero
# > WARNING - User left field blank in the form
# > ERROR - Couldn't find specified file


logging.basicConfig(level=0,filename='python-log.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Something happened')
logging.info('Something else happened, and it was bad')

# > 2020-06-21 10:55:40,278 - INFO - Something happened
# > 2020-06-21 10:55:40,278 - INFO - Something else happened, and it was bad

