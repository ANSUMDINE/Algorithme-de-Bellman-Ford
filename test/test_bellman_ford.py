import sys
import os

# Ajouter le répertoire parent au chemin d'importation
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'implementation'))

import pytest
from belleman_ford_list import Graph as GraphList
from belleman_ford_dict import GraphDict as GraphDict

def test_bellman_ford_list():
    g = GraphList(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    assert g.bellman_ford(0) == [0, -1, 2, -2, 1]

def test_bellman_ford_dict():
    g = GraphDict(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    assert g.bellman_ford(0) == {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
