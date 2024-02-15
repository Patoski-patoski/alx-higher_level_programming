#!/usr/bin/node

/**
 * a function that returns the reversed version of a list
 *
 * Run: ./7-main.js
 **/

exports.esrever = function (list) {
  const store = [];

  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    store[j] = list[i];
  }
  return store;
};
