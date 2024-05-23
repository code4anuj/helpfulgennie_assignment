from flask import Flask, render_template, request, jsonify, send_from_directory
from source.speech_to_text import SpeechToText
from source.text_to_speech import TextToSpeech
from source.llm_responsing import AiChat

app = Flask(__name__)

# INITIALISING
model = AiChat()
speech_to_text = SpeechToText()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    result = speech_to_text.process()
    print("Result STT: {}".format(result))
    if result:
        return jsonify({'message': result})
    else:
        return jsonify({'message': "Sorry, I could not understand the audio."})

@app.route('/process-message', methods=['POST'])
def process_message():
    user_message = request.json['message']
    model_response = model.generate_response(user_message)
    response_text = f"{model_response}"
    tts = TextToSpeech(text=response_text, filename='static/output.mp3')
    tts.process()
    return jsonify({'message': response_text, 'audio': 'output.mp3'})

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
