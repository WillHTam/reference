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
        if type(name) is not str:
            raise ValueError
        self.name = name
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


def buildCityGraph(graphType):
    # build the graph as shown in the picture
    # a cycle is possible of NY -> Chi -> Denver -> back to NY
        # the presence of cycles complicates shortest path problems
        # possible to leave LA but not enter
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

"""
~ ~ Adjacency List ~ ~
BOS: Providence, NY
Providence: BOS, NY
NY: CHI
CHI: DEN, PHX
DEN: PHX, NY
LS: BOS
"""

print(buildCityGraph(Digraph))