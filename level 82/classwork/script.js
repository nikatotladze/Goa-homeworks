
let person = {
    firstName: "nika",
    lastName: "totladze",
    age: 15
};

localStorage.setItem("personData", JSON.stringify(person));

let storedPerson = JSON.parse(localStorage.getItem("personData"));
console.log("name:", storedPerson.firstName);

storedPerson.firstName = "ნიკა";

localStorage.setItem("personData", JSON.stringify(storedPerson));

let updatedPerson = JSON.parse(localStorage.getItem("personData"));
console.log("განახლებული სახელი:", updatedPerson.firstName); 
