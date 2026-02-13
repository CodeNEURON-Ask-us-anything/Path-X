import osmnx as ox

place = "Vellore, Tamil Nadu, India"

print("Downloading Vellore road network...")

G = ox.graph_from_place(place, network_type="drive")

ox.save_graphml(G, "vellore_roads.graphml")

print("Saved successfully as vellore_roads.graphml")
