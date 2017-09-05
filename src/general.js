$('#modal-content').on('shown.bs.modal', function () {
    $("body.modal-open").removeAttr("style");
});

let lastWindowPosition = window.pageYOffset;
let navbar = null;
let navtop = 0;
let navbarElements = null;
let dropdown = null;

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

window.addEventListener('load', () => {
    navbar = document.querySelector('.navbar');
    navbarElements = $('#navbarElements');
    dropdown = $('.dropdown>.dropdown');
    let feedback_button = document.querySelector('.feedback-button');
    let feedback_close_button = document.querySelector('.feedback-close-button');
    let feedback_window = document.querySelector('.feedback-wrapper');
    let send_feedback_button = document.getElementById('send_feedback');
    feedback_button.addEventListener('click', (event) => {
        feedback_window.setAttribute('class', 'feedback-wrapper');
    });

    feedback_close_button.addEventListener('click', (event) => {
        event.preventDefault();
        feedback_window.setAttribute('class', 'feedback-wrapper hidden');
    });

    send_feedback_button.addEventListener('click', (event) => {
        event.preventDefault();
        feedback_window.setAttribute('class', 'feedback-wrapper hidden');
        let request = new XMLHttpRequest();
        let response = new Promise((resolve, reject) => {
            request.open('POST', '/feedback', true);
            request.onload = function () {
                if (this.status >= 200 && this.status < 300) {
                    resolve(request.response);
                } else {
                    reject(request.response);
                }
            };
            request.onError = function () {
                reject(request.response);
            };
            let email = document.getElementById('feedback_email').value;
            let message = document.getElementById('feedback_message').value;
            if (message.length < 10) {
                alert('Опишите, пожалуйста, проблему');
                reject();
                return;
            }
            let payload = {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                email: email,
                message: message,
            };
            request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
            request.send(JSON.stringify(payload));
            alert('Спасибо за отзыв!');
        });
        response.then((response) => {
            console.log(response);
        }).catch((response) => {
            console.log(response);
        });
    })
})
;

window.addEventListener('scroll', (event) => {
    if (navbarElements.hasClass('collapsing') || dropdown.hasClass('show')) {
        lastWindowPosition = window.pageYOffset;
        navbar.setAttribute('style', `top: 0`);
        return;
    }

    let coordDifference = lastWindowPosition - window.pageYOffset;
    if (coordDifference < 0 && navbar.offsetHeight > -navtop) {
        navtop += coordDifference;
    } else if (coordDifference > 0 && navtop < 0) {
        navtop += coordDifference
    }
    if (navtop > 0) {
        navtop = 0;
    }
    navbar.setAttribute('style', `top: ${navtop}`);
    lastWindowPosition = window.pageYOffset;
});