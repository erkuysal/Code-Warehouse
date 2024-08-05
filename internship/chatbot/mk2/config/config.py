import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
INTENTS_PATH = os.path.join(DATA_DIR, 'intents.json')
DB_PATH = os.path.join(DATA_DIR, 'interactions.db')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')