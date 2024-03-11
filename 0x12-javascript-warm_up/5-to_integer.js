#!/usr/bin/node
// convert string to integer and print

const argument = process.argv[2];
const number = Number(argument);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
