import osmnx as ox
import networkx as nx
from risk import RiskEngine

# Load graph once
G = ox.load_graphml("vellore_roads.graphml")

# Initialize risk engine
risk_engine = RiskEngine(G)

# Assign risk weights ONCE
print("Assigning risk weights...")
for u, v, key, data in G.edges(keys=True, data=True):
    data["risk"] = risk_engine.compute_edge_risk(u, v, data)
print("Risk weights assigned!")

# ---------------- Routing ----------------

def nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def fastest_route(source, target):
    return nx.shortest_path(G, source, target, weight="length")

def safest_route(source, target):
    return nx.shortest_path(G, source, target, weight="risk")

def route_to_coordinates(route):
    return [(G.nodes[n]["y"], G.nodes[n]["x"]) for n in route]
