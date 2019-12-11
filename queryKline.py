#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
from datetime import datetime, date, timedelta
from binance.client import Client

#open public key
client = Client("", "")
Ticker = 'BTCUSDT'

#for duration
StartTime = ((date.today()-timedelta(1)).strftime("%d %b %Y"))
EndTime = ((date.today()-timedelta(-1)).strftime("%d %b %Y"))

#download data
klines = client.get_historical_klines(Ticker, Client.KLINE_INTERVAL_15MINUTE, StartTime, EndTime)
 
#transfer data into dataframe
df = pd.read_json(json.dumps(klines))

#remove others data
for i in range(6,12):
     df = df.drop(columns=i)
    
#timestamp to date    
df[0] = pd.to_datetime(df[0],unit= 'ms')

#rename columns
list = ["TimeStamp", "Open", "High", "Low", "Close", "Vol."]
for i in range(6):
    df = df.rename(columns={i: list[i]})
    
print(df)
