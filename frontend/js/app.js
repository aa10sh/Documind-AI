// Change this when deploying to AWS
const BASE_URL = "http://127.0.0.1:8000/api";

async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];
    if (!file) return alert("Select a file first");

    document.getElementById("uploadStatus").innerText = "Uploading...";

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${BASE_URL}/upload`, {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("uploadStatus").innerText = "Document ready!";
}

async function askQuestion() {
    const question = document.getElementById("question").value;
    if (!question) return;

    addMessage("You: " + question, "user");

    const res = await fetch(`${BASE_URL}/ask`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({question})
    });

    const data = await res.json();
    addMessage("AI: " + data.answer, "bot");

    document.getElementById("question").value = "";
}

function addMessage(text, cls) {
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");
    msg.className = "message " + cls;
    msg.innerText = text;
    chatBox.appendChild(msg);
}

