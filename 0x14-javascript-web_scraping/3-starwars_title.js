#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request (`${url}${id}`, function (err, response, body) {
  if (err) { console.log(err); return; }
  console.log(JSON.parse(body).title);
});
