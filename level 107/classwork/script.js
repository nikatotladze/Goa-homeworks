// 1

function calculateSumAndMultiply(a, b, ...restNumbers) {
  const first = a;
  const second = b;

  console.log("Product of the first and second numbers:", first * second);

  let restSum = 0;
  for (let num of restNumbers) {
    restSum += num;
  }

  console.log("Sum of the remaining numbers:", restSum);
}

calculateSumAndMultiply(2, 3, 4, 5, 6);


// 2

const fruits = ['apple', 'banana', 'cherry'];
const vegetables = ['cucumber', 'Tomato', 'carrot'];
const drinks = ['water', 'juice', 'coke'];

const allItems = [
  ...fruits,
  ...vegetables,
  ...drinks,
  'bread',
  'butter',
  'coffee',
  'tea',
  'chocolate'
];

console.log("All products combined:", allItems);
