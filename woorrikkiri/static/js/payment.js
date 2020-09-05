// payment //
var money_amount = document.querySelector("#money_amount");
const plus_5000 = document.querySelector("#plus_5000");
const money_x_btn = document.querySelector("#x_btn");

// payment //
plus_5000.addEventListener('click', function () {
    let money = parseFloat(money_amount.innerText);
    money += 5;
    if (money > 1000) {
        alert("금액이 너무 큽니다.");
        money_amount.innerHTML = "0";
    } else {
        money_amount.innerHTML = money + ",000";
    }
});
money_x_btn.addEventListener('click', function () {
    money_amount.innerHTML = "0";
});
