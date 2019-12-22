from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue = []
        seen = []
        queue.append(s)
        seen.append(s)
        
        while len(queue) != 0:
            v = queue.pop(0)
            nodes = self.graph[v]
            for i in nodes:
                if i not in seen:
                    queue.append(i)
                    seen.append(i)
        return seen
                
     def DFS(self, s):
        stack = [];final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != len(final)-1:
            for i in reversed(stack):
                if i in final:
                    continue
                final.append(i)
                for n in self.graph[i]:
                    if n not in stack:
                        if n not in final:
                            stack.append(n)
                break
        return final
