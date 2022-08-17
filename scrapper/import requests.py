import requests
import json

# set up the request parameters
params = {
'api_key': 'CB3619DBE0524CCB902451AC72E49822',
  'q': 'crypto ownership usa figures'
}

# make the http GET request to Scale SERP
api_result = requests.get('https://api.scaleserp.com/search', params)

# print the JSON response from Scale SERP
print(json.dumps(api_result.json(), indent = 4))