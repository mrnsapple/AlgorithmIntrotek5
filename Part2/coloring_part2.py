from networkx.generators.random_graphs import erdos_renyi_graph

# Function to assign colors to vertices of a graph
def colorGraph(graph):
    # keep track of the color assigned to each vertex	
	result = {}
	# assign a color to vertex one by one
	for u in range(graph.N):
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
	return result
    