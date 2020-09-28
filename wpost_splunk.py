import splunklib.client as client
import splunklib.results as results
import sys
import json

from datetime import datetime, timedelta

# time range we want to use for the search (last 24 hours by default)
number_of_hours = 24

# creates the data in a way the Splunk API expects it. 
earliest_time = str((datetime.utcnow() - timedelta(hours = number_of_hours)).strftime('%Y-%m-%dT%H:%M:%S'))


# creates connection to Splunk 

service = client.connect(host='10.1.4.58',port='8089', username='briandav',  password='Belathedog')


# time frame arguments 

kwargs_oneshot = {"earliest_time": earliest_time,
                  "latest_time": 'now',}


# search we are going to use 

searchquery_oneshot = "search 10.1.5.1"

oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)


# manipulate results here. 
reader = results.ResultsReader(oneshotsearch_results)

for item in reader:
    item = dict(item)
    print(item['_raw'])
    print('host ='+ item['host'] +'|' ' source=' + item['source'])