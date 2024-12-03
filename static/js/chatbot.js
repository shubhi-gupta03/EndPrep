async function sendMessage() {
    try {
        const input = document.getElementById("chatbot-input");
        const message = input.value;
        input.value = "";

        const messagesContainer = document.getElementById("chatbot-messages");
        messagesContainer.innerHTML += `<div class="user-message">${message}</div>`;

        const paperId = document.getElementById("chatbot-container").getAttribute("data-paper-id");

        const response = await fetch(`/chatbot-api/${paperId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}",
            },
            body: JSON.stringify({ question: message }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        messagesContainer.innerHTML += `<div class="bot-message">${data.answer}</div>`;
    } catch (error) {
        console.error("Error:", error);
        const messagesContainer = document.getElementById("chatbot-messages");
        messagesContainer.innerHTML += `<div class="bot-message">An error occurred. Please try again later.</div>`;
    }
}
