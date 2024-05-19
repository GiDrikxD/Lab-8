import logging

# Налаштування логера
logger = logging.getLogger('coinbaseloader')
logger.setLevel(logging.DEBUG)  # Встановлення рівня логування

# Створення власного форматера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Створення хендлера, що пише у файл
file_handler = logging.FileHandler('coinbaseloader.log')
file_handler.setFormatter(formatter)

# Додавання хендлера до логера
logger.addHandler(file_handler)
