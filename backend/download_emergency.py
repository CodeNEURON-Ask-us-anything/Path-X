import osmnx as ox

place = "Vellore, Tamil Nadu, India"

police = ox.features_from_place(
    place,
    tags={"amenity": "police"}
)

hospitals = ox.features_from_place(
    place,
    tags={"amenity": "hospital"}
)

police.to_file("police.geojson", driver="GeoJSON")
hospitals.to_file("hospitals.geojson", driver="GeoJSON")

print("Emergency datasets saved!")
