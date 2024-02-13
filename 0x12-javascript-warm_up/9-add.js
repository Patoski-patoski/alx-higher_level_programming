#!/usr/bin/node

// a script that prints the addition of 2 integers

const cmdArg = process.argv[2];
const cmdArg2 = process.argv[3];

function add (a, b) {
  console.log(Number(a) + Number(b));
}

add(cmdArg, cmdArg2);
