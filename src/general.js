$('#modal-content').on('shown.bs.modal', function() {
       $("body.modal-open").removeAttr("style");
 });

let lastWindowPosition = window.pageYOffset;
let navbar = null;
let navtop= 0;
let navbarElements = null;
let dropdown = null;

window.addEventListener('load', () => {
    navbar = document.querySelector('.navbar');
    navbarElements = $('#navbarElements');
    dropdown = $('.dropdown>.dropdown')
});

window.addEventListener('scroll', (event) => {
    if (navbarElements.hasClass('collapsing') || dropdown.hasClass('show')) {
        lastWindowPosition = window.pageYOffset;
        navbar.setAttribute('style', `top: 0`);
        return;
    }

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