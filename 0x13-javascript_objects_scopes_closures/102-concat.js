#!/usr/bin/node

const { readFileSync, writeFileSync } = require('fs');
const { argv } = require('process');

const fileContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concatenatedContent = fileContent(argv[2]) + '' + fileContent(argv[3]);

writeFileSync(argv[4], concatenatedContent, 'utf8', err => {
  if (err) throw err;
});
