$(document).ready(function headerRed() {

    const redHeaderDiv = $('#red_header');

    redHeaderDiv.click(function () {

        const header = $('header');

        header.css('color', '#FF0000');
    });
});
