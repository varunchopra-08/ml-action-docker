import pandas as pd
import psycopg2

# Connect to Postgres
conn = psycopg2.connect(
    host="postgres",
    database="ab_db",
    user="ab",
    password="ab_post",
    port=5432
)

# Load into pandas
df = pd.read_sql("SELECT * FROM iris", conn)
print("Retrieved Iris dataset from Postgres:")
print(df.head())

conn.close() 