import json
import math
from geopy.distance import geodesic
from datetime import datetime


class RiskEngine:

    def __init__(self, graph, hotspot_path="hotspots.json"):
        self.G = graph
        with open(hotspot_path) as f:
            self.hotspots = json.load(f)

        self.max_degree = max(dict(self.G.degree()).values())

    def crime_score(self, lat, lon):

        min_dist = float("inf")

        for h in self.hotspots:
            d = geodesic((lat, lon), (h["lat"], h["lon"])).meters
            min_dist = min(min_dist, d)

        return math.exp(-min_dist / 300)

    def road_type_score(self, highway):

        mapping = {
            "motorway": 0.1,
            "primary": 0.2,
            "secondary": 0.3,
            "residential": 0.6,
            "service": 0.8
        }

        if isinstance(highway, list):
            highway = highway[0]

        return mapping.get(highway, 0.5)

    def connectivity_score(self, u, v):

        degree_u = self.G.degree(u)
        degree_v = self.G.degree(v)

        return (degree_u + degree_v) / (2 * self.max_degree)

    def time_multiplier(self):

        hour = datetime.now().hour

        if 6 <= hour < 20:
            return 1.0
        elif 20 <= hour < 24:
            return 1.3
        return 1.6

    def compute_edge_risk(self, u, v, data):

        lat = (self.G.nodes[u]["y"] + self.G.nodes[v]["y"]) / 2
        lon = (self.G.nodes[u]["x"] + self.G.nodes[v]["x"]) / 2

        C = self.crime_score(lat, lon)
        R = self.road_type_score(data.get("highway", "residential"))
        D = self.connectivity_score(u, v)

        risk = (
            0.6 * C +
            0.3 * R +
            0.1 * (1 - D)
        )

        return risk * self.time_multiplier()
