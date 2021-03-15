#!/usr/local/bin/node

const m = require('./moment/src/moment')
const date = process.argv[2]
console.log(m(date, 'MM/DD/YYYY').format('dddd'))