window.addEventListener('load', () => {
    let exitButton = document.querySelector('.exit_button');
    exitButton.addEventListener('click', (event) => {
        event.preventDefault();
        let cookies = document.cookie.split(";");

        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i];
            let eqPos = cookie.indexOf("=");
            let name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
        console.log('cookies are dead!');
        window.location = '/management';
    })
});