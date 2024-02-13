#!/usr/bin/node

// a script that prints x times “C is fun”

const cmdArg = process.argv[2];

if (cmdArg === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(cmdArg); i++) {
    console.log('C is fun');
  }
}
