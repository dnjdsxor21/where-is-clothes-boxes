var mapDiv = document.getElementById('map'); // 'map'으로 선언해도 동일
var mapOptions = {
    center: new naver.maps.LatLng(37.3595704, 127.105399),
    zoom: 15,
    minZoom: 7,
    zoomControl: true,
    zoomControlOptions: {
        position: naver.maps.Position.TOP_RIGHT
    }
};
var map = new naver.maps.Map(mapDiv, mapOptions);

var marker = new naver.maps.Marker({
    position: new naver.maps.LatLng(37.3595704, 127.105399),
    map: map
});