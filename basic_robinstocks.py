import robin_stocks as r
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()
RH_USER = os.getenv("RH_USER")
RH_PASS = os.getenv("RH_PASS")

r.login(RH_USER, RH_PASS)

my_stocks = r.build_holdings()

df = pd.DataFrame(my_stocks)
df = df.T
df['ticker'] = df.index
df = df.reset_index(drop=True)

print(df.head())

tsla_data = r.stocks.get_stock_historicals("TSLA",
                                           span='week',
                                           bounds='regular')
tsla = pd.DataFrame(tsla_data)

column_list = ['close_price', 'high_price', 'low_price', 'open_price']
for i in column_list:
    tsla[i] = tsla[i].astype(float)

tsla['close_price'].plot(legend=True, figsize=(12, 5))
