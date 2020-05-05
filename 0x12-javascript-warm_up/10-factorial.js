#!/usr/bin/node
// Script that computes and prints a factorial.
if (Number.isNaN(Number(process.argv[2]))) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}

function factorial (n) {
  if (n > 1) {
    return (n * factorial(n - 1));
  }
  return 1;
}
