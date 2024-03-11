#!/usr/bin/node
// print the frist arg passed to this script

const arg = process.argv[2];

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
