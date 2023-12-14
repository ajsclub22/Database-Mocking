from graph import Graph


class Adjacent(Graph):
    def neighbour_edges(self, start, end):
        if end not in self.graph[start][1] or start not in self.graph[end][1]:
            print("There is no edge between {} and {} ".format(start, end))
            return
        res = []
        for node in self.graph[start][1]:
            if node != end:
                res.append([start, node])
        for node in self.graph[end][1]:
            if node != start:
                res.append([end, node])

        return "Connected Edges", {[start, end]: res}
