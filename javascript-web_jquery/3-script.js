$(document).ready(function AddHeadertoRed() {

    const RedHeaderDiv = $('#red_header');

    RedHeaderDiv.click(function () {

        const header = $('header');

        header.addClass('red');
    });
});
