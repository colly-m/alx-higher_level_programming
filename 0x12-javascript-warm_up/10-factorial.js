#!/usr/bin/node

const computeFactorial = (n) => {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

const inputArgument = process.argv[2];
const n = parseInt(inputArgument);

console.log(computeFactorial(n));
