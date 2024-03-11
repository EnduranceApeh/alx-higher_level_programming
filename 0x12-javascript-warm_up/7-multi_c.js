#!/usr/bin/node
// script that print x times c is fun

const x = parseInt(process.argv[2]);
let count = 0;

if (isNaN(x)) {
  console.log('Missing number of occurances');
} else {
  while (count < x) {
    console.log('C is fun');
    count += 1;
  }
}
