import networkx as nix
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(graph,ax):
    pos = nix.spring_layout(graph)
    nix.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10,ax=ax)

adj_matrix1 = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
adj_matrix2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

graph1 = nix.Graph(adj_matrix1)
graph2 = nix.Graph(adj_matrix2)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].set_title("Graph 1")
visualize_graph(graph1, axes[0])

axes[1].set_title("Graph 2")
visualize_graph(graph2, axes[1])

plt.tight_layout()
plt.show()