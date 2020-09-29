import splunklib.client as client
import splunklib.results as results
import sys
import json
from username_inserter import Add_users
from datetime import datetime, timedelta

# time range we want to use for the search (last 24 hours by default)
number_of_hours = 24

# Splunk server information 
splunk_host = 'splunk_IP_Address'
splunk_port = '8089'
splunk_user = 'splunk_user_name'
splunk_password = 'splunk_user_password'

# Scrutinizer Server Information 

db_name = 'plixer'
scrutinizer_user = 'scrutremote'
scrutinizer_password = 'scrutinizer_Admin_Password'
scrutinizer_host = 'scrutinizer_IP_Address'

# set up DB connector 

scrut_inserter = Add_users(db_name,scrutinizer_user,scrutinizer_password,scrutinizer_host)


# splunk query - you will need to build this witht he end user, it's going to vary depending on what they have for indexes / etc. You want to get the UserName and the IP back do you can parse it below. 
searchquery_oneshot = "search use a search that returnes users and ips | dedup host "




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

#this will convert the splunk results to a dictionary. You will likely want to look at what comes back so you can pass the correct info into the inserter. 
for item in reader:
    item = dict(item)
    scrut_inserter.insert_users('IP Address Goes here','User Name Here','Domain','splunk')


##closes the connection
scrut_inserter.close_connection()