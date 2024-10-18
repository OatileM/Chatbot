from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import boto3
import os
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the Amazon Comprehend client
try:
    comprehend = boto3.client('comprehend',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('AWS_REGION', 'us-east-1')
    )
except Exception as e:
    logger.error(f"Failed to initialize Comprehend client: {str(e)}")
    comprehend = None

class ChatBot:
    def __init__(self):
        self.vader_analyzer = SentimentIntensityAnalyzer()

    def analyze_with_comprehend(self, text):
        if not comprehend:
            logger.warning("Comprehend client not initialized. Skipping Comprehend analysis.")
            return None, None
        try:
            response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
            return response['Sentiment'], response['SentimentScore']
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {str(e)}")
            return None, None

    def detect_key_phrases(self, text):
        if not comprehend:
            logger.warning("Comprehend client not initialized. Skipping key phrase detection.")
            return []
        try:
            response = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
            return [phrase['Text'] for phrase in response['KeyPhrases']]
        except Exception as e:
            logger.error(f"Error in key phrase detection: {str(e)}")
            return []

    def process_input(self, user_input):
        vader_scores = self.vader_analyzer.polarity_scores(user_input)
        
        comprehend_sentiment, comprehend_scores = self.analyze_with_comprehend(user_input)
        key_phrases = self.detect_key_phrases(user_input)
        
        # Determine overall sentiment
        if comprehend_sentiment == "POSITIVE" or vader_scores['compound'] > 0.05:
            sentiment = "positive"
        elif comprehend_sentiment == "NEGATIVE" or vader_scores['compound'] < -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Generate conversational response
        if sentiment == "positive":
            response = "I'm glad to hear that! Your message seems quite positive. "
        elif sentiment == "negative":
            response = "I'm sorry to hear that. Your message seems to have a negative tone. "
        else:
            response = "I see. Your message seems to be neutral in tone. "

        if key_phrases:
            response += f"The key points I picked up were: {', '.join(key_phrases)}. "

        response += "Is there anything specific you'd like to discuss further?"

        # Add detailed analysis as a separate field
        detailed_analysis = f"Sentiment: {sentiment}. VADER Scores: {vader_scores}. "
        if comprehend_sentiment and comprehend_scores:
            detailed_analysis += f"Comprehend Sentiment: {comprehend_sentiment}, Scores: {comprehend_scores}. "
        if key_phrases:
            detailed_analysis += f"Key phrases: {', '.join(key_phrases)}."
        
        return {"response": response, "analysis": detailed_analysis}

chatbot = ChatBot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    result = chatbot.process_input(user_input)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
