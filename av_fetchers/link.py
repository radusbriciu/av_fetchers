# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:02:17 2024

@author: boomelage
"""
import requests

def link(date,symbol,api_key):
    try:
        options_url = str(
            "https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&"
            f"symbol={symbol}"
            f"&date={date}"
            f"&apikey={api_key}"
            )
        r = requests.get(options_url)
        data = r.json()
        return data['data']
    except Exception as e:
        print(e)
        return None