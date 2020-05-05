#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.
if (process.argv.length < 4) {
  console.log(0);
} else if (process.argv.length > 3) {
  const av = process.argv;
  let biggest = Number(av[2]);
  let second = Number(av[3]);
  for (let i = 3; i <= av.length; i++) {
    if (Number(av[i]) > biggest) {
      second = biggest;
      biggest = Number(av[i]);
    } else if (Number(av[i]) > second) {
      second = Number(av[i]);
    }
  }
  console.log(second);
}
