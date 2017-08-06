function initMap() {
    var uluru = {lat: 41.753551, lng: 47.933762};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: uluru,
        mapTypeId: 'roadmap'
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}