#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/';
let movid = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const res = JSON.parse(body);
    const results = res.results;
    if (id < 4) {
      movid += 3;
    } else {
      movid -= 3;
    }
    for (let m = 0; m < results.length; m++) {
      if (results[m].episode_id === movid) {
        characters = results[m].characters;
        break;
      }
    }
    for (let c = 0; c < characters.length; c++) {
      request(characters[c], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
