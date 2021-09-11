# dinero_machine_test
I have used Market stack API to get the stock data and by using that data I calculated the Tracking Error

Here is the link to the Marketstack API: https://marketstack.com/documentation

Example. KOTAK NIFTY ETF and Nifty 50 Index
For KOTAK NIFTY ETF, EOD data for 2021-06-07 is 130
For Nifty 50 Index, EOD data for 2021-06-07 is 15,100
For KOTAK NIFTY ETF, EOD data for 2020-06-07 is 100 For Nifty 50 Index, EOD data for 2021-06-07 is 15,000

The 1year percentage change for Kotak Nifty ETF is 30% (130/100-1) The 1year percentage change for Nifty 50 is 0.6% (15100/15000-1) The tracking error is 29.4% (absolute value of (30%-0.6%))
