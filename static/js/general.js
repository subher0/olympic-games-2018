$('#modal-content').on('shown.bs.modal', function() {
       $("body.modal-open").removeAttr("style");
 });

let lastWindowPosition = window.pageYOffset;
let navbar = null;
let navtop= 0;

window.addEventListener('load', () => {
    navbar = document.querySelector('.navbar');
});

window.addEventListener('scroll', (event) => {
    let coordDifference = lastWindowPosition - window.pageYOffset;
    if (coordDifference < 0 && navbar.offsetHeight > -navtop) {
        navtop+= coordDifference;
    } else if (coordDifference > 0 && navtop < 0) {
        navtop+= coordDifference
    }
    if (navtop > 0) {
        navtop = 0;
    }
    navbar.setAttribute('style', `top: ${navtop}`);
    lastWindowPosition = window.pageYOffset;
});