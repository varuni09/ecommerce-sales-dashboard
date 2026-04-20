import pandas as pd

df = pd.read_csv("data/cleaned_sales.csv")

print("Total Revenue:", df['revenue'].sum())

print("Top Category:")
print(df.groupby('category')['revenue'].sum().sort_values(ascending=False))

print("Best Product:")
print(df[['title','revenue']].sort_values(by='revenue', ascending=False).head(5))