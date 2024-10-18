document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function addMessage(message, isUser) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
        
        if (isUser) {
            messageElement.textContent = message;
        } else {
            // Parse the bot's response
            const mainResponse = message.response;
            const details = message.analysis;

            // Create main response element
            const mainElement = document.createElement('p');
            mainElement.textContent = mainResponse;
            messageElement.appendChild(mainElement);

            // Create details element
            if (details) {
                const detailsElement = document.createElement('div');
                detailsElement.classList.add('analysis-details');
                const detailLine = document.createElement('p');
                detailLine.textContent = details;
                detailsElement.appendChild(detailLine);
                messageElement.appendChild(detailsElement);
            }
        }

        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage(message, true);
            userInput.value = '';

            fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data, false);
                console.log("Detailed analysis:", data.analysis);  // Log the detailed analysis if needed
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage({response: 'Sorry, there was an error processing your request.'}, false);
            });
        }
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
