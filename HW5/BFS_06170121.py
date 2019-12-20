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
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != 0:
            s = stack.pop()
            final.append(s)
            plus = []
            plus = plus+self.graph[s]
            for i in plus:
                if i in stack:
                    plus.remove(i)
                if i in final:
                    plus.remove(i)
            stack = stack+plus
        return final
