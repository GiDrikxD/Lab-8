import logging

logger = logging.getLogger('coinbaseloader')
logger.setLevel(logging.DEBUG)  # Встановлення рівня логування

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('coinbaseloader.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
