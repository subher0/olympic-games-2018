function initMap() {
    var uluru = {lat: 42.987002, lng: 47.473353};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: uluru,
        mapTypeId: 'roadmap'
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}