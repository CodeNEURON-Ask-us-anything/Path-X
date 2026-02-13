import osmnx as ox

G = ox.load_graphml("vellore_roads.graphml")

print("Graph loaded successfully!")
print("Total Nodes:", len(G.nodes))
print("Total Edges:", len(G.edges))
