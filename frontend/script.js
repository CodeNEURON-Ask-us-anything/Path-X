
var map = L.map('map').setView([12.9716, 77.5946], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'OpenStreetMap'
}).addTo(map);

var safeRoute, unsafeRoute, marker;

function showRoutes() {

    if (safeRoute) {
        map.removeLayer(safeRoute);
        map.removeLayer(unsafeRoute);
    }

    // Unsafe route
    unsafeRoute = L.polyline([
        [12.9716, 77.5946],
        [12.968, 77.590]
    ], {color: 'red', weight: 6}).addTo(map);

    // Safe route
    safeRoute = L.polyline([
        [12.9716, 77.5946],
        [12.974, 77.600]
    ], {color: 'green', weight: 6}).addTo(map);

    // Heat zone
    L.circle([12.968, 77.590], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 250
    }).addTo(map);
}

function activateSafe() {
    document.getElementById("badge").style.display = "block";

    if (marker) {
        map.removeLayer(marker);
    }

    marker = L.marker([12.974, 77.600]).addTo(map)
        .bindPopup("You are on the safest route")
        .openPopup();
}

function triggerSOS() {
    document.getElementById("popup").style.display = "block";

    if (marker) {
        marker.setLatLng([12.973, 77.602]);
    }
}

