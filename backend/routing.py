import osmnx as ox
import networkx as nx
from risk import RiskEngine

G = ox.load_graphml("vellore_roads.graphml")

risk_engine = RiskEngine(G)

def nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def fastest_route(source, target):
    return nx.shortest_path(G, source, target, weight="length")

def safest_route(source, target):

    def risk_weight(u, v, data):
        return risk_engine.compute_edge_risk(u, v, data)

    return nx.shortest_path(G, source, target, weight=risk_weight)

def route_to_coordinates(route):
    return [(G.nodes[n]["y"], G.nodes[n]["x"]) for n in route]
