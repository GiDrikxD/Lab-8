import cbpro
import pandas as pd
from datetime import datetime
from .logging_config import logger

def get_historic_rates(product, granularity, start, end):
    logger.info(f'Отримання історичних даних для продукту {product} з {start} по {end} з гранулярністю {granularity}')
    public_client = cbpro.PublicClient()
    try:
        data = public_client.get_product_historic_rates(product, granularity=granularity, start=start.isoformat(), end=end.isoformat())
        logger.info(f'Успішно отримано дані для продукту {product}')
        return data
    except Exception as e:
        logger.error(f'Помилка при отриманні даних для продукту {product}: {e}')
        return None

def create_dataframe(historical_data):
    logger.info('Створення DataFrame з історичних даних')
    try:
        df = pd.DataFrame(historical_data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        logger.info('Успішно створено DataFrame')
        return df
    except Exception as e:
        logger.error(f'Помилка при створенні DataFrame: {e}')
        return None
