window.addEventListener('load', () => {
    $('.rangePicker').daterangepicker({
        "locale": {
            "format": "DD/MM/YYYY",
            "separator": " - ",
            "applyLabel": "Применить",
            "cancelLabel": "Закрыть",
            "fromLabel": "От",
            "toLabel": "До",
            "customRangeLabel": "Свой",
            "weekLabel": "Нд",
            "daysOfWeek": [
                "Пн",
                "Вт",
                "Ср",
                "Чт",
                "Пт",
                "Сб",
                "Вс"
            ],
            "monthNames": [
                "Январь",
                "Февраль",
                "Март",
                "Апрель",
                "Май",
                "Июнь",
                "Июль",
                "Август",
                "Сентябрь",
                "Октябрь",
                "Ноябрь",
                "Декабрь"
            ],
            "firstDay": 1
        },
    }, function (start, end, label) {
        console.log("New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')");
    });

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