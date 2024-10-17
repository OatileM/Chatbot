# Sentiment-Aware Chatbot with Web Interface

## Description
This project implements a sentiment-aware chatbot with a web-based user interface. The application consists of a Python backend using Flask and VADER for sentiment analysis, and a frontend built with HTML, CSS, and JavaScript. The chatbot analyzes the sentiment of user input in real-time and responds accordingly, providing a more empathetic and context-aware conversation experience.

## Key Features
- **Sentiment Analysis**: Utilizes VADER (Valence Aware Dictionary and sEntiment Reasoner) for accurate sentiment detection, especially effective for social media-style text and short messages.
- **Real-time Processing**: Analyzes user input on-the-fly and generates appropriate responses.
- **Web-based Interface**: User-friendly chat interface built with HTML, CSS, and JavaScript.
- **Responsive Design**: The chat interface is designed to be responsive and work well on various screen sizes.
- **Asynchronous Communication**: Uses JavaScript fetch API for asynchronous communication with the backend.
- **Flask Backend**: Implements a Flask server to handle HTTP requests and perform sentiment analysis.
- **CORS Support**: Includes Cross-Origin Resource Sharing (CORS) for seamless integration of frontend and backend.
- **Detailed Sentiment Feedback**: Provides comprehensive sentiment scores including positive, negative, neutral, and compound values.

## Technology Stack
- **Backend**: 
  - Python
  - Flask (Web framework)
  - VADER (Sentiment analysis)
- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
- **API**: RESTful API with JSON responses
- **Cross-Origin Support**: Flask-CORS

## Application Structure
1. **`index.html`**: The main HTML file that structures the chat interface.
   - Contains a chat container with message display area and input field.
   - Links to the CSS file and JavaScript file.

2. **`styles.css`**: Defines the styling for the chat interface.
   - Implements a responsive layout.
   - Styles chat messages, input area, and send button.
   - Differentiates between user and bot messages visually.

3. **`script.js`**: Handles the frontend logic and communication with the backend.
   - Manages sending messages to the server and displaying responses.
   - Implements asynchronous communication using fetch API.
   - Dynamically updates the chat interface with new messages.

4. **`App.py`**: The Flask application that serves as the backend.
   - Implements the ChatBot class with sentiment analysis functionality.
   - Provides a `/chat` endpoint for processing messages.
   - Uses VADER to analyze sentiment and generate appropriate responses.
   - Returns detailed sentiment scores along with the chatbot's response.

## How It Works
1. The user types a message in the web interface and sends it.
2. The JavaScript code sends this message to the Flask backend via a POST request.
3. The Flask app receives the message and passes it to the ChatBot instance.
4. VADER analyzes the sentiment of the input, providing detailed sentiment scores.
5. Based on the sentiment scores, particularly the compound score, the chatbot generates an appropriate response.
6. The response, along with detailed sentiment information, is sent back to the frontend.
7. The JavaScript code receives the response and updates the chat interface, displaying the bot's message.

## Setup and Installation
1. Clone the repository
2. Install required packages:
