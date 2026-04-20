import requests
import pandas as pd

url = "https://fakestoreapi.com/products"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.to_json("data/raw_products.json", orient="records", indent=4)

print("Raw data saved")