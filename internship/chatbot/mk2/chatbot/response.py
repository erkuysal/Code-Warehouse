import random
from chatbot.model import load_model
from chatbot.preprocess import preprocess_text
from chatbot.database import log_interaction

model, vectorizer, encoder = load_model()

def get_response(user_input):
    tokens = preprocess_text(user_input)
    user_input_vector = vectorizer.transform([' '.join(tokens)])
    predicted_tag = model.predict(user_input_vector)[0]
    intent = encoder.inverse_transform([predicted_tag])[0]
    response = random.choice(intents[intent]['responses'])
    log_interaction(user_input, intent, None, response)
    return response.replace("[Product]", "your product")