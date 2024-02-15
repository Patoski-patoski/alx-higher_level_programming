#!/usr/bin/node

/**
 * a class Rectangle that defines a rectangle:
 *
 * Run: ./3-main.js/3-rectangle.js
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
};
