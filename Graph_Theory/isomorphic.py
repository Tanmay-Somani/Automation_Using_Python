import networkx as nix
import matplotlib.pyplot as plt
import numpy as np

adj_matrix1 = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
adj_matrix2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

graph1 = nix.Graph(adj_matrix1)
graph2 = nix.Graph(adj_matrix2)

