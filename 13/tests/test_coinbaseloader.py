import pytest
from datetime import datetime, timedelta
from coinbaseloader.loader import get_historic_rates, create_dataframe

@pytest.mark.parametrize("product, granularity, start, end", [
    ('BTC-USD', 3600, datetime.now() - timedelta(days=1), datetime.now()),
    ('ETH-USD', 21600, datetime.now() - timedelta(days=30), datetime.now()),
    ('LTC-USD', 86400, datetime.now() - timedelta(days=365), datetime.now())
])
def test_get_historic_rates(product, granularity, start, end):
    data = get_historic_rates(product, granularity, start, end)
    assert data is not None
    assert isinstance(data, list)

@pytest.mark.parametrize("historical_data", [
    ([
        [1625097600, 33213.68, 33612.63, 33213.68, 33407.69, 14.53901897],
        [1625094000, 33213.68, 33612.63, 33213.68, 33407.69, 14.53901897]
    ]),
    ([
        [1625097600, 2000.68, 2100.63, 2000.68, 2050.69, 10.53901897],
        [1625094000, 1900.68, 2200.63, 1900.68, 2100.69, 12.53901897]
    ])
])
def test_create_dataframe(historical_data):
    df = create_dataframe(historical_data)
    assert df is not None
    assert not df.empty
    assert 'close' in df.columns
    assert 'volume' in df.columns

def test_create_dataframe_empty():
    historical_data = []
    df = create_dataframe(historical_data)
    assert df is None
