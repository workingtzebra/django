import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute an SQL query to fetch all data from a specific table
# Replace 'your_table_name' with the actual table name from your database
cursor.execute('SELECT * FROM homepage_contact')

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
