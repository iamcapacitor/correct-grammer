'''
Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
Assume these locations represent nodes of a graph. If there is a route between two locations,
it is represented as connections between nodes. Find out the sequence in which you will
visit these locations, starting from (say A) using 
(i) BFS and 
(ii) DFS. 
Represent a given graph using an adjacency matrix to perform DFS and an adjacency list to perform BFS.

-----------------------------------------------
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
E 0,0,0,1,0

'''
from collections import deque

nodes = ['A','B','C','D','E']

adjancencymatrix = [
    [0,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,1,0],
    [1,0,1,0,1],
    [0,0,0,1,0],
]

adjancencylist = {
    'A':['B','C','D'],
    'B':['A'],
    'C':['A','D'],
    'D':['A','C','E'],
    'E':['D']
}

class Traversal:
    def BFSTraversal(self ,adlist, startnode):
        visited = []
        queue = deque([startnode])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
            for adjacent in adlist[node]:
                if adjacent not in visited:
                    queue.append(adjacent)
        print(f"DFS Traversal : {visited}")

    def DFSTraversal(self , admatrix , startnode):
        startindex = nodes.index(startnode)
        stack = [startindex]
        order = []
        visited = [False]*len(admatrix)
        visited[startindex] = True
        while stack:
            nodei = stack.pop()
            order.append(nodes[nodei])
            for i in range(len(admatrix[nodei])):
                if admatrix[nodei][i] == 1 and not visited[i]:
                    stack.append(i)
                    visited[i] = True
        print(f"BFS Traversal : {order}")

t = Traversal()

t.BFSTraversal(adjancencylist , 'D')
t.DFSTraversal(adjancencymatrix , 'E')


