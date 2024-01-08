#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);

  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    for (let o = 0; o < x; o++) {
      console.log('C is fun');
    }
  }
}
