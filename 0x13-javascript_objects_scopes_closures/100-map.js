#!/usr/bin/node

/**
 * a script that imports an array and computes a new array
 *
 * Run ./100-maps.js
 **/

const myList = require('./100-data').list;
const newList = myList.map((number, index) => number * index);

console.log(myList);
console.log(newList);
