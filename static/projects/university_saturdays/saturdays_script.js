window.addEventListener('load', () => {
    reg_buttons.forEach((item) => {
        item.addEventListener('click', (event) => {
            reg_window.setAttribute('class', 'registration-form-wrapper');
            document.getElementById('eventId').setAttribute('value', item.id);
        })
    });
});