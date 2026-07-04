const welcomeMessage = document.getElementById("welcomeMessage");
const currentDate = document.getElementById("currentDate");
const currentTime = document.getElementById("currentTime");

function updateDashboard() {

    const today = new Date();

    const hour = today.getHours();

    let greeting = "";

    if (hour < 12) {
        greeting = "☀️ Good Morning";
    }
    else if (hour < 18) {
        greeting = "🌤 Good Afternoon";
    }
    else {
        greeting = "🌙 Good Evening";
    }

    welcomeMessage.textContent = `${greeting}, Rishu 👋`;

    currentDate.textContent = today.toDateString();

    currentTime.textContent = today.toLocaleTimeString();

}

updateDashboard();