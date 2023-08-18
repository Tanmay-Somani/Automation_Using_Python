def safeVertex(node):
    if(node in path):
        return False
    
    return True     

def cycleDetection(E,n,root):
    path.append(root)
    for i in E[root]:
        if(safeVertex(i)):
            if(cycleDetection(E,n,i)):
                return True

    if(len(path) == n):
        if(path[0] in E[path[len(path)-1]]):
            return True 
        else:
            return False
    path.pop()


def HamiltonianCycle(E,n,root):
    if(cycleDetection(E,n,root)):
        print("True")
    else:
        print("False")


path = []

N_Vertices = int(input())

matrix = list()
for i in range(N_Vertices):
    matrix.append([])

N_Edges = int(input())

for j in range(N_Edges):
    edge_vertices = input().split()
    u = int(edge_vertices[0])
    v = int(edge_vertices[1])
    matrix[u-1].append(v-1)
    matrix[v-1].append(u-1)
    
HamiltonianCycle(matrix,N_Vertices,0)

print(path)
