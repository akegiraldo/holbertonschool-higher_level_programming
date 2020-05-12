#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) { console.log(err); return; }

  const movies = JSON.parse(body).results;
  let count = 0;

  for (const movie of movies) {
    const people = movie.characters;
    if (people.includes('https://swapi-api.hbtn.io/api/people/18/')) { count++; }
  }

  console.log(count);
});
