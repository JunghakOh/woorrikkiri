var coffee_count = document.querySelector("#coffee_count");
var point_count = document.querySelector("#point_count");
var left_point = document.querySelector('#left_point');
const plus_btn = document.querySelector('#plus');
const minus_btn = document.querySelector('#minus');

var c_count = parseFloat(coffee_count.innerText);
var p_count = parseFloat(point_count.innerText);
var lp = parseFloat(left_point.innerText);

plus_btn.addEventListener('click', function () {
    c_count += 1;
    p_count += 2900;
    lp -= 2900;
    if (lp < 0){
        alert('포인트가 부족합니다.');
    } else{
        coffee_count.innerHTML = c_count;
        point_count.innerHTML = p_count;
        left_point.innerHTML = lp;    
    }
});
minus_btn.addEventListener('click', function () {
    if (c_count === 1) {
        alert('최소 1잔은 선택해야 합니다.');
    } else {
        c_count -= 1;
        p_count -= 2900;
        lp +=2900;
        coffee_count.innerHTML = c_count;
        point_count.innerHTML = p_count;
        left_point.innerHTML = lp;
    }
});
