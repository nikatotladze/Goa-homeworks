// 1

const numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

const isPrime = num => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const primes = numbers.filter(isPrime);
console.log(primes); // [2, 3, 5, 7, 11]


// 2

const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" }
  ];
  
  const names = users.map(user => user.name);
  console.log(names); // ["Alice", "Bob"]

  
// 3

const products = [
    { name: "Pen", price: 1.5 },
    { name: "Notebook", price: 5 },
    { name: "Bag", price: 30 }
  ];
  
  const cheapProducts = products.filter(product => product.price < 10);
  console.log(cheapProducts);
  // [{ name: "Pen", price: 1.5 }, { name: "Notebook", price: 5 }]

  
// 4

const books = [
    { title: "1984", author: "George Orwell" },
    { title: "The Hobbit", author: "J.R.R. Tolkien" }
  ];
  
  const bookStrings = books.map(book => `${book.title} by ${book.author}`);
  console.log(bookStrings);

  
// 5

const Numbers = [5, 12, 18, 25, 33, 40];

const filtered = numbers.filter(num => num > 10 && num % 3 === 0);
console.log(filtered); // [12, 18, 33]


// 6

const Users = [
    { name: "Anna", age: 17 },
    { name: "John", age: 21 }
  ];
  
  const updatedUsers = users.map(user => ({
    ...user,
    isAdult: user.age >= 18
  }));
  
  console.log(updatedUsers);


// 7

const NUmbers = [30, 60, 80, 90, 40];

const result = numbers
  .filter(num => num > 50)
  .map(num => num / 2);

console.log(result);


// 8

const words = ["apple", "banana", "apple", "orange", "banana", "apple"];

const frequency = {};
words.forEach(word => {
  frequency[word] = (frequency[word] || 0) + 1;
});

console.log(frequency);


// 9

const cars = [
    { brand: { name: "Toyota" }, model: "Corolla" },
    { brand: { name: "Honda" }, model: "Civic" },
    { brand: { name: "Toyota" }, model: "Camry" }
  ];
  
  const toyotaCars = cars.filter(car => car.brand.name === "Toyota");
  console.log(toyotaCars);
