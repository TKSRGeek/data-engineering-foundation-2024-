import psycopg2
import yaml

class DatabaseConnector:
    def __init__(self, config_path='config/config.yaml'):
        self.config = self.load_config(config_path)
        self.connection = None

    def load_config(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.config['database']['host'],
            port=self.config['database']['port'],
            user=self.config['database']['user'],
            password=self.config['database']['password'],
            dbname=self.config['database']['dbname']
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=()):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_non_query(self, query, params=()):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print(f"Executed non-query: {query} with params: {params}")
        except Exception as e:
            self.connection.rollback()
            print(f"Error executing non-query: {query} with params: {params}")
            print(f"Exception: {e}")
            raise


