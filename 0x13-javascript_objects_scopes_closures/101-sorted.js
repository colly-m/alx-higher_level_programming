#!/usr/bin/node

const data = require('./101-data.js');

function computeUserIdsByOccurrence (inputData) {
  const userIdsByOccurrence = {};

  for (const userId in inputData) {
    const occurrences = inputData[userId];

    if (userIdsByOccurrence[occurrences] === undefined) {
      userIdsByOccurrence[occurrences] = [userId];
    } else {
      userIdsByOccurrence[occurrences].push(userId);
    }
  }

  return userIdsByOccurrence;
}
const result = computeUserIdsByOccurrence(data);

console.log(result);
