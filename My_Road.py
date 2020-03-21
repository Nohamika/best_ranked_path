def CalcAvg(path, graph, Arc):
    """this fucntion will calculate the avg
    of the path that is giving"""
    summ = 0
    count = len(path) - 1
    if count == 0:
        return 0
    for i in range(len(path) - 1):
        temp = (path[i], path[i + 1])
        # each arc in Arc is kept in a sorten order so even though the path (1,2) and (2,1) is
        # the same to me is it not to Arc so im changing the order according to what is in Arc
        if temp not in Arc:
            temp = (path[i + 1], path[i])
        summ = summ + Arc[temp][0]
    return summ / count


from collections import defaultdict


class Graph:
    best = []

    "this class represents a graph"

    def __init__(self):

        # default dictionary to store the graph
        self.graph = defaultdict(list)
        # default dictionary to store the ratings of the Arcs
        self.Arc = defaultdict(list)
        # default dictionary to store all the paths that were giving with the key of their rating to pick the best one in the end
        self.best = defaultdict(list)

    def addEdge(self, u, v, Rate):
        """this func creates the graph"""
        # the edges in the graph that are connected to each other
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.Arc[(u, v)].append(Rate)

    def route(self, path, visited, s, d):
        """this func will find all the possible routes
        s is starting point and d is destination"""

        path.append(s)
        visited.append(s)

        # the function will get into this if, only when the path has reached the destination
        if (s == d):
            # print("path:",path)

            # clac the avg
            avg = CalcAvg(path, self.graph, self.Arc)

            # I convert path into a tuple so the dictionary doesnt like lists
            path2 = tuple(path)
            self.best[avg] = path2


        else:
            # print("not ready yet",path)
            for x in self.graph[s]:
                if x not in visited:
                    self.route(path, visited, x, d)

        path.pop()
        visited.remove(s)

    def activeRoute(self, s, d):
        """this function will activate the function route and initialize it"""

        path = []
        visited = []
        self.route(path, visited, s, d)

    def BestPath(self):
        """this function finds the best path and prints it"""
        k = 0
        # For loop to go though all the paths and compare their scores to find the best one
        for i in self.best:
            if i > k:
                k = i
        print("the best path is", self.best[k], "with the avg of:", k)


# creating the graph
g = Graph()
g.addEdge('A', 'B', 0)
g.addEdge('C', 'B', 3)
g.addEdge('A', 'D', 4)
g.addEdge('D', 'B', 9)

g.activeRoute('D', 'A')
g.BestPath()
