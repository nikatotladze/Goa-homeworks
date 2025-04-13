// 1) 

//  1 
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
  }
  console.log(sum(1, 2, 3, 4)); 
  
  // 2  
  const [first, second, ...rest] = [10, 20, 30, 40, 50];
  console.log(first); 
  console.log(second); 
  console.log(rest); 
  
  //  3  
  const user = { name: "nika", age: 15, city: "rustavi" };
  const { name, ...details } = user;
  console.log(name); 
  console.log(details); 
  
  // 2)  
  
  //  1   
  const arr1 = [1, 2, 3];
  const arr2 = [4, 5, 6];
  const combined = [...arr1, ...arr2];
  console.log(combined); 
  
  // 2     
  const person = { name: "nika", age: 15 };
  const updatedPerson = { ...person, age: 31 };
  console.log(updatedPerson); 
  
  // 3 
  const original = [10, 20, 30];
  const copy = [...original];
  console.log(copy); 
  
  // 3)  
  
  function filterAndClone(first, ...others) {
    return [first, ...others.filter(n => n > 10)];
  }
  console.log(filterAndClone(5, 8, 15, 20, 3)); 
  
  // 4)
  /*
  localStorage არის ბრაუზერის შიდა მეხსიერება, რომელიც ინახავს მონაცემებს key-value ფორმატში.
  */


  // 5)

  document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

    let name = document.getElementById('name').value;

    window.location.href = "welcome.html?name=" + encodeURIComponent(name);
});