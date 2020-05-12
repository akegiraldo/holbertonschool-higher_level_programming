#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, function (err, response, body) {
  if (err) { console.log(err); return; }

  const characters = JSON.parse(body).characters;

  for (const people of characters) {
    request(people, function (err, response, body) {
      if (err) { console.log(err); return; }
      const character = JSON.parse(body).name;
      console.log(character);
    });
  }
});
