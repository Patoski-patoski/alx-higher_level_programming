#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 *
 * Return: Nothing
 **/

const endPoint = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${endPoint}`;

if (process.argv.length !== 3) {
  console.error('Usage: file and second argument for endpoint', endPoint);
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).characters;
  for (const film of films) {
    request(film, (error, response, body) => {
      if (error) {
        console.eror(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
