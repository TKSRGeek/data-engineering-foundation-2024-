class DataLoader:
    def __init__(self, connector):
        self.connector = connector

    def create_modified_table(self):
        query = open('queries/ddl/create_modified_table.sql', 'r').read()
        self.connector.execute_non_query(query)

    def load_data(self, data):
        query = open('queries/dml/insert_modified_data.sql', 'r').read()
        for row in data:
            self.connector.execute_non_query(query, row)
