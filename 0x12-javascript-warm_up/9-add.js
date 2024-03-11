#!/usr/bin/node
// scrot that print addition os 2 numbers

function add (a, b) {
  return a + b;
}

// retrieve integer from command line

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// invoke function
console.log(add(num1, num2));
