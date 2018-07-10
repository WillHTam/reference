from graph import Node, Edge, Graph, Digraph, dfsPath, DFS, printPath, BFS, bfsPath

def split(n):
    print('~'*n)

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

print(buildCityGraph(Graph))

split()

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = dfsPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print('Shortest path from ', source, 'to',
                destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP('Chicago', 'Boston')

split()

testSP('Boston', 'Phoenix')

split()

def testSP2(source, destination):
    g = buildCityGraph(Digraph)
    sp = bfsPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    if sp != None:
        print('Shortest path from ', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP2('Boston', 'Phoenix')
