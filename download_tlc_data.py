from dateutil.rrule import rrule, MONTHLY
from datetime import datetime
import pandas as pd
import os
import csv
import requests

def months(start_month, start_year, end_month, end_year):
    start = datetime(start_year, start_month, 1)
    end = datetime(end_year, end_month, 1)
    return [(d.month, d.year) for d in rrule(MONTHLY, dtstart=start, until=end)]

months_to_download = months(1, 2019, 7, 2021)

import os
if not os.path.exists("data"):
    os.makedirs("data")

for month_tuple in months_to_download:
	month, year = month_tuple
	month = str(month).rjust(2, '0')
	print(month)
	print(year)
	filename = f"yellow_tripdata_{year}-{month}.csv"
	download_link = f"https://s3.amazonaws.com/nyc-tlc/trip+data/{filename}"
	response = requests.get(download_link)   
	with open(f"data/{filename}", 'w') as f:
	    writer = csv.writer(f)
	    for line in response.iter_lines():
	        writer.writerow(line.decode('utf-8').split(','))
	# df = pd.read_csv(download_link)  
	# df.to_csv(f"data/{filename}")