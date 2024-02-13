#!/usr/bin/node

// a script that prints a square

const size = process.argv[2];
let temp = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    if (temp.length > 1) {
      temp += '\n';
    }
    for (let j = 0; j < size; j++) {
      temp += 'X';
    }
  }
  console.log(temp);
}
