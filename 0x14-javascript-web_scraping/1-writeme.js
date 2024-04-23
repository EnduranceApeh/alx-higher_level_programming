#!/usr/bin/node
// This script writes a string to a file

const args = process.argv;
const fs = require('fs');

const arg = args[2];
const text = args[3];

fs.writeFile(arg, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
