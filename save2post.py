import pandas as pd
import psycopg2
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris(as_frame=True)
df = iris.frame  # Pandas DataFrame

# Connect to Postgres (service container)
conn = psycopg2.connect(
    host="postgres",
    database="ab_db",
    user="ab",
    password="ab_post",
    port=5432
)

cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS iris (
        sepal_length FLOAT,
        sepal_width FLOAT,
        petal_length FLOAT,
        petal_width FLOAT,
        target INT
    )
""")

# Insert rows
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, target)
        VALUES (%s, %s, %s, %s, %s)
    """, (row['sepal length (cm)'], row['sepal width (cm)'],
          row['petal length (cm)'], row['petal width (cm)'], row['target']))

conn.commit()
cur.close()
conn.close()

print("Iris dataset saved to Postgres.")