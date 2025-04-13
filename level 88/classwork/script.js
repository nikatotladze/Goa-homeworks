// 1

function sumAll(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
  }
  

  console.log(sumAll(1, 2, 3));             
  console.log(sumAll(10, 20));             
  console.log(sumAll(5, 15, 25, 35));      
  

  
// 2

const person = {
    name: "nika",
    age: 15
  };
  
  const contact = {
    email: "nikatot@gmai.com",
    phone: "579-123123"
  };
  
  const mergedObject = { ...person, ...contact };
  
  console.log(mergedObject);



// 3

const list1 = [1, 2, 3];
const list2 = [4, 5, 6];

const mergedList = [...list1, ...list2];

console.log(mergedList);  

  