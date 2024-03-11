#!/usr/bin/node
// a script that computes and prints a factorial

function factorial (n) {
  // Base case: If n is NaN or less than 0, return 1
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = parseInt(process.argv[2]);

console.log(factorial(number));
