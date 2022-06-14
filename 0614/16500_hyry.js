
// 시초 1 regex
let [S, _, ...A] = require('fs').readFileSync('1.txt')
  .toString().trim().split('\n');

S = S.trim();
A = A.map(a => `(${a.trim()})+`).join('|');

const regEx = new RegExp(`^(${A})+$`, 'gm');
const possible = regEx.test(S);

console.log(+possible);

// 시초 2 재귀 + 백트래킹
const matchString = (str) => {
  if (str.length === 0) {
    return 1;
  }

  for (const [len, subStr] of A) {
    let strV = str.substring(0, len);
    if (strV !== subStr) continue;
    if (matchString(str.substring(len))) {
      return 1;
    }
  }

  return 0;
}

let [S, N, ...A] = require('fs').readFileSync('1.txt')
  .toString().trim().split('\n');

S = S.trim();
N = +N;
A = A.map(a => [a.trim().length ,a.trim()]);

const ans = matchString(S);
console.log(ans);

// DP
let [S, N, ...A] = require('fs').readFileSync('1.txt')
  .toString().trim().split('\n');

S = S.trim();
N = +N;
A = A.map(a => a.trim());

const memo = new Array(S.length).fill(0)
memo[S.length] = 1 

for (let i = S.length - 1; i > -1; i--) {
  for (let word of A) {
    if (S.substring(i, i + word.length) === word && memo[i + word.length] === 1) {
      memo[i] = 1
    }
  }
}

console.log(memo[0])