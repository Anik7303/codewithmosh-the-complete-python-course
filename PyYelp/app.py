import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": f"Bearer {config.API_KEY}"
}

params = {
    "location": "NYC",
    "term": "resturants"
}

response = requests.get(url, headers=headers, params=params)

businesses = response.json()['businesses']
print(businesses)

# names of businesses with atleast 4.5 rating
names = [business['name']
         for business in businesses if business['rating'] >= 4.5]
print(names)
