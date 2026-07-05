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
const student = {
    name: "Riyan",
    age: 21,
    branch: "Computer Science"
};

document.getElementById("studentName").textContent = student.name;
document.getElementById("studentAge").textContent = `Age: ${student.age}`;
document.getElementById("studentBranch").textContent = `Branch: ${student.branch}`; 