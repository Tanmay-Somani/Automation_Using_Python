def safeVertex(node, path):
    if node in path:
        return False
    return True     

def cycleDetection(E, n, root, path):
    path.append(root)
    for i in E[root]:
        if safeVertex(i, path):
            if cycleDetection(E, n, i, path):
                return True
    if len(path) == n:
        if path[0] in E[path[len(path) - 1]]:
            return True 
        else:
            return False
    path.pop()
    return False

def HamiltonianCycle(E, n, root):
    path = []
    if cycleDetection(E, n, root, path):
        print("True")
        print(path)
    else:
        print("False")

N_Vertices = int(input())
matrix = [[] for _ in range(N_Vertices)]

N_Edges = input()

for j in range(int(N_Edges)):
    edge_vertices = input().split()
    u = int(edge_vertices[0])
    v = int(edge_vertices[1])
    matrix[u - 1].append(v - 1)
    matrix[v - 1].append(u - 1)
    
HamiltonianCycle(matrix, N_Vertices, 0)
