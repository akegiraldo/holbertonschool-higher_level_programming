#!/usr/bin/node
// Script that prints a square.
if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let X = '';
  for (let i = 0; i < x; i++) {
    X += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(X);
  }
}
