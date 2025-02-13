// 1) 

let score = parseInt(prompt("Enter your score:"));

if (score >= 90 && score <= 100) {
    console.log("Grade A");
} else if (score >= 80 && score < 90) {
    console.log("Grade B");
} else if (score >= 70 && score < 80) {
    console.log("Grade C");
} else if (score >= 60 && score < 70) {
    console.log("Grade D");
} else {
    console.log("Grade F");
}

// 2) 

let age = parseInt(prompt("Enter your age:"));

if (age < 13) {
    console.log("You are kid");
} else if (age < 18) {
    console.log("You are not adult yet");
} else {
    console.log("You are adult");
}


// 4.

let counter = 0;
while (counter <= 100) {
    console.log(counter);
    counter++;
}



// 5. 

let num = 5;
while (num <= 10) {
    console.log(num);
    num++;
}
