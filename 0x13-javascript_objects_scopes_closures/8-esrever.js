#!/usr/bin/node
// Function that returns the reversed version of a list.
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) { newList[j] = list[i]; }
  return newList;
};
