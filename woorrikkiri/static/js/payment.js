const money_amount = document.querySelector("#money_amount");
const plus_5000 = document.querySelector("#plus_5000");
const money_x_btn = document.querySelector("#x_btn");
const user = document.querySelector('#user').innerHTML;
const bank_input = document.querySelector('#bank');
const account_input = document.querySelector('#account');

var money = money_amount.nodeValue;

plus_5000.addEventListener('click', function () {
    money += 5000;
    money_amount.value = money;
});
money_x_btn.addEventListener('click', function () {
    money_amount.value = 0;
    money = 0;
});


// 제출전 금액 확인
function check(){ 
    var bank =  bank_input.nodeValue;
    var account = account_input.nodeValue;
    console.log(bank);

    if (!money){
        alert('금액을 선택해주세요.');
        return false;
    }
    if (user === 'mentor'){
        console.log('은행');
        conosole.loge(bank);
        if (!bank){
            alert('은행을 입력해주세요.');
            return false;
        } else if(!account){
            alert('계좌번호를 입력해주세요.');
            return false;
        }
    }
    return false;
}