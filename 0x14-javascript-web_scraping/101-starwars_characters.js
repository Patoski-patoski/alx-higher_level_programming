#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie in the same order
 * of the list
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

function getCharacterNames (films, index = 0) {
  if (index >= films.length) {
    return;
  }

  request(films[index], (error, response, body) => {
    if (error) {
      console.error(error);
      getCharacterNames(films, index + 1);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);
    getCharacterNames(films, index + 1);
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).characters;
  getCharacterNames(films);
});
