import unittest
from unittest.mock import patch
from database import Database
from traversal import Traversal


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.conn = unittest.mock.MagicMock()
        # Create a mock cursor object
        self.cur = unittest.mock.MagicMock()

        # Set the return value of the `conn.cursor` method to the mock cursor object
        self.conn.cursor.return_value = self.cur

        self.connect_patch = unittest.mock.patch('psycopg2.connect', return_value=self.conn)
        self.connect_patch.start()

        # Patch the `conn.cursor` method with the mock cursor object
        self.cursor_patch = unittest.mock.patch.object(self.conn, 'cursor', return_value=self.cur)
        self.cursor_patch.start()

        # Create an instance of the Database class
        self.db = Database()
        self.graph = Traversal()
        self.create_graph()

    def test_agraph(self):
        print("Graph Testing Correct One...\n")
        print()
        # return value of Graph_node
        self.cur.fetchall.return_value = [(1, 0, 1), (2, 0, 2), (3, 1, 4), (4, 2, 3), (5, 5, 4)]

        # Call the connect method (which will now use the mock connection)
        self.db.connect()

        # Perform the test using the mocked connection and fetch_data method
        data1 = self.db.fetch_data('Graph_Node')

        # return value of Graph Edge
        self.cur.fetchall.return_value = [(1, 0, 1), (2, 0, 2), (3, 1, 4), (4, 2, 3), (5, 5, 4)]
        data2 = self.db.fetch_data("Graph_Edge")

        # Create graphs from data fetch from database
        result = self.graph.make_graph(data1, data2)
        print("Actual Result:", result)
        print("Expected Result:", self.graph.graph)

        # Your assertions
        self.assertEqual(result, self.graph.graph)
        print()

    def create_graph(self):
        self.graph.add_node(0, 100)
        self.graph.add_node(2, 200)
        self.graph.add_node(3, 500)
        self.graph.add_node(1, 200)
        self.graph.add_node(5, 600)
        self.graph.add_node(4, 700)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(5, 4)
        self.graph.add_edge(2, 3)

    def test_bfs_correct(self):
        print("BFS Testing Correct One...\n")
        self.cur.fetchall.return_value = {0: [0, 1, 2, 4]}
        # Call the connect method (which will now use the mock connection)
        self.db.connect()

        # Perform the test using the mocked connection and fetch_data method
        result = self.db.fetch_data('Graph_result')
        ans = self.graph.bfs(0)
        print("Actual Result:", result)
        print("Expected Result:", ans[1])

        # Your assertions
        self.assertEqual(result, ans[1])
        print()

    def test_bfs_incorrect(self):
        print("BFS Testing Incorrect One...\n")
        self.cur.fetchall.return_value = {5: [5, 3]}
        # Call the connect method (which will now use the mock connection)
        self.db.connect()

        # Perform the test using the mocked connection and fetch_data method
        result = self.db.fetch_data('Graph_result')
        ans = self.graph.bfs(5)
        print("Actual Result:", result)
        print("Expected Result:", ans[1])

        # Your assertions
        self.assertEqual(result, ans[1])
        print()

    def test_dfs_correct(self):
        print("DFS Testing Correct One...\n")
        self.cur.fetchall.return_value = {0: [[0, 1, 4], [0, 2, 3]]}

        # Call the connect method (which will now use the mock connection)
        self.db.connect()

        # Perform the test using the mocked connection and fetch_data method
        result = self.db.fetch_data('Graph_result')
        ans = self.graph.dfs(0)
        print("Actual Result:", result)
        print("Expected Result:", ans[1])

        # Your assertions
        self.assertEqual(result, ans[1])
        print()

    def test_dfs_incorrect(self):
        print("DFS Testing Incorrect One...\n")
        self.cur.fetchall.return_value = {1: [[1, 5]]}

        # Call the connect method (which will now use the mock connection)
        self.db.connect()

        # Perform the test using the mocked connection and fetch_data method
        result = self.db.fetch_data('Graph_result')
        ans = self.graph.dfs(1)
        print("Actual Result:", result)
        print("Expected Result:", ans[1])

        # Your assertions
        self.assertEqual(result, ans[1])

    def tearDown(self):
        # Stop the patches
        self.connect_patch.stop()
        self.cursor_patch.stop()
        self.db.connection_close()
        print()


if __name__ == '__main__':
    unittest.main()
