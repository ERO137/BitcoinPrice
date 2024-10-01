import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

# Check json file recept
print(json.dumps(response.json(), indent = 4))


