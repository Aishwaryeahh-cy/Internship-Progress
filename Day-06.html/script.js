const questions = [
    {
        question: "What is HTML?",
        options: [
            "Programming Language",
            "Markup Language",
            "Database",
            "Operating System"
        ]
    },
    {
        question: "What is CSS?",
        options: [
            "Database",
            "Styling Language",
            "Browser",
            "Programming Language"
        ]
    },
    {
        question: "JavaScript is a ______?",
        options: [
            "Database",
            "Scripting Language",
            "Browser",
            "Operating System"
        ]
    }
];

let currentQuestion = 0;

const question = document.getElementById("question");

const labels = [
    document.getElementById("label1"),
    document.getElementById("label2"),
    document.getElementById("label3"),
    document.getElementById("label4")
];

const progress = document.getElementById("progress");
const progressText = document.getElementById("progressText");

function loadQuestion() {

    question.textContent = questions[currentQuestion].question;

    for (let i = 0; i < 4; i++) {
        labels[i].textContent = questions[currentQuestion].options[i];
    }

    let percent = ((currentQuestion + 1) / questions.length) * 100;

    progress.value = percent;
    progressText.textContent = percent + "%";
}

loadQuestion();

document.getElementById("nextBtn").onclick = function () {

    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        loadQuestion();
    }

};

document.getElementById("prevBtn").onclick = function () {

    if (currentQuestion > 0) {
        currentQuestion--;
        loadQuestion();
    }

};