from graph import Node, Edge, Graph

# def canSwap(a, b):
#     for i in range(len(a) - 1):
#         if a[i] != b [i]:
#             return a[i] == b [i+1] and b[i] == a[i+1]

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))

print('nodes', [i.__str__() for i in nodes])
print(g)

