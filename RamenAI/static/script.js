const BASE_URL = 'http://127.0.0.1:5000'; 

// Function to create a message bubble
function createMessageBubble(text, classes) {
    const messageBubble = document.createElement('div');
    messageBubble.classList.add(...classes);
    messageBubble.innerText = text;
    return messageBubble;
}

// Function to append a message bubble to the message container
function appendMessageBubble(messageBubble) {
    const messageContainer = document.getElementById('message-container');
    messageContainer.appendChild(messageBubble);
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

// Function to handle form submission
document.getElementById('inputForm').addEventListener("submit", function(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input').value;

    // Fetch call to the Flask backend API endpoint
    fetch(`${BASE_URL}/api/maruchat`, {
        method: 'POST',
        headers: {
            'Content-Type': "application/json"
        },
        body: JSON.stringify({userInput: userInput})
    })
    .then(response => response.json())
    .then(data => {
        const chatMessageBubble = createMessageBubble(data.chatResponse, ['chat-response']);
        appendMessageBubble(chatMessageBubble);
    });

    const userMessageBubble = createMessageBubble(userInput, ['message-bubble', 'user-message']);
    appendMessageBubble(userMessageBubble);

    document.getElementById('user-input').value = '';
});


/*
// Function to fetch and display previous conversations
function fetchConversations() {
    fetch(`${BASE_URL}/api/conversations`, {
        method: 'GET',
        headers: {
            'Content-Type': "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(conversation => {
            const messageBubble = createMessageBubble(conversation.content, 
                conversation.role === 'user' ? ['message-bubble', 'user-message'] : ['chat-response']);
            appendMessageBubble(messageBubble);
        });
    });
}

document.addEventListener("DOMContentLoaded", function() {
    fetchConversations(); // Load conversations when the page loads
});


*/