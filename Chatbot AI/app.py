from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

def generate_response(message):
    # Simple rule-based response for demonstration
    responses = {
        "what is my name": "Your name is Prem Rajesh.",
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!"
    }
    return responses.get(message.lower(), "I didn't understand that. Can you please rephrase?")

if __name__ == '__main__':
    app.run(debug=True)
