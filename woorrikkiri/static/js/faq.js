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
        const faq_content = document.querySelector("#faq_content_" + pk);
        faq_content.classList.toggle('display');
    }
};

if (delegation) {
    delegation.addEventListener('click', delegationFunc);
};

