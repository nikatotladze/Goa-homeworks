// 1

function solution(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
      reversed += str[i];
    }
    return reversed;
  }


// 2

function points(games) {
    let totalPoints = 0;
  
    games.forEach(game => {
      let [x, y] = game.split(':').map(Number); 
      if (x > y) {
        totalPoints += 3; 
      } else if (x < y) {
        totalPoints += 0; 
      } else {
        totalPoints += 1; 
      }
    });
  
    return totalPoints;
  }


// 3

const binaryArrayToNumber = arr => {
    return parseInt(arr.join(''), 2); 
  };

  
// 4

function factorial(n) {
    if (n === 0) {
      return 1; 
    } else {
      return n * factorial(n - 1);
    }
  }

  

// 5

function removeUrlAnchor(url){
    return url.split('#')[0];
  }


// 6

function kebabize(str) {
    return str.replace(/[0-9]/g, '').split(/(?=[A-Z])/).join('-').toLowerCase()
}