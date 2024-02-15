#!/usr/bin/node

const argNum = parseInt(process.argv[2]);

if (Number.isInteger(argNum)) {
  console.log(`My number: ${argNum}`);
} else {
  console.log('Not a number');
}
