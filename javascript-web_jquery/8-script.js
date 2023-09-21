$(document).ready(function () {

    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

    $.ajax({
        url: apiUrl,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            const movies = data.results;
            const movieList = $('#list_movies');

            $.each(movies, function (index, movie) {
                liItem = $('<li>').text(movie.title);

                movieList.append(liItem);
            });
        }
    });
});

