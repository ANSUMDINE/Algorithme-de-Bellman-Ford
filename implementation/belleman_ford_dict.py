from collections import defaultdict

class GraphDict:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def bellman_ford(self, src):
        dist = {i: float("Inf") for i in range(self.V)}
        dist[src] = 0

        for _ in range(self.V - 1):
            for u in self.graph:
                for v, w in self.graph[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        for u in self.graph:
            for v, w in self.graph[u]:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("Graphe contient un cycle de poids négative")
                    return

        return dist