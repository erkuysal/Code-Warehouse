import nltk

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


lemmatizer = WordNetLemmatizer()

intents = {
    "greetings": {
        "patterns": ["hello",
                     "hi", "good morning",
                     "good evening", "hey"],

        "responses": ["Hello!", "Hi there!",
                      "Good day!", "Hello! How can I assist you today?"]
    },
    "product_info": {
        "patterns": ["Tell me about [Product]",
                     "What are the features of [Product]?",
                     "Give me information on [Product]"],

        "responses": ["[Product] is an excellent choice. It has features like..."]
    },
    "complaint": {
        "patterns": ["I have a complaint",
                     "I want to report an issue",
                     "There is a problem with my order"],

        "responses": ["I'm sorry to hear that. Can you please provide more details?",
                      "We apologize for the inconvenience. Please describe the issue."]
    }
}


def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return tokens


for intent in intents:
    for pattern in intents[intent]["patterns"]:
        intents[intent]["patterns"] = [preprocess_text(pattern) for pattern in intents[intent]["patterns"]]


patterns = []
tags = []
for intent in intents:
    for pattern in intents[intent]["patterns"]:
        patterns.append(' '.join(pattern))
        tags.append(intent)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

encoder = LabelEncoder()
y = encoder.fit_transform(tags)


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X, y)