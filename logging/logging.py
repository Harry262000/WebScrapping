import logging
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='activity.log')

# Log the start time of the work session
logging.info('Work session started: {}'.format(datetime.datetime.now()))

# Your code goes here...

# Log important events or milestones
logging.info('Performed task A')

# More code...

# Log the end time of the work session
logging.info('Work session ended: {}'.format(datetime.datetime.now()))
