#!/usr/local/bin/node

const m = require('./moment')
const date = process.argv[2]
console.log(m(date, 'MM/DD/YYYY').format('dddd'))