# Sentiment analysis is the process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral.

# Import Flask, a lightweight web framework for Python.
from flask import Flask, request, jsonify
from flask_cors import CORS 
# Import TextBlob to help the chatbot understand language nuances
from textblob import TextBlob # type: ignore


app = Flask(__name__)
CORS(app)  # This allows cross-origin requests, which is necessary for development



# Defining the Chatbot Class for Interaction.
class ChatBot:
    def __init__(self):
        # Initialize the sentiment analysis tool
        self.sentiment_analyzer = TextBlob("")
        
              
    def process_input(self, user_input):
        self.sentiment_analyzer = TextBlob(user_input)
        sentiment_score = self.sentiment_analyzer.sentiment.polarity

        # Analyze the sentiment of the user's input
        self.sentiment_analyzer = TextBlob(user_input)
        sentimemnt_score = self.sentiment_analyzer.sentiment.polarity
        
        # Generate the chatbot's response based on the sentiment
        if sentiment_score > 0:
            response = f"That's great to hear! Sentiment Score: {sentiment_score:.2f}"
        elif sentiment_score < 0:
            response = f"I'm sorry to hear that. Would you like me to transfer you to a live agent? Sentiment Score: {sentiment_score:.2f}"
        else:
            response = f"Hmm I see. Can you please provide more information? Sentiment Score: {sentiment_score:.2f}"

        # Print the chatbot's response and sentiment
        return response

chatbot = ChatBot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot.process_input(user_input)
    return jsonify({'response': response})

# To run this server, you'll need to install Flask and Flask-CORS:
# pip install flask flask-cors
# python App.py to run
if __name__ == '__main__':
    app.run(debug=True)