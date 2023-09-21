$(document).ready(function toggleHeader() {
    const tHeader = $('#toggle_header');

    tHeader.click(function () {

        const header = $('header');

        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else if (header.hasClass('green')) {
            header.removeClass('green').addClass('red');
        }

    });
});
