#!/usr/bin/node
/**
 * a script that display the status code of a GET request.
 *
 *  Return nothing
 * */

const url = process.argv[2];
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: file and second argument for link', process.argv[1]);
  process.exit(1);
}
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
