// 1) 
function sumArray(numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
}

// 2) 
function minMaxArray(numbers) {
    return {
        min: Math.min(...numbers),
        max: Math.max(...numbers)
    };
}

// 3) 
function generateRandomArray(N) {
    return Array.from({ length: N }, () => Math.floor(Math.random() * 100) + 1);
}

// 4) 
function squareArray(numbers) {
    return numbers.map(num => num ** 2);
}

// 5) 
function roundNumber(num) {
    return {
        floor: Math.floor(num),
        ceil: Math.ceil(num),
        round: Math.round(num)
    };
}

// test
const testArray = [5, 10, 15, 20];

console.log("Sum:", sumArray(testArray));
console.log("Min and Max:", minMaxArray(testArray));
console.log("Random Array:", generateRandomArray(5));
console.log("Squared Array:", squareArray(testArray));
console.log("Rounding 4.7:", roundNumber(4.7));
