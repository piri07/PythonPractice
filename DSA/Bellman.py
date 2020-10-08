class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    #prints the solution
    def printArr(self,dist):
        print("vertex distance from Source")
        for i in range(self.V): 
            print("{0}\t\t{1}".format(i, dist[i])) 
    # The main function that finds shortest distances from src to all other vertices using Bellman-Ford algorithm. The function also detects negative weight cycle
    def BellmanFord(self,src):
    #initalize all as infinite except the source node
        dist =[float("Inf")]*self.V
        dist[src]=0
        for i in range(self.V - 1):
            for u,v,w in self.graph:
                if dist[u] !=float("Inf") and dist[u] + w < dist[v]:
                    dist[v]= dist[u] + w
    
        for u,v,w in self.graph:
            if dist[u]!=float("Inf") and dist[u] + w < dist[v]:
                print("graph doesnt containt any negative cycle")
                return
        self.printArr(dist)



g = Graph(5)  
g.addEdge(0, 1, -1)  
g.addEdge(0, 2, 4)  
g.addEdge(1, 2, 3)  
g.addEdge(1, 3, 2)  
g.addEdge(1, 4, 2)  
g.addEdge(3, 2, 5)  
g.addEdge(3, 1, 1)  
g.addEdge(4, 3, -3) 
  
# Print the solution  
g.BellmanFord(0) 
