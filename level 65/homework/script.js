// 4

function Book(title, author, year, genre, pages) {
    this.title = title;
    this.author = author;
    this.year = year;
    this.genre = genre;
    this.pages = pages;
}

const myBook = new Book("hsdhkjg", "nika totladze", 2025, "horror", 201);

console.log(myBook);



// 5

function Motorcycle(brand, model, year, speed) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.speed = speed;

    this.boostSpeed = function() {
        this.speed += 20;
        console.log(`${this.brand} ${this.model} now has a speed of ${this.speed} km/h!`);
    };
}

const myBike = new Motorcycle("ninja kavazaki", "399", 2022, 200);

console.log(`Before: ${myBike.speed} km/h`);
myBike.boostSpeed(); 
console.log(`After: ${myBike.speed} km/h`);
