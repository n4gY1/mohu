

var map = L.map('map').setView([46.43936366506428,19.485710116535913], 14);


function showPosition(position) {
    map.setView([position.coords.latitude, position.coords.longitude], 14);
}

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    x.innerHTML = "Geolocation is not supported by this browser.";
}

document.getElementById("gps").addEventListener("click", function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
});

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("Nincs engedélyezve a helymeghatározás a böngésző számára");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Helymeghatározás nem elérhetó");
            break;
        case error.TIMEOUT:
            alert("Helymeghatározás lekérése nem sikerült időhatáron belül");
            break;
        case error.UNKNOWN_ERROR:
            alert("Ismeretlen hiba történt");
            break;
    }
}

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);


function getCameraIcon(type) {
    return L.icon({
        iconUrl: `/static/img/${type}.png`,
        iconSize: [32, 32], // méret (szélesség, magasság) pixelben
        iconAnchor: [16, 32], // az ikon pozíciója (bal felső sarok)
        popupAnchor: [0, -32] // az ikonhoz kapcsolt popup pozíciója
    });
}



fetch('/reponts')
    .then(response => response.json())
    .then(data => {

        L.geoJSON(data, {
            pointToLayer: function (feature, latlng) {
                return L.marker(latlng, { icon: getCameraIcon(feature.properties.state) });
            },
            onEachFeature: function (feature, layer) {
                if (feature.properties.state && feature.properties.name) {
                    var popupContent = '<strong>' + feature.properties.name + '</strong>' + '<br>' +
                        '<i class="bi bi-clock w-100">' + feature.properties.last_report + '</i><br>' +
                        '<button class="btn w-100 my-3 btn-dark" onclick="window.location.href=\'/view/' + feature.properties.id + '\'">Bejelentés</button>'

                        ;
                    layer.bindPopup(popupContent);
                }
            }
        }).addTo(map);
    });

