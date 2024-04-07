const sidoSelect = document.getElementById('sido');
// 두 번째 select 요소
const gudongSelect = document.getElementById('gudong');

refreshBtn();
// sidoSelect 변경 이벤트 리스너 추가
sidoSelect.addEventListener('change', function(e) {
    refreshBtn();
});

function refreshBtn() {
    // 선택된 값 가져오기
    const selectedValue = sidoSelect.value;

    // 두 번째 select 요소 업데이트
    if (selectedValue == '서울시') {
        // '서울시'가 선택된 경우
        gudongSelect.innerHTML = `
        <option value="동작구>동작구</option>
        <option value="서대문구">서대문구</option>
        <option value="성동구">성동구</option>
        <option value="성북구">성북구</option>
        `;
        //gudongSelect.innerHTML = '냐ㅠㅁ'
    } else if (selectedValue == '경기도') {
        // '경기도'가 선택된 경우
        gudongSelect.innerHTML = `
            <option value="수원시">수원시</option>
            <option value="성남시">성남시</option>
        `;
    } else {
        // 다른 값이 선택된 경우
        gudongSelect.innerHTML = ''; // 두 번째 select 요소 비우기
    }
};