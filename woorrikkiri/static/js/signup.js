var pass1 = document.querySelector('#id_password1');
var pass2 = document.querySelector('#id_password2');


const container = document.querySelector('#id_name');
const button = document.querySelector('#button');

// 비밀번호 일치 확인
pass2.addEventListener('change', function(){
    if (pass1.value != pass2.value){
        alert('비밀번호가 일치하지 않습니다.');
        pass1.value = '';
        pass2.value = '';
    }
    
})