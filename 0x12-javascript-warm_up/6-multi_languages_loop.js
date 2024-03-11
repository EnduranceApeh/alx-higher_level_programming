#!/usr/bin/node
// print 3 lines using arrays of str and loop

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const arrayLength = myArray.length;
let index = 0;

while (index < arrayLength) {
  console.log(myArray[index]);
  index += 1;
}
