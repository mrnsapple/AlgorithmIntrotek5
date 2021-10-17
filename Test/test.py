import sys

sys.path.insert(0, '..')
import numpy as np
from graphviz import Graph
import time
import matplotlib.pyplot as plt
import networkx as nx
import unittest
from Part3.line_graph_generator import generate_line_graph
from Part1.snowplowProblem import parcours
from Part2.coloring_part2 import colorGraph



N = 61
global dot
edges = {
	(0, 5),
	(0, 18),
	(0, 53),
	(0, 59),
	(1, 13),
	(1, 35),
	(1, 43),
	(1, 46),
	(1, 51),
	(1, 57),
	(2, 7),
	(2, 8),
	(2, 27),
	(3, 4),
	(3, 14),
	(3, 16),
	(3, 19),
	(3, 20),
	(3, 30),
	(3, 45),
	(3, 55),
	(3, 56),
	(4, 25),
	(4, 50),
	(5, 20),
	(5, 35),
	(5, 40),
	(5, 54),
	(6, 32),
	(6, 41),
	(6, 46),
	(6, 55),
	(7, 40),
	(8, 11),
	(8, 23),
	(8, 31),
	(8, 32),
	(8, 40),
	(9, 28),
	(9, 46),
	(9, 57),
	(10, 14),
	(10, 15),
	(10, 24),
	(10, 25),
	(10, 27),
	(11, 19),
	(11, 36),
	(11, 50),
	(12, 33),
	(12, 41),
	(12, 48),
	(13, 14),
	(13, 23),
	(13, 27),
	(13, 36),
	(13, 41),
	(14, 24),
	(14, 42),
	(15, 44),
	(15, 45),
	(15, 55),
	(16, 35),
	(16, 52),
	(17, 18),
	(17, 19),
	(17, 22),
	(17, 30),
	(17, 36),
	(17, 44),
	(17, 49),
	(19, 41),
	(19, 44),
	(19, 57),
	(19, 58),
	(20, 26),
	(20, 29),
	(21, 46),
	(21, 49),
	(21, 59),
	(22, 32),
	(22, 59),
	(23, 31),
	(23, 45),
	(23, 56),
	(24, 28),
	(24, 40),
	(24, 43),
	(24, 50),
	(25, 56),
	(26, 28),
	(26, 37),
	(26, 38),
	(27, 28),
	(27, 33),
	(27, 37),
	(27, 56),
	(28, 49),
	(29, 31),
	(30, 37),
	(30, 45),
	(30, 54),
	(33, 43),
    (34, 51),
	(35, 50),
	(35, 57),
	(35, 59),
	(36, 49),
	(36, 50),
	(37, 40),
	(39, 54),
	(41, 55),
	(43, 59),
	(44, 45),
    (47, 45),
	(48, 53),
	(50, 56),
	(50, 59),
	(51, 53),
	(54, 59),
    (60, 52)
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
	def __init__(self, edges, N):
		self.adj = [[] for _ in range(N)]
		self.N = N
		for (src, dest) in edges:
			self.adj[src].append(dest)
			self.adj[dest].append(src)


class TestLineGraph(unittest.TestCase):

    def print_graph(L, graph_name):
        graph_name = f"images/{graph_name}{len(L.nodes())}_vx_{1}_edgs.pdf"
        nx.draw(L,
                node_size=[2],
                node_color=["#46b2e0"],
                edge_color=["#46b2e0"],
                width=[0.4])
        plt.savefig(graph_name)

    def test_line_graph(self):
        G = nx.star_graph(4)
        G = nx.fast_gnp_random_graph(80, 0.4)
        L = nx.line_graph(G)
        print("GRAPH:")
        print(sorted(G.edges()))
        print("NX LINE GRAPH:")
        print(sorted(L.edges()))
        print("MY LINE GRAPH:")
        LineGraph = generate_line_graph(G)
        print(sorted(LineGraph.edges()))
        # Check networkx result is the same
        for g in L.edges():
            self.assertTrue(g in LineGraph.edges())
        for g in LineGraph.edges():
            self.assertTrue(g in L.edges())


class TestColoring(unittest.TestCase):
	def	test_coloring(self):
		dot = Graph()
		for edge in edges:
			dot.edge(str(edge[0]), str(edge[1]), color='black', penwidth='1.1')
		graph_name = 'graphs/coloring_1'
		graph = Graph1(edges, N)
		result = colorGraph(graph)
		for v in range(graph.N):
			dot.node(str(v), color=colors[result[v]], penwidth='2')
		print("Color assigned to vertex", v, "is", colors[result[v]])
		print(graph)
		dot.render(graph_name)


class TestParcours(unittest.TestCase):

    def check_list(self, house_list, sorted_house_list):
        self.assertTrue(len(sorted_house_list) == len(house_list))
        self.assertTrue(house in sorted_house_list  for house in house_list)            
        self.assertTrue(house in house_list  for house in sorted_house_list)            
        print("\n{}".format(sorted_house_list))
        # print("result:")
        # print(result)

    def test_parcours(self):
        houses_list =np.random.normal(0,1000,1000).tolist()
        start = time.time()
        sorted_house_list = parcours(houses_list)
        end = time.time()
        self.check_list(houses_list, sorted_house_list)
        print("Runtime of the program is {}".format(end-start))
        #
        houses_list =np.random.normal(0,10,10).tolist()
        start = time.time()
        sorted_house_list = parcours(houses_list)
        end = time.time()
        self.check_list(houses_list, sorted_house_list)
        print("Runtime of the program is {}".format(end-start))
        
if __name__ == '__main__':
    unittest.main()
