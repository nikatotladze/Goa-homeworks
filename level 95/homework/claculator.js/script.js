// 1

function calculator(a, b, operation) {
    if (operation === '+') {
        return a + b;
    } else if (operation === '-') {
        return a - b;
    } else if (operation === '*') {
        return a * b;
    } else if (operation === '/') {
        return a / b;
    } else {
        return 'Invalid operation';
    }
}

// ფუნქციის ექსპორტი
module.exports = calculator;



// 2

function calculator(a, b, operation) {
    if (operation === '+') return a + b;
    if (operation === '-') return a - b;
    if (operation === '*') return a * b;
    if (operation === '/') return a / b;
    return 'Invalid operation';
}

function filter(array, func) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        if (func(array[i])) {
            result.push(array[i]);
        }
    }
    return result;
}

// ორივე ფუნქციის ექსპორტი
module.exports = { calculator, filter };



// 3

export function calculator(a, b, operation) {
    if (operation === '+') return a + b;
    if (operation === '-') return a - b;
    if (operation === '*') return a * b;
    if (operation === '/') return a / b;
    return 'Invalid operation';
}

export function filter(array, func) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        if (func(array[i])) {
            result.push(array[i]);
        }
    }
    return result;
}


// 8

import add, { subtract } from './mathOperations.js';

console.log(add(7, 3));        // 10
console.log(subtract(7, 3));   // 4


