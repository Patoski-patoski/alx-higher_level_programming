#!/usr/bin/node

/**
 * a script that imports an array and computes a new array
 *
 * Run ./100-maps.js
 **/

let myList = require('./100-data').list;

const multiply = (x, y) => x * y;
let newList;

for (let i = 0; i < myList.length; i++) {
  newList = myList.map(multiply, myList[i]);
}

console.log(myList);
console.log(newList);
