import requests
def underlying(symbol,api_key):
	url = str(
		'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+
		symbol+'&outputsize=full&apikey='+
		api_key)
	r = requests.get(url)
	spots = r.json()['Time Series (Daily)']
	spots_dict = {}
	for date,item in spots.items():
		spots_dict[date] = item['4. close']
	return spots_dict
