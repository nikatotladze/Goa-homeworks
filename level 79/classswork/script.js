// 1

// ES6 გამოვიდა 2015 წელს ეს update ები გამოვიდა js-ს კოდების გამარტივებისთის და ხდიდა უფრო ორგანიზებულს 


// 2

// ?


// 3

const numbers = ["123", "456", "789", "1011"];

for (const number of numbers) {
    console.log(` ${number}`);
}


// 4

const user = {
    name: "ნიკა",
    age: 15,
    city: "რუსთავი"
};

for (const key in user) {
    console.log(`${key}: ${user[key]}`);
}


// 5

// ?


// 6

const greet = (name) => {
    return `გამარჯობა, ${name}!`;
};

console.log(greet("ნიკა"));
