import time, requests
import pandas as pd
import re
from io import StringIO
from database import *
from config import Config

config_data = Config()
# companies=['PD','ZUO','PINS','ZM','PVTL','DOCU','CLDR','RUN']

def scrap_data(company):
    res = requests.get('https://finance.yahoo.com/quote/' + company + '/history')
    
    url_price = 'https://query1.finance.yahoo.com/v7/finance/download/' \
                '{0}?period1=0&period2={1}&interval=1d&filter=history' \
                '&frequency=1d&includeAdjustedClose=true'.format(company, int(time.time()))
    response = requests.get(url_price)

    return pd.read_csv(StringIO(response.text))

if __name__ == '__main__':
    # database = 'stocks.db'

    # create a database connection
    conn = create_connection(config_data.DB_NAME)

    # create tables
    if conn is not None:
        # create projects tablea
        for c in config_data.COMPANIES:
            create_table(conn, create_table_query%(c))
    else:
        print("Error! cannot create the database connection.")

    for c in config_data.COMPANIES:
        print('Getting data for {0}..'.format(c))
        try:
            data = scrap_data(c)
            df = pd.DataFrame(data, columns= ['Date','Open','High', 'Low', 'Close', 'Adj_Close', 'Volume'])  
            # Insert DataFrame to Table
            for row in df.itertuples():
                insert_data(conn, (row.Date, row.Open, row.High, row.Low, row.Close, row.Adj_Close, row.Volume), c)
            print('Data fetched!')
        except Exception as e:
            print('Error occurred getting the data for {0}'.format(c))
            print(e)
        print('Completed!')
    
    #service will start to serving data
