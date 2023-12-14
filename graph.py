import json
from database import Database


class Graph:
    """
    This is the main graph class
    """

    def __init__(self):
        self.graph = {}
        self.db = Database()

    def add_edge(self, start, end):
        """
        This method is for adding edge
        in the graph
        """
        if start not in self.graph:
            print("Start is not resent in graph")
            return

        if end not in self.graph:
            print("End vertex is not resent in graph")
            return

        self.graph[start][1].append(end)
        self.graph[end][1].append(start)

    def add_node(self, node, value):
        """
        This method is for connecting the node
        in the graph
        """
        if node not in self.graph:
            self.graph[node] = []
            self.graph[node].append(value)
            self.graph[node].append([])

    def print_graph(self):
        """
        This method of printing the graph
        """
        for edge in self.graph:
            print(edge, " : ", self.graph[edge])

    def create_graph(self):
        self.db.connect()
        node_data = self.db.fetch_data("GRAPH_NODE")
        edge_data = self.db.fetch_data("GRAPH_EDGE")
        self.make_graph(node_data,edge_data)

    def make_graph(self, node_data, edge_data):
        for node in node_data:
            self.add_node(node[1], node[2])
        for edge in edge_data:
            self.add_edge(edge[1], edge[2])
        return self.graph

    def result(self, data):
        self.db.store_result(data)

    def close(self):
        self.db.connection_close()
