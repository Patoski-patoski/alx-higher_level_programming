#!/usr/bin/node
/**
 *  a script that reads and prints the content of a file
 *
 *  Return: Nothing
 */

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
