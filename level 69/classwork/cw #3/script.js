let timer;
let seconds = 0;
let running = false;

function updateTimerDisplay() {
    let hrs = String(Math.floor(seconds / 3600)).padStart(2, '0');
    let mins = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0');
    let secs = String(seconds % 60).padStart(2, '0');
    document.getElementById("timer").textContent = `${hrs}:${mins}:${secs}`;
}

function startTimer() {
    if (!running) {
        running = true;
        timer = setInterval(() => {
            seconds++;
            updateTimerDisplay();
        }, 1000);
    }
}

function stopTimer() {
    running = false;
    clearInterval(timer);
}

function resetTimer() {
    stopTimer();
    seconds = 0;
    updateTimerDisplay();
}
