import requests

r = requests.post('http://127.0.0.1:8000/get_stock/DOCU')

print(r.json())

