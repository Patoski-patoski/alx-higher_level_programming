#!/usr/bin/node
/**
 * a script that gets the contents of a webpage and stores it in a file.
 *
 * Return nothing
 * */

const url = process.argv[2];
const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];

if (process.argv.length === 21) {
  console.error('Usage: file and second argument for link', process.argv[2]);
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
