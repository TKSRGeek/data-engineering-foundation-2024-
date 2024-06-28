
import psycopg2

# PostgreSQL database connection parameters
db_host = 'localhost'
db_name = 'postgres'
db_port = '5433'
db_user = 'postgres'
db_password = '12345'

# Establish a connection to the database
conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)

# Create a cursor object using the connection
cursor = conn.cursor()

# Define your SELECT query
query = "SELECT * FROM film;"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()

