#!/usr/bin/node
// Script that concats 2 files.

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', function (err, data) {
  if (err) throw err;
  fs.writeFile(fileC, data, function (err) {
    if (err) throw err;
  });
});

fs.readFile(fileB, 'utf8', function (err, data) {
  if (err) throw err;
  fs.appendFile(fileC, data, function (err) {
    if (err) throw err;
  });
});
