#!/usr/bin/node

// a script that computes and prints a factorial

const cmdArg = parseInt(process.argv[2]);

function factorial (cmdArg) {
  if (isNaN(cmdArg)) {
    return (1);
  } else {
    if (cmdArg === 0) {
      return (1);
    }
    return (cmdArg * factorial(cmdArg - 1));
  }
}
console.log(factorial(cmdArg));
