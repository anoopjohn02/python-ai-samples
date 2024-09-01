from flask import Flask
from flask_cors import CORS
from flask import request
import json
from chatbot import chat

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']
    return chat(input_text)

if __name__ == '__main__':
    app.run()