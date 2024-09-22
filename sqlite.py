import pandas as pd
import sqlite3

# Step 1: Create a connection to SQLite database
conn = sqlite3.connect('test_database.db')

# Step 2: Create a Pandas DataFrame

df = pd.read_csv ('https://healthdata.gov/resource/xs6e-ics5.csv')

print(df)

# Step 4: Query the table to verify the data
query = 'SELECT * FROM users'
result_df = pd.read_sql(query, conn)

# Step 5: Display the result
print(result_df)

# Close the connection
conn.close()
