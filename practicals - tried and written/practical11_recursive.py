'''
A----B
|\
| \
|  \
C---D---E

  A B C D E
A 0,1,1,1,0
B 1,0,0,0,0
C 1,0,0,1,0
D 1,0,1,0,1
E 0,0,0,0,1
'''

nodes = ['A','B','C','D','E']

adjancencymatrix = [
    [0,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,1,0],
    [1,0,1,0,1],
    [0,0,0,0,1],
]

adjancencylist = {
    'A':['B','C','D'],
    'B':['A'],
    'C':['A','D'],
    'D':['A','C','E'],
    'E':['D']
}

def DFS_traversal(mat , startnode):
    start = nodes.index(startnode)
    stack = [start]
    visited = [False]*len(mat)
    visited[start] = True
    def DFS(stac):
        if not stac:
            return
        else:
            node = stac.pop()
            print(f" {nodes[node]}->",end="")
            for i in range(0 , len(mat[node])):
                if mat[node][i] == 1 and not visited[i]:
                    stac.append(i)
                    visited[i] = True
        DFS(stac)
    DFS(stack)



def BFS_traversal(adjlist , startnode):
    q = [startnode] # we are trying to use python list and an queue , by using its pop and append functions
    visited = []
    # defining inner functions
    def bfs(que):
        if not que: # base case
            return
        else:
            node = que.pop(0)
            if node not in visited:
                visited.append(node)
                for adjacent in adjlist[node]:
                    if adjacent not in visited:
                        que.append(adjacent)
        bfs(que)

    bfs(q)
    print(f"BFS Traversal = ",visited)



DFS_traversal(adjancencymatrix , 'A')
# BFS_traversal(adjancencylist , 'A')