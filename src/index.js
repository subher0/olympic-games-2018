window.addEventListener('load', () => {
    preventOverlapping();
    hoverOnMobiles();
    $('.project-slider').slick({
        dots: true,
        slidesToShow: screen.width < 1000 ? screen.width > 600 ? 3 : 2 : 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false
    });
});

function preventOverlapping() {
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
}

function hoverOnMobiles() {
    let circles = document.querySelectorAll('.olymp-circle');
    let clickedId;
    let prevClickedId = '';
    if (screen.width < 992) {
        for (let i = 0; i < circles.length; i++) {
            circles[i].addEventListener('click', (event) => {
                event.stopPropagation();
                clickedId = circles[i].getAttribute('class');
                if (clickedId === prevClickedId) {
                    window.location = circles[i].getAttribute('href');
                } else {
                    prevClickedId = clickedId;
                }
            });
        }
    } else {
        for (let i = 0; i < circles.length; i++) {
            circles[i].addEventListener('click', (event) => {
                window.location = circles[i].getAttribute('href');
            });
        }
    }

    window.addEventListener('click', () => prevClickedId = '');
}