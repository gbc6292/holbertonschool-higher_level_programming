$(document).ready(function () {
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    $.ajax({
        url: apiUrl,
        type: 'GET',
        dataType: 'json',
        success: function (data) {

            const charName = data.name;

            const charDiv = $('#character');

            charDiv.text(charName);


        }
    });
});
