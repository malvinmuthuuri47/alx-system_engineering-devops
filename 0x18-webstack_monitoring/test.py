#!/usr/bin/python3
"""
This script gets the dashbaord id from the Datadog API
"""
import requests

api_key = 'my_api_key'
app_key = 'my_application_key'

url = 'https://api.datadoghq.com/api/v1/dashboard/'

headers = {
        'Content-Type': 'application/json',
        'DD-API-KEY': api_key,
        'DD-APPLICATION-KEY': app_key
}

# This specifies the host the request is being made for
test_param = {'filter': 'host:167989-web-01'}

# make call to the API
response = requests.get(url, headers=headers, params=test_param)

if response.status_code == 200:
    # turn the data to json
    data = response.json()
    # get the dashboard id from the json response
    dashboard_id = data.get('dashboards', [{}])[0].get('id')
    print(dashboard_id)
else:
    print(f"Error retreiving hosts. Status code: {response.status_code}")
