const siSelect = document.getElementById('si');
const doSelect = document.getElementById('do');
const metaData = JSON.parse(JSON.stringify(metaFile));
const metaDataKey = Object.keys(metaData);
refreshBtn();
// sidoSelect 변경 이벤트 리스너 추가
siSelect.addEventListener('change', function(e) {
    refreshBtn();
});

function refreshBtn() {

    
    const selectedValue = siSelect.value;
    let names=['---'];
    for(let i=0; i<metaDataKey.length; i++){
        key = metaDataKey[i];

        if(key.includes(selectedValue)){
            names = metaData[key].sort();
            break;
        }
    }
    let tag = "";
    for (let i=0; i<names.length; i++){
        tag += `<option value="${names[i]}">${names[i]}</option>`
    }
    doSelect.innerHTML = tag;
};