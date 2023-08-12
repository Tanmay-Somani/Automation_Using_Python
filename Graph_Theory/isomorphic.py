import networkx as nix
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10)
    plt.show()


adj_matrix1 = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
adj_matrix2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

graph1 = nix.Graph(adj_matrix1)
graph2 = nix.Graph(adj_matrix2)

print("Graph 1:")
visualize_graph(graph1)

print("Graph 2:")
visualize_graph(graph2)