#!/usr/bin/env python
# coding: utf-8

# In[17]:


from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 

        self.graph_matrix[u][v] = w
        
        
        
    def Dijkstra(self, s): 

        values = [math.inf]*self.V
        values[s] = 0
        visited =  set()
        unvisited = set([x for x in range(self.V)])
        curr = s
        while curr is not None: 
            
            neighbors = self.graph[curr]
            for i, x in enumerate(neighbors):
                if x == 0 or i in visited: continue
                values[i] = min(values[i], values[curr] + x)

            visited.add(curr)
            unvisited.remove(curr)
            
            next_curr = None
            min_val = max(values)
            
            if not unvisited: break
            for node in unvisited:
                if values[node] < min_val:
                    next_curr = node
                    min_val = values[node]
            curr = next_curr
           
        ret = {str(i):x for i, x in enumerate(values)}
        return ret
            
     
                
   
    def has_Cycle(self,s,aj):
        visited = [False]*self.V
        def inner(v, visited, parent):
            visited[v]= True
            for neigh in aj[v]:
                if visited[neigh] == False:
                    if inner(neigh, visited, v):
                        return True
                elif parent != neigh:
                    return True
            return False  
        
        return inner(s, visited, -1)
        
    def Kruskal(self):

        edges = []
        for r in range(self.V):
            for c in range(self.V):
                if self.graph_matrix[r][c] == 0: continue
                edges.append([r,c,self.graph_matrix[r][c]])
        edges = sorted(edges, key=lambda edge: edge[2])
        
        aj = {i:set() for i in range(self.V)}
        ret = {}
        for u,v,w in edges:
            aj[u].add(v)
            aj[v].add(u)
            if self.has_Cycle(u, aj):
                aj[u].remove(v)
                aj[v].remove(u)
            else:
                ret['{}-{}'.format(u,v)] = w
        return ret


# In[18]:


g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]
          ]
print("Dijkstra" ,g.Dijkstra(0))




g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
print("Kruskal" ,g.Kruskal () )


# In[ ]:




