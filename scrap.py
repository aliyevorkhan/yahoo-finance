import time, requests
import pandas as pd
import re
from io import StringIO

companies=['PD','ZUO','PINS','ZM','PVTL','DOCU','CLDR','RUN']

def scrap_data(company):
    res = requests.get('https://finance.yahoo.com/quote/' + company + '/history')
    
    url_price = 'https://query1.finance.yahoo.com/v7/finance/download/' \
                '{0}?period1=0&period2={1}&interval=1d&filter=history' \
                '&frequency=1d&includeAdjustedClose=true'.format(company, int(time.time()))
    response = requests.get(url_price)

    return pd.read_csv(StringIO(response.text))

for c in companies:
    print('Getting data for {0}..'.format(c))
    try:
        print(scrap_data(c))    
        print('Data fetched!')
    except Exception as e:
        print('Error occurred getting the data for {0}'.format(c))
        print(e)
    print('Completed!')