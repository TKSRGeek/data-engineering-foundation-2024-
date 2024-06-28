from database import DatabaseConnector
from data_retriever import DataRetriever
from data_transformer import DataTransformer
from data_loader import DataLoader


def main():
    connector = DatabaseConnector()
    connector.connect()
    print("-------application running-------------")

    try:
        retriever = DataRetriever(connector)
        print("-------retriever initiated-------------")
        data = retriever.get_film_data()
        print("-------data fetched-------------")
        print(data)

        transformer = DataTransformer()
        transformed_data = transformer.transform(data)

        loader = DataLoader(connector)
        loader.create_modified_table()
        loader.load_data(transformed_data)
    finally:
        print("-------closing connection-------------")
        connector.disconnect()


if __name__ == '__main__':
    main()
