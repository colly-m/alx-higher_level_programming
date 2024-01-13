#!/usr/bin/node

const { list } = require('./100-data');
const nList = list.map((value, index) => value * index);

console.log(list);
console.log(nList);
