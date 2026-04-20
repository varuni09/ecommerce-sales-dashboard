import pandas as pd

df = pd.read_json("data/raw_products.json")

# Clean columns
df = df[['id', 'title', 'price', 'category', 'rating']]

# Extract rating count
df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
df['rating_count'] = df['rating'].apply(lambda x: x['count'])

# Remove old column
df.drop('rating', axis=1, inplace=True)

# Add fake sales quantity
df['quantity_sold'] = df['rating_count'] * 2

# Revenue column
df['revenue'] = df['price'] * df['quantity_sold']

df.to_csv("data/cleaned_sales.csv", index=False)

print("Cleaned data saved")