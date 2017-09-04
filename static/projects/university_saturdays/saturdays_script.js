window.addEventListener('load', () => {
    let reg_buttons = document.querySelectorAll('.reg-button');
    let reg_window = document.querySelector('.registration-form-wrapper');
    let close_button = document.querySelector('.close-button');
    close_button.addEventListener('click', (event) => {
        event.preventDefault();
        reg_window.setAttribute('class', 'registration-form-wrapper hidden');
    });

    reg_buttons.forEach((item) => {
        item.addEventListener('click', (event) => {
            reg_window.setAttribute('class', 'registration-form-wrapper');
            document.getElementById('eventId').setAttribute('value', item.id);
        })
    });
});