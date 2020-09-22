const money_amount = document.querySelector("#money_amount");
const plus_5000 = document.querySelector("#plus_5000");
const money_x_btn = document.querySelector("#x_btn");

var money = money_amount.nodeValue;

plus_5000.addEventListener('click', function () {
    money += 5000;
    money_amount.value = money;
});
money_x_btn.addEventListener('click', function () {
    money_amount.value = 0;
});
