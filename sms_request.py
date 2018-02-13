import requests

# url = "http://101.132.74.234:11246/sms"
url = "http://101.132.74.234:8768/sms"

querystring = {"phone":"15251707112"}

headers = {
    'hospital': "999",
    'authorization': "Basic c21zOnNtc3NlY3JldA==",
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)