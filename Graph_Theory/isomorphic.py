import networkx as nix
import matplotlib.pyplot as plt
import numpy as np

def displ_grph(graph, ax):
    pos = nix.spring_layout(graph)
    nix.draw(graph, pos, with_labels=True, node_size=500, node_color='#5CA904', font_size=9, ax=ax)

def vertex_count(adj_matrix):
    return len(adj_matrix)

def edge_count(adj_matrix):
    return int(np.sum(adj_matrix) / 2)

def edge_connection_match(adj_matrix1, adj_matrix2):
    sorted_sums1 = sorted(np.sum(adj_matrix1, axis=0))
    sorted_sums2 = sorted(np.sum(adj_matrix2, axis=0))
    return sorted_sums1 == sorted_sums2

adj_matrix1 = np.array([
    [0, 1, 1, 0, 0],[1, 0, 1, 1, 0],[1, 1, 0, 0, 1],[0, 1, 0, 0, 1],[0, 0, 1, 1, 0]
])

adj_matrix2 = np.array([
    [0, 1, 0, 0, 1],[1, 0, 1, 1, 0],[0, 1, 0, 1, 0],[0, 1, 1, 0, 1],[1, 0, 0, 1, 0]
])
if vertex_count(adj_matrix1)==vertex_count(adj_matrix2):
    print("The vertices in both the matrix match")
    if edge_count(adj_matrix1)==edge_count(adj_matrix2):
        print("The edges in both the matrix match")
        if edge_connection_match(adj_matrix1, adj_matrix2):
            print("The graphs are Isomorphic")
        else:
            print("The graphs are not Isomorphic")
    else:
        print("The graphs are not Isomorphic")
else:
    print("The graphs are not Isomorphic")                
            
graph1 = nix.Graph(adj_matrix1)
graph2 = nix.Graph(adj_matrix2)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].set_title("Graph 1")
displ_grph(graph1, axes[0])
axes[1].set_title("Graph 2")
displ_grph(graph2, axes[1])

plt.tight_layout()
plt.show()
