#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movId}/`;
let characters = [];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  getCharacters(0);
});

const getCharacters = (idx) => {
  if (idx === characters.length) {
    return;
  }

  request(characters[idx], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(idx + 1);
  });
};
