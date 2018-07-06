import requests

headers = {'Authorization': 'Token {}'.format('f7f7153ebf26ef8265694f9602743c97f646bb00')}
url_completed = 'http://192.168.1.251:5001/crm/update_agreement/'
result = requests.post(url_completed, data={}, headers=headers)
print("Done")
