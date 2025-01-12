
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            lat = position.coords.latitude;
            lon = position.coords.longitude;

            showPosition(position);
        },
        (error) => {
            setIcon(46.42906218136214,19.481412719705105);
            alert("Nincs engedélyezve a böngésző számára a helymeghatározás");
        }
    );
} else {
    setIcon(46.42906218136214,19.481412719705105);
    alert("Nincs engedélyezve a böngésző számára a helymeghatározás");
}




function showPosition(position) {
    if (position.coords.latitude != null) {
        console.log("show position");
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        setIcon(lat,lon);
    }


}

function get_current_position() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
        console.log("current position is valid");

    }
}



function setIcon(lat,lon) {

    var map = L.map('map').setView([lat,lon], 17);
    console.log('seticon' + " " + lat + " " + lon);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
    }).addTo(map);

    var cameraIcon = L.icon({
        iconUrl: '/static/img/3.png',
        iconSize: [32, 32], // méret (szélesség, magasság) pixelben
        iconAnchor: [16, 32], // az ikon pozíciója (bal felső sarok)
        popupAnchor: [0, -32] // az ikonhoz kapcsolt popup pozíciója
    });
    console.log("seticon");

    var marker = L.marker(
        [lat, lon],
        { icon: cameraIcon,draggable: true })
            .addTo(map);

    marker.on('dragend', function(event) {
            var marker = event.target;
            var position = marker.getLatLng();
            marker.setLatLng(new L.LatLng(position.lat,position.lng), { draggable: 'true' }).bindPopup(position).update();
            document.getElementById("lat").value = position.lat.toFixed(6);
            document.getElementById("lon").value = position.lng.toFixed(6);
    });
}

