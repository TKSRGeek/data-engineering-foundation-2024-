class DataRetriever:
    def __init__(self, connector):
        self.connector = connector

    def get_film_data(self):
        query = open('queries/dml/fetch_film_data.sql', 'r').read()
        return self.connector.execute_query(query)
