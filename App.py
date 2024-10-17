# Import Flask, a lightweight web framework for Python.
from flask import Flask, request, jsonify
from flask_cors import CORS 
# Import VADER to help the chatbot understand language nuances
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__)
CORS(app)  # This allows cross-origin requests, which is necessary for development


# Defining the Chatbot Class for Interaction.
class ChatBot:
    def __init__(self):
        # Initialize the sentiment analysis tool
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
              
    def process_input(self, user_input):
        sentiment_scores = self.sentiment_analyzer.polarity_scores(user_input)
        compound_score = sentiment_scores['compound']

        # Generate the chatbot's response based on the compound score
        if compound_score >= 0.05:
            response = f"That's great to hear! Your message seems positive. Sentiment Score: {compound_score:.2f}"
        elif compound_score <= -0.05:
            response = f"I'm sorry to hear that. Your message seems negative. Would you like to talk more about it? Sentiment Score: {compound_score:.2f}"
        else:
            response = f"I see. Your message seems neutral. Can you please provide more information? Sentiment Score: {compound_score:.2f}"
        
        # Add more detailed sentiment information
        response += f"\nPositive: {sentiment_scores['pos']:.2f}, Negative: {sentiment_scores['neg']:.2f}, Neutral: {sentiment_scores['neu']:.2f}"
        
        return response

chatbot = ChatBot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot.process_input(user_input)
    return jsonify({'response': response})

# To run this server, you'll need to install Flask and Flask-CORS:
# pip install flask flask-cors vaderSentiment
# python App.py to run
if __name__ == '__main__':
    app.run(debug=True)
