import requests

uri = 'https://feriadosbancarios.febraban.org.br/feriados.asp'

response = requests.get(uri)

print(response.content)

