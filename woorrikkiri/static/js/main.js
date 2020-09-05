// vertical navbar //
const ham = document.querySelector('.ham_container');
const ver_cate = document.querySelector('.ver_category_box');
const blind = document.querySelector('.blind');


// vertical navbar //
ham.addEventListener('click', function () {
    ver_cate.classList.toggle('display');
    blind.classList.toggle('display');
    x_btn.classList.toggle('display');
    ham.classList.toggle('display');
});

x_btn.addEventListener('click', function () {

window.addEventListener('resize', function () {
    ver_cate.classList.remove('display');
    blind.classList.remove('display');
    ham.classList.remove('display');
    x_btn.classList.remove('display');
});


