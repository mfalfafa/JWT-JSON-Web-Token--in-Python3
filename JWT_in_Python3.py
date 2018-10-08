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
PARAMS_GET = {'id' : '1'}
r = requests.get(url = dataFactoriesURL, params = PARAMS_GET, headers=hed)
# Convert from single quote mark to double quote mark
json_data=json.dumps(r.json()[0])
# Parsing json data
parsed_json=json.loads(json_data)
# Array of parsed json
id_=str(parsed_json['id'])
email=str(parsed_json['email'])
code=str(parsed_json['code'])
name=str(parsed_json['name'])
phone=str(parsed_json['phone'])
# print result
print (json_data)
print ('id = '+ id_)
print ('email = '+ email)
print ('name = '+ name)
