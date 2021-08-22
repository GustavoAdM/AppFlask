import requests

resposta = requests.get('http://127.0.0.1:5000/')

print(resposta.status_code)