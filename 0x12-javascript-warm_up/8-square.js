#!/usr/bin/node

const size = process.argv[2];

if (!isNaN(parseInt(size))) {
  const squareSize = parseInt(size);

  for (let z = 0; z < squareSize; z++) {
    let row = '';
    for (let s = 0; s < squareSize; s++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
