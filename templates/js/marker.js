

$('#submit').on('click', function(e) {
    const sd = document.getElementById('sido');
    const gd = document.getElementById('gudong');
    //console.log(`${sd.value} ${gd.value}`);
    if(sd.value=='서울시' || gd.value=='성동구'){
        fetchData('/seongdong-gu');
    } else if (sd.value=='서울시' || gd.value=='서대문구'){
        fetchData('/seongdong-gu');
    }
    else if (sd.value=='서울시' || gd.value=='동작구'){
        fetchData('/dongjak-gu');
    }
    else if (sd.value=='서울시' || gd.value=='성북구'){
        fetchData('/seongbuk-gu');
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
    data.forEach(item => {
        for (const key in item) {
            if (Object.prototype.hasOwnProperty.call(item, key)) {
                if (key.includes('설치장소') || key.includes('위치') || key.includes('주소')) {
                    searchAddressToCoordinate(item[key], is_center=false);
                    break;
                }
            }
        }
    });
    
}

