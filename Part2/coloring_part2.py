from graphviz import Graph
from networkx.generators.random_graphs import erdos_renyi_graph

N = 61 
global dot
edges = {
	(0,5),
	(0,18),
	(0,53),
	(0,59),
	(1,13),
	(1,35),
	(1,43),
	(1,46),
	(1,51),
	(1,57),
	(2,7),
	(2,8),
	(2,27),
	(3,4),
	(3,14),
	(3,16),
	(3,19),
	(3,20),
	(3,30),
	(3,45),
	(3,55),
	(3,56),
	(4,25),
	(4,50),
	(5,20),
	(5,35),
	(5,40),
	(5,54),
	(6,32),
	(6,41),
	(6,46),
	(6,55),
	(7,40),
	(8,11),
	(8,23),
	(8,31),
	(8,32),
	(8,40),
	(9,28),
	(9,46),
	(9,57),
	(10,14),
	(10,15),
	(10,24),
	(10,25),
	(10,27),
	(11,19),
	(11,36),
	(11,50),
	(12,33),
	(12,41),
	(12,48),
	(13,14),
	(13,23),
	(13,27),
	(13,36),
	(13,41),
	(14,24),
	(14,42),
	(15,44),
	(15,45),
	(15,55),
	(16,35),
	(16,52),
	(17,18),
	(17,19),
	(17,22),
	(17,30),
	(17,36),
	(17,44),
	(17,49),
	(19,41),
	(19,44),
	(19,57),
	(19,58),
	(20,26),
	(20,29),
	(21,46),
	(21,49),
	(21,59),
	(22,32),
	(22,59),
	(23,31),
	(23,45),
	(23,56),
	(24,28),
	(24,40),
	(24,43),
	(24,50),
	(25,56),
	(26,28),
	(26,37),
	(26,38),
	(27,28),
	(27,33),
	(27,37),
	(27,56),
	(28,49),
	(29,31),
	(30,37),
	(30,45),
	(30,54),
	(33,43),
    (34,51),
	(35,50),
	(35,57),
	(35,59),
	(36,49),
	(36,50),
	(37,40),
	(39,54),
	(41,55),
	(43,59),
	(44,45),
    (47,45),
	(48,53),
	(50,56),
	(50,59),
	(51,53),
	(54,59),
    (60,52)
}
node_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

colors = ["", "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
            "BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"]

class Graph1:
 
    # Constructor
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph):
 
    # keep track of the color assigned to each vertex
    result = {}
 
    # assign a color to vertex one by one
    for u in range(N):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(N):
        dot.node(str(v),
                 color=colors[result[v]],
                 penwidth='2')
        print("Color assigned to vertex", v, "is", colors[result[v]])
 
# save this simple graph
dot = Graph()
for edge in edges:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='black',
             penwidth='1.1')
graph_name = 'graphs/coloring_0'
graph = Graph1(edges, N)
colorGraph(graph)
dot.render(graph_name)