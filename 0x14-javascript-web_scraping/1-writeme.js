#!/usr/bin/node
/**
 *  a script that writes a string to a file.
 *
 * Return nothing
 **/

const fs = require('fs');

const writeup = process.argv[3];
const filepath = process.argv[2];

fs.writeFile(filepath, writeup, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
