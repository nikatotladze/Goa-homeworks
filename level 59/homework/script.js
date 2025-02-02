// 1 
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));
console.log("Sum:", num1 + num2);

// 2
let username = prompt("Enter your name:");
console.log("Hello, " + username + "!");

// 2
let number1 = Number(prompt("Enter the first number:"));
let number2 = Number(prompt("Enter the second number:"));
let number3 = Number(prompt("Enter the third number:"));
console.log("Sum of three numbers:", number1 + number2 + number3);

// 3
let sentence1 = prompt("Enter the first sentence:");
let sentence2 = prompt("Enter the second sentence:");
console.log("Combined Sentence:", sentence1 + " " + sentence2);

// 3
document.body.innerHTML = `
    <form id="nameForm">
        <input type="text" name="name" id="nameInput" placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>
`;

document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault(); // ფორმის განახლების თავიდან ასაცილებლად
    let inputName = document.getElementById("nameInput").value;
    console.log("Submitted Name:", inputName);
});


// 4 

document.body.innerHTML = `
    <form id="nameForm">
        <input type="text" name="name" id="nameInput" placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>
`;

document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let inputName = document.getElementById("nameInput").value;
    console.log("Submitted Name:", inputName);
});


//5


/*
name ატრიბუტის მნიშვნელობა:
    ფორმის მონაცემების გადაცემა სერვერზე: საჭირო ფორმის მონაცემების გასაგზავნად.
    FormData API: მარტივად წვდომა ფორმის მონაცემებზე.
    ვალიდაცია: ბრაუზერის მიერ ავტომატური ვალიდაციისთვის.
    მრავალფუნქციური ფორმების მართვა: სხვადასხვა მონაცემების ერთმანეთისგან გარჩევისთვის.
*/




