import pandas as pd
import mysql.connector

df = pd.read_csv("data/cleaned_sales.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ecommerce_db"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales 
        (id,title,price,category,rating_rate,rating_count,quantity_sold,revenue)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
print("Data Loaded")