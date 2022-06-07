const input = require('fs').readFileSync('/dev/stdin').toString().trim();

const regex = /^(100+1+|01)+$/;
const match = regex.test(input);
if (match) console.log('SUBMARINE');
else console.log('NOISE');