from flask import Flask, request, jsonify, render_template
from chatbot import response, database

# Initialize Flask app
app = Flask(__name__)

# Initialize database
database.init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    bot_response = response.get_response(user_input)
    return jsonify({"response": bot_response})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    database.log_feedback(data)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)