#!/usr/bin/node

/**
 * a function that returns the number of occurrences in a list
 *
 * Run: ./7-main.js
 *
 **/

exports.nbOccurences = function (list, searchElement) {
    let count = 0;

    for (i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            count++;
        }
    }
    return count;
}
