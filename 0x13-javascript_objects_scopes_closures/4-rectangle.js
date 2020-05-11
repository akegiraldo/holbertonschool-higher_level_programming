#!/usr/bin/node
// Create an instance method called rotate() that exchanges the width and the height of the rectangle.
// Create an instance method called double() that multiples the width and the height of the rectangle by 2.
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let width = '';
    for (let i = 0; i < this.width; i++) {
      width += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
