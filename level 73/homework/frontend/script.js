// 1

// Global Scope

// const და let არ ქმნიან გლობალურ ცვლადებს.
// var კი ქმნის და ხდება window ობიექტის ნაწილი.

// Function Scope 
// სამივე (const, let, var) ფუნქციურ სკოუპში ჩანს.

// Block Scope 
// const და let არის ბლოკ-სკოუპის მქონე (ანუ, {} ბლოკში დეკლარირებულ ცვლადებს ვერ ვიყენებთ მის გარეთ).
// var არ არის ბლოკ-სკოუპის მქონე და ხელმისაწვდომია ბლოკის გარეთ.

// Reassignment
// const-ის ხელახლა მინიჭება შეუძლებელია.
// let და var-ის შემთხვევაში შესაძლებელია მნიშვნელობის შეცვლა.


// 2

// Scope განსაზღვრავს ცვლადის ხილვადობას და ხელმისაწვდომობის არეს კოდის სხვადასხვა ნაწილში.

// 3

// Hoisting არის მექანიზმი, სადაც JavaScript წინასწარ "წევს" ცვლადებისა და ფუნქციების დეკლარაციებს კოდის ზედა ნაწილში.


document.addEventListener("DOMContentLoaded", () => {
    const billInput = document.getElementById("bill");
    const tipButtons = document.querySelectorAll(".tip-btn");
    const customTipInput = document.getElementById("custom-tip");
    const peopleInput = document.getElementById("people");
    const tipAmountDisplay = document.getElementById("tip-amount");
    const totalAmountDisplay = document.getElementById("total-amount");
    const resetButton = document.getElementById("reset");

    let bill = 0, tipPercent = 15, people = 1;

    function calculateTip() {
        if (bill > 0 && people > 0) {
            let tip = (bill * tipPercent) / 100;
            let total = bill + tip;
            tipAmountDisplay.textContent = `$${(tip / people).toFixed(2)}`;
            totalAmountDisplay.textContent = `$${(total / people).toFixed(2)}`;
        }
    }

    billInput.addEventListener("input", (e) => {
        bill = parseFloat(e.target.value) || 0;
        calculateTip();
    });

    tipButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            tipButtons.forEach(btn => btn.classList.remove("active"));
            e.target.classList.add("active");
            tipPercent = parseInt(e.target.getAttribute("data-tip"));
            customTipInput.value = "";
            calculateTip();
        });
    });

    customTipInput.addEventListener("input", (e) => {
        tipButtons.forEach(btn => btn.classList.remove("active"));
        tipPercent = parseFloat(e.target.value) || 0;
        calculateTip();
    });

    peopleInput.addEventListener("input", (e) => {
        people = parseInt(e.target.value) || 1;
        calculateTip();
    });

    resetButton.addEventListener("click", () => {
        billInput.value = "";
        customTipInput.value = "";
        peopleInput.value = "1";
        bill = 0;
        tipPercent = 15;
        people = 1;
        tipAmountDisplay.textContent = "$0.00";
        totalAmountDisplay.textContent = "$0.00";
        tipButtons.forEach(btn => btn.classList.remove("active"));
        tipButtons[2].classList.add("active");
    });

    calculateTip();
});
