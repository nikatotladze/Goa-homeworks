// 2

function startTimer() {
    let seconds = 0;
    setInterval(() => {
        let minutes = Math.floor(seconds / 60);
        let secs = seconds % 60;
        console.log(`${minutes} min : ${secs} sec`);
        seconds++;
    }, 1000);
}

startTimer();


// 3

let count = 0;
let interval = setInterval(() => {
    console.log(count);
    count++;
    if (count > 15) {
        clearInterval(interval);
    }
}, 500);


// 4

setTimeout(() => console.log(2), 1000);
setTimeout(() => console.log(1), 2000);
setTimeout(() => console.log(3), 3000);
