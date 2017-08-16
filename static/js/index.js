$('.project-slider').slick({
    dots: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    arrows: false
});

window.onload = () => {
    let ring4 = document.querySelector('.ring-4');
    let ring5 = document.querySelector('.ring-5');
    let id4 = 0;
    let id5 = 0;

    ring4.addEventListener('mouseleave', () => {
        clearTimeout(id4);
        id4 = setTimeout(() => {
            ring4.setAttribute('style', 'z-index: 0')
        }, 200);
    });

    ring4.addEventListener('mouseover', () => {
        clearTimeout(id4);
        ring4.setAttribute('style', 'z-index: 1')
    });

    ring5.addEventListener('mouseleave', () => {
        clearTimeout(id5);
        id5 = setTimeout(() => {
            ring5.setAttribute('style', 'z-index: 0')
        }, 200);
    });

    ring5.addEventListener('mouseover', () => {
        clearTimeout(id5);
        ring5.setAttribute('style', 'z-index: 1');
    });
};
