from fastapi import FastAPI
from routing import (
    nearest_node,
    fastest_route,
    safest_route,
    route_to_coordinates
)

app = FastAPI()

@app.get("/route")
def get_route(lat1: float, lon1: float,
              lat2: float, lon2: float,
              mode: str = "safe"):

    source = nearest_node(lat1, lon1)
    target = nearest_node(lat2, lon2)

    if mode == "fast":
        route = fastest_route(source, target)
    else:
        route = safest_route(source, target)

    coords = route_to_coordinates(route)

    return {
        "mode": mode,
        "points": coords
    }
