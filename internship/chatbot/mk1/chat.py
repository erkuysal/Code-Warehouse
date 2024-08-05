import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, request, jsonify, render_template

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load intents JSON
with open('intents.json') as json_file:
    intents = json.load(json_file)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess text function
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return tokens

# Prepare data
patterns = []
tags = []
for intent in intents:
    for pattern in intents[intent]['patterns']:
        patterns.append(' '.join(preprocess_text(pattern)))
        tags.append(intent)

# Vectorize data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(tags)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Get response function
def get_response(user_input):
    tokens = preprocess_text(user_input)
    user_input_vector = vectorizer.transform([' '.join(tokens)])
    predicted_tag = model.predict(user_input_vector)[0]
    intent = encoder.inverse_transform([predicted_tag])[0]
    response = random.choice(intents[intent]['responses'])
    return response.replace("[Product]", "your product")

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)