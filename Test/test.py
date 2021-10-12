import sys
sys.path.insert(0,'..')
from Part3.line_graph_generator import generate_line_graph
import networkx as nx
import matplotlib.pyplot as plt
import unittest

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
        G = nx.fast_gnp_random_graph(80,0.4)
        L = nx.line_graph(G)
        print("GRAPH:")
        print(sorted( G.edges()))
        print("NX LINE GRAPH:")
        print(sorted( L.edges()))
        print("MY LINE GRAPH:")
        LineGraph =generate_line_graph(G)
        print(sorted(LineGraph.edges()))
        #Check networkx result is the same
        for g in L.edges():
            self.assertTrue(g in LineGraph.edges())
        for g in LineGraph.edges():
            self.assertTrue(g in L.edges())
 
if __name__ == '__main__':
    unittest.main()