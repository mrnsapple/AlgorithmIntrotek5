import networkx as nx


def sort_edgers(a, b):
    return (b,a) if a > b else (a,b)

def generate_line_graph(G):
    LineGraph = nx.Graph()

    for n, nbrsdict in G.adjacency():
        edges =list(nbrsdict.keys())
        if len(edges) == 1:
            LineGraph.add_node(sort_edgers(n, edges[0]))
            continue
        for i, edge in enumerate(edges):
            for b in edges[i+1:]:
                edge_two = sort_edgers(n ,edge)
                edge_one = sort_edgers(n, b)
                if not LineGraph.has_edge(edge_one, edge_two):
                    LineGraph.add_edge(edge_one, edge_two)
    return LineGraph