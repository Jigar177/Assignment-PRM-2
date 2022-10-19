'''Q1

You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the input graph starting from node x. Complete the following function in order to give the required output.

Input Format:

The first line of input contains a list containing sets representing a graph. The second line of input contains the number x. 

Output Format:

Complete the function in order to return the required output.

Sample Input 0:

[[1,0],[2,0],[3,0],[3,2]]

3

Sample Output 0:

3 0 2'''

from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
 

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 0)
    g.addEdge(2, 0)
    g.addEdge(3, 0)
    g.addEdge(3, 2)

 
    print("Following is DFS from (starting from vertex 2)")
    g.DFS(3)