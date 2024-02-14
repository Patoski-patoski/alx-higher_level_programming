#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.

const myArr = process.argv;
const arr = [];
let temp;

if (isNaN(myArr[2]) || isNaN(myArr[3])) {
  console.log(0);
  process.exit(0);
} else {
  for (let k = 2; k < myArr.length; k++) {
    arr.push(parseInt(myArr[k]));
  }

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] > arr[i]) {
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
}
console.log(arr[1]);
