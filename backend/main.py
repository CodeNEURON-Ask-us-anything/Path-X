from fastapi import FastAPI
from routing import (
    nearest_node,
    fastest_route,
    safest_route,
    route_to_coordinates
)
import networkx as nx

app = FastAPI()


@app.get("/route")
def get_route(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    mode: str = "fast"
):
    try:
        # Find nearest nodes
        source = nearest_node(lat1, lon1)
        target = nearest_node(lat2, lon2)

        # Choose routing mode
        if mode.lower() == "safe":
            path = safest_route(source, target)
        elif mode.lower() == "fast":
            path = fastest_route(source, target)
        else:
            return {"error": "Invalid mode. Use 'fast' or 'safe'."}

        # Convert route to coordinates
        route_coords = route_to_coordinates(path)

        return {
            "mode": mode,
            "route": route_coords
        }

    except nx.NetworkXNoPath:
        return {"error": "No path found between the selected locations."}

    except Exception as e:
        return {"error": str(e)}
