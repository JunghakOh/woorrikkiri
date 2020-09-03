// signup - select //
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "gender_select": */
x = document.getElementsByClassName("gender_select");
l = x.length;
for (i = 0; i < l; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    ll = selElmnt.length;
    /* For each element, create a new DIV that will act as the selected item: */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x[i].appendChild(a);
    /* For each element, create a new DIV that will contain the option list: */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 1; j < ll; j++) {
        /* For each option in the original select element,
        create a new DIV that will act as an option item: */
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function (e) {
            /* When an item is clicked, update the original select box,
            and the selected item: */
            var y, i, k, s, h, sl, yl;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            sl = s.length;
            h = this.parentNode.previousSibling;
            for (i = 0; i < sl; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    yl = y.length;
                    for (k = 0; k < yl; k++) {
                        y[k].removeAttribute("class");
                    }
                    this.setAttribute("class", "same-as-selected");
                    break;
                }
            }
            h.click();
        });
        b.appendChild(c);
    }
    x[i].appendChild(b);
    a.addEventListener("click", function (e) {
        /* When the select box is clicked, close any other select boxes,
        and open/close the current select box: */
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
    });
}

function closeAllSelect(elmnt) {
    /* A function that will close all select boxes in the document,
    except the current select box: */
    var x, y, i, xl, yl, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");
    xl = x.length;
    yl = y.length;
    for (i = 0; i < yl; i++) {
        if (elmnt == y[i]) {
            arrNo.push(i)
        } else {
            y[i].classList.remove("select-arrow-active");
        }
    }
    for (i = 0; i < xl; i++) {
        if (arrNo.indexOf(i)) {
            x[i].classList.add("select-hide");
        }
    }
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);


// vertical navbar //
const ham = document.querySelector('.ham_container');
const ver_cate = document.querySelector('.ver_category_box');
const blind = document.querySelector('.blind');

ham.addEventListener('click', function () {
    ver_cate.classList.toggle('display');
    blind.classList.toggle('display');
});

window.onload = function () {
    window.addEventListener('resize', function () {
        ver_cate.classList.remove('display');
        blind.classList.remove('display');
    });
}


// payment //
window.onload=function(){
var money_amount = document.querySelector("#money_amount");
const plus_5000 = document.querySelector("#plus_5000");
const x_btn = document.querySelector("#x_btn");


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
    x_btn.addEventListener('click', function () {
        money_amount.innerHTML = "0";
    });
    
}



// faq //
const delegation = document.querySelector('.faq_box');

function delegationFunc(e) {
    let elem = e.target;
    while (!elem.getAttribute('data-name')) {
        elem = elem.addEventListener

        if (elem.nodeName === 'BODY') {
            elem = null
            return;
        };
    };
    if (elem.matches('[data-name="faq_title"]')) {
        var pk = elem.getAttribute('name');
        const faq_content = document.querySelector("#faq_content_"+pk);
        faq_content.classList.toggle('display');
    }
};

delegation.addEventListener('click', delegationFunc);
