#!/usr/bin/node

const dict = require('./101-data.js').dict;

const Keys = Object.keys(dict);
const values = Object.values(dict);
let same;
const output = {};

for (let n = 0; n < values.length; n++) {
  output[JSON.stringify(values[n])] = [];
  same = Keys.filter(key => dict[key] === values[n]);
  same.forEach(item => output[JSON.stringify(values[n])].push(item));
}

console.log(output);
