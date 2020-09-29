import splunklib.client as client
import splunklib.results as results
import sys
import json
from username_inserter import Add_users
from datetime import datetime, timedelta

# time range we want to use for the search (last 24 hours by default)
number_of_hours = 24

# Splunk server information 
splunk_host = '10.1.4.58'
splunk_port = '8089'
splunk_user = 'admin'
splunk_password = 'memorizeM3'

# Scrutinizer Server Information 

db_name = 'plixer'
scrutinizer_user = 'scrutremote'
scrutinizer_password = 'admin'
scrutinizer_host = '10.30.16.26'

# set up DB connector 

scrut_inserter = Add_users(db_name,scrutinizer_user,scrutinizer_password,scrutinizer_host)


# splunk query 
searchquery_oneshot = "search 10.1.4.104 | dedup host "




# creates the data in a way the Splunk API expects it. 
earliest_time = str((datetime.utcnow() - timedelta(hours = number_of_hours)).strftime('%Y-%m-%dT%H:%M:%S'))


# creates connection to Splunk 

service = client.connect(host=splunk_host,port=splunk_port, username=splunk_user,  password=splunk_password)


# time frame arguments 

kwargs_oneshot = {"earliest_time": earliest_time,
                  "latest_time": 'now',}



oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)


# manipulate results here. 
reader = results.ResultsReader(oneshotsearch_results)

# ip, user_name, domain, data_source are the params the inserter takes. 
for item in reader:
    item = dict(item)
    scrut_inserter.insert_users(item['host'],'briantestnew','plxr','splunk')



scrut_inserter.close_connection()