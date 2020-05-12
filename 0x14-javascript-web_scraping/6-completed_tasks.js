#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) { console.log(err); return; }

  const tasks = JSON.parse(body);
  const tasksCompleted = {};

  for (const task of tasks) { tasksCompleted[task.userId] = 0; }

  for (const task of tasks) {
    if (task.completed === true) { tasksCompleted[task.userId]++; }
  }

  console.log(tasksCompleted);
});
