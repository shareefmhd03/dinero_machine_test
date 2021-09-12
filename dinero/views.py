import json
import requests
from django.shortcuts import render
from decouple import config

def home(request):
    # key can be obtained from marketstack website
    # https://marketstack.com/documentation
    params = {'access_key': config('SECRET_KEY')}

    # API call
    etf_current    = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/latest',params).json()['close']
    etf_previous   = requests.get('http://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/2021-03-10T00:00:00+0000',params).json()['close']
    nifty_current  = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/latest',params).json()['close']
    nifty_previous = requests.get('http://api.marketstack.com/v1/tickers/NN50.INDX/eod/2021-03-10T00:00:00+0000', params).json()['close']
    
    # Tracking Error calculation
    tracking_err = "Tracking Error: {0:.2f}%".format(abs(((etf_current/etf_previous-1)-(nifty_current/nifty_previous-1))*100))


    # Testing webhooks--------------------------------------->
    # data = {
    #     'tracking_error':tracking_err
    # }

    # webhook_url = 'https://webhook.site/7172fecd-e1a6-4a5c-b3f1-e5001120b425'
    # requests.post(webhook_url,data = json.dumps(data), headers={'Content-Type':'application/json'})

    return render (request,'home.html',{'data':tracking_err})
