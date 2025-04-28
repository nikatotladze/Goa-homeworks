// 1

const calculator = require('./calculator');


console.log(calculator(10, 5, '+')); // 15
console.log(calculator(10, 5, '*')); // 50



// 2

// calculator და filter ფუნქციების იმპორტი
const { calculator, filter } = require('./calculator');

// calculator-ის გამოყენება
console.log(calculator(15, 3, '*')); // 45

// filter-ის გამოყენება
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = filter(numbers, (n) => n % 2 === 0);
console.log(evenNumbers); // [2, 4, 6]



// 3

import { calculator, filter } from './calculator.js';

// calculator-ის გამოყენება
console.log(calculator(8, 2, '/')); // 4

// filter-ის გამოყენება
const Numbers = [10, 15, 20, 25, 30];
const filteredNumbers = filter(numbers, (n) => n > 20);
console.log(filteredNumbers); // [25, 30]


