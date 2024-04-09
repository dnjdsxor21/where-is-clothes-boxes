$('#submit').on('click', function(e) {
    const sd = document.getElementById('si');
    const gd = document.getElementById('do');
    //console.log(`${sd.value} ${gd.value}`);
    const url = `/map/${sd.value}-${gd.value}`;
    fetchData(url);
}
);

async function fetchData(endpoint) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            markData(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

async function markData(data){
    console.log(data);
    var map = new naver.maps.Map(mapDiv, {
        center: new naver.maps.LatLng(data[0]['lat'], data[0]['lon']),
        zoom: 15,
        minZoom: 7,
        zoomControl: true,
        zoomControlOptions: {
            position: naver.maps.Position.TOP_RIGHT
        }
    });

    data.forEach(item=>{
        var marker = new naver.maps.Marker({
            position: new naver.maps.LatLng(item['lat'], item['lon']),
            map: map
        });
    })
}


