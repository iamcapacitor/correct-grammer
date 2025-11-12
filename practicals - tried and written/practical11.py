'''
Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
Assume these locations represent nodes of a graph. If there is a route between two locations,
it is represented as connections between nodes. Find out the sequence in which you will
visit these locations, starting from (say A) using 
(i) BFS and 
(ii) DFS. 
Represent a given graph using an adjacency matrix to perform DFS and an adjacency list to perform BFS.
---------------------------------------------------------------------------------

A-----B
|\
| \
|  \
C---D---E

  A B C D E
A 0,1,1,1,0
B 1,0,0,0,0
C 1,0,0,1,0
D 1,0,1,0,1
E 0,0,0,1,0

'''
from collections import deque

nodes = ['A','B','C','D','E']

adjancencymatrix = [
    [0,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,1,0],
    [1,0,1,0,1],
    [0,0,0,1,0]
]

# making adjancency list using python dictionary
adjancencylist = {
    'A':['B','C','D'],
    'B':['A'],
    'C':['A','D'],
    'D':['A','C','E'],
    'E':['D']
}

# DFS algorithm code
def DFS_algorithm(matrix , startnode):
    start = nodes.index(startnode)
    mat = matrix
    stack = [start]
    visited = [False]*len(mat[start])
    visited[start] = True 
    order = []
    while stack :
        node = stack.pop()
        order.append(nodes[node])
        for i in range(len(mat[node])):
            if mat[node][i] == 1 and not visited[i]:
              stack.append(i)
              visited[i] = True
    print("DFS Traversal completed ")
    print(str(order))
    
  

def BFS_algorithm(dlist , startnode):
    q = deque([startnode],len(dlist))
    visited = []
    while q:
      node = q.popleft()
      if node not in visited:
        visited.append(node)
        for adjacents in dlist[node]:
            if adjacents not in visited:
                q.append(adjacents)
    print("BFS traversal completed")
    print(visited)

DFS_algorithm(adjancencymatrix , 'A') 
BFS_algorithm(adjancencylist , 'A')