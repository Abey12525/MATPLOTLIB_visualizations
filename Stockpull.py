#Pulling data from internet

import matplotlib.pyplot as plt 
import numpy as np 
import urllib as ul
import maplotlib.dates as mdates

def graph_data(stock):
	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
	source_code = ul.request.urlopen(stock_price_url).read().decode()
	stock_data = []
	split_source = source_code.split('\n')
	
	
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title('internet_plot')
	plt.legend()
	plt.show()
	
graph_data('TESLA')