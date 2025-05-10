// 1

const names = ["Liam", "Emma", "Noah", "Olivia", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin"];

for (let i = 0; i < names.length; i++) {
    const curValue = names[i];
    if (i % 2 === 0) {
        console.log(`${curValue} is on even index`);
    } else {
        console.log(`${curValue} is on odd index`);
    }
}


// 2

const numbers = [57, 23, 89, 11, 78, 36, 64, 5, 92, 44];

function customMap(array, callback) {
  const result = [];
  for (let i = 0; i < array.length; i++) {
    result.push(callback(array[i], i, array));
  }
  return result;
}

const newNumbers = customMap(numbers, (curValue, index, curArray) => {
  if (index % 2 === 0) {
    return Math.floor(curValue / 2);
  } else {
    return curValue * 2;
  }
});

console.log(newNumbers);

