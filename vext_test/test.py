import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.getenv("API_KEY_VEXT")
my_query= "what is machine learning"
print(api_key)

headers = {
    'Content-Type':'application/json',
    'Apikey':f'Api-Key {api_key}',
}

data = {
    "playload": my_query
}

url = "https://payload.vextapp.com/hook/<your-endpoint-id>/catch/$(channel_token)"

response = requests.post(url, json=data, headers=headers)

print(response.text)




