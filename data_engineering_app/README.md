# Data Engineering Application

This project is a data engineering application designed to fetch data from a source table in a PostgreSQL database, process it, and insert it into a new table with an additional column. The application is built using Python, with a focus on Object-Oriented Programming (OOP) principles.

## Project Structure


```

## Project Structure

data-engineering-foundation-2024/
│
├── data_engineering_app/
│ ├── config/
│ │ └── config.yaml
│ ├── queries/
│ │ ├── ddl/
│ │ │ └── create_modified_table.sql
│ │ └── dml/
│ │ └── insert_modified_data.sql
│ ├── src/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── data_loader.py
│ │ └── data_retriever.py
│ └── main.py
└── README.md

```

## Configuration

### config/config.yaml

```yaml
database:
  host: "your_host"
  port: 5432
  user: "your_user"
  password: "your_password"
  dbname: "your_database"

```

## Explanation
1. Configuration: The config/config.yaml file contains the database connection details.
2. SQL Queries: SQL scripts for creating the modified table, fetching data, and inserting modified data are stored in the queries folder.
3. Python Modules:
- DatabaseConnector manages the database connection and query execution.
- DataRetriever fetches data using the DatabaseConnector.
- DataTransformer handles any data transformation logic.
- DataLoader creates the modified table and loads the transformed data into it.
4. Main Application: The main.py script orchestrates the workflow by connecting to the database, fetching data, transforming it, and loading it into the modified table.

## Example Relationships and Interactions
1. The DataEngineeringApp creates an instance of DatabaseConnector to manage database connections.
2. The DataRetriever uses the DatabaseConnector instance to fetch raw data.
3. The DataTransformer processes this raw data to apply necessary transformations.
4. The DataStorer then takes the transformed data and uses the DatabaseConnector to insert it into the target table.

## Entities
### 1. database.py
    The DatabaseConnector class handles database connections and execution of SQL queries.This class encapsulates the functionality related to connecting to a database, executing queries, and managing the connection lifecycle. It is responsible for interacting directly with the database.

- Attributes:

1. config: Configuration details loaded from config.yaml.
2. connection: The PostgreSQL database connection.
- Methods:

1. __init__(self, config_path='config/config.yaml'): Initializes the database connector and loads the configuration.
2. load_config(self, config_path): Loads the database configuration from a YAML file.
3. connect(self): Establishes a connection to the PostgreSQL database.
4. execute_non_query(self, query, params=(): Executes SQL queries that do not return results (e.g., INSERT, UPDATE).
5. close(self): Closes the database connection.


### 2. data_retriever.py
    The DataRetriever class handles the fetching of data from the source table.This class relies on the DatabaseConnector to fetch data from the database. It is designed to separate the concern of data retrieval from other operations like transformation and storage.

- Attributes:

1. db_connector: An instance of DatabaseConnector.

- Methods:

1. __init__(self, db_connector): Initializes the data retriever with a database connector.
2. fetch_data(self): Fetches data from the source table using a predefined SQL query.

### 3. data_loader.py
    The DataLoader class handles the insertion of processed data into the destination table.

- Attributes:

1. db_connector: An instance of DatabaseConnector.

- Methods:

1. __init__(self, db_connector): Initializes the data loader with a database connector.
2. load_data(self, data): Inserts processed data into the destination table using a predefined SQL query. 

### 4. main.py
    The main.py file serves as the entry point of the application. It coordinates the data retrieval and loading processes.

- Methods:
1. main(): The main function that orchestrates the data retrieval and loading processes.


## Setup Instructions
1. Clone the Repository:

```bash
git clone https://github.com/your-username/data-engineering-foundation-2024.git
cd data-engineering-foundation-2024/data_engineering_app
```
2. Install Dependencies:

```bash
pip install -r requirements.txt
```

3. Configure Database Connection:

- Update the config/config.yaml file with your PostgreSQL database connection details.

4. Run the Application:
```
python src/main.py
```