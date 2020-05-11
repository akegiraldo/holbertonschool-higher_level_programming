#!/usr/bin/node
// Instance method called charPrint(c) that prints the rectangle using the character c.
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let width = '';
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.width; i++) {
      width += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }
}
module.exports = Square;
