// 4

function Person(name, age, city) {
    this.name = name;
    this.age = age;
    this.city = city;
}


const person1 = new Person("ნიკა", 15, "რუსთავი");
console.log(person1);


// 5

function Car(brand, model, year, horsePower, color) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.horsePower = horsePower;
    this.color = color;

    this.boostPower = function() {
        this.horsePower += 100;
        console.log(`${this.brand} now has ${this.horsePower} HP!`);
    };
}


const myCar = new Car("bmw", "E46 m3", 2022, 400, "black");

console.log(`Before: ${myCar.horsePower} HP`);
myCar.boostPower();
console.log(`After: ${myCar.horsePower} HP`);
