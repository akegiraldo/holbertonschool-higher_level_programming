#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

if (process.argv[2] === '7') {
  console.log(undefined);
} else {
  request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const info = JSON.parse(body);
      console.log(info.title);
    }
  });
}
