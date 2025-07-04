document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("sendButton");
    const userInput = document.getElementById("userInput");
    const chatBody = document.querySelector(".chat-body");

    sendButton.addEventListener("click", function () {
        const message = userInput.value.trim();
        if (message === "") return;

        // Add user message
        const userMessage = document.createElement("div");
        userMessage.className = "message user-message";
        userMessage.textContent = "You: " + message;
        chatBody.appendChild(userMessage);

        // Add typing indicator
        const typingMessage = document.createElement("div");
        typingMessage.className = "message typing-message";
        typingMessage.textContent = "Doc is typing...";
        chatBody.appendChild(typingMessage);
        chatBody.scrollTop = chatBody.scrollHeight;

        // Send to Flask backend
        fetch("/get", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `msg=${encodeURIComponent(message)}`
        })
        .then(response => response.text())
        .then(data => {
            // Remove "typing..." message
            chatBody.removeChild(typingMessage);

            // Add bot reply
            const botMessage = document.createElement("div");
            botMessage.className = "message bot-message";
            botMessage.textContent = "Doc: " + data;
            chatBody.appendChild(botMessage);

            chatBody.scrollTop = chatBody.scrollHeight;
        })
        .catch(error => {
            console.error("Error:", error);
            typingMessage.textContent = "Error retrieving answer.";
        });

        userInput.value = "";
    });
});
