#!/usr/bin/node
// This script display the status code of a GET request

const request = require('request');
const args = process.argv;

const url = argv[2];

request.get(url, (error, reponse, body) => {
  const statusCode = response.statusCode;
  console.log('code: ', statusCode);
});
