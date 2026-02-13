import osmnx as ox

place = "Vellore, Tamil Nadu, India"

lights = ox.features_from_place(
    place,
    tags={"highway": "street_lamp"}
)

lights.to_file("lights.geojson", driver="GeoJSON")

print("Streetlights saved as lights.geojson")
