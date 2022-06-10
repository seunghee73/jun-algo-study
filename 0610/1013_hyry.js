let [N, ...input] = require('fs').readFileSync('/dev/stdin')
  .toString().trim().split('\n');
N = +N;
input.forEach(i => i.trim());

let ans = '';
const regex = /^(100+1+|01)+$/;
for (const signal of input) {
  if (regex.test(signal)) {
    ans += 'YES\n'
  } else {
    ans += 'NO\n'
  }
}

console.log(ans);