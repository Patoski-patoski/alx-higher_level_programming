#!/usr/bin/node
/**
 *  a script that prints the title of a Star Wars movie where the episode
 *  number matches a given integer.
 *
 *  Return nothing
 * */

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: file and second argument for link', process.argv[2]);
  process.exit(1);
}
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const newBody = (JSON.parse(body));
  console.log(newBody.title);
});
