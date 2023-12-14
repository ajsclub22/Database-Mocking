from graph import Graph


class Traversal(Graph):

    def bfs(self, source):
        """
        This method takes the parameter as source node
        where intersect the graph using BFS
        Next node is bigger than previous node
        and store this result in path variable list
        and this method returns the path
        :param source:
        :return  path:
        """
        vis = []
        queue = []
        path = []
        vis.append(source)
        queue.append(source)
        while len(queue) != 0:
            curr_node = queue.pop(0)
            if len(path) > 0:
                prev_node_val = self.graph[path[len(path) - 1]][0]
                curr_node_val = self.graph[curr_node][0]
                if prev_node_val > curr_node_val:
                    break

            if curr_node not in path:
                path.append(curr_node)

            for vertex in self.graph[curr_node][1]:
                if vertex not in vis:
                    vis.append(vertex)
                    queue.append(vertex)

        return "bfs", {source: path}

    def dfs(self, source, vis=None, prev=-1, ans=None, res=None, flags=None):
        if flags is None:
            flags = [1]
        if res is None:
            res = []
        if ans is None:
            ans = []
        if vis is None:
            vis = []
        vis.append(source)
        ans.append(source)

        for node in self.graph[source][1]:
            if node not in vis and self.graph[node][0] >= self.graph[source][0]:
                flags[0] = 1
                self.dfs(node, vis, source, ans, res, flags)

        if flags[0] == 1:
            res.append(list(ans))
            flags[0] = 0
        ans.pop()
        return "dfs", {source: res}
