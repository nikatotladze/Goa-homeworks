// 1)
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));
console.log("Sum:", num1 + num2);

// 2)
let username = prompt("Enter your name:");
console.log("Hello, " + username + "!");

// 3)
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
