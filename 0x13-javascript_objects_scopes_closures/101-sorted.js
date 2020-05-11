#!/usr/bin/node
// Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;

function sortByOccurrences (obj) {
  const dict = {};
  for (const key in obj) {
    dict[obj[key]] = [];
  }
  for (const key in obj) {
    dict[obj[key]].push(key);
  }
  return dict;
}

console.log(sortByOccurrences(dict));
