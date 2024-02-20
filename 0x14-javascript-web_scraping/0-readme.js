#!/usr/bin/node

const fs = require('fs');

function readFile (filename) {
  fs.readFile(filename, 'utf-8', (error, data) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length < 3) {
  console.log('Usage: node script.js <filename>');
} else {
  const filename = process.argv[2];
  readFile(filename);
}
