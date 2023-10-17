#!/usr/bin/node

const fs = require('fs');
const [, , inputFile1, inputFile2, outputFile] = process.argv;

const content1 = fs.readFileSync(inputFile1, 'utf8');
const content2 = fs.readFileSync(inputFile2, 'utf8');
const combinedContent = content1 + content2;

fs.writeFileSync(outputFile, combinedContent);
