// 2

const arr = [10, 20, 30, 40, 50];
const [a, b, c, d, e] = arr;

console.log(a, b, c, d, e); 


// 3

const person = {
    name: "nika",
    age: 15,
    city: "rustavi"
  };
  
  const { name, age, city } = person;
  
  console.log(name, age, city); 

  
// 4


const nums = [1, 2, 3];
const newNums = [...nums, 4, 5];


function sum(...numbers) {
  return numbers.reduce((acc, num) => acc + num, 0);
}


// 5

function sumNumbers(...nums) {
    return nums.reduce((acc, num) => acc + num, 0);
  }
  
  console.log(sumNumbers(1, 2)); 
  console.log(sumNumbers(5, 10, 15)); 
  console.log(sumNumbers(100, 200, 300, 400)); 


// 6

const originalArray = [1,2,3,4,5,6,7,8,9,10];
const copiedArray = [...originalArray];

console.log(copiedArray); 


// 7

const user = {
    id: 101,
    username: "giorgi_dev",
    email: "giorgi@example.com",
    role: "admin",
    isActive: true
  };
  
  const { id, username, ...otherInfo } = user;
  
  console.log(id); 
  console.log(username); 
  console.log(otherInfo); 
 
  
