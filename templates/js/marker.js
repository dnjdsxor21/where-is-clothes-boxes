

$('#submit').on('click', function(e) {
    const sd = document.getElementById('sido');
    const gd = document.getElementById('gudong');
    console.log(`${sd.value} ${gd.value}`)
    if(sd.value=='서울시' || gd.value=='성동구'){
        //searchAddressToCoordinate('성동구', is_center=true);
        fetchData('/seongdong-gu');
    }
        
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

function markData(data) {
    // const dataContainer = document.getElementById('data-container');
    // dataContainer.innerHTML = `<p>Data: ${JSON.stringify(data)}</p>`;
    data.forEach(item =>{
        searchAddressToCoordinate(item['설치장소'], is_center=false)
    });
}

