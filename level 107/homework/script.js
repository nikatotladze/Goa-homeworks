// 2

// Rest ოპერატორი

// გამოიყენება ფუნქციის პარამეტრებში, როცა გვინდა ვიღოთ კიდევ დამატებითი არგუმენტები, 
// რომლებიც არ არის კონკრეტულად დადგენილი და ჩავდოთ ისინი ერთ მასივში

// Spread ოპერატორი 

// გამოიყენება მასივების ან ობიექტების გაშლაში მაგალითად
// როცა გვინდა ერთი მასივის/ობიექტის ყველა ელემენტი ან კუთვნილება გადავიტანოთ ახალში


// რა განს არის მათ შორის

// Rest–ი აგროვებს მონაცემებს ერთიან ობიექტში 
// Spread–ი შლის ან გაშლის მათ სხვა კონტექსტში


// 3

const person = {
  name: "Nika",
  age: 15,
  height: 170
};


const { name, ...otherProps } = person;

console.log("Name:", name);
console.log("Other properties:", otherProps);


// 4

const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const obj3 = { e: 5, f: 6 };


const combinedObj = { ...obj1, ...obj2, ...obj3 };

console.log("Combined object:", combinedObj);


// 5


function printNames(...names) {

  console.log("Here are the names you gave me:");
  for (const name of names) {
    console.log("-", name);
  }
}


const nameList = ["Ana", "Beka", "Luka", "Maya", "Goga"];


printNames(...nameList);



