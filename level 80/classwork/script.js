// 1

function sum(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
      total += numbers[i];
    }
    return total;
  }

  
// 2

function findAverage(array) {
    if (array.length === 0) return 0; 
    
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
      sum += array[i]; 
    }
    
    return sum / array.length; 
  }

  

// 3

function countBy(x, n) {
    let z = [];
    for (let i = 1; i <= n; i++) {
      z.push(x * i); 
    }
    return z;
  }


// 4

const reverseSeq = n => {
    let result = [];
    for (let i = n; i > 0; i--) {
      result.push(i); 
    }
    return result;
  };


// 5

function findMissingLetter(array) {
    const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    for(let i = 0; i < array.length - 1; i++) {
      if(alphabet[alphabet.indexOf(array[i]) + 1] !== array[i + 1]) {
        return alphabet[alphabet.indexOf(array[i]) + 1];
      }
    }
    
  }