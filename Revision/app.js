const fs = require('fs');

const file1 = fs.readFileSync('./content/first.txt', 'utf-8');
console.log(file1);
// fs.writeFileSync('./content/second.txt', 'this is second line');
const file2 = fs.readFileSync('./content/second.txt', 'utf-8');
console.log(file2);