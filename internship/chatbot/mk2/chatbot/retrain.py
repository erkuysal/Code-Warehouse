import sqlite3
from chatbot.model import preprocess_text
from chatbot.model import vectorizer, encoder, model
from config import config


def load_interactions():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT user_input, actual_intent FROM interactions WHERE actual_intent IS NOT NULL')
    interactions = cursor.fetchall()
    conn.close()
    return interactions


def retrain_model():
    interactions = load_interactions()
    patterns = []
    tags = []
    for user_input, actual_intent in interactions:
        if actual_intent != 'unknown':
            patterns.append(' '.join(preprocess_text(user_input)))
            tags.append(actual_intent)

    X = vectorizer.fit_transform(patterns)
    y = encoder.fit_transform(tags)
    model.fit(X, y)

# Call retrain_model() periodically or based on a specific trigger