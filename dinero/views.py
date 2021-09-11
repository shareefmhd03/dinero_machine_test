import requests
import numpy as np
from django.shortcuts import render
from decouple import config

def home(request):
    params = {'access_key': config('SECRET_KEY')}

    etf_current    = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/latest',params).json()['close']
    etf_previous   = requests.get('http://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/2021-03-10T00:00:00+0000',params).json()['close']
    nifty_current  = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/latest',params).json()['close']
    nifty_previous = requests.get('http://api.marketstack.com/v1/tickers/NN50.INDX/eod/2021-03-10T00:00:00+0000', params).json()['close']

    tracking_err = "Tracking Error: {0:.2f}%".format(abs(((etf_current/etf_previous-1)-(nifty_current/nifty_previous-1))*100))
    return render (request,'home.html',{'data':tracking_err})
