// Change this when deploying to AWS
const BASE_URL = "http://127.0.0.1:8000/api";

let currentFilename = null;

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

    if (res.ok) {
        currentFilename = data.filename;   // 🔥 store filename

        document.getElementById("uploadStatus").innerText =
            "Document ready!";

        document.getElementById("summarizeBtn").disabled = false;
    } else {
        document.getElementById("uploadStatus").innerText =
            "Upload failed.";
    }
}

async function summarizeDocument() {
    if (!currentFilename) {
        return alert("Upload a document first");
    }

    const summaryCard = document.getElementById("summaryCard");
    const summaryBox = document.getElementById("summaryBox");

    summaryCard.style.display = "block";
    summaryBox.innerHTML = "Generating summary...";

    const res = await fetch(
        `${BASE_URL}/summarize/${currentFilename}`,
        { method: "POST" }
    );

    const data = await res.json();

    if (res.ok) {
        summaryBox.innerHTML = `<p>${data.summary}</p>`;
    } else {
        summaryBox.innerHTML = "Failed to summarize document.";
    }
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

