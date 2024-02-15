#!/usr/bin/node

/**
 * a class Square that defines a square and inherits from Square of
 * 5-square.js:
 *
 * Run: ./6-main.js
 *
 **/

const s1 = require('./5-square');

class Square extends s1 {
  charPrint (c) {
    if (c === undefined) {
      let temp = '';

      for (let i = 0; i < this.height; i++) {
        if (temp.length >= 1) {
          temp += '\n';
        }
        for (let j = 0; j < this.width; j++) {
          temp += 'X';
        }
      }
      console.log(temp);
    } else {
      let temp = '';

      for (let i = 0; i < this.height; i++) {
        if (temp.length >= 1) {
          temp += '\n';
        }
        for (let j = 0; j < this.width; j++) {
          temp += 'C';
        }
      }
      console.log(temp);
    }
  }
}
module.exports = Square;
