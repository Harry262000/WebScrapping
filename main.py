import logging
import datetime

# Set up logging
logging.basicConfig(filename='logging/setup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Log the start time of the work session
    logging.info('Work session started: {}'.format(datetime.datetime.now()))
    
    # Your code goes here...
    logging.info("Welcome to our custom logging")
    
    # More code...
    
    # Log the end time of the work session
    logging.info('Work session ended: {}'.format(datetime.datetime.now()))

if __name__ == "__main__":
    main()
