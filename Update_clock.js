// update_clock.js

setInterval(() => {
    const now = new Date();
    const timeElement = document.getElementById('current-time');
    timeElement.innerText = `Current date and time: ${now.toLocaleString()}`;
}, 1000);
