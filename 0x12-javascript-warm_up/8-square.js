#!/usr/bin/node

const argNum = parseInt(process.argv[2]);

if (Number.isInteger(argNum)) {
  for (let i = 0; i < argNum; i++) {
    for (let j = 0; j < argNum; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
