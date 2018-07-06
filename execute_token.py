import requests

IP = 'http://192.168.1.251:5001/'
API = 'crm/update_agreement/'
headers = {'Authorization': 'Token {}'.format('f7f7153ebf26ef8265694f9602743c97f646bb00')}
url_completed = IP + API
result = requests.post(url_completed, data={}, headers=headers)
print("Done")
