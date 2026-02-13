import osmnx as ox
import geopandas as gpd

place = "Vellore, Tamil Nadu, India"

tags = {"amenity": "fuel"}

fuel = ox.features_from_place(place, tags)

fuel.to_file("petrol.geojson", driver="GeoJSON")

print("Petrol bunks downloaded successfully!")
