var coffee = document.querySelector("#coffee_count");
var point = document.querySelector("#point_count");
var left_point = document.querySelector('#left_point');
const plus_btn = document.querySelector('#plus');
const minus_btn = document.querySelector('#minus');
const ask_btn = document.querySelector('#ask_btn');

// var c_count = parseFloat(coffee.innerText);
var c_count = coffee.nodeValue;
var p_count = point.nodeValue;
var lp = parseFloat(left_point.innerText);

plus_btn.addEventListener('click', function () {
    if (lp-2900 < 0){
        alert('포인트가 부족합니다.');
    } else{
        c_count += 1;
        p_count += 2900;
        lp -= 2900;
        coffee.value = c_count;
        point.value = p_count;
        left_point.innerHTML = lp;    
    }
});
minus_btn.addEventListener('click', function () {
    if (c_count <= 1) {
        alert('커피는 최소 1잔 선택해야 합니다.');
    } else {
        c_count -= 1;
        p_count -= 2900;
        lp +=2900;
        coffee.value = c_count;
        point.value = p_count;
        left_point.innerHTML = lp;
    }
});

// 제출전 커피 선택여부 확인
function check(){ 
    console.log(c_count);
    if (!c_count){
        alert('커피는 최소 1잔 선택해야 합니다.');
        return false;
    }else {
        return true;
    }
}