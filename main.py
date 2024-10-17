
from implementation.belleman_ford_list import Graph as GraphList
from implementation.belleman_ford_dict import GraphDict as GraphDict

def main():
    # Exemple avec GraphList
    g_list = GraphList(5)
    g_list.add_edge(0, 1, -1)
    g_list.add_edge(0, 2, 4)
    g_list.add_edge(1, 2, 3)
    g_list.add_edge(1, 3, 2)
    g_list.add_edge(1, 4, 2)
    g_list.add_edge(3, 2, 5)
    g_list.add_edge(3, 1, 1)
    g_list.add_edge(4, 3, -3)
    print("Distances avec GraphList:", g_list.bellman_ford(0))

    # Exemple avec GraphDict
    g_dict = GraphDict(5)
    g_dict.add_edge(0, 1, -1)
    g_dict.add_edge(0, 2, 4)
    g_dict.add_edge(1, 2, 3)
    g_dict.add_edge(1, 3, 2)
    g_dict.add_edge(1, 4, 2)
    g_dict.add_edge(3, 2, 5)
    g_dict.add_edge(3, 1, 1)
    g_dict.add_edge(4, 3, -3)
    print("Distances avec GraphDict:", g_dict.bellman_ford(0))

if __name__ == "__main__":
    main()
