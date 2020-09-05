var coffee_count = document.querySelector("#coffee_count");
var point_count = document.querySelector("#point_count");
const plus_btn = document.querySelector('#plus');
const minus_btn = document.querySelector('#minus');

plus_btn.addEventListener('click', function () {
    var c_count = parseFloat(coffee_count.innerText);
    var p_count = parseFloat(point_count.innerText);

    c_count += 1;
    p_count += 2900;
    coffee_count.innerHTML = c_count;
    point_count.innerHTML = p_count;
});
minus_btn.addEventListener('click', function () {
    var c_count = parseFloat(coffee_count.innerText);
    var p_count = parseFloat(point_count.innerText);

    if (c_count === 0) {
        alert('0잔 이하를 선택할 수 없습니다.');
    } else {
        c_count -= 1;
        p_count -= 2900;
        coffee_count.innerHTML = c_count;
        point_count.innerHTML = p_count;
    }
});
