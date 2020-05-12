#!/usr/bin/node
// Script that prints all characters of a Star Wars movie in the same order of the list “characters” in the /films/ response.

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, function (err, response, body) {
  if (err) { console.log(err); return; }

  const characters = JSON.parse(body).characters;
  const i = characters.entries();
  for (const e of i) {
    request(e[1], function (err, response, body) {
      if (err) { console.log(err); return; }
      const character = JSON.parse(body).name;
      console.log(character);
    });
  }

  /* for (const character of characters) {
    request(character, function (err, response, body) {
      if (err) { console.log(err); return; }
      const character = JSON.parse(body).name;
      console.log(character);
    });
  } */
});
