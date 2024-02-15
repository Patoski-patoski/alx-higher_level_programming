#!/usr/bin/node

/**
 * Create an instance method called rotate() that exchanges the width and the
 * height of the rectangle
 *
 * Create an instance method called double() that multiples the width and the
 * height of the rectangle by 2
 *
 * Run: ./4-main.js
 **/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let temp = '';

    for (let i = 0; i < this.height; i++) {
      if (temp.length > 1) {
        temp += '\n';
      }
      for (let j = 0; j < this.width; j++) {
        temp += 'X';
      }
    }
    console.log(temp);
  }

  rotate () {
    const width = this.width;
    const height = this.height;

    this.width = height;
    this.height = width;
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
};
