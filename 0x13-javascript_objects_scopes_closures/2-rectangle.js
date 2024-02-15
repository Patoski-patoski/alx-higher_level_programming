#!/usr/bin/node

/**
 * a class Rectangle that defines a rectangle:
 *
 * Run: ./2-main.js/2-rectangle.js
 **/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
