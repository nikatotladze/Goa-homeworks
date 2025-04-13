// 1

class Car {
    constructor(make, model) {
      this.make = make;
      this.model = model;
    }
  }
  
  const myCar = new Car("Toyota", "Corolla");
  console.log(`Make: ${myCar.make}, Model: ${myCar.model}`);

  
// 2

class BankAccount {
    #balance = 0;
  
    deposit(amount) {
      if (amount > 0) {
        this.#balance += amount;
      }
    }
  
    withdraw(amount) {
      if (amount > 0 && amount <= this.#balance) {
        this.#balance -= amount;
      }
    }
  
    getBalance() {
      return this.#balance;
    }
  }
  
  const account = new BankAccount();
  account.deposit(500);
  account.withdraw(200);
  console.log(`Balance: ${account.getBalance()}`);

  
// 3

class MathOperations {
    static PI = 3.14159265359;
  
    static add(a, b) {
      return a + b;
    }
  }
  
  console.log(MathOperations.add(5, 7));
  console.log(MathOperations.PI);

  

// 4

class Rectangle {
    #width = 1;
    #height = 1;
  
    constructor(width, height) {
      this.width = width;
      this.height = height;
    }
  
    get area() {
      return this.#width * this.#height;
    }
  
    set width(value) {
      if (value > 0) this.#width = value;
      else console.error("Width must be positive");
    }
  
    set height(value) {
      if (value > 0) this.#height = value;
      else console.error("Height must be positive");
    }
  }
  
  const rect = new Rectangle(5, 3);
  console.log(`Area: ${rect.area}`);
  rect.width = -1; 


// 5

class User {
    #password = "";
  
    setPassword(password) {
      if (this.#validatePassword(password)) {
        this.#password = password;
        console.log("Password set successfully.");
      } else {
        console.log("Password is too weak.");
      }
    }
  
    #validatePassword(password) {
      return password.length >= 6;
    }
  }
  
  const user = new User();
  user.setPassword("123");      
  user.setPassword("strongP@ss"); 
  


  // 6

  class Book {
    title;
    #pages = 0;
  
    constructor(title, pages) {
      this.title = title;
      this.pages = pages;
    }
  
    get pages() {
      return this.#pages;
    }
  
    set pages(value) {
      if (value > 0) {
        this.#pages = value;
      } else {
        console.error("Number of pages must be positive.");
      }
    }
  }
  
  const book = new Book("JavaScript Guide", 350);
  console.log(`${book.title} has ${book.pages} pages.`);
  book.pages = -50; 


  // 7

  class Player {
    static count = 0;
  
    constructor(name) {
      this.name = name;
      Player.count++;
    }
  
    static getPlayerCount() {
      return Player.count;
    }
  }
  
  const p1 = new Player("Alice");
  const p2 = new Player("Bob");
  console.log(`Total Players: ${Player.getPlayerCount()}`);

  
  // 8

  class Vehicle {
    #speed = 0;
  
    setSpeed(speed) {
      if (speed >= 0) {
        this.#speed = speed;
      }
    }
  
    getSpeed() {
      return this.#speed;
    }
  }
  
  class Bike extends Vehicle {
    accelerate() {
      let newSpeed = this.getSpeed() + 10;
      this.setSpeed(newSpeed);
      console.log(`Accelerated to ${newSpeed} km/h`);
    }
  }
  
  const bike = new Bike();
  bike.setSpeed(20);
  bike.accelerate(); 


  // 9

  class Student {
    constructor(name, grade) {
      this.name = name;
      this.grade = grade;
    }
  
    static compareGrades(student1, student2) {
      if (student1.grade > student2.grade) {
        return `${student1.name} has a higher grade.`;
      } else if (student1.grade < student2.grade) {
        return `${student2.name} has a higher grade.`;
      } else {
        return "Both students have the same grade.";
      }
    }
  }
  
  const s1 = new Student("John", 85);
  const s2 = new Student("Jane", 90);
  console.log(Student.compareGrades(s1, s2));

  
  // 10

  // done
  
  
  