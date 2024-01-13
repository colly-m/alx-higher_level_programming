#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const ary = process.argv.slice(2).map(Number);
  const sec = ary.sort((a, b) => b - a)[1];
  console.log(sec || 0);
}
