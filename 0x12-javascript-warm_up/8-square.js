#!/usr/bin/node
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let j = 0;
    let result = '';

    while (j < x) {
      result += 'X';
      j++;
    }
    console.log(result);
  }
}