import requests
import urllib.parse
from Rugby.settings import DOMAIN, PORT, API_KEY
import os

headers = {'Authorization': API_KEY}


DOMAIN = "localhost" 
PORT = "8000"


url = urllib.parse.urljoin(f"http://{DOMAIN}:{PORT}",'api/formation/')
data = requests.get(url, headers=headers)
print(url)
data = data.json()

### Retituer le résultat..
print(data)
