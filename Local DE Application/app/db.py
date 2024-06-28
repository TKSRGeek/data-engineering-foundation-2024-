import psycopg2
from config.config import DB_CONFIG

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**DB_CONFIG)
            print("Connected to PostgreSQL!")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from PostgreSQL.")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
            cursor.close()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
