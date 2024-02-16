#!/usr/bin/node

/**
 * a function that converts a number from base 10 to another base passed as
 * argument
 *
 * Run ./10-main.js
 **/

exports.converter = function (base) {
  return function (number) {
    return number.toString(base)
  }
}
