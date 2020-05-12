#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(`${url}${id}`, function (err, response, body) {
  if (err) { console.log(err); return; }
  if (JSON.parse(body).title !== undefined) { console.log(JSON.parse(body).title); } else { console.log(JSON.parse(body)); }
});
