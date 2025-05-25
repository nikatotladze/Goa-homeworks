

const adviceList = [
  "It is easy to sit up and take notice, what’s difficult is getting up and taking action.",
  "Success usually comes to those who are too busy to be looking for it.",
  "Don't watch the clock; do what it does. Keep going.",
  "The secret of getting ahead is getting started.",
  "The best way to get something done is to begin."
];

const adviceText = document.querySelector(".card p");
const diceButton = document.querySelector(".dice-button");


diceButton.addEventListener("click", () => {
  const randomIndex = Math.floor(Math.random() * adviceList.length);
  adviceText.textContent = `“${adviceList[randomIndex]}”`;
});
