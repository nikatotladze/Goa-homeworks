// 1.
let paragraphs = document.getElementsByClassName("txt");
console.log(paragraphs);

// 2.
let elementById = document.querySelector("image");
console.log(elementById);

let elementByClass = document.querySelector(".txt");
console.log(elementByClass);

// 3. ?

// 4. 
let paragraph = document.querySelector(".text");
paragraph.style.color = "white";
paragraph.style.backgroundColor = "blue";
paragraph.style.fontSize = "20px";

// 5. 
let newParagraph = document.createElement("paragraph");
let textNode = document.createTextNode("nika ABCD");
newParagraph.appendChild(textNode);

let targetDiv = document.getElementById("targetDiv");
targetDiv.appendChild(newParagraph);

