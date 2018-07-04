"""
    - Adjacency matrix
        - Rows: source nodes
        - Columns: destination nodes
        - Cells[s, d] = 1 if there is an edge from s(ource) to d(estination), 0 otherwise
    - Adjacency list
        - Associate with each node a list of destination nodes
    - Digraphs
        - Two kinds of graphs, if the graph is dense (i.e. has a lot of nodes),
            convenient to use an adjacency matrix
"""


class Node():
    def __init__(self, name):
        try:
            self.name = name
        except:
            raise TypeError
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge():
    """Allows for defining the direction of an edge"""
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->'\
            + self.dest.getName()


class Digraph():
    """
    adjacency list implementation
    edges is a dict mapping each node to a list of its children
    """
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        """
        checks for errors, if not, adds it
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        """
        gets the source & destination node from edge param
        checks if it exists, if it does adds it
        """
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1] # omit final newline


class Graph(Digraph):
    # Graph is a subclasss of Digraph rather than the other way around?
        # Substitution rule:
        # If client code works correctly using an instance of the supertype, 
        # it should also work correctly when an instance of the subtype 
        # is substituted for the instace of the supertype
    # Any code that works with a digraph should work with a digraph
    # should work with a graph, but not vice versa

    def addEdge(self, edge):
        """
        override Digraph's addEdge,
        to add two edges, one in each direction
        """
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """
    Depth-First Search
    - Assumes graph is a Digraph; start and end are nodes
    - path and shortest are lists of nodes
    - Returns a shortest path form start to end in graph

    - Similar to left-first depth-first method of enumerating a search tree
    - Main difference is that grpah might have cycles, so must keep track of what nodes already visited

    - Continues until reaching goal node or node with no children
    - Search then backtracks until it reaches most recent node with children that it has not visited
    - Returns shortest path after exploring, if there is one from start to goal
    - Keeps track of nodes visited to avoid being stuck in a cycle
    - Keep track of shortest path traveled
    - Don't bother exploring paths that are longer than the current shortest
    """
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start ==end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    """ 
    DFS called from this wrapper function
    - this funciton gets recursion started properly 
    - provides appropriate abstraction
    """
    return DFS(graph, start, end, [], None, toPrint)
    
