#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof this.printedArgs === 'undefined') {
    this.printedArgs = 0;
  }
  console.log(this.printedArgs + ': ' + item);
  this.printedArgs++;
};
