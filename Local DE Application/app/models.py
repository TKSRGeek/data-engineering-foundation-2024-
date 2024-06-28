from app.db import Database

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        db = Database()
        db.connect()
        query = f"INSERT INTO users (username, email) VALUES ('{self.username}', '{self.email}');"
        db.execute_query(query)
        db.disconnect()

    @staticmethod
    def fetch_all():
        db = Database()
        db.connect()
        query = "SELECT * FROM users;"
        cursor = db.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        db.disconnect()
        return rows
