#!/usr/bin/node
/**
 *  a script that computes the number of tasks completed by user id.
 *
 * Return: Nothing
 **/

const request = require('request');
const urlpath = process.argv[2];

request(urlpath, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTask = {};

  for (const task of tasks) {
    if (task.completed) {
      if (!completedTask[task.userId]) {
        completedTask[task.userId] = 0;
      }
      completedTask[task.userId]++;
    }
  }
  console.log(completedTask);
});
