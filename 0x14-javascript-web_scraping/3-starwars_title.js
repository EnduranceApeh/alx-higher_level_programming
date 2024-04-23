#!/usr/bin/node
// This script that print the title of a star war movie

const arg = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + arg, (error, response, body) => {
  if (error) {
    return;
  }
  const responseJSON = JSON.parse(body);
  console.log(responseJSON.title);
});
