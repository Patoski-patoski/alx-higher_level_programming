#!/usr/bin/node

/**
 * a function that prints the number of arguments already printed and the new
 * argument value.
 *
 * Run: ./9-main.js
 **/


let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter++}: ${item}`);
}
