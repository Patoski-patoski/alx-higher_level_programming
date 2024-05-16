#!/usr/bin/node
/**
 *  a script that prints the number of movies where the character
 *  “Wedge Antilles” is present.
 *
 * Return: Nothing
 **/

const request = require('request');
const arg = process.argv[2];

request(arg, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) { count += 1; }
    }
  }
  console.log(count);
});
