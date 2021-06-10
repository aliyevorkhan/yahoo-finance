import requests

r = requests.get('http://0.0.0.0:8000/get_stock/DOCU')

print(r.json())

