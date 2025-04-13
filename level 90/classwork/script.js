// 1

class BankAccount {
    #accountNumber;
    #balance;
    #pin;
  
    constructor(accountNumber, initialBalance, pin) {
      this.#accountNumber = accountNumber;
      this.#balance = initialBalance;
      this.#pin = pin;
    }
  
    #validatePin(pin) {
      return this.#pin === pin;
    }
  
    #setBalance(amount) {
      this.#balance = amount;
    }
  
    deposit(amount) {
      if (amount > 0) {
        this.#setBalance(this.#balance + amount);
      } else {
        console.log("Deposit amount must be positive.");
      }
    }
  
    withdraw(amount, pin) {
      if (!this.#validatePin(pin)) {
        console.log("Invalid PIN.");
        return;
      }
      if (amount > this.#balance) {
        console.log("Insufficient funds.");
        return;
      }
      this.#setBalance(this.#balance - amount);
    }
  
    checkBalance(pin) {
      return this.#validatePin(pin) ? this.#balance : "Invalid PIN.";
    }
  
    get accountNumber() {
      return this.#accountNumber;
    }
  
    set pin(newPin) {
      if (typeof newPin === 'string' && newPin.length >= 4) {
        this.#pin = newPin;
      } else {
        console.log("New PIN must be a string with at least 4 characters.");
      }
    }
  }


// 2

class UserProfile {
    #username;
    #email;
    #password;
  
    constructor(username, email, password) {
      this.#username = username;
      this.#email = email;
      this.#password = password;
    }
  
    #validatePassword(password) {
      return this.#password === password;
    }
  
    updateEmail(newEmail) {
      if (/^\S+@\S+\.\S+$/.test(newEmail)) {
        this.#email = newEmail;
      } else {
        console.log("Invalid email format.");
      }
    }
  
    updatePassword(newPassword) {
      if (newPassword.length >= 6) {
        this.#password = newPassword;
      } else {
        console.log("Password must be at least 6 characters.");
      }
    }
  
    getUsername() {
      return this.#username;
    }
  }

  

// 3

class Car {
    #engineStatus = false;
    #speed = 0;
    #fuelLevel;
  
    constructor(fuelLevel) {
      this.#fuelLevel = fuelLevel;
    }
  
    #startEngine() {
      if (!this.#engineStatus && this.#fuelLevel > 0) {
        this.#engineStatus = true;
      }
    }
  
    #consumeFuel(amount) {
      this.#fuelLevel -= amount;
      if (this.#fuelLevel <= 0) {
        this.#fuelLevel = 0;
        this.stop();
        console.log("Out of fuel!");
      }
    }
  
    drive(speed) {
      if (this.#fuelLevel <= 0) {
        console.log("Cannot drive: no fuel.");
        return;
      }
      this.#startEngine();
      this.#speed = speed;
      this.#consumeFuel(speed * 0.05); 
    }
  
    refuel(amount) {
      if (amount > 0) {
        this.#fuelLevel += amount;
      } else {
        console.log("Refuel amount must be positive.");
      }
    }
  
    stop() {
      this.#speed = 0;
      this.#engineStatus = false;
    }
  }
  

 // 4

 class LibraryBook {
    #title;
    #author;
    #isCheckedOut = false;
  
    constructor(title, author) {
      this.#title = title;
      this.#author = author;
    }
  
    #toggleCheckOutStatus() {
      this.#isCheckedOut = !this.#isCheckedOut;
    }
  
    checkOut() {
      if (!this.#isCheckedOut) {
        this.#toggleCheckOutStatus();
        console.log(`You've checked out "${this.#title}".`);
      } else {
        console.log(`"${this.#title}" is already checked out.`);
      }
    }
  
    returnBook() {
      if (this.#isCheckedOut) {
        this.#toggleCheckOutStatus();
        console.log(`"${this.#title}" has been returned.`);
      } else {
        console.log(`"${this.#title}" wasn't checked out.`);
      }
    }
  
    getBookInfo() {
      return `Title: ${this.#title}, Author: ${this.#author}`;
    }
  }

  
  // 5

  class SmartLight {
    #brightness = 0;
    #color = "white";
    #isOn = false;
  
    constructor(brightness = 50, color = "white") {
      if (this.#validateBrightness(brightness)) this.#brightness = brightness;
      if (this.#validateColor(color)) this.#color = color;
    }
  
    #validateBrightness(brightness) {
      return brightness >= 0 && brightness <= 100;
    }
  
    #validateColor(color) {
      const validColors = ["white", "red", "blue", "green", "yellow", "purple"];
      return validColors.includes(color.toLowerCase());
    }
  
    turnOn() {
      this.#isOn = true;
    }
  
    turnOff() {
      this.#isOn = false;
    }
  
    setBrightness(level) {
      if (this.#validateBrightness(level)) {
        this.#brightness = level;
      } else {
        console.log("Brightness must be between 0 and 100.");
      }
    }
  
    setColor(newColor) {
      if (this.#validateColor(newColor)) {
        this.#color = newColor;
      } else {
        console.log("Invalid color.");
      }
    }
  }
  
  