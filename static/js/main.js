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
const students = [
    {
        name: "Riyan",
        age: 21,
        branch: "Computer Science"
    },
    {
        name: "Rahul",
        age: 20,
        branch: "Mechanical"
    },
    {
        name: "Aman",
        age: 22,
        branch: "Electrical"
    }
];
const studentContainer = document.getElementById("studentContainer");

studentContainer.innerHTML = "";
students.map(student => {

    studentContainer.innerHTML += `

        <div class="bg-slate-800 p-4 rounded-xl">

            <h3 class="text-green-400 font-bold">

                👤 ${student.name}

            </h3>

            <p>🎂 ${student.age}</p>

            <p>🎓 ${student.branch}</p>

        </div>

    `;

});