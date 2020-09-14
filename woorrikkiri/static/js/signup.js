var pass1 = document.querySelector('#id_password1');
var pass2 = document.querySelector('#id_password2');

const button = document.querySelector('#button');

button.addEventListener('click', function(){
    if (pass1 != pass2){
        alert('비밀번호가 일치하지 않습니다.');
    }
    
})