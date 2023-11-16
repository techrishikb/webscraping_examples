##Amazon merchant data

##------------ Get product details by search term---------------------
import os
import pandas as pd
from pandas import json_normalize 
import requests
import json
from dotenv import load_dotenv

load_dotenv()



url = "https://amazon-merchant-data.p.rapidapi.com/search-products"

querystring = {"term":"Latest Sony DSLR Cameras","country":"in"}

headers = {
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": os.getenv("X-RapidAPI-Host")
}

response = requests.get(url, headers=headers, params=querystring)



#print(response.json())

# Store JSON data in API_Data
API_Data = response.json()
 
print(json.dumps(API_Data, indent=4, sort_keys=True))

#------------------Get user reviews using ASIN as input--------------------
import requests
import json

url = "https://amazon-merchant-data.p.rapidapi.com/get-reviews"

querystring = {"asin":"B081JS1Q2Y","country":"in","page":"1"}

headers = {
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": os.getenv("X-RapidAPI-Host")
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

# Store JSON data in API_Data
API_Reviews = response.json()
 
print(json.dumps(API_Reviews, indent=4, sort_keys=True))