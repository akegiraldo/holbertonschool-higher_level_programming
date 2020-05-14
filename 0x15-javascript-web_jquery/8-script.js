// Script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json.
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const movies = data.results;
  for (const movie of movies) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
