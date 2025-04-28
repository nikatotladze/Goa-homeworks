// 1

class BankAccount {
    #balance; 

    constructor() {
        this.#balance = 0;
    }

    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
            console.log(`ჩარიცხულია: ${amount}. ახალი ბალანსი: ${this.#balance}`);
        } else {
            console.log("ჩასარიცხი თანხა უნდა იყოს დადებითი.");
        }
    }

    withdraw(amount) {
        if (amount > 0) {
            if (this.#balance >= amount) {
                this.#balance -= amount;
                console.log(`გატანილია: ${amount}. ახალი ბალანსი: ${this.#balance}`);
            } else {
                console.log("არასაკმარისი თანხა ბალანსზე.");
            }
        } else {
            console.log("გასატანი თანხა უნდა იყოს დადებითი.");
        }
    }

    getBalance() {             
        return this.#balance;
    }
}


// 2

class Author {
    constructor(name, nationality) {
        this.name = name;
        this.nationality = nationality;
    }
}

class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author; 
    }

    displayBookInfo() {
        console.log(`წიგნის სათაური: ${this.title}`);
        console.log(`ავტორი: ${this.author.name}`);
    }
}

// 3

class Employee {
    #salary; 

    constructor(name, salary) {
        this.name = name;
        this.#salary = salary;
    }

    getSalary() {
        return this.#salary;
    }

    displayEmployeeInfo() {
        console.log(`სახელი: ${this.name}`);
        console.log(`ხელფასი: ${this.getSalary()}`);
    }
}

class Manager extends Employee {
    constructor(name, salary, department) {
        super(name, salary); 
        this.department = department; 
    }

    displayManagerInfo() {
        console.log(`სახელი: ${this.name}`);
        console.log(`განყოფილება: ${this.department}`);
        console.log(`ხელფასი: ${this.getSalary()}`);
    }
}
