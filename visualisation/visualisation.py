import networkx as nx
from pyvis.network import Network

class GraphVisualization:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.network = Network(notebook=True)

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graphe contient un cycle de poids négative")
                return
        
        self.visualize_graph(dist)

    def visualize_graph(self, dist):
        g = nx.DiGraph()
        for u, v, w in self.graph:
            g.add_edge(u, v, weight=w)

        for node in g.nodes:
            self.network.add_node(node, label=f"{node}\n{dist[node]:.2f}", title=f"Distance: {dist[node]:.2f}")

        for u, v, data in g.edges(data=True):
            self.network.add_edge(u, v, label=str(data['weight']), title=f"Weight: {data['weight']}")

        self.network.show("bellman_ford.html")

# Exemple d'utilisation
g = GraphVisualization(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

print("Lancement de l'algorithme Bellman-Ford")
g.bellman_ford(0)
