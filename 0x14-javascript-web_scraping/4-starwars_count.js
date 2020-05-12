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
    for (const character of people) {
      if (character.includes('18')) { count++; }
    }
  }

  console.log(count);
});
