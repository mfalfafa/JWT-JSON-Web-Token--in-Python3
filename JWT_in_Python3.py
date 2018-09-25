import json
import requests

dataFactoriesURL = 'http://192.168.10.151:8080/api/factories'
loginURL='http://192.168.10.151:8080/api/auth/login'
headers = {'content-type': 'application/json'}
payload = {
    'email': 'admin@yahoo.com',
    'password': '123qwe'
    }

# Get Token (JSON Web Token) using Post method
r = requests.post(loginURL,
                  data=json.dumps(payload),
                  headers=headers)
token=r.json()['access_token']
token_type=r.json()['token_type']

print (token)
print (token_type)

# Get Data from API using Get method and token
hed = {'Authorization':token_type+' '+token}
PARAMS_GET = {'id' : '2'}
r = requests.get(url = dataFactoriesURL, params = PARAMS_GET, headers=hed)
print(r.json())
