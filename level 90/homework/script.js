// 2

// 1

class Thermostat {
    #temperature;
    #minTemp;
    #maxTemp;
    #mode;
  
    constructor(minTemp, maxTemp, initialTemp, mode) {
      this.#minTemp = minTemp;
      this.#maxTemp = maxTemp;
      this.#mode = mode;
      this.#setTemperature(initialTemp);
    }
  
    #setTemperature(value) {
      if (value < this.#minTemp) {
        this.#temperature = this.#minTemp;
      } else if (value > this.#maxTemp) {
        this.#temperature = this.#maxTemp;
      } else {
        this.#temperature = value;
      }
    }
  
    adjustTemperature(value) {
      this.#setTemperature(value);
    }
  
    changeMode(mode) {
      this.#mode = mode;
    }
  
    getCurrentTemperature() {
      return this.#temperature;
    }
  }

  

// 2

class SecureNote {
    #content;
    #pin;
  
    constructor(content, pin) {
      this.#content = content;
      this.#pin = pin;
    }
  
    #validatePin(pin) {
      return this.#pin === pin;
    }
  
    updateContent(newContent, pin) {
      if (this.#validatePin(pin)) {
        this.#content = newContent;
        return true;
      }
      return false;
    }
  
    getContent(pin) {
      return this.#validatePin(pin) ? this.#content : "Access Denied!";
    }
  }

  

  // 3

  class InventoryItem {
    #name;
    #quantity;
    #cost;
  
    constructor(name, quantity, cost) {
      this.#name = name;
      this.#quantity = quantity;
      this.#cost = cost;
    }
  
    #validateQuantityChange(amount) {
      return this.#quantity + amount >= 0;
    }
  
    restock(amount) {
      if (amount > 0) {
        this.#quantity += amount;
      }
    }
  
    sell(amount) {
      if (amount > 0 && this.#validateQuantityChange(-amount)) {
        this.#quantity -= amount;
        return true;
      }
      return false;
    }
  
    getInfo() {
      return { name: this.#name, quantity: this.#quantity };
    }
  }

  

  // 4

  class EmailClient {
    #email;
    #password;
    #inbox = [];
  
    constructor(email, password) {
      this.#email = email;
      this.#password = this.#hashPassword(password);
    }
  
    #hashPassword(password) {
      return `hashed_${password}`;
    }
  
    #validatePassword(password) {
      return this.#hashPassword(password) === this.#password;
    }
  
    #receiveEmail(email) {
      this.#inbox.push(email);
    }
  
    login(password) {
      return this.#validatePassword(password);
    }
  
    sendEmail(to, message) {
      const email = { from: this.#email, to, message };
      console.log(`Email sent to ${to}: "${message}"`);
    }
  
    readInbox() {
      return [...this.#inbox];
    }
  
    simulateIncoming(email) {
      this.#receiveEmail(email);
    }
  }
  

// 5

class Subscription {
    #userID;
    #plan;
    #paymentMethod;
  
    constructor(userID, plan, paymentMethod) {
      this.#userID = userID;
      this.#plan = plan;
      this.#paymentMethod = paymentMethod;
    }
  
    #validatePayment(paymentMethod) {
      return typeof paymentMethod === 'string' && paymentMethod.length > 3;
    }
  
    upgradePlan(newPlan) {
      this.#plan = newPlan;
    }
  
    updatePaymentMethod(newPaymentMethod) {
      if (this.#validatePayment(newPaymentMethod)) {
        this.#paymentMethod = newPaymentMethod;
        return true;
      }
      return false;
    }
  
    getSubscriptionInfo() {
      return {
        userID: this.#userID,
        plan: this.#plan
      };
    }
  }
  