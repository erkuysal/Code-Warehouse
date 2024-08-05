import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from config import config

nltk.download('punkt')
nltk.download('wordnet')

# Load intents JSON
with open(config.INTENTS_PATH) as json_file:
    intents = json.load(json_file)

lemmatizer = WordNetLemmatizer()

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

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

encoder = LabelEncoder()
y = encoder.fit_transform(tags)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
joblib.dump((model, vectorizer, encoder), config.MODEL_PATH)

def load_model():
    return joblib.load(config.MODEL_PATH)