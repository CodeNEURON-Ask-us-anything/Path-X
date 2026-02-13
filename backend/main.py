from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routing import nearest_node, fastest_route, safest_route, route_to_coordinates
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "PathX Backend Running", "version": "1.0"}

@app.get("/route")
def get_route(lat1: float, lon1: float, lat2: float, lon2: float, mode: str):
    try:
        source = nearest_node(lat1, lon1)
        target = nearest_node(lat2, lon2)
        
        if mode == "fast":
            path = fastest_route(source, target)
        else:
            path = safest_route(source, target)
        
        coords = route_to_coordinates(path)
        return {"mode": mode, "route": coords, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}

if __name__ == "__main__":
    print("🚀 Starting PathX Backend Server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)