# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:23:09 2016

@author: Archon
"""

import pandas as pd
import numpy as np
from matplotlib import pylab

def get_poloinex_data(s, a, b, c):
    
    import requests
    from pandas import DataFrame
    from io import StringIO
    
    url = 'https://poloniex.com/public?command=returnChartData'
    
    url += '&currencyPair=' + s #USDT a dollár
    url += '&start=' + a
    url += '&end=' + b
    url += '&period=' + c
  
    csv = requests.get(url)
    
    if csv.ok:
        return DataFrame.from_csv(StringIO(csv.text), sep=',') #Separátor itt!
    else:
        return None
        
params = {
    # specify stock
    "s": 'USDT_ETH',   # BTC_ETH, USDT_ETH stb
    
    # query data from
    'a': '1422230400',     # unix date stamp, 2015 jan 26 : 1422230400

    # query until
    'b': '1492905600',     # unix dates tamp, 2016 sep 23 : 1492905600
    
    # frequency
    'c': '14400'      # unix time stamp (1970.jan.01. től eltelt másodpercek száma, itt másodperc ablakot kér), 4 óránlént itt (240 perc)
}
    
    
poloinex_df = get_poloinex_data(**params)

TransposedData = poloinex_df.transpose