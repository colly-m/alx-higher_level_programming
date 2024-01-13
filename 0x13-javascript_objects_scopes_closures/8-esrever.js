#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let r = list.length - 1; r >= 0; r--) {
    reversedList.push(list[r]);
  }

  return reversedList;
};
