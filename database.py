import psycopg2
import json
from config import config


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        params = config()
        print("Connecting to PostgreSQL DataBase...")
        self.connection = psycopg2.connect(**params)
        cursor = self.pointer()
        print("PostgreSQL DataBase Version...")
        cursor.execute('SELECT version()')

    def pointer(self):
        if self.connection:
            return self.connection.cursor()

    def connection_close(self):
        if self.connection:
            self.connection.close()
            print("Close PostgreSQL DataBase...")
        else:
            raise Exception("connection doesn't exists...")

    def fetch_data(self, table):
        """
        This method is to fetch node data
        from table of Graph
        DataBase.
        """

        if self.connection:
            cursor = self.pointer()
            query = "SELECT * FROM {0}".format(table)
            cursor.execute(query)
            print("fetching data from {0}".format(table))
            data = cursor.fetchall()

            return data

    def query_execute(self, query):
        if self.connection:
            cursor = self.pointer()
            cursor.execute(query)
            self.connection.commit()

    def store_result(self, data):
        cursor = self.pointer()
        cursor.execute("INSERT INTO GRAPH_RESULT (ALGO_NAME,RESULT) VALUES(%s,%s)", (data[0], json.dumps(data[1])))
        self.connection.commit()
