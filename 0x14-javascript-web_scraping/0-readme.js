#!/usr/bin/node
// This script reads and prints the content of a file

const args = process.argv;
const fs = require('fs');

const arg = args[2];

fs.readFile(arg, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
