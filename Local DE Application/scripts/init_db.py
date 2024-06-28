import psycopg2
from config.config import DB_CONFIG

def init_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        with open('config/queries.sql', 'r') as f:
            queries = f.read()
            cursor.execute(queries)

        conn.commit()
        print("Database schema initialized.")
    except psycopg2.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    init_db()
